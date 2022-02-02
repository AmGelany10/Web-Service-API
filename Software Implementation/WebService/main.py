import requests

import main


def search_recipe(recipe_name):
    url = "https://spoonacular-recipe-food-nutrition-v1.p.rapidapi.com/recipes/search"

    querystring = {"query": f"{recipe_name}"}

    headers = {
        'x-rapidapi-host': "spoonacular-recipe-food-nutrition-v1.p.rapidapi.com",
        'x-rapidapi-key': "48231313a4mshf5aa65b685917d4p1a471cjsnf2019145ef1d"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)

     #print(response.text)
    #print(response.json())
    dict_content = {}
    list_data = response.json()['results']
    i = 0
    #print(len(list_data))
    while i < len(list_data):
        for item in list_data[i]:
            dict_content[item] = list_data[i][item]
        # To be continued
        i = i + 1
    if len(dict_content) == 0:
        return "not found"  #Mulukhiyah
    #print(dict_content)
    key_list = list(dict_content.keys())
    val_list = list(dict_content.values())
    x = key_list[1]+" : "+str(val_list[1]) + "\n" + key_list[2]+" : "+str(val_list[2]) + "\n" + key_list[3]+" : "+str(val_list[3]) +"\n" + key_list[4] + " : " + str(val_list[4]) + "\n" + key_list[6]+" : " + str(val_list[6])
    #print(str(x))
    return x
################################################
def post_secret_instructions(instructions):

    url = "https://spoonacular-recipe-food-nutrition-v1.p.rapidapi.com/recipes/analyzeInstructions"

    payload = f"instructions={instructions.replace(' ', '%20')}"
    headers = {
        'content-type': "application/x-www-form-urlencoded",
        'x-rapidapi-host': "spoonacular-recipe-food-nutrition-v1.p.rapidapi.com",
        'x-rapidapi-key': "48231313a4mshf5aa65b685917d4p1a471cjsnf2019145ef1d"
    }

    response = requests.request("POST", url, data=payload, headers=headers)

    return(response.status_code)
################################################
def get_secret_instructions():
    url = "https://spoonacular-recipe-food-nutrition-v1.p.rapidapi.com/recipes/324694/analyzedInstructions"

    querystring = {"stepBreakdown": "true"}

    headers = {
        'x-rapidapi-host': "spoonacular-recipe-food-nutrition-v1.p.rapidapi.com",
        'x-rapidapi-key': "48231313a4mshf5aa65b685917d4p1a471cjsnf2019145ef1d"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)
    ### to get only the steps
    dict_content = {}
    list_data = response.json()
    i = 0
    while i < len(list_data):
        for item in list_data[i]:
            dict_content[item] = list_data[i][item]
        # To be continued
        i = i + 1
    j = 0
    x = ""
    while j < len(dict_content['steps']):
        x=x+str(j+1) + ") "
        x = x + dict_content['steps'][j]['step'] + "\n"
        # To be continued
        j = j + 1
    return x

    #return(response.text)
# get_secret_instructions()
# # secret_instructions("Gelany")
# #search_recipe('koshary')



########################################
#1# search_recipe(recipe_name) ==> takes recipe name and return all the matched results,
# if you want you can either get all the results and list them or to be satisfied by only the last match.
# If you want to list all of matches then there exists a part after the inner loop called
# to be continued you can continue from there by utilizing each resulted dict
#2# secret_instructions(instructions) ==> pass the instructions to it and it will be posted
#3# get_secret_instructions() ==> just call it and it will return all the values recorded
########################################


######################################################### GUI part ###########################
import sys

from PyQt5.QtWidgets import (
    QApplication,
    QCheckBox,
    QLineEdit,
    QLabel,
    QMessageBox,
    QPushButton,
    QTabWidget,
    QFormLayout,
    QVBoxLayout,
    QWidget,
)

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Yummy Recipes")
        self.resize(370, 100)
        # Create a top-level layout
        layout = QVBoxLayout()
        self.setLayout(layout)
        # Create the tab widget with two tabs
        tabs = QTabWidget()
        tabs.addTab(self.getReceipeTabUI(), "Get Recipe")
        tabs.addTab(self.getInsTabUI(), "Get Instruction")
        tabs.addTab(self.postInsTabUI(), "Post Instruction")
        layout.addWidget(tabs)

    def getReceipeTabUI(self):
        """Create the Get Recipe page UI."""

        generalTab = QWidget()
        outer_layout = QVBoxLayout()
        # Create a form layout for the label and line edit
        topLayout = QFormLayout()
        # Add a label and a line edit to the form layout
        l1 = QLineEdit("e.g. Koshari")
        topLayout.addRow("Recipe Name:", l1)
        # Create a layout for the checkboxes
        optionsLayout = QVBoxLayout()
        # optionsLayout.addWidget(QCheckBox("General Option 1"))
        # optionsLayout.addWidget(QCheckBox("General Option 2"))
        # Nest the inner layouts into the outer layout
        outer_layout.addLayout(topLayout)
        outer_layout.addLayout(optionsLayout)
        #######################
        the_recp = QLabel()
        def button_1_clicked():
            the_recp.setText(f'{main.search_recipe(l1.text())}')
            optionsLayout.addWidget(the_recp)
            # optionsLayout.addWidget(QLabel("you pressed the button"))
            # optionsLayout.update()
            # optionsLayout.addRow("you pressed the button", QLineEdit())

        b1 = QPushButton("Gotta")
        optionsLayout.addWidget(b1)
        b1.clicked.connect(button_1_clicked)
        ##########################
        generalTab.setLayout(outer_layout)
        return generalTab

    def getInsTabUI(self):
        """Create the Get Instruction page UI."""
        networkTab2 = QWidget()
        Outerlayout2 = QVBoxLayout()
        # Outerlayout2.addWidget(QCheckBox("Network Option 1"))
        # Outerlayout2.addWidget(QCheckBox("Network Option 2"))
        the_ins = QLabel()
        def button_2_clicked():
            the_ins.setText(f'{main.get_secret_instructions()}')
            Outerlayout2.addWidget(the_ins)
        b2 = QPushButton("Give me instruction")
        Outerlayout2.addWidget(b2)
        b2.clicked.connect(button_2_clicked)
        networkTab2.setLayout(Outerlayout2)
        return networkTab2

    def postInsTabUI(self):
        """Create the Post Instruction page UI."""
        networkTab1 = QWidget()
        Outerlayout3 = QVBoxLayout()
        # Create a form layout for the label and line edit
        topLayout = QFormLayout()
        # Nest the inner layouts into the outer layout
        Outerlayout3.addLayout(topLayout)
        # message box to be shown when b3 clicked
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setWindowTitle("Notification")
        msg.setText("Request proceeded")
        # Add a label and a line edit to the form layout
        post_ins = QLineEdit()
        topLayout.addRow("Post Ins:", post_ins)
        # button creation + listener method
        def button_3_clicked():
            main.post_secret_instructions(post_ins.text())
            msg.exec_()
        b3 = QPushButton("Post")
        Outerlayout3.addWidget(b3)
        b3.clicked.connect(button_3_clicked)
        networkTab1.setLayout(Outerlayout3)
        return networkTab1


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec_())