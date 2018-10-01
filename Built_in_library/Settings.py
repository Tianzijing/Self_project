from External_library.logs import get_log_path


class Settings():

    # 首页地址 IP地址
    base_url = "http://172.31.23.60/"
    # 后台管理地址
    admin_url = base_url + "admin/"

    # 详细日志地址
    log = get_log_path(__file__, __name__)

    # 异常重试次数
    n = 2

    # 运行速度 默认
    speed_default = 0
    # 运行速度 减速
    speed_down = 3

    # 后台管理员
    Admin = {'name': 'admin',
             'password': 'Asd890*()'}

    # 用户
    Test01 = {'name': 'Test01',
              'password': '123456'}

    # 收货人信息
    address_01 = {'country': '中国',
                  'province': '黑龙江',
                  'city': '大庆',
                  'district': '让胡路区',
                  'name': 'Test01',
                  'address': '东方广场C座11楼',
                  'phone': '15368742581'}
