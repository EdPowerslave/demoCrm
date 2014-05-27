from customer.models import Customer, Meeting
from django.shortcuts import render, redirect, get_object_or_404
from customer.forms import CustomerForm, MeetingForm, SearchForm
from django.shortcuts import render_to_response
from django.core.paginator import Paginator
from django.template import RequestContext
from django.db.models import Q

def customer_list(request, template_name='customer/customer_list.html'):
    customers = Customer.objects.order_by('name')
    data = {'customer_list': customers}
    return render(request, template_name, data)


def customer_view(request, id, template_name='customer/customer.html'):
    customers = Customer.objects.get(id=id)
    meeting = Meeting.objects.filter(customer_id=customers.id)
    data = {'customer': customers, 'customer_meeting': meeting}
    return render(request, template_name, data)

def customer_create(request, template_name='customer/customer_add.html'):
    form = CustomerForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('customer_list')
    return render(request, template_name, {'form': form})

def customer_update(request, id, template_name='customer/customer_update.html'):
    customer = Customer.objects.get(id=id)
    form = CustomerForm(request.POST or None, instance=customer)
    if form.is_valid():
        form.save()
        return redirect('customer_list')
    return render(request, template_name, {'form': form})

def customer_delete(request, id):
    customer = Customer.objects.get(id=id)
    data = {'customer': customer}
    customer.delete()
    return redirect('customer_list')
    return render(request, data)


def meeting_list(request, template_name='customer/meeting_list.html'):
    meetings = Meeting.objects.all()
    data = {'meeting_list': meetings}
    return render(request,template_name, data)

def meeting_view(request, id, template_name='customer/meeting.html'):
    meetings = Meeting.objects.get(id=id)
    data = {'meeting': meetings}
    return render(request,template_name, data)

def meeting_create(request, id, template_name='customer/meeting_add.html'):
    customer = get_object_or_404(Customer, id=id)
    initial = {'customer': customer}
    form = MeetingForm(request.POST or None, initial=initial)
    if form.is_valid():
        meeting = form.save(commit=False)
        meeting.customer = customer
        meeting.customer_id = id
        meeting.save()
        return redirect('customer')
    return render(request, template_name, {'form': form})

def meeting_update(request, id, template_name='customer/meeting_update.html'):
    meeting = Meeting.objects.get(id=id)
    form = MeetingForm(request.POST or None, instance=meeting)
    if form.is_valid():
        form.save()
        return redirect('meeting_list')
    return render(request, template_name, {'form': form})

def meeting_delete(request, id):
    meeting = Meeting.objects.get(id=id)
    data = {'meeting_list': meeting}
    meeting.delete()
    return redirect('meeting_list')
    return render(request, data)

def search_in_customers(request, template_name = 'customer/customer_search.html'):
    search_form = SearchForm
    if request.GET.get('search_query'):
        search_form = SearchForm(request.GET)
        if search_form.is_valid():
            search_query = search_form.cleaned_data['search_query']
            all_customers = Customer.objects.all().filter(Q(name=search_query) | Q(surname=search_query))
            customer_count = all_customers.count()

    return render_to_response(template_name, locals(), context_instance=RequestContext(request))




