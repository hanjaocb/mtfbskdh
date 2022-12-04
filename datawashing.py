import pandas as pd

#-----------------------------------------------
#函数名：基础队伍的筛选 
#输入：初始的队伍 或可称作目标队伍  ，经过筛选的数据（type：dataframe）
#输出：下一个需要进行筛选的队伍名称，和筛选出的数据哪一行数据包含的所有信息
#-----------------------------------------------
def match_game_basic_func(team_wanted,df_filtered):
    df_2 = df_filtered.loc[df_ini['Home'] == team_wanted][:1]# 筛选出主队名字符合输入名称的一行
    team_next = df_2["Away"].iloc[0]#获取客队名字
    print("team_next:",team_next)
    return team_next,df_2

#-----------------------------------------------
#函数名：通过输入初始队伍返回之前所有相关比赛的数据
#输入：初始的队伍 或可称作目标队伍  ，经过筛选的数据（type：dataframe）
#输出：下一个需要进行筛选的队伍名称，和筛选出的数据哪一行数据包含的所有信息
#-----------------------------------------------

def Run_selection(initial_team,df_filtered): 
    df_final= pd.DataFrame()#最后的信息总表
    for i in range(10):
        team_next_find,df_iter= match_game_basic_func(initial_team,df_filtered)#获取客队名字与那场比赛的整体数据
        initial_team=team_next_find #将想要筛选的队伍名更新成上一场比赛的客场队伍
        df_final=df_final.append(df_iter) #插入总表
        print(df_final)
    return df_final
    
    # df_final.to_csv(r"\\Mac\Home\Desktop\booking\out11111111.csv")
         
    

if __name__ == "__main__":
    df_ini = pd.read_csv(r"\\Mac\Home\Desktop\booking\Ligue1Fixture.csv")
    df_filtered = df_ini[["Date", "Home", "Away", "MatchID"]]#里面的列可以随意更改
    initial_team = "Lens"#输入队伍
    Run_selection(initial_team,df_filtered)


    
    
    
    
    
    
    
    
    
    
    
    
    
    
    # team_next_find= match_game_basic_func(team_wanted,df_filtered)
    # team_wanted = team_next_find
    # print (team_wanted)
    # team_next_find = match_game_basic_func(team_wanted_2)
    # team_next_find, df_insert = match_game_basic_func(team_wanted)

    # # while team_next_find !=  team_wanted:
    # for i in range(3):

    #     team_previous = team_wanted
    #     team_next_find, df_insert = match_game_basic_func(team_previous)
    #     print(team_previous)
    #     team_wanted = team_next_find
    #     print(team_previous)
    #     print(df_insert)

    # df_final=df_final.append({'A': i}, ignore_index=True)###问题出在这里 --
    # print (df_final)
    # if team_next_find ==  team_wanted:
    #     break
