"""from prefect import task, Flow

@task
def hello_world():
	print("Hello world!")

with Flow("my first flow!") as f:
	r = hello_world()

f.run()"""

from prefect import task, Flow

@flow #Decorator
def hello_world():
	print("Hello world!")
	return "Hello Prefect!"

@task
def prefect_say(s: str):
	print(s)

with Flow("my first flow!") as f:
	r = hello_wold()
	s2 = prefect_say(r)

f.run()