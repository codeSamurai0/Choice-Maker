# A program to helps make choices.

import random
import time
import sys

def main():
	print("Select language, just press Enter for English or type JP for Japanese.")
	language = str(input("> ")	)
	choice_number = 1
	list_of_choices = []
	
	if language == "":
		try:
			print("Press ctrl+c to quit!")
			
			while True:
				choices = int(input("How many choices are there? "))
				print(f"You selected {choices} choices")
				
				for n_of_choices in range(choices):
					choice = str(input(f"What is your {choice_number} choice? "))
					choice_number += 1
					list_of_choices.append(choice)
					print(f"{choice} added to the list")
				result = random.choice(list_of_choices)
				print(f"Here's the result! {result}")
				break
		
		except KeyboardInterrupt:
		    print("\nQuitting...")
		    time.sleep(1)
		    print("Successfully Exited")
		    sys.exit()
		
		except ValueError:
		    print("Please type a number!\n")
		    main()
	
	elif language == "JP".lower():
		try:
			print("ctrl+cでいつでもプログラムを終了できます。")
			
			while True:
				choices = int(input("選択肢の数を指定して下さい。"))
				print(f"あなたは {choices} の選択肢を選んだ。")
				
				for n_of_choices in range(choices):
					choice = str(input(f"{choice_number} の選択は？ "))
					choice_number += 1
					list_of_choices.append(choice)
					print(f"{choice} がリストに追加されました。")
				result = random.choice(list_of_choices)
				print(f"これが結果です！ {result}")
				break
		
		except KeyboardInterrupt:
		    print("\n終了しています...")
		    time.sleep(1)
		    print("終了完了！")
		    sys.exit()
		
		except ValueError:
		    print("数字を入れて下さい！\n")
		    main()
	
	else:
		print("\nType JP or press enter for English!")
		main()
main()
