---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/automatically-generate-a-pynamodb-model-and-crud-functions-for-amazon-dynamodb-by-using-a-python-application.html
---

# Automatically generate a PynamoDB model and CRUD functions for Amazon DynamoDB by using a Python application
<a name="automatically-generate-a-pynamodb-model-and-crud-functions-for-amazon-dynamodb-by-using-a-python-application"></a>

*Vijit Vashishtha, Dheeraj Alimchandani, and Dhananjay Karanjkar, Amazon Web Services*

## Summary
<a name="automatically-generate-a-pynamodb-model-and-crud-functions-for-amazon-dynamodb-by-using-a-python-application-summary"></a>

It's common to require entities and create, read, update, and delete (CRUD) operations functions to efficiently perform Amazon DynamoDB database operations. PynamoDB is a Python-based interface that supports Python 3. It also provides features such as support for Amazon DynamoDB transactions, automatic attribute value serialization and deserialization, and compatibility with common Python frameworks, such as Flask and Django. This pattern helps developers working with Python and DynamoDB by providing a library that streamlines the automatic creation of PynamoDB models and CRUD operation functions. While it generates essential CRUD functions for database tables, it can also reverse engineer PynamoDB models and CRUD functions from Amazon DynamoDB tables. This pattern is designed to simplify database operations by using a Python-based application.

The following are the key features of this solution:
+ **JSON schema to PynamoDB model** – Automatically generate PynamoDB models in Python by importing a JSON schema file.
+ **CRUD function generation** – Automatically generate functions to perform CRUD operations on DynamoDB tables.
+ **Reverse engineering from DynamoDB** – Use PynamoDB object-relational mapping (ORM) to reverse engineer PynamoDB models and CRUD functions for existing Amazon DynamoDB tables.

## Prerequisites and limitations
<a name="automatically-generate-a-pynamodb-model-and-crud-functions-for-amazon-dynamodb-by-using-a-python-application-prereqs"></a>

