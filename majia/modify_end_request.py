# -*- coding: utf-8 -*

import os

# 需要修改的类名前缀 （需替换）
end_str = 'Request'
# 不需要修改的类名后缀 （需替换）
not_end_str = []
# 新的类名后缀 （需替换）
end_to_str = 'NetRequest'



# 搜寻以下文件类型 （根据自己需求替换）
suf_set = ('.h', '.m', '.xib', '.storyboard', '.mm')
# 项目路径   （找到自己的项目路径）
project_path = '/Users/tonyreet/Documents/Code/NewBanana/BananaReading'
# 项目project.pbxproj文件路径 需要更新配置文件中的类名 （找到自己的项目project.pbxproj路径）
pbxpro_path = '/Users/tonyreet/Documents/Code/NewBanana/BananaReading/BananaReading.xcodeprojBananaReading.xcodeproj'

# 文件重命名函数，返回新的文件名
def file_rename(file_path):
    root_path = os.path.split(file_path)[0]     # 文件目录
    root_name = os.path.split(file_path)[1]     # 文件名包含扩展名
    filename = os.path.splitext(root_name)[0];  # 文件名
    filetype = os.path.splitext(root_name)[1];  # 文件扩展名

    new_path = os.path.join(root_path, filename.replace(end_str, end_to_str) + filetype)    # 拼接新路径
    # print(new_path)
    os.renames(file_path, new_path)             # 文件重命名
    return filename.replace(end_str, end_to_str)
def end_check(name):
    for str in not_end_str:
        if name.find(str) != -1 or name == end_str:
            return True
    return False
# 定义一个字典 key=旧类名 value=新类名
needModifyDic = {}

# 遍历文件，符合规则的进行重命名
for (root, dirs, files) in os.walk(project_path):
    for file_name in files:
        fileName = os.path.splitext(file_name)[0];  # 文件名
        if fileName.endswith(end_str) and file_name.endswith(suf_set) and end_check(fileName)==False:
            
            # print(file_name)
            old_name = os.path.splitext(file_name)[0]
            new_name = file_rename(os.path.join(root, file_name))
            needModifyDic[old_name] = new_name

# 遍历文件，在文件中更换新类名的引用
print(needModifyDic)
for (root, dirs, files) in os.walk(project_path):
    for file_name in files:
        if file_name.endswith(suf_set):
            print('-----fileName-------' + file_name)
            with open(os.path.join(root, file_name), 'r+') as f:
                print('========fileName========' + file_name)
                s0 = f.read()
                f.close()
                for key in needModifyDic:
                    if key in s0:
                        with open(os.path.join(root, file_name), 'r+') as f4:
                            s1 = f4.read().replace(key, needModifyDic[key])
                            print(key + ' ------> ' + needModifyDic[key])
                            f4.seek(0)
                            f4.write(s1)
                            f4.truncate()
                            f4.close()
# 替换配置文件中的类名
for key in needModifyDic:
    with open(pbxpro_path, 'r+') as f:
        s0 = f.read()
        f.close()
        if key in s0:
            with open(pbxpro_path, 'r+') as f2:
                s = f2.read().replace(key, needModifyDic[key])
                f2.seek(0)
                f2.write(s)
                f2.truncate()
                f2.close()

