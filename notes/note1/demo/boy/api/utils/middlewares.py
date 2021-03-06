
from django.utils.deprecation import MiddlewareMixin

class CorsMiddleWare(MiddlewareMixin):


    def process_response(self,request,response):

        if request.method=="OPTIONS":
            print("跨域跨域请求")
            response["Access-Control-Allow-Methods"] = "GET,POST,DELETE,PUT"
            response["Access-Control-Allow-Headers"] = "Content-Type,AUTHORIZATION"

        response["Access-Control-Allow-Origin"] = "*"

        return response