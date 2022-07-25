import streamlit as st
import sys

tab1, tab2= st.tabs(["First ", "Second"])
with tab1:
    st.title("Welcome to streamlit practices lab !")
    st.write("Here we're going to use python to solve some problems .")
    st.write("There'll be a practice followed by the solution that would be explained through a comment .")

    st.write("Here i'll import the library that we'll be using through that line of code :")
    st.code("""
    import streamlit as st
    #I've used that to import streamlit library as st for a shortcut so
    #i won't write on every call streamlit , i'll write st unstaid


    import sys
    #I've used that to display the used version of python
    """,language="python")
    st.write('---')

    st.header("First practice : ")
    st.write("### Display -hello world !- on the page ")
    st.write("here's the solution : hello world !")
    code="""
    #This is the code solution :
    st.write("hello world !")
    #I've used the function st.write
    """
    st.code(code,language="python")



    st.write('---')




    st.header("Second practice : ")
    st.write("### Display -Hello , i'm born on the year 1997 welcome !- with the date number stored on another variable .")


    year=1997
    st.write("Here's the solution : i'm born on the year ",year,' welcome ! ')
    st.write("Here's another solution : i'm born on the year "+str(year)+" welcome !")
    st.write(f"and here's another solution :i'm born on the year {year} welcome!")

    st.code("""
    year=1997
    st.write("i'm born on the year ",year,' welcome ! ')
    #Here as you can see , i've used a coma to separate the year from the string
    #so it displayed it not as a string but as a number , as it is ,
    #and that's why it's wroten differently .

    st.write("i'm born on the year "+str(year)+" welcome !")
    #Here i've changed the type of the number to a string then i've
    #concatenate it with the rest of the string and that's why it's
    #all writen on the same way .


    st.write(f"i'm born on the year {year}")
    #This is the same thing as the second solution but it's faster .

    """,language="python")


    st.write('---')
    st.header("3rd practice : ")
    st.write('### Display the used version of streamlit and python .')
    st.write("here's the solution : ")
    st.write("The used version of streamlit : "+st.__version__ )
    st.write("The used version of python : "+sys.version)
    st.code("""
    #Here's the code solution :
    st.write("The used version of streamlit : "+st.__version__ )
    #st.__version__ would giveback the streamlit version used .
    st.write("The used version of python : "+sys.version)
    #sys.version would give back the version of python used with
    #more informations

    """,language="python")


    st.write('---')
    st.header('4th practice : ')
    st.write("### Display the current time and date ")
    st.write("Here's the solution : ")


    import datetime
    current_time_and_date = datetime.datetime.now()
    st.write("The current time and date is : "+str(current_time_and_date))
    st.code("""
    import datetime
    #I've imported that library to use it to extract the time and the date of
    #the current momment .


    current_time_and_date = datetime.datetime.now()
    #Then i've called the function now from datetime to extract the data
    #and put it into a variable

    st.write("The current time and date is : "+str(current_time_and_date))
    #Then i've wrote it through concatenation with the string also
    #changing the datatype to str
    """,language="python")





with tab2:
    st.title("This is the continuation of the previous practices .")
    st.header("5th Practice")
    st.write("### Write a program that would take two intiger as an entry , then the user would choose to substract , add ,devide or multiply them together .(Take in consideration the devision by 0)")
    st.write("Here's the solution : ")
    #Definition of the functions with lambda
    add=lambda x,y:x+y
    substract=lambda x,y:x-y
    devide=lambda x,y:x/y if y!=0 else 'error'
    multiply=lambda x,y:x*y
    t1,t2=st.columns([1,1])
    with t1:
        x = st.number_input('Enter the first number')
    with t2:
        y = st.number_input('Enter the second number')

    st.write("choose the operation :")
    result=0
    f1,f2,f3,f4=st.columns([1,1,1,1])
    with f1:
        addition=st.button('Addition')
    with f2:
        substraction=st.button('Substraction')
    with f3:
        multiplication=st.button('Multiplication')
    with f4:
        devision=st.button('Devision')
    if addition:
        result=add(x,y)
    elif substraction:
        result=substract(x,y)
    elif devision:
        result=devide(x,y)
    elif multiplication:
        result=multiply(x,y)
    st.write(f'The result is : {result}')

    st.write("Here's the code solution :")
    st.code("""

add=lambda x,y:x+y
substract=lambda x,y:x-y
devide=lambda x,y:x/y if y!=0 else 'error'
multiply=lambda x,y:x*y

#I've defined all the functions with lambda , it's faster and effecient .

t1,t2=st.columns([1,1])
#Then i've created colummns with equal size in order to be displayed on
#the same row and to let the user freely enter the variable and on
#a clean way .

with t1:
    x = st.number_input('Enter the first number')
with t2:
    y = st.number_input('Enter the second number')
#Then i've got the variables given by the input function and stored it
#on x and y


st.write("choose the operation :")
#That would print to choose the operation

result=0
#I've made a variable called result to store the calculation in it .


f1,f2,f3,f4=st.columns([1,1,1,1])
#Then i've created columns in order to let the user the freedom of choise

with f1:
    addition=st.button('Addition')
with f2:
    substraction=st.button('Substraction')
with f3:
    multiplication=st.button('Multiplication')
with f4:
    devision=st.button('Devision')
#I've stored the button calls in variables by their name

if addition:
    result=add(x,y)
elif substraction:
    result=substract(x,y)
elif devision:
    result=devide(x,y)
elif multiplication:
    result=multiply(x,y)
#Then i've checked each independent variable name with the if and
#else statements then stored the return value from each
#function call on the result.


st.write(f'The result is : {result}')
#And by the end i've wrote the result with st.write and used the format
#function to write it on a simple way .
#And voila !
    """,language="python")

    st.write('---')
    st.header("6th practice")
    st.write("### Write an algorithm that would calculate a second degree function :(x+c)^2  ")
    sdf=lambda x,c:x*x+2*x+c
    st.write("Here's the formula of a second degree function : (x+c)^2 , please enter the following numbers")
    lm1,lm2=st.columns([1,1])
    with lm1:
        x=st.number_input("Enter the value of X :")
    with lm2:
        c=st.number_input("Enter the value of C ;")
    st.write("Here's the result : ",sdf(x,c))

    st.write("Here's the code solution : ")
    st.code("""
sdf=lambda x,c:x*x+2*x+c
#Here i've created a function with lambda , it's quick and effecient
#to calculate the result of the second degree function


lm1,lm2=st.columns([1,1])
#Then i've created two columns so the user would see clearly
#what to enter and where


with lm1:
    x=st.number_input("Enter the value of X :")
with lm2:
    c=st.number_input("Enter the value of C ;")
#I've used same thing on the previous practice .
#i received the input using the streamlit api call .


st.write("Here's the result : ",sdf(x,c))
#By the end i've displayed the results and didn't switch to string .
    """,language ="python")