**Prerequisites**
+ An active AWS account
+ Python version 3.8 or later, [downloaded](https://www.python.org/downloads/) and installed
+ Jinja2 version 3.1.2 or later, [downloaded](https://pypi.org/project/Jinja2/#files) and installed
+ Amazon DynamoDB tables for which you want to generate ORM
+ AWS Command Line Interface (AWS CLI), [installed](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html) and [configured](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-configure.html)
+ PynamoDB version 5.4.1 or later, [installed](https://pynamodb.readthedocs.io/en/stable/tutorial.html#installation)

## Architecture
<a name="automatically-generate-a-pynamodb-model-and-crud-functions-for-amazon-dynamodb-by-using-a-python-application-architecture"></a>

**Target technology stack**
+ JSON script
+ Python application
+ PynamoDB model
+ Amazon DynamoDB database instance

**Target architecture**

![Using a Python app to generate CRUD functions and PynamoDB model from DynamoDB tables.](https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/images/pattern-img/74cc4c73-5c8b-448d-98fb-b681cfa5f860/images/c2c367d6-d88a-4f49-8571-89160539eb08.png)

1. You create an input JSON schema file. This JSON schema file represents the attributes of the respective DynamoDB tables that you want to create PynamoDB models from and CRUD functions for. It contains the following three important keys:
   + `name` –The name of the target DynamoDB table.
   + `region` – The AWS Region where the table is hosted
   + `attributes` – The attributes that are part of the target table, such as the [partition key](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/HowItWorks.CoreComponents.html#HowItWorks.CoreComponents.PrimaryKey) (also known as a *hash attribute*), [sort key](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/HowItWorks.CoreComponents.html#HowItWorks.CoreComponents.PrimaryKey), [local secondary indexes](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/LSI.html), [global secondary indexes](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/GSI.html), and any [non-key attributes](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/HowItWorks.CoreComponents.html#HowItWorks.CoreComponents.TablesItemsAttributes). This tool expects the input schema to only provide the non-key attributes as the application fetches the key attributes directly from the target table. For an example of how to specify attributes in the JSON schema file, see the [Additional information](#automatically-generate-a-pynamodb-model-and-crud-functions-for-amazon-dynamodb-by-using-a-python-application-additional) section of this pattern.

1. Run the Python application and provide the JSON schema file as an input.

1. The Python application reads the JSON schema file.

1. The Python application connects to the DynamoDB tables to derive the schema and data types. The application runs the [describe\_table](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dynamodb/client/describe_table.html) operation and fetches the key and index attributes for the table.

1. The Python application combines the attributes from the JSON schema file and DynamoDB table. It uses the Jinja template engine to generate a PynamoDB model and corresponding CRUD functions.

1. You access the PynamoDB model to perform CRUD operations on the DynamoDB table.

## Tools
<a name="automatically-generate-a-pynamodb-model-and-crud-functions-for-amazon-dynamodb-by-using-a-python-application-tools"></a>

**AWS services**
+ [Amazon DynamoDB](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/Introduction.html) is a fully managed NoSQL database service that provides fast, predictable, and scalable performance.

**Other tools**
+ [Jinja](https://jinja.palletsprojects.com/en/) is an extensible templating engine that compiles templates into optimized Python code. This pattern uses Jinja to to generate dynamic content by embedding placeholders and logic within templates.
+ [PynamoDB](https://pynamodb.readthedocs.io/en/stable/) is a Python-based interface for Amazon DynamoDB.
+ [Python](https://www.python.org/) is a general-purpose computer programming language.

**Code repository**

The code for this pattern is available in the GitHub [Auto-generate PynamoDB models and CRUD functions](https://github.com/aws-samples/amazon-reverse-engineer-dynamodb) repository. The repository is divided into two main parts: the controller package and the templates.

*Controller package*

The controller Python package contains the main application logic that helps generate the PynamoDB model and the CRUD functions. It contains the following:
+ `input_json_validator.py` – This Python scripts validates the input JSON schema file and creates the Python objects that contain the list of target DynamoDB tables and the required attributes for each.
+ `dynamo_connection.py` – This script establishes a connection to the DynamoDB table and uses the `describe_table` operation to extract the attributes that are necessary to create the PynamoDB model.
+ `generate_model.py` – This script contains a Python class `GenerateModel` that creates the PynamoDB model based on the input JSON schema file and the `describe_table` operation.
+ `generate_crud.py` – For the DynamoDB tables that are defined in the JSON schema file, this script uses the `GenerateCrud` operation to create the Python classes.

*Templates*

This Python directory contains the following Jinja templates:
+ `model.jinja` – This Jinja template contains the template expression for generating the PynamoDB model script.
+ `crud.jinja` – This Jinja template contains the template expression for generating the CRUD functions script.

## Epics
<a name="automatically-generate-a-pynamodb-model-and-crud-functions-for-amazon-dynamodb-by-using-a-python-application-epics"></a>

### Set up the environment
<a name="set-up-the-environment"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Clone the repository. | Enter the following command to clone the [Auto-generate PynamoDB models and CRUD functions](https://github.com/aws-samples/amazon-reverse-engineer-dynamodb) repository.<pre>git clone https://github.com/aws-samples/amazon-reverse-engineer-dynamodb.git</pre> | App developer |
| Set up the Python environment. | 1. Navigate into the top-level directory in the cloned repository.<pre>cd amazon-reverse-engineer-dynamodb</pre><br />2. Enter the following command to install the required libraries and packages.<pre>pip install -r requirements.txt</pre> | App developer |

### Generate the PynamoDB model and CRUD functions
<a name="generate-the-pynamodb-model-and-crud-functions"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Modify the JSON schema file. | 1. Navigate into the top-level directory in the cloned repository.<pre>cd amazon-reverse-engineer-dynamodb</pre><br />2. Open the `test.json` file in your preferred editor. You can use this file as a reference to create your own JSON schema file, or you can update the values in this file to match your environment.<br />3. Modify the name, AWS Region, and attributes values for your target DynamoDB tables.If you define a table that does not exist in the JSON schema file, this solution does not generate models or CRUD functions for that table.<br />4. Save and close the `test.json` file. We recommend that you save this file with a new name. | App developer |
| Run the Python application. | Enter the following command to generate the PynamoDB models and CRUD functions, where `<input_schema.json>` is the name of your JSON schema file.<pre>python main.py --file <input_schema.json></pre> | App developer |

### Verify the PynamoDB model and CRUD functions
<a name="verify-the-pynamodb-model-and-crud-functions"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Verify the generated PynamoDB model. | 1. In the top-level directory of the cloned repository, enter the following command to navigate into the `models` repository.<pre>cd models</pre><br />2. By default, this solution names the PynamoDB model file `demo_model.py`. Validate that this file is present. | App developer |
| Verify the generated CRUD functions. | 1. In the top-level directory of the cloned repository, enter the following command to navigate into the `crud` repository.<pre>cd crud</pre><br />2. By default, this solution names the script `demo_crud.py`. Validate that this file is present.<br />3. Use the Python classes in the `demo_crud.py` file to perform a CRUD operation on the target DynamoDB table. Confirm that the operation completed successfully. | App developer |

## Related resources
<a name="automatically-generate-a-pynamodb-model-and-crud-functions-for-amazon-dynamodb-by-using-a-python-application-resources"></a>
+ [Core components of Amazon DynamoDB](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/HowItWorks.CoreComponents.html) (DynamoDB documentation)
+ [Improving data access with secondary indexes](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/SecondaryIndexes.html) (DynamoDB documentation)

## Additional information
<a name="automatically-generate-a-pynamodb-model-and-crud-functions-for-amazon-dynamodb-by-using-a-python-application-additional"></a>

**Sample attributes for the JSON schema file**

```
[
{
"name": "test_table",
"region": "ap-south-1",
"attributes": [
{
"name": "id",
"type": "UnicodeAttribute"
},
{
"name": "name",
"type": "UnicodeAttribute"
},
{
"name": "age",
"type": "NumberAttribute"
}
]
}
]
```
