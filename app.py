from flask import Flask                                 #Import Flask library
app = Flask(__name__) 

#URL of webpage we'll visit to view result '/' = homepage
@app.route('/')
#defines route function. The return will show up in browser when you vist above URL                          
def homepage():  
    #docstring. This is for you to read. Doesn't do anything.                                  
    """Shows a greeting to the user."""
    #Returns page contents. 
    return 'Are you there, world? It\'s me, Ducky!'

@app.route('/penguins')
def penguins():
    return 'Penguins are cute!'

@app.route('/animal/<users_animal>')
def favorite_animal(users_animal):
    """Display a message to the user that changes based on their favorite animal"""
    return f"Wow, {users_animal} is my favorite animal, too!"

@app.route('/dessert/<users_dessert>')
def favorite_dessert(users_dessert):
    return f"How did you know I liked {users_dessert}?"

@app.route('/madlibs/<adjective>/<noun>')
def mad_lib(adjective, noun):
    return f"...as he jumped into his convertible {noun} and drove off with his {adjective} wife."

@app.route('/multiply/<number1>/<number2>')
def multiply_nums(number1, number2):
    number3 = int(number1) * int(number2)
    if number1.isdigit() and number2.isdigit() != True:
        return "Invalid inputs. Please try again by entering 2 numbers!"
    if number1.isdigit() and number2.isdigit() == True:
        return f"{number1} times {number2} is {number3}"

@app.route('/sayntimes/<word>/<n>')
def multiply_words(word, n):
    return " ".join([word] * int(n))


#How to run the server? "python3 app.py" in terminal to run after this line. 
if __name__ == '__main__':
    app.run(debug=True)

