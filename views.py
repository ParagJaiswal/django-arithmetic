from django.shortcuts import render

def index(request):
	return render(request,'guest/front.html')

def maths(request):
	return render(request,'guest/input.html')

def logic(request):
	l = request.POST['num1']
	b = request.POST['num2']

	if request.POST.get("aot"):
		res = (float(l)*float(b))/2
	elif request.POST.get("aor"):
		res = (float(l)*float(b))
	elif request.POST.get("aoc"):
		res = (3.14*float(l)*float(l))

	return render(request,'guest/input.html',{"key":"result is = "+str(res),"l":l,"b":b})

