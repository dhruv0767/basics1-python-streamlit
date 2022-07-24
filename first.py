import streamlit as st
import sys


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
