import pandas as pd
if __name__ == '__main__':#导入pandas包
    ratings = pd.read_csv('D:\movie_data\ml-latest/ratings.csv')
    #print (ratings.head(20))
    movies = pd.read_csv('D:\movie_data\ml-latest/movies.csv')
    #print(movies.head(5))
    data = pd.merge(movies, ratings, on='movieId')
    #print(data.head(5))
    data[['userId', 'rating', 'movieId', 'title']].sort_values('userId').to_csv('D:\movie_data\ml-latest/data.csv', index=False)
    # 将合并后的数据集输出保存到桌面 以备后续分析
    files = pd.read_csv('D:\movie_data\ml-latest/data.csv',encoding='utf-8')
    #print(files.head(5))
    # 逐行读取刚刚合并并保存的数据集
    content = []
    with open('D:\movie_data\ml-latest/data.csv',encoding='utf8') as fp:
        content = fp.readlines()

    # 将用户、评分、和电影写入字典data
    data = {}
    for line in content[1:100]:
        line = line.strip().split(',')
        # 如果字典中没有某位用户，则使用用户ID来创建这位用户
        if not line[0] in data.keys():
            data[line[0]] = {line[3]: line[1]}
        # 否则直接添加以该用户ID为key字典中
        else:
            data[line[0]][line[3]] = line[1]
    print(data)
