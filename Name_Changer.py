print "Welcome to Efosa's Amazing Name Generator\n"
print "Please type in your first and last name\n and see what your new name will be.\n"
print "It's exciting isn't it!!!!"
first_name = raw_input("Please type in your first name: ")
second_name = raw_input("Please type in your last name: ")
print 
print "Now your new name is...\n"
first_names = {"a":"Obnoxious", "b":"Gifted", "c":"Beautiful", "d":"Enormous", "e":"Crazy", "f":"Childish", "g":"Frosty", "h":"Creative", "i":"Edgy", "j":"Powerful", "k":"Bloody", "l":"Stormy", "m":"Sleepy", "n":"Wandering", "o":"Danger", "p":"Fancy", "q":"Grumpy", "r":"Creepy", "s":"Charming", "t":"Lucky", "u":"Fantastic", "v":"Glorious", "w":"Zany", "x":"Empty", "y":"Dirty", "z":"Silky"}
second_names = {"a":"Beyond", "b":"Gears", "c":"War", "d":"Money", "e":"City", "f":"Sandwich", "g":"Banana", "h":"Podcast", "i":"Halo", "j":"Baby", "k":"Punch", "l":"Arm", "m":"Star", "n":"Kick", "o":"Gamer", "p":"Tacos", "q":"Ham", "r":"Duck", "s":"Contender", "t":"Challenge", "u":"Puzzles", "v":"Knight", "w":"Ranger", "x":"Ice Cream", "y":"Apple", "z":"Sega"}

first_name = first_name.lower()
second_name = second_name.lower()

for change in first_names:
	if first_name[0] == change:
		new_first_name = first_names[change]
		print new_first_name 
			
for changes in second_names:
	if second_name[0] == changes:
		new_second_name = second_names[changes]
		print new_second_name 

print 
print "Congratulations!! your new first name is %s, and last name is %s" % (new_first_name, new_second_name)
print 
final_name = new_first_name + " " + new_second_name
print "Welcome", final_name 
