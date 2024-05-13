def hello(name):
    print(f"Hello {name}")
def year_of_birth(name,age):
    year = 2024-age
    print(f"Hello {name}, you were born in {year}")
def my_country(country = "Uganda"):
    print(f"Hello Akirachix from {country}")
def greet(*names):
    for name in names:
        print (f"Hello {name}")
def create_sentence(**words):
    print(words)
    sentence = " "
    for word in words.values():
        sentence += word
        sentence += " "
    return sentence
def sum_and_greet(*args, **kwargs):
    total = 0
    for x in args:
        total += x
    f = kwargs["first_name"]
    l = kwargs["last_name"]
    greeting = f"Hello {f} {l}, total of your numbers is {total}."
    return greeting


class Following{
   constructor(user ){
       this.user=user
       this.followers=[]
   }
   addUser(follower){
       if(this.followers.includes (follower)){
           console.log("already exists")
       }
       else{
           this.followers.push(follower)
       }
   }
}
# const yvonne=new Following("Yvonne")
# const brigo=new Following("brigo")
# brigo.addUser("Umurerwa")
# brigo.addUser("Digne")
# yvonne.addUser("Faith")
# yvonne.addUser("Queen")
# yvonne.addUser("Bella")
# console.log(yvonne)
# console.log(brigo)


# const student={
#     name:"karen",
#     age:23,
#     grades:[23,45,67,89]
# }

# fun averageGrades(student){
#     let sum =0
#      for (let i=0;i<student.grades.length;++i){
#          sum+=student.grades[i]
#          let average = sum/student.grades.length
#          console.log(average)
#      }
# } 
# console.log(verageGrades(student))
