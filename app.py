import inquirer, os
import pandas as pd



class LaStartup_Workiz:

    def __init__(self) -> None:
        pass


    def query_term(self):

        questions = [
            inquirer.List(
                "selected_term",
                message="What term are you looking for?",
                choices=list(data['title2']),
            ),

            inquirer.List(
                "selected_length",
                message="What nm do you need?",
                choices=["Short Answer", "Full Answer"],
            ),
        ]

        answers = inquirer.prompt(questions)

        return answers


    def run_app(self, data):
        while True:
            result = self.query_term()
            os.system('clear')
            subset = data[data['title2'] == result['selected_term']].reset_index(drop = True)
            print("-"*20)
            print(subset['title2'][0])
            print("-"*40)
            print(subset['main_header'][0])
            print("-"*100)
            print(subset['sub_header'][0])
            print("-"*100, "\n")

            if result['selected_length'] == "Short Answer":
                print_mini_text = [print(f"\n{sentence}") for sentence in subset['mini_answer'][0].split(".")]
            else:
                print_large_text = [print(f"\n{sentence}") for sentence in subset['large_answer'][0].split(" | ")]

            print("\n\n\n\n")

    def remove_last_row(self, data, save_it):
        data = data[:-1]

        if save_it:
            print("Updating Data...")
            data_tmp = data.copy()
            try:
                print("Removing Last Data Sample...")
                del data_tmp['title2']
            except:
                pass
            data_tmp.to_csv("lastartup_content.csv", index = False)

        return data
    
    def print_last_row(self, data):
        print(data[-1:])

    def insert_new_sample(self, data, save_it):

        term = input("\nEnter Term Name\n----------\n")
        title = input("\nEnter Term Title\n----------\n")
        main_header = input("\nEnter Main Header\n----------\n")
        sub_header = input("\nEnter Sub Header\n----------\n")
        mini_answer = input("\nEnter Short Answer\n----------\n")
        large_answer = input("\nEnter Full Answer\n----------\n")

        new_data = pd.DataFrame({"title":[" מה זה"+title+"?"], "abbreviated_description":[None],
                                "link":[None], "main_header":[main_header], "sub_header":[sub_header], 
                                "mini_answer":mini_answer, "large_answer":large_answer,  "title2":[term]})
        #self.print_last_row(data)
        #print(new_data[-1:])
        data = pd.concat([data, new_data])

        if save_it:
            print("Updating Data...")
            data_tmp = data.copy()
            try:
                del data_tmp['title2']
            except:
                pass
            data_tmp.to_csv("lastartup_content.csv", index = False)

        print("\n\n\n\n")
        return data




if __name__ == "__main__":

    data = pd.read_csv("lastartup_content.csv")
    data['title2'] = [i.split("מה זה")[1].split("?")[0] for i in data['title']]

    lsw = LaStartup_Workiz()
    #lsw.print_last_row(data)
    #data = lsw.insert_new_sample(data, True)
    #lsw.print_last_row(data)
    #data = lsw.remove_last_row(data, True)
    #lsw.print_last_row(data)
    lsw.run_app(data)

