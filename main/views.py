from django.shortcuts import render

# Create your views here.
def show_main(request):
    context = {
        'nama_aplikasi' : 'karesu',
        'nama': 'Fariz Muhammad Rayhansyah Ramadhan',
        'kelas': 'PBP B'
    }

    return render(request, "main.html", context)