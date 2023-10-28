# Simple python script to generate random indian user data
import requests
import csv

api = r"https://randomuser.me/api/?noinfo" # Random user api which is being used
# here, ?noinfo strips the other data from api unwanted in this program.

def gen_random_data():
    try:
        # Getting user preferences
        num = int(input("How many user data do you want? ")) 
        gender = input("Specify which gender (m/f)(optional) : ").lower()
        save = input("Do you want to save to csv? (y/n) : ").lower()
        
        # The api limits maximum 5000 user data so checking it.
        if num > 0 and num < 5000:
            # Arguments to give to the api get request
            args = {"nat":"in", 
                    "exc":"picture,registered,login,nat",
                    "format":"pretty",
                    "results":num
                    }
            if gender in "m" or gender in "f":
                args["gender"] = gender
            
            # Sending get request to the api
            data = requests.get(api, args)
            results = data.json()["results"]
            if save in "y":
                file_name = input("Enter the file name (without extension) : ")
                # Writing into the csv file
                with open(f"./{file_name}.csv", "w", newline="") as file:
                    writer = csv.DictWriter(file, ("gender", "title", "first_name", "last_name", "street_no", "street", "city", "state", "pincode", "email", "dob", "phone","cell", "Aadhar_no"))
                    writer.writeheader()
                    for result in results:
                        results_dict = {"gender":result["gender"],
                                        "title":result["name"]["title"],
                                        "first_name":result["name"]["first"],
                                        "last_name":result["name"]["last"],
                                        "street_no": result["location"]["street"]["number"],
                                        "street": result["location"]["street"]["name"],
                                        "city": result["location"]["city"], 
                                        "state": result["location"]["state"],
                                        "pincode": result["location"]["postcode"],
                                        "email": result["email"],
                                        "dob": result["dob"]["date"].partition("T")[0],
                                        "phone": result["phone"],
                                        "cell": result["cell"], 
                                        "Aadhar_no": result["id"]["value"]}
                        writer.writerow(results_dict)
            elif save in "n":
                for result in results:
                    print({"gender":result["gender"],
                           "title":result["name"]["title"],
                           "first_name":result["name"]["first"],
                           "last_name":result["name"]["last"],
                           "street_no": result["location"]["street"]["number"],
                           "street": result["location"]["street"]["name"],
                           "city": result["location"]["city"], 
                           "state": result["location"]["state"],
                           "pincode": result["location"]["postcode"],
                           "email": result["email"],
                           "dob": result["dob"]["date"].partition("T")[0],
                           "phone": result["phone"],
                           "cell": result["cell"], 
                           "Aadhar_no": result["id"]["value"]})
        else:
            raise ValueError
    except ValueError:
        print("Invalid input! try again...")
        gen_random_data()

if __name__ == "__main__":
    gen_random_data()

