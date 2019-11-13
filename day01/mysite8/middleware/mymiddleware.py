from django.utils.deprecation import MiddlewareMixin

class MyMw(MiddlewareMixin):

    def process_request(self, request):
        #请求到达urls.py主路由之前 调用
        #返回None 则请求继续执行
        #返回HttpResponse 则请求终止，直接响应
        print('MyMw process_request do ---')

    def process_view(self, request, callback, callback_args, callback_kwargs):
        #进入views试图之前调用
        #返回值同上
        print('MyMw process_view do ---')


    def process_response(self, request, response):
        #响应返给浏览器之前调用
        #必须返回HttpResponse
        print('MyMw process_response do ---')
        return response


class MyMw2(MiddlewareMixin):

    def process_request(self, request):
        #请求到达urls.py主路由之前 调用
        #返回None 则请求继续执行
        #返回HttpResponse 则请求终止，直接响应
        print('MyMw2 process_request do ---')

    def process_view(self, request, callback, callback_args, callback_kwargs):
        #进入views试图之前调用
        #返回值同上
        print('MyMw2 process_view do ---')


    def process_response(self, request, response):
        #响应返给浏览器之前调用
        #必须返回HttpResponse
        print('MyMw2 process_response do ---')
        return response