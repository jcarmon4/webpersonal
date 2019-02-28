from django.shortcuts import render, HttpResponse

html_base = """
<h1>Alejocram</h1>
<ul>
    <li><a href="/">Home</a></li>
    <li><a href="/portfolio/">Portafolio</a></li>
    <li><a href="/contact/">Contactenos</a></li>
    <li><a href="/about/">Acerca de</a></li>
</ul>
"""

# Create your views here.
def home(request):
    return render(request, "core/home.html" )

def about(request):
    html_response = """
        <h3>Acerca de</h3>
    """
    return HttpResponse(html_base + html_response)

def portfolio(request):
    html_response = """
        <h3>Portafolio</h3>
    """
    return HttpResponse(html_base + html_response)

def contact(request):
    html_response = """
        <h3>Contactenos</h3>
    """
    return HttpResponse(html_base + html_response)
