import requests
import json
r = requests.get("https://api.stratz.com/api/v1/player/179017926")

player = r.text
#convert str dict to real dict
dict_player = json.loads(player)
#ดึงข้อมูลภาพรวม
steam_account = dict_player['steamAccount']
# print(dict_player)
# #rank part
# rank = {
#     "1":"Herald",
#     "2":"Guardian",
#     "3":"Crusader",
#     "4":"Archon",
#     "5":"Legend",
#     "6":"Ancient",
#     "7":"Divine",
#     "8":"Immortal"
# }
# rank_player = str(steam_account["seasonRank"])
# for i in rank:
#     if i == rank_player[0] :
#         if rank_player[0] == "8":
#             real_rank = rank[i]
#             real_rank+=(" {}".format(steam_account['seasonLeaderboardRank']))
#             break
#         else:
#             real_rank = rank[i] #เเรงค์ของผู้เล่น
#             real_rank+=(" {}".format(rank_player[1]))
#             break
#     else:
#         pass
# print(real_rank)

#check smurf
check_smurf = steam_account['smurfFlag']
if check_smurf > 0:
    print("Smurf !!!!!")
else:
    print("Not smurf (Maybe)")