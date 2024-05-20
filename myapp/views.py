from django.shortcuts import render, get_object_or_404, redirect
from .models import Package
from .forms import PackageForm

def package_list(request):
    packages = Package.objects.all()
    return render(request, 'myapp/package_list.html', {'packages': packages})

def package_detail(request, pk):
    package = get_object_or_404(Package, pk=pk)
    return render(request, 'myapp/package_detail.html', {'package': package})

def package_create(request):
    if request.method == 'POST':
        form = PackageForm(request.POST)
        if form.is_valid():
            package = form.save()
            return redirect('package_detail', pk=package.pk)
    else:
        form = PackageForm()
    return render(request, 'myapp/package_form.html', {'form': form})

def package_update(request, pk):
    package = get_object_or_404(Package, pk=pk)
    if request.method == 'POST':
        form = PackageForm(request.POST, instance=package)
        if form.is_valid():
            package = form.save()
            return redirect('package_detail', pk=package.pk)
    else:
        form = PackageForm(instance=package)
    return render(request, 'myapp/package_form.html', {'form': form})

def package_delete(request, pk):
    package = get_object_or_404(Package, pk=pk)
    if request.method == 'POST':
        package.delete()
        return redirect('package_list')
    return render(request, 'myapp/package_confirm_delete.html', {'package': package})
