import company as cmp
import customer as cst


company_new = cmp.Company(name="Stream")
customer_new = cst.Customer("1", 3, 10000, 6)  # name, importance, budget, expected_duration
p = company_new.create_project_for_customer("New Project", customer_new)
p.start()
p.assign_tasks()

for i in p.execute():
    if i:
        break
    p.check_status()
