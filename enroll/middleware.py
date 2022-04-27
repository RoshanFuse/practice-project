

from django.shortcuts import render


class MyMiddleware:
    def __init__(self,get_responce):
        self.get_responce = get_responce
        print("one time initializations")
        
    def __call__(self, request):
         print("my before view")
         responce = self.get_responce(request)
        #  responce = render(request,'enroll/middleware.html')  
         print("my after view")
         return responce