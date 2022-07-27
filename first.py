import streamlit as st
import sys

tab1, tab2,tab3,tab4= st.tabs(["First ", "Second","Third","Fourth"])
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

with tab3:
    st.title("This is the third part of the basics of python and streamlit .")
    st.header("7th practice")
    st.write("### Write a program that would find the smallest and the biggest number in an array of 1 Dimention , the length of the array could be any , the array contains floats . (take into consideration the empty array .)")
    st.write("Here's the solution :")

    array=[14,8,9,25,0,-1]
    #array=[]

    #I've defined two arrays one that contains numbers and the other is
    #empty

    #At the beginning i've defined the array that i'll be working with.
    st.write("The array is : ",array)

    def small_big(arr):
        if len(arr)!=0:
            small=arr[0]
            big=arr[0]
        else :
            return "The array is empty ."
        for i in array:
            if i<small :
                small=i
            if i>big:
                big=i
        return big,small



    result = small_big(array)
    if isinstance(result, str):
        st.write("The array is empty")
    else :
        big,small=small_big(array)
        st.write(f"The smallest number of the array is {small} and the biggest number of the array is {big} .")
    st.write("Here's the code solution :")


    st.code("""
array=[14,8,9,25,0,-1]
#array=[]

#I've defined two arrays one that contains numbers and the other is
#empty

#At the beginning i've defined the array that i'll be working with.
st.write("The array is : ",array)

def small_big(arr):
    if len(arr)!=0:
        small=arr[0]
        big=arr[0]
    else :
        return "The array is empty ."
    for i in array:
        if i<small :
            small=i
        if i>big:
            big=i
    return big,small
#Then i've defined the function that has two return vales .
#I've put the first array of the list into the variable
#small and big that refers to the smallest and the biggest
#variables on the array .
#Then i went through the list looking if there was any variable
#inside the list if its bigger than the big or smaller than the
#small variable and from there i've changed the values .
result = small_big(array)
if isinstance(result, str):
    st.write("The array is empty")
else :
    big,small=small_big(array)
    st.write(f"The smallest number of the array is {small} and the biggest number of the array is {big} .")
#I've displayed the results in case the array is empty and in case
#there's numbers on the array .
""" ,language="python")
    st.write("---")

    st.header("8th practice ")
    st.write("### Write a program that would append one number into the array and remove it from the array .(take in consideration the empty array )")
    st.write("Here's the solution :")

    arrr=[0,5,12,150,25]
    if "arrr" not in st.session_state:
        st.session_state['arrr']=arrr

    added_value=st.number_input("Enter the value of the last element: ",1)
    ladd=st.button("Add to the list ! !")
    if ladd:
        st.session_state['arrr'].append(added_value)
    popping=st.button("Pop the last element out !")
    if popping:
        if st.session_state['arrr']!=[]:
            st.session_state['arrr'].pop()

    st.write(st.session_state['arrr'])

    st.write("Here's the code solution : ")
    st.code("""
arrr=[0,5,12,150,25]
#first i initiated the list .


if "arrr" not in st.session_state:
    st.session_state['arrr']=arrr

#Then i've charged the variable into a session_state to store it
#and to make it accecible and modifiable because
#we're going to use it all along the program .


added_value=st.number_input("Enter the value of the last element: ",1)
#Then i've took an input of the user entered number.


ladd=st.button("Add to the list ! !")
#After that i've used a button to add to the list .

if ladd:
    st.session_state['arrr'].append(added_value)
#Then i've used the if statement set to be triggered
#if the user enter a new value .
#So the entered value would be automatically stored
#into our array .


popping=st.button("Pop the last element out !")
#Then i've added a button to pop out the last element .


if popping:
    if st.session_state['arrr']!=[]:
        st.session_state['arrr'].pop()
#if it's triggered and array is not empty , the last element
#would pop out .

st.write(st.session_state['arrr'])
#By the end i've wrote down all the array with st.write
""",language="python"
    )


with tab4:
    st.title("4th part of solving practices using python and streamlit .")
    st.write("On this part we're going to make plots using different libraries ")
    st.write("---")
    st.header("8th practice")
    st.write("### Plot a line chart of a random 1D table .")
    st.write("Here's the solution : ")
    from numpy import random
    x = random.randint(0,5,10)
    st.line_chart(x)
    st.write("Here's the code solution : ")

    st.code("""
from numpy import random
#We'll use that library to generate random numbers .

x = random.randint(0,5,10)
#In here i generated 10 random numbers from 0 to 4.

st.line_chart(x)
#This is how i plotted the line chart .
    """)

    st.write("---")
    st.header("9th practice")
    st.write("### Plot a bar chart of a random 1D table")
    st.write("Here's the solution : ")
    x = random.randint(0,5,10)
    st.bar_chart(x)
    st.write("Here's the code solution : ")

    st.code("""
x = random.randint(0,5,10)
#In here i generated 10 random numbers from 0 to 4 ,
#same thing is we did before .

st.bar_chart(x)
#This is how i plotted the bar chart .

    """)
    st.write('---')
    st.header("10th practice")
    st.write("### Plot an area chart of a 2D array .")
    st.write("Here's the solution : ")
    x = random.randint(0,5,(10,2))
    st.area_chart(x)
    st.write("Here's the code solution : ")
    st.code("""
x = random.randint(0,5,(10,2))
#In here i've done the same thing as before but now , i've
#choose 2D array with the length of 10 in each .


st.area_chart(x)
#With that line of code i've plotted the line chart of the array.
    """,language="python")
    st.write("---")
    st.header("11th practice")
    st.write("### Use matplotlib to plot a 1D chart .")
    st.write("Here's the solution : ")
    import matplotlib.pyplot as plt
    x=random.randint(0,5,10)

    
    fig, ax = plt.subplots()
    ax.hist(x)
    st.pyplot(fig)
    st.write("Here's the code solution : ")
    st.code("""
import matplotlib.pyplot as plt
#Here i've imported pyplot from matplotlib as plt
#as a shortcut .

x=random.randint(0,5,10)
#in here i've generated the empty array .

fig, ax = plt.subplots()
ax.hist(x)
#here i've called the function subplots to plot
#the selected data
#i've received two variables
#one that we'll use to plot
#and the other to assign the array that we want to plot

st.pyplot(fig)
#this function would plot the graph in streamlit web application
    """,language="python")











































    #
