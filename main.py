def main():
    workhours = int(input('Enter your work hours: '))
    reg_hours = 40
    reg_rate = 18.25
    ov_rate = 27.78

   ##################################################
   # Code your program here
   ##################################################
    #Calculate regular hours and overtime
    overtime = max(workhours - reg_hours, 0)
    
    #Calculate overtime wage
    overtime_wage = overtime * ov_rate
    
    #Calculate regular wage 
    regular_wage = min(workhours, reg_hours) * reg_rate

    #Calculate total wage
    total_wage = regular_wage + overtime_wage

    print(f"Regular hours: {reg_hours} Regular Charge: ${regular_wage:.2f}")
    print(f"Overtime hours: {overtime} Overtime Charge: ${overtime_wage:.2f}")
    print(f"Total wage : ${total_wage:.2f}")

   ##################################################
   # Do not delete the return statement
   ##################################################
    return regular_wage, overtime_wage, total_wage


if __name__ == '__main__':
    main()
