from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from django.http import JsonResponse
from common.models import Country
import json
def register_user(request):
          
    if request.method == 'POST':
        try:
            # 解析 POST 请求的 JSON 数据
            data = json.loads(request.body)
            username = data['username']
            password = data['password']
            country = data['country']
            # 检查用户名是否已经存在
            if User.objects.filter(username=username).exists():
                return JsonResponse({'error': 'Username already exists1'}, status=401)

            # 创建新用户并保存到数据库
            user = User(username=username, password=make_password(password))
            user.save()

            return JsonResponse({'success': 'User registered successfully'})

        except KeyError:
            return JsonResponse({'error': 'Invalid data provided2'}, status=402)

    else:
        return JsonResponse({'error': 'Only POST requests are allowed5'}, status=405)
def get_country_data(request):
    if request.method == 'GET':
        # 查询数据库获取所有的国家数据
        countries = Country.objects.all()
        # 将查询到的国家数据转换成字典列表
        country_list = [{'id': country.id, 'name': country.country} for country in countries]
        # 构建要返回的数据格式
        response_data = {'countries': country_list}
        
        # 返回 JSON 格式的响应
        return JsonResponse(response_data)
