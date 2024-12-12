project=int(input("enter project score"))
internal=int(input("enter internal score"))
external=int(input("enter external score"))
if project < 50:
   print(f'failed in project and marks are: {project}')
if internal < 50:
   print(f'failed in internal and marks are: {internal}')
if external < 50:
   print(f'failed in external and marks are: {external}')
else:
   p=(70/100)*project
   i=(10/100)*internal
   e=(20/100)*external
   total=p+i+e
   if total>90:
       print("A grade")
   elif total>80:
       print("B grade")
   elif total>50:
       print("C grade")
