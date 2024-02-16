from django.shortcuts import render
from django.http import JsonResponse
def allotment(request):
    return render(request,"Allotment.html")

def submit_form(request):
    if request.method == 'POST':
        # Assuming you're expecting JSON data in the request
        form_data = request.POST.get('formData')
        # Process the form data as needed
        # For simplicity, let's just return the received data as JSON
        return JsonResponse({'success': True, 'data': form_data})
    else:
        return JsonResponse({'success': False, 'error': 'Invalid request method'})
