from urllib.parse import urlparse

def display_banner():
    banner = r"""
    ==========================
    URL 处理工具 by 黄豆安全实验室
    ==========================
    """
    print(banner)

def process_urls(input_file, output_file, mode):
    with open(input_file, 'r') as infile, open(output_file, 'w') as outfile:
        for line in infile:
            url = line.strip()  # 去掉行首尾的空格和换行符
            parsed_url = urlparse(url)  # 解析 URL
            
            if mode == 1:
                # 模式 1: 只保留主机名，不带端口号
                host = parsed_url.hostname  # 获取主机名
            elif mode == 2:
                # 模式 2: 保留主机名和端口号
                host = parsed_url.netloc.split(':')[0]  # 获取主机名
                port = parsed_url.port  # 获取端口号
                if port:
                    host += f":{port}"  # 如果有端口号，添加上
            
            if host:  # 确保主机名不为空
                outfile.write(host + '\n')  # 写入输出文件

def main():
    display_banner()  # 显示字符画
    
    input_file = 'urls.txt'
    output_file = 'processed_urls.txt'
    
    # 输出菜单供用户选择
    print("请选择处理模式:")
    print("1: 只保留主机名，不带端口号")
    print("2: 保留主机名和端口号")
    
    while True:
        try:
            mode = int(input("请输入模式 (1 或 2): "))
            if mode in [1, 2]:
                break
            else:
                print("无效输入，请输入 1 或 2。")
        except ValueError:
            print("无效输入，请输入 1 或 2。")

    # 执行处理函数
    process_urls(input_file, output_file, mode)
    print("URL 处理完成，结果已保存到", output_file)

if __name__ == "__main__":
    main()