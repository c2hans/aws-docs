---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/best-practices-code-generation/examples-python.html
---

# Python examples
<a name="examples-python"></a>

The following Python examples demonstrate how you can get started in generating in-line code suggestions with Amazon Q Developer. These illustrative examples show you how to trigger the coding assistant for your own projects. A majority of the following examples are applicable to other languages:
+ [Generate classes and functions](#classes-python)
+ [Document code](#code-python)
+ [Generate algorithms](#algorithms-python)
+ [Generate unit tests](#tests-python)

## Generate classes and functions
<a name="classes-python"></a>

 To generate full or partial class implementation, use code comments. The comment describes the intention of the class. Start simple, and add more details if necessary. After you generate a class. you can continue to generate functions within its skeleton.

When you write comments, it's preferable to use the language's comment structure. In Python, for single line comments, use `#`***. ***For multiline comments, use `''' '''` or `""" """`.

Input:

```
'''
DocumentReader class. has a name, children and optional parent.
Includes I/O functions to read and
write document
'''
```

Output:

```
class DocumentReader:
    def __init__(self, name, children, parent=None):
        self.name = name
        self.parent = parent
        self.children = children

    def read(self):
        """Reads current document and returns text"""
        pass

    def write(self, text):
        """Writes text to current document"""
        pass
```

Now that there is an initial class, an additional function can be generated with additional comments.

Input:

```
'''
function to read document from local directory path and print the first line of the document
'''
```

Output:

```
def read_document(self, path):
        """Reads document from path and prints first line"""
        import os
        if os.path.isfile(path):
            with open(path, 'r') as f:
                print(f.readline())
        else:
            print(f"File not found at {path}")
```

## Document code
<a name="code-python"></a>

Reduce time in code documentation by relying on in-line documentation. Add Python comment breaks `''' '''`.

Input:

```
class S3Utils:
    '''
    <place cursor here>
    '''
    def __init__(self):
        self.base_url = "https://s3"

    def generate_s3_url(self, bucket_name, region):
        return f"{self.base_url}.{region}.amazonaws.com/{bucket_name}"

# Example usage:
if __name__ == "__main__":
    s3_util = S3Utils()
    bucket_name = "my-example-bucket"
    region = "us-west-1"
    s3_url = s3_util.generate_s3_url(bucket_name, region)
    print(f"S3 URL for bucket '{bucket_name}' in region '{region}': {s3_url}")
```

Output:

```
class S3Utils:
    '''
    Class to generate S3 URL from bucket name and region
    '''
    def __init__(self):
        self.base_url = "https://s3"

    def generate_s3_url(self, bucket_name, region):
        return f"{self.base_url}.{region}.amazonaws.com/{bucket_name}"

# Example usage:
if __name__ == "__main__":
    s3_util = S3Utils()
    bucket_name = "my-example-bucket"
    region = "us-west-1"
    s3_url = s3_util.generate_s3_url(bucket_name, region)
    print(f"S3 URL for bucket '{bucket_name}' in region '{region}': {s3_url}")
```

## Generate algorithms
<a name="algorithms-python"></a>

Amazon Q Developer can generate popular algorithms, especially as related to AWS SDKs. In your script, add a prompt that specifies the function you want.

This example shows how to generate a dictionary of user id keys to name values, and then generate a sorting function by using the bubble sort algorithm.

Input:

```
class SortList:
    @staticmethod
    def get_user_id_name_map():
        user_id_name_map = {
            1: "Amit",
            2: "Rahul",
            3: "Vijay",
            4: "Raj",
            5: "Kumar"
        }
        return user_id_name_map

    '''
    Sort the list of user id's alphabetically using bubble sort
    '''
```

Output:

```
    @staticmethod
    def sort_user_id_name_map():
        user_id_name_map = SortList.get_user_id_name_map()
        list_of_user_ids = list(user_id_name_map.keys())
        list_of_user_names = list(user_id_name_map.values())
        print("Before sort: ", list_of_user_ids)
        for i in range(len(list_of_user_ids)):
            for j in range(len(list_of_user_ids) - i - 1):
                if list_of_user_names[j] > list_of_user_names[j + 1]:
                    list_of_user_ids[j], list_of_user_ids[j + 1] = list_of_user_ids[j + 1], list_of_user_ids[j]
                    list_of_user_names[j], list_of_user_names[j + 1] = list_of_user_names[j + 1], list_of_user_names[j]
        print("After sort: ", list_of_user_ids)
```

In addition, you can create prompts for standard procedures. In this example, the user creates a prompt to store the dictionary to an Amazon DynamoDB table. At the beginning of the script, the user adds a prompt to add DynamoDB libraries to help provide Amazon Q Developer with additional context.

Input:

```
'''
Add libraries for Amazon Dynamo DB
'''
```

Output:

```
'''
Add libraries for Amazon Dynamo DB and JSON.

iMport necessary libraries for working with Amazon DynamoDB and JSON data.
'''

import boto3
import json
from botocore.exceptions import ClientError

def load_data_to_dynamodb(table_name, data_file):
    # Create a DynamoDB resource
    dynamodb = boto3.resource('dynamodb')

    # Get a reference to the table
    table = dynamodb.Table(table_name)

    # Load data from the JSON file
    with open(data_file, 'r') as file:
        data = json.load(file)

    # Iterate over the data and load it to the table
    for item in data:
        try:
            table.put_item(Item=item)
            print(f"Successfully loaded data: {item}")
        except ClientError as e:
            print(f"Error loading data: {e.response['Error']['Message']}")

# Example usage
load_data_to_dynamodb('myTable', 'data.json')
```

Now, the user can easily ask Amazon Q to help with storing the dictionary in DynamoDB.

Input:

```
'''
   function to store the above sorted dict to dynamodb table named users
'''
```

Output:

```
@staticmethod
    def store_user_id_name_map_in_dynamodb():
        user_id_name_map = SortList.get_user_id_name_map()
        list_of_user_ids = list(user_id_name_map.keys())
        list_of_user_names = list(user_id_name_map.values())
        dynamodb = boto3.resource('dynamodb')
        table = dynamodb.Table('users')
        for i in range(len(list_of_user_ids)):
            try:
                response = table.put_item(
                    Item={
                        'user_id': list_of_user_ids[i],
                        'user_name': list_of_user_names[i]
                    }
                )
            except ClientError as e:
                print(e.response['Error']['Message'])
```

## Generate unit tests
<a name="tests-python"></a>

With in-line comments, Amazon Q Developer can generate unit tests to perform assertions and other tests. In this example, the user asks Amazon Q to generate applicable libraries for unit testing to set the context of the test script. Then, the user asks Amazon Q to write a test function for the `sort_user_id_name_map` function.

Input:

```
'''
Import all the required unit test libraries for python and then generate a unit test for sort_user_id_name_map function.
'''
```

Output:

```
import unittest
from unittest.mock import patch
from sort_user_id_name_map import sort_user_id_name_map

class TestSortUserIdNameMap(unittest.TestCase):
    @patch('sort_user_id_name_map.sort_user_id_name_map')
    def test_sort_user_id_name_map(self, mock_sort):
        mock_sort.return_value = {'id1': 'name1', 'id2': 'name2'}
        result = sort_user_id_name_map({'id2': 'name2', 'id1': 'name1'})
        self.assertEqual(result, {'id1': 'name1', 'id2': 'name2'})

if __name__ == '__main__':
    unittest.main()
```

In addition, in a chat between the user and Amazon Q Developer, it suggests and generates unit tests based on the user's code input prompts. For more information, see [Chat examples](examples-chat.md).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
