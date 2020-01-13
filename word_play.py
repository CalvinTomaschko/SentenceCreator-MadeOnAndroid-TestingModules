import random

def add_to_a_list(a_list):
	
	string_to_add = input("Type in the word or punctuation you'd like to have added")
	print (f"Is this what you'd like added -->{string_to_add}<--")
	confirming = "bad answer"
			
	# if enter incorrectly
	confirmation_counter = 0 
	while confirming[0] not in ['y','n']:
		confirmation_counter += 1
		if confirmation_counter > 1:
			print ("Sorry, invalid response")		
		confirming = input ("if yes type 'y' if not type 'n' ")
	
	# if entered "no", resubmit, then confirm, check if correct
	while confirming[0] == 'n':
		string_to_add = input("Ok, let's try again, type in what you'd like to submit here.")
		print (f"Is this what you'd like added -->{string_to_add}<--")
		confirming = "bad answer"
		
		# if entered incorrectly within a no response correction
		confirmation_counter = 0 
		while confirming[0] not in ['y','n']:
			confirmation_counter += 1
			if confirmation_counter > 1:
				print ("Sorry, invalid response")		
			confirming = input ("if yes type 'y' if not type 'n' ")
			
	a_list.append(string_to_add)
	print (a_list)
				
def article_add_previous_string_delete(a_string,a_list):
	article_to_add = random.choice(a_list)
	a_string = article_to_add	
	return a_string

def add_noun (a_string, a_list):	
	random_noun = random.choice(a_list)
	space_random_noun = " "+random_noun
	a_string += space_random_noun
	return a_string			

def add_verb (a_string, a_list):	
	random_verb = random.choice(a_list)
	space_random_verb = " "+random_noun
	a_string += space_random_verb
	return a_string
			
def add_punctuation (a_string, a_list):	
	random_punctuation = random.choice(a_list)
	space_random_punctuation = " "+random_punctuation
	a_string += space_random_punctuation
	return a_string
			
def run_random_sentence (string, art_list, noun_list, verb_list, punct_list):
	tester_string = article_add_previous_string_delete(string,art_list)	
	# print (tester_string)
	tester_string_2 = add_noun(tester_string, noun_list)	
	# print (tester_string_2)
	tester_string_3 = add_noun(tester_string_2, verb_list)	
	# print (tester_string_3)	
	tester_string_4 = add_noun(tester_string_3, punct_list)	
	print (tester_string_4)
	#This runs a the sentence generator and outputs a sentence
