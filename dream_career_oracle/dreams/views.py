# dreams/views.py
from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import F
from django.contrib import messages
from .models import Dream, PathStep
from . import forms


def home(request):
    total_dreams = Dream.objects.count()
    top_liked_dreams = Dream.objects.order_by("-likes", "-created_at")[:3]
    return render(
        request,
        "home.html",
        {
            "total_dreams": total_dreams,
            "top_liked_dreams": top_liked_dreams,
        },
    )


def dream_list(request):
    dreams = Dream.objects.all()
    return render(request, "dream_list.html", {"dreams": dreams})


def create_dream(request):
    if request.method == "POST":
        title = request.POST.get("title")
        description = request.POST.get("description")
        level = request.POST.get("level")

        category = request.POST.get("category")
        if category == "Others":
            category = request.POST.get("other_category", "Others")

        if title and description and category and level:
            dream = Dream.objects.create(
                title=title, description=description, category=category, level=level
            )
            messages.success(request, f'Dream "{title}" created successfully! 🎉')
            return redirect("dream_detail", pk=dream.pk)
        else:
            messages.error(request, "Please fill all required fields.")

    return render(request, "create_dream.html")


def dream_detail(request, pk):
    dream = get_object_or_404(Dream, pk=pk)
    steps = dream.steps.all()
    total_steps = steps.count()
    completed_steps = steps.filter(status="Completed").count()
    progress = 0
    if total_steps > 0:
        progress = int((completed_steps / total_steps) * 100)

    return render(
        request,
        "dream_detail.html",
        {
            "dream": dream,
            "steps": steps,
            "total_steps": total_steps,
            "completed_steps": completed_steps,
            "progress": progress,
        },
    )


def delete_dream(request, pk):
    dream = get_object_or_404(Dream, pk=pk)

    # try:
    #     student = Dream.objects.get(id=id)
    # except Dream.DoesNotExist:
    #     raise Http404("Dream not found")

    if request.method == "POST":
        dream_title = dream.title
        dream.delete()
        messages.error(request, f'Dream "{dream_title}" has been deleted.')
        return redirect("dream_list")

    return render(request, "delete_dream.html", {"dream": dream})


def add_step(request, dream_id):
    dream = get_object_or_404(Dream, pk=dream_id)
    if request.method == "POST":
        step_title = request.POST.get("step_title")
        description = request.POST.get("description")
        estimated_time = request.POST.get("estimated_time")
        status = request.POST.get("status", "Pending")

        if step_title and description and estimated_time:
            PathStep.objects.create(
                dream=dream,
                step_title=step_title,
                description=description,
                estimated_time=estimated_time,
                status=status,
            )
            messages.success(request, "Step added successfully!")
            return redirect("dream_detail", pk=dream.pk)
    return render(request, "add_step.html", {"dream": dream})


# def add_step(request, dream_id):
#     dream = get_object_or_404(Dream, pk=dream_id)
#     if request.method == "POST":
#         fm = forms.AddNewStep(request.POST)
#         if fm.is_valid():
#             step_title = fm.cleaned_data["step_title"]
#             description = fm.cleaned_data["description"]
#             estimated_time = fm.cleaned_data["estimated_time"]
#             status = fm.cleaned_data["status"]

#         if step_title and description and estimated_time:
#             PathStep.objects.create(
#                 dream=dream,
#                 step_title=step_title,
#                 description=description,
#                 estimated_time=estimated_time,
#                 status=status,
#             )
#             messages.success(request, "Step added successfully!")
#             return redirect("dream_detail", pk=dream.pk)
#         context = {"form": fm}
#         return render(request, "add_step.html", context)
#     context = {"form": forms.AddNewStep(), "dream": dream}
#     return render(request, "add_step.html", context)


def edit_step(request, step_id):
    step = get_object_or_404(PathStep, pk=step_id)
    if request.method == "POST":
        step.step_title = request.POST.get("step_title")
        step.description = request.POST.get("description")
        step.estimated_time = request.POST.get("estimated_time")
        step.status = request.POST.get("status", step.status)
        step.save()
        messages.success(request, "Step updated successfully!")
        return redirect("dream_detail", pk=step.dream.pk)
    return render(request, "edit_step.html", {"step": step})


def delete_step(request, step_id):
    step = get_object_or_404(PathStep, pk=step_id)
    step_title = step.step_title
    dream_pk = step.dream.pk
    if request.method == "POST":
        step.delete()
        messages.error(request, f'Step "{step_title}" has been deleted.')
        return redirect("dream_detail", pk=dream_pk)
    return render(request, "delete_step.html", {"step": step})


def edit_dream(request, pk):
    dream = get_object_or_404(Dream, pk=pk)
    if request.method == "POST":
        dream.title = request.POST.get("title")
        dream.description = request.POST.get("description")
        dream.category = request.POST.get("category")
        if dream.category == "Others":
            dream.category = request.POST.get("other_category", "Others")
        dream.level = request.POST.get("level")
        dream.save()
        messages.success(request, "Dream updated successfully!")
        return redirect("dream_detail", pk=dream.pk)
    return render(request, "edit_dream.html", {"dream": dream})


def like_dream(request, pk):
    dream = get_object_or_404(Dream, pk=pk)
    if request.method == "POST":
        Dream.objects.filter(pk=dream.pk).update(likes=F("likes") + 1)
    next_url = request.POST.get("next")
    if next_url:
        return redirect(next_url)
    return redirect("dream_detail", pk=pk)
