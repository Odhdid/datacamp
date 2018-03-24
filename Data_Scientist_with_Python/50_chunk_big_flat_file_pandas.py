Extracting information for large amounts of Twitter data

Great job chunking out that file in the previous exercise. You now know how to deal with situations 
where you need to process a very large file and that's a very useful skill to have!

It's good to know how to process a file in smaller, more manageable chunks, but it can become very
tedious having to write and rewrite the same code for the same task each time. In this exercise, 
you will be making your code more reusable by putting your work in the last exercise in a function definition.

The pandas package has been imported as pd and the file 'tweets.csv' is in your current directory for your use.
Instructions
100xp

    Define the function count_entries(), which has 3 parameters. The first parameter is csv_file 
    for the filename, the second is c_size for the chunk size, and the last is colname for the column name.
    Iterate over the file in csv_file file by using a for loop. Use the loop variable chunk and 
    iterate over the call to pd.read_csv(), passing c_size to chunksize.
    In the inner loop, iterate over the column given by colname in chunk by using a for loop. 
    Use the loop variable entry.
    Call the count_entries() function by passing to it the filename 'tweets.csv', the size of chunks 
    10, and the name of the column to count, 'lang'. Assign the result of the call to the variable result_counts.
    
    # Define count_entries()
def count_entries(csv_file,c_size,colname):
    """Return a dictionary with counts of
    occurrences as value for each key."""
    
    # Initialize an empty dictionary: counts_dict
    counts_dict = {}

    # Iterate over the file chunk by chunk
    for chunk in pd.read_csv(csv_file,chunksize=c_size):

        # Iterate over the column in DataFrame
        for entry in chunk[colname]:
            if entry in counts_dict.keys():
                counts_dict[entry] += 1
            else:
                counts_dict[entry] = 1

    # Return counts_dict
    return counts_dict

# Call count_entries(): result_counts
result_counts = count_entries('tweets.csv',10,'lang')

# Print result_counts
print(result_counts)

<script.py> output:
    {'favorite_count': 10, 'in_reply_to_status_id_str': 10, 'timestamp_ms': 10, 'filter_level': 10, 'quoted_status_id_str': 10, 'place': 10, 'truncated': 10, 'text': 10, 'in_reply_to_status_id': 10, 'retweeted': 10, 'favorited': 10, 'possibly_sensitive': 10, 'quoted_status': 10, 'in_reply_to_user_id_str': 10, 'retweet_count': 10, 'source': 10, 'user': 10, 'retweeted_status': 10, 'quoted_status_id': 10, 'extended_entities': 10, 'is_quote_status': 10, 'coordinates': 10, 'entities': 10, 'created_at': 10, 'id_str': 10, 'lang': 10, 'contributors': 10, 'in_reply_to_user_id': 10, 'id': 10, 'in_reply_to_screen_name': 10, 'geo': 10}

<script.py> output:
    {'en': 97, 'und': 2, 'et': 1}
