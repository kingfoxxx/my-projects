from django.shortcuts import render
from .models import Dash

def dashboard(request):
    if request.method == 'GET':
        # Retrieve filter criteria from the form
        end_year = request.GET.get('end_year')
        intensity = request.GET.get('intensity')
        likelihood = request.GET.get('likelihood')
        relevance = request.GET.get('relevance')
        year = request.GET.get('year')
        country = request.GET.get('country')
        topics = request.GET.get('topics')
        region = request.GET.get('region')
        
        # Filter data based on the criteria
        filtered_data = Dash.objects.all()
        if end_year:
            filtered_data = filtered_data.filter(end_year=end_year)
        if intensity:
            filtered_data = filtered_data.filter(intensity=intensity)
        if likelihood:
            filtered_data = filtered_data.filter(likelihood=likelihood)
        if relevance:
            filtered_data = filtered_data.filter(relevance=relevance)
        if year:
            filtered_data = filtered_data.filter(start_year=year)
        if country:
            filtered_data = filtered_data.filter(country=country)
        if topics:
            filtered_data = filtered_data.filter(topic=topics)
        if region:
            filtered_data = filtered_data.filter(region=region)
        
        # Pass filtered data to the template
        return render(request, 'dashboard.html', {'data': filtered_data})
    else:
        # Handle other HTTP methods (e.g., POST) if needed
        pass
