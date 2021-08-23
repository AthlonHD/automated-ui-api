# -*- coding=utf-8 -*-

mall_path = r'/Users/athlonhd/mall30/'


class Config:  # 默认配置
    DEBUG = False

    # get attribute
    def __getitem__(self, key):
        return self.__getattribute__(key)


class ProductionEnv(Config):
    pass


class DevelopmentEnv(Config):
    path = mall_path
    bmeuat_url = 'https://bmeactuat.capitaland.com.cn/api'
    kmalluat_url = 'https://kamall30apiuat.capitaland.com.cn/api'
    bmeparkuat_url = 'https://bmeparkapiuat.capitaland.com.cn/api'
    bmecouponuat_url = 'https://bmecouponuat.capitaland.com.cn/api'

    with open(path + r"use_case/uat_chuancan/free_daijin.json", 'r', encoding='utf-8') as f:
        free_daijin_json = f.read()
    with open(path + r"use_case/uat_chuancan/free_lipin.json", 'r', encoding='utf-8') as f:
        free_lipin_json = f.read()
    with open(path + r"use_case/uat_chuancan/free_tingche.json", 'r', encoding='utf-8') as f:
        free_tingche_json = f.read()
    with open(path + r"use_case/uat_chuancan/free_tiyan.json", 'r', encoding='utf-8') as f:
        free_tiyan_json = f.read()
    with open(path + r"use_case/uat_chuancan/free_zhekou.json", 'r', encoding='utf-8') as f:
        free_zhekou_json = f.read()
    with open(path + r"use_case/uat_chuancan/point_daijin.json", 'r', encoding='utf-8') as f:
        point_daijin_json = f.read()
    with open(path + r"use_case/uat_chuancan/point_lipin.json", 'r', encoding='utf-8') as f:
        point_lipin_json = f.read()
    with open(path + r"use_case/uat_chuancan/point_tingche.json", 'r', encoding='utf-8') as f:
        point_tingche_json = f.read()
    with open(path + r"use_case/uat_chuancan/point_tiyan.json", 'r', encoding='utf-8') as f:
        point_tiyan_json = f.read()
    with open(path + r"use_case/uat_chuancan/point_zhekou.json", 'r', encoding='utf-8') as f:
        point_zhekou_json = f.read()


mapping = {
    'pro': ProductionEnv,
    'dev': DevelopmentEnv
}

config = mapping['dev']


# if __name__ == '__main__':
#     var = config.url
#     print(var, logs_exact_path)
#     pass
