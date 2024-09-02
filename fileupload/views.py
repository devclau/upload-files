from django.http import JsonResponse
from django.shortcuts import render
from fileupload.forms import FileForm
from fileupload.models import Files
# Create your views here.

def upload_file_old(request):
    if request.method == 'POST':
        form = FileForm(request.POST, request.FILES)
        if form.is_valid():
            Files.objects.create(nombre= form.cleaned_data['nombre'], file = form.cleaned_data['file'] )
            return render(request, 'inicio.html', {'form':form})
        print(form.errors)
    form = FileForm
    return render(request, 'inicio.html', {'form':form})

def upload_file(request):
    if request.method == 'POST':
        form = FileForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()  # Guarda el nuevo archivo en la base de datos

            if request.headers.get('x-requested-with') == 'XMLHttpRequest':
                all_files = Files.objects.all().values('id', 'nombre', 'file', 'fecha')
                files_list = list(all_files)  # Convertir QuerySet a lista
                return JsonResponse({
                    'message': 'File uploaded successfully!',
                    'files': files_list
                }, status=200)

            return render(request, 'inicio.html', {'form': form})

        else:
            if request.headers.get('x-requested-with') == 'XMLHttpRequest':
                return JsonResponse({'errors': form.errors}, status=400)
            print(form.errors)
    else:
        form = FileForm()
        all_files = Files.objects.all()  # Obtener todos los archivos al cargar la página

    return render(request, 'inicio.html', {'form': form, 'files': all_files})

def delete_file(request):
    if request.method == 'POST':
        file_id = request.POST.get('id')
        try:
            file = Files.objects.get(id=file_id)
            file.delete()
            return JsonResponse({'message': 'File deleted successfully!'}, status=200)
        except Files.DoesNotExist:
            return JsonResponse({'errors': 'File not found.'}, status=404)
    return JsonResponse({'errors': 'Invalid request.'}, status=400)