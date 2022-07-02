import nacl


A={"name": {"firstName": "Luke", "lastName": "Freeman"}, "age": 33, "partnerStatus": "single"}


print(A['name']['firstName'] +" " + A['name']['lastName'] + ' is ' + str(A["age"]) + ' years old')