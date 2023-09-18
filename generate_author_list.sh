#!/bin/bash

# Initialize the AUTHOR list
AUTHOR_LIST="AUTHORS"

# Function to add author
add_author() {
    read -p "Enter author's name (or 'exit' to quit): " name
    if [[ "$name" == "exit" ]]; then
        return 1
    fi

    read -p "Enter author's Gmail address: " email

    # Append author to the AUTHOR list
    AUTHOR_LIST+="\n$name <$email>"

    echo "Author added: $name <$email>"
    return 0
}

# Prompt for new authors' information
while add_author; do
    :
done

# Save the AUTHOR list to a file
echo -e "$AUTHOR_LIST" > AUTHORS

echo "AUTHOR list generated and saved to AUTHORS file."
