## Name of Project: Quizz app (CLI)

The game will store questions and answers in a file. When you run it, it will ask the questions and check your answers against those in the file. At the end of the quiz, it will tell you how many questions you got right. It will also allow you to add new questions and answers to the quiz file. 

To use this app clone the repository or open in gitpod. You will have to install the following packages using these commands in the CLI:

pip3 install flask
pip3 install flask-pymongo
pip3 install pymongo
pip3 install dnspython

To run the app type:

pyhton3 quiz.py

When you run the game, you will be presented with a menu in the CLI, with the following options: the first option to ask questions; the second to add a question; and the third to exit the game. If you select option 1 to ask questions, the game will display each quiz question in turn, asking for the answer to each one. When you give an answer, the game will indicate whether it's right or wrong before moving to the next question. After all of the questions have been answered, the game will display how many out of the total number of questions asked that you got right. It will then return to the main menu. If we select option 2 to add a question, the game will prompt the user for the question and the answer, and it will append these to the questions file. It will then return to the main menu. Finally, if we choose option 3 then the game will simply shut down.
