from django.shortcuts import render, get_object_or_404, redirect
from .models import Result
from .forms import ResultForm

def result_list(request):
    results = Result.objects.all()
    student_name = request.GET.get('student_name')
    subject = request.GET.get('subject')
    if student_name:
        results = results.filter(student_name__icontains=student_name)
    if subject:
        results = results.filter(subject__icontains=subject)
    return render(request, 'results/result_list.html', {'results': results})

def result_create(request):
    form = ResultForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('result_list')
    return render(request, 'results/result_form.html', {'form': form})

def result_update(request, pk):
    result = get_object_or_404(Result, pk=pk)
    form = ResultForm(request.POST or None, instance=result)
    if form.is_valid():
        form.save()
        return redirect('result_list')
    return render(request, 'results/result_form.html', {'form': form})

def result_delete(request, pk):
    result = get_object_or_404(Result, pk=pk)
    if request.method == 'POST':
        result.delete()
        return redirect('result_list')
    return render(request, 'results/result_confirm_delete.html', {'result': result})