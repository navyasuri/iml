fp = open('pokemon.csv')

# wp = open('clean.csv', 'w')

# for line in fp:
#     line = line.strip().split(",")
#     print(line)

# fp.close()
# wp.close()
# for line in fp:
#     line = line.lower()
#     print(line)
#     exit()


s = "number,name,type_1,type_2,total,hp,attack,defense,sp_atk,sp_def,speed,generation,islegendary,color,hasgender,pr_male,egg_group_1,egg_group_2,hasmegaevolution,height_m,weight_kg,catch_rate,body_style"
fields = s.split(',')
q = "CREATE TABLE pokemon "
for field in fields:
    q += str(field)+" VARCHAR (255), "
print(q)

CREATE TABLE pokemon (number VARCHAR (255), name VARCHAR (255), type_1 VARCHAR (255), type_2 VARCHAR (255), total VARCHAR (255), hp VARCHAR (255), attack VARCHAR (255), defense VARCHAR (255), sp_atk VARCHAR (255), sp_def VARCHAR (255), speed VARCHAR (255), generation VARCHAR (255), islegendary VARCHAR (255), color VARCHAR (255), hasgender VARCHAR (255), pr_male VARCHAR (255), egg_group_1 VARCHAR (255), egg_group_2 VARCHAR (255), hasmegaevolution VARCHAR (255), height_m VARCHAR (255), weight_kg VARCHAR (255), catch_rate VARCHAR (255), body_style VARCHAR (255))