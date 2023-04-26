from math import *
class EuclideanDistance(object):
    data = {}
    content = []
    def __init__(self):

        with open('D:\movie_data\ml-latest/data.csv', encoding='utf8') as fp:
            self.content = fp.readlines()
        # 将用户、评分、和电影写入字典data
        for line in self.content[1:100]:
            line = line.strip().split(',')
            # 如果字典中没有某位用户，则使用用户ID来创建这位用户
            if not line[0] in self.data.keys():
                self.data[line[0]] = {line[3]: line[1]}
            # 否则直接添加以该用户ID为key字典中
            else:
                self.data[line[0]][line[3]] = line[1]
    #print(data)


    def Euclidean(self,user1,user2):
        # 取出两位用户评论过的电影和评分
        user1_data = self.data[user1]
        user2_data = self.data[user2]
        distance = 0
        # 找到两位用户都评论过的电影，并计算欧式距离
        for key in user1_data.keys():
            if key in user2_data.keys():
                # 注意，distance越大表示两者越相似
                distance += pow(float(user1_data[key]) - float(user2_data[key]), 2)

        return 1 / (1 + sqrt(distance))  # 这里返回值越小，相似度越大

    # 计算某个用户与其他用户的相似度
    def top10_simliar(self,userID):
        #userID = str(userID)
        res = []
        for userid in self.data.keys():
            # 排除与自己计算相似度
            if not userid == userID:
                simliar = self.Euclidean(userID, userid)
                res.append((userid, simliar))
        res.sort(key=lambda val: val[1])
        return res[:4]


    # RES = top10_simliar('2')
    # print(RES)
    # 用户之间相似度结果：0表示两位的影评几乎一样，1表示没有共同的影评
    #根据相似度来推荐用户：

    def recommend(self,user):
        #user = str(user)
        # 相似度最高的用户
        top_sim_user = self.top10_simliar(user)[0][0]
        # 相似度最高的用户的观影记录
        items = self.data[top_sim_user]
        recommendations = []
        # 筛选出该用户未观看的电影并添加到列表中
        for item in items.keys():
            if item not in self.data[user].keys():
                recommendations.append((item, items[item]))
        recommendations.sort(key=lambda val: val[1], reverse=True)  # 按照评分排序
        # 返回评分最高的10部电影
        return recommendations[:10]


    # Recommendations = recommend('1',data)
    # print(Recommendations)
