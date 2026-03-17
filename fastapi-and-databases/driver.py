from .create_meta_tables import create_tables
from .crud import create_user, fetch_all_users, update_city, delete_by_age


print("Creating tables if not exists")
create_tables()  # this will create db as well

create_user(input_name="raviteja", input_age=36, input_city="Bengaluru")
# create_user(input_name="X", input_age=16, input_city="Bengaluru")
create_user(input_name="satyavada", input_age=19, input_city="Bengaluru")
create_user(input_name="Y", input_age=25, input_city="Bengaluru")
create_user(input_name="Rahul", input_age=25, input_city="Banglore")

print(f"After creating all the users\n {fetch_all_users()}")

update_city(input_name="Rahul", update_to_city="Bengaluru")

print(f"After updating the city for Rahul \n {fetch_all_users()}")

delete_by_age(20)

print(f"After deleting the records after deleting age <20 \n {fetch_all_users()}")
