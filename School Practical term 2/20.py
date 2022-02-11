players=[(103,"Ritika",3001),(104,"John",2819),(101, "Razia",3451),(105, "Tarandeep", 2971)]
points=[i[2] for i in players]
for i in range(len(points)-1):
    for j in range(len(points)-i-1):
        if points[j] > points[j+1]:
            points[j],points[j+1] = points[j+1],points[j]
            players[j],players[j+1] = players[j+1],players[j]

print("Players according to their points  \n",players)
            