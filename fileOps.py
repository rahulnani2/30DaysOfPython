def update_server_conf(file_path, key , value):
    
# Read the contents of file to variable
    with open(file_path,'r') as file:
        lines = file.readlines()

# Open the file in write mode to update the configuration
    with open(file_path , 'w') as file:
        for line in lines:
            if key in line:
                # Update the line with new value 
                file.write(key + "=" + value + "\n")
            else:
                file.write(line)

# Assign the vars 
file_path = 'server.conf' 
key = "MAX_CONNECTIONS"
value = "500"

# Function call 
update_server_conf(file_path , key , value)
