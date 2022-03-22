"""from prefect import task, Flow 

@task
def hello_world():
	print("Hello world!")

with Flow("my first flow!") as f:
	r = hello_world()

f.run() """

from prefect import task, Flow

@task #Decorator
def hello_world():
	print("Hello world!")
	return "Hello Prefect!"

@task #New
def prefect_say(s: str):
	print(s)

with Flow("my first flow!") as f:
	r = hello_world()
	s2 = prefect_say(r) # r pass as an argument

f.run() # Call run method