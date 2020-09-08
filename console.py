import psycopg2

connection = psycopg2.connect(user = "201701250",
                              password = "Csheth99#0229",
                              host = "10.100.71.21",
                              port = "5432",
                              database = "201701250")

print("You are connected to - 201701250 \n")
cursor = connection.cursor()
cursor.execute("set search_path to cricket")


def Highlights():
	var  =input("Match_ID,Inning_ID,Over,Batsman_ID,Bowler_ID\n").split(',')
	quary = "INSERT INTO highlights VALUES(" + var[0] + "," + var[1] + "," + var[2] + "," + var[3] + "," + var[4] + ")"
	print(quary)
	cursor.execute(quary)

def Highlight_status():
	var = input("Match_ID,Inning_ID,Over,Delivery_status\n").split(',')
	quary = "INSERT INTO highlight VALUES(" + var[0] + "," + var[1] + "," + var[2] + "," + var[
		3] + ")"
	print(quary)
	cursor.execute(quary)

def Statistics():
	var = input("Player_ID,Match_ID,Run_scored,\n").split(',')
	quary = "INSERT INTO highlight VALUES(" + var[0] + "," + var[1] + "," + var[2] + "," + var[
		3] + ")"
	print(quary)
	cursor.execute(quary)

def update():
    x = input("enter your update query : \n ")
    cursor.execute(x)
    print(cursor.statusmessage)
    connection.commit()

def selspecific():
	list = ["How many wickets taken by deepak chahar against BAN in t20 match.",
			"Which player scored more than 50runs more than two times.",
			"Give the player name and team name of player which has best batting average in odi.",
			"Give the player name and team name of player which has   best bowling  average in t20.",
			"Give the player info of the top 5 performance in  given odi match.",
			"How many % of boundary of total runs scored by all player."]
	listq = ["select \"Wickets\" from \"statistics\" s natural join(select distinct \"Match_ID\" from \"Match_Team\" mt natural join(select \"Match_ID\" from player join \"Match_Player\" mp on player.\"ID\" = mp.\"Player_ID\" join \"match\" on mp.\"Match_ID\" = \"match\".\"ID\"where match.\"Type\" = 'T20') as abc join \"team\" on team.\"ID\"=mt.\"Team_ID\" where team.\"Name\"='Bangladesh') as def join \"player\" on player.\"ID\"=s.\"Player_ID\" where player.\"Name\"='Deepak Chahar';",
			 "select \"Player_ID\" from(select count(\"Player_ID\"),\"Player_ID\" from \"statistics\"  where \"Runs_scored\">=50 group by \"Player_ID\")as abc where abc.count>=2",
			 "select pl.*,average from average_runs('ODI') ar  join player  pl on pl.\"ID\" = ar.\"player_id\"  where average is not null  order by ar.average desc  limit 1; ",
			 "select pl.*,average from bowling_average('T20') ba join player pl on pl.\"ID\" = ba.\"player_id\"where average>0.00 order by average limit 1; ",
			 "select * from statistics s  join match m on m.\"ID\"=s.\"Match_ID\" where m.\"ID\" = 5 and s.\"Runs_scored\" is not null order by s.\"Runs_scored\" desc limit 5; ",
			 "select p.\"ID\",((sum(s.\"Fours\" * 4)+sum(s.\"Sixes\" *6 )) *1.0/ sum(s.\"Runs_scored\"))*100 as boundaries from player p join statistics s on s.\"Player_ID\" = p.\"ID\" where s.\"Fours\" is not null and s.\"Runs_scored\" is not null and s.\"Runs_scored\">0 group by p.\"ID\" order by boundaries desc "
			]

	print(" Enter a number to choose query from list")
	z = int(input("\n Enter 1: " + list[0] + "\n Enter 2:" + list[1] + "\n Enter 3: " + list[2] +
				  "\n Enter 4: " + list[3] + "\n Enter 5:" + list[4] + "\n Enter 6: " + list[5] + "\n"))
	if (z > 6):
		print("Enter valid number \n")
		selspecific()
	x = listq[int(z - 1)]
	y = x
	cursor.execute(y)
	colnames = [desc[0] for desc in cursor.description]
	print(colnames)
	cursor.execute(x)
	rows = cursor.fetchall()
	for r in rows:
		print(r)
	print("\n\n")

connection.commit()




while True:
	print('1 : Insert')
	print('2 : Update')
	print('3 : Query')
	print('4 : End')

	choice = input()
	if (int(choice) ==1):
		print('1 : Make Highlight \n')
		print('2 : Make Highlight_Status \n')
		print('3 : Create Statistics \n')
		enter_choice =input()
		if (int(enter_choice) == 1):
			Highlights()
		elif (int(enter_choice) == 2):
			Highlight_status()
		elif (int(enter_choice) == 3):
			Statistics()
		else:
			print('Invalid ')

	elif (int(choice) ==2):
		update()
	elif (int(choice)==3):
		selspecific()
	else:
		break;

if(connection):
    cursor.close()
    connection.close()
    print("PostgreSQL connection is closed")
