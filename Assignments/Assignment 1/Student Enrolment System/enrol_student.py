class EnrolStudent():
    id_counter_maths = 1
    id_counter_biology = 1
    id_counter_commerce = 1

    def apply(self, course, age, disable, phone_number, enroled_students):
        if(course == "maths"):
            EnrolStudent.id_counter_maths += 1
            curr_id = course[0] + str(EnrolStudent.id_counter_maths)
            enroled_students[course][curr_id] = {
                "age": age,
                "disable": disable,
                "phone_number": phone_number
            }

        elif(course == "biology"):
            EnrolStudent.id_counter_biology += 1
            curr_id = course[0] + str(EnrolStudent.id_counter_biology)
            enroled_students[course][curr_id] = {
                "age": age,
                "disable": disable,
                "phone_number": phone_number
            } 
        
        elif(course == "commerce"):
            EnrolStudent.id_counter_commerce += 1
            curr_id = course[0] + str(EnrolStudent.id_counter_commerce)
            enroled_students[course][curr_id] = {
                "age": age,
                "disable": disable,
                "phone_number": phone_number
            }            

        return enroled_students
