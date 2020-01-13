# tester project: modules on Android device
# make a sentence using modules for add an article, noun, verb, punctuation 

# This is a project to get used to working on the android system
# ultimately so that I could work on other bigger projects when on the go
# and for the fun of saying I've done this. I have a bluetooth keyboard and enjoy hanging
# my phone on it's bendable tripod legs, using it on buses and trains!

# Jan 3, 2020
# Created by Calvin Tomaschko

import random 
import word_play


random_sentence = "empty"

article_list = ["Dis here","Some kinda", "Ye Ol'", "The", "Thee","Thy", "Thyiest", "A", "Itsa", "Le" ]

noun_list = ["frog", "car", "parade", "pickle", "bologna sandwich","classic statue","light bulb", "1940s airplane", "cat hairball" ]

verb_list = ["launched", "moved", "lept", "paraded","sassed", "clambored", "sang", "collided","danced", "ran", "voted 'yay'"]

punctuation_list = ["!!!!!", "!?", "(punctuation not found, this is not an error)", "? ; )", "..." , ".", "?...!", "mic drop", "!", "?"]

list_dictionary = {"1":article_list, "2":noun_list, "3":verb_list, "4":punctuation_list}

print ("This is a humorous random sentence generator! \n Consisting of an article, noun, verb, then punctuation. \n You can add to the base lists of each category if you'd like \n or submit over and over for some strange sentences.")


#def add_to_a_list(a_list):
#def article_add_previous_string_delete(a_string,a_list):
#def add_noun (a_string, a_list):	
#def add_verb (a_string, a_list):				
#def add_punctuation (a_string, a_list):				
#def run_random_sentence (string, art_list, noun_list, verb_list, punct_list):


still_going = True

while still_going == True:

	user_answer = input("Would you like to 's' for submit, or 'a' for add to a list?")

	while user_answer[0] not in ["s","a"]:
		print ("Woops, it appears that response was not an 's' or an 'a', \n please enter one of those into this prompt to move forward")
		user_answer = input("Would you like to 's' for submit, or 'a' for add to a list?")
	
	# need to make an else of "user_answer == "s" for submit
	
	# They want to Add
	if user_answer == "a":
		chosen_list = input("Which list would you like to add to? \n please input the number next to the list of your choice. \n 1. Article list \n 2. Noun list \n 3. Verb list \n 4. Punctuation list")	
	
		# In case of error			
		while chosen_list not in ["1","2","3","4"]:
			print ("Woopsie, response isn't reading as either 1, 2, 3, or 4")
			chosen_list = input("Let's try again \n Which list would you like to add to? \n please input the number next to the list of your choice. \n 1. Article list \n 2. Noun list \n 3. Verb list \n 4. Punctuation list")
				
		chosen_list_referenced = list_dictionary[chosen_list]
		print (chosen_list_referenced)
		
		# MODULE FUNC
		word_play.add_to_a_list(chosen_list_referenced)
		
		
	else:
		#this is if they picked "s" for submit
		# MODULE FUNC
		word_play.run_random_sentence(random_sentence, article_list, noun_list, verb_list, punctuation_list)
	
	want_continue = input("Continue for another Add or Submit? 'y' for yes, 'n' for no")
	
	#if incorrect, ask a 2nd time, otherwise breaks out
	want_counter = 0
	while want_continue[0] not in ['y','n']:
		want_counter += 1
		if want_counter >2:
			still_going = False
			print ("We're having trouble reading your response, sorry, we'll exit out now \n please leave a note on the github page if this was an error. \n I hope you enjoyed this little work!")
			break
		print ("We're not reading a 'y' or a 'n', please try again")
		want_continue = input("Continue for another Add or Submit? 'y' for yes, 'n' for no")
	if want_continue == "n":
		print ("I hope you enjoyed this little project of fun! Thank you for trying it out")
		still_going = False	
		 		 			 		
		


