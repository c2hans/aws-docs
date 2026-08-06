---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/copy-amazon-dynamodb-tables-across-accounts-using-a-custom-implementation.html
---

# Copy Amazon DynamoDB tables across accounts using a custom implementation
<a name="copy-amazon-dynamodb-tables-across-accounts-using-a-custom-implementation"></a>

*Ramkumar Ramanujam, Amazon Web Services*

## Summary
<a name="copy-amazon-dynamodb-tables-across-accounts-using-a-custom-implementation-summary"></a>

When working with Amazon DynamoDB on Amazon Web Services (AWS), a common use case is to copy or sync DynamoDB tables in development, testing, or staging environments with the table data that are in the production environment. As a standard practice, each environment uses a different AWS account.

DynamoDB now supports cross-account backup using AWS Backup. For information about associated storage costs when using AWS Backup, see [AWS Backup pricing](https://aws.amazon.com/backup/pricing/). When you use AWS Backup to copy across accounts, the source and target accounts must be part of an AWS Organizations organization. There are other solutions for cross-account backup and restore using AWS services such as AWS Glue. Using those solutions, however, increases the application footprint, because there are more AWS services to deploy and maintain.

You can also use Amazon DynamoDB Streams to capture table changes in the source account. Then you can initiate an AWS Lambda function, and make the corresponding changes in the target table in the target account. But that solution applies to use cases in which source and target tables must always be kept in sync. It might not apply to development, testing, and staging environments where data are updated frequently.

This pattern provides steps to implement a custom solution to copy a Amazon DynamoDB table from one account to another. This pattern can be implemented using common programming languages such as C\#, Java, and Python. We recommend using a language that is supported by an [AWS SDK](https://aws.amazon.com/tools/).

## Prerequisites and limitations
<a name="copy-amazon-dynamodb-tables-across-accounts-using-a-custom-implementation-prereqs"></a>

**Prerequisites **
+ Two active AWS accounts
+ DynamoDB tables in both the accounts
+ Knowledge of AWS Identity and Access Management (IAM) roles and policies
+ Knowledge of how to access Amazon DynamoDB tables using any common programming language, such as C\#, Java, or Python

**Limitations **

This pattern applies to DynamoDB tables that are around 2 GB or smaller. With additional logic to handle connection or session interruptions, throttling, and failures and retries, it can be used for larger tables.

The DynamoDB scan operation, which reads items from the source table, can fetch only up to 1 MB of data in a single call. For larger tables, greater than 2 GB, this limitation can increase the total time to perform a full table copy.

## Architecture
<a name="copy-amazon-dynamodb-tables-across-accounts-using-a-custom-implementation-architecture"></a>

The following diagram shows the custom implementation between the source and target AWS accounts. IAM policies and security tokens are used with the custom implementation. Data is read from Amazon DynamoDB in the source account and written to DynamoDB in the target account.

![Source and target account architecture for copying by using the custom implementation.](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/images/pattern-img/ba8175be-9809-4c2e-b2d1-6b9180ed056c/images/d9d4c2c8-ff04-443f-9137-e37b8e23ccb5.png)

**Automation and scale**

This pattern applies to DynamoDB tables that are smaller in size, around 2 GB.

To apply this pattern for larger tables, address the following issues:
+ During the table copy operation, two active sessions are maintained, using different security tokens. If the table copy operation takes longer than the token expiration times, you must put in place logic to refresh the security tokens.
+ If enough read capacity units (RCUs) and write capacity units (WCUs) are not provisioned, reads or writes on the source or target table might get throttled. Be sure to catch and handle these exceptions.
+ Handle any other failures or exceptions and put a retry mechanism in place to retry or continue from where the copy operation failed.

## Tools
<a name="copy-amazon-dynamodb-tables-across-accounts-using-a-custom-implementation-tools"></a>

**Tools**
+ [Amazon DynamoDB](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/Introduction.html) – Amazon DynamoDB is a fully managed NoSQL database service that provides fast and predictable performance with seamless scalability.
+ The additional tools required will differ based on the programming language that you choose for the implementation. For example, if you use C\#, you will need Microsoft Visual Studio and the following NuGet packages:
  + `AWSSDK`
  + `AWSSDK.DynamoDBv2`

**Code **

The following Python code snippet deletes and recreates a DynamoDB table using the Boto3 library.

Do not use the `AWS_ACCESS_KEY_ID` and `AWS_SECRET_ACCESS_KEY` of an IAM user because these are long-term credentials, which should be avoided for programmatic access to AWS services. For more information about temporary credentials, see the *Best practices* section.

The `AWS_ACCESS_KEY_ID`, `AWS_SECRET_ACCESS_KEY`, and `TEMPORARY_SESSION_TOKEN` used in the following code snippet are temporary credentials fetched from AWS Security Token Service (AWS STS).

```
import boto3
import sys
import json

#args = input-parameters = GLOBAL_SEC_INDEXES_JSON_COLLECTION, ATTRIBUTES_JSON_COLLECTION, TARGET_DYNAMODB_NAME, TARGET_REGION, ...

#Input param: GLOBAL_SEC_INDEXES_JSON_COLLECTION
#[{"IndexName":"Test-index","KeySchema":[{"AttributeName":"AppId","KeyType":"HASH"},{"AttributeName":"AppType","KeyType":"RANGE"}],"Projection":{"ProjectionType":"INCLUDE","NonKeyAttributes":["PK","SK","OwnerName","AppVersion"]}}]

#Input param: ATTRIBUTES_JSON_COLLECTION
#[{"AttributeName":"PK","AttributeType":"S"},{"AttributeName":"SK","AttributeType":"S"},{"AttributeName":"AppId","AttributeType":"S"},{"AttributeName":"AppType","AttributeType":"N"}]

region = args['TARGET_REGION']
target_ddb_name = args['TARGET_DYNAMODB_NAME']

global_secondary_indexes = json.loads(args['GLOBAL_SEC_INDEXES_JSON_COLLECTION'])
attribute_definitions = json.loads(args['ATTRIBUTES_JSON_COLLECTION'])

# Drop and create target DynamoDB table
dynamodb_client = boto3.Session(
        aws_access_key_id=args['AWS_ACCESS_KEY_ID'],
        aws_secret_access_key=args['AWS_SECRET_ACCESS_KEY'],
        aws_session_token=args['TEMPORARY_SESSION_TOKEN'],
    ).client('dynamodb')

# Delete table
print('Deleting table: ' + target_ddb_name + ' ...')

try:
    dynamodb_client.delete_table(TableName=target_ddb_name)

    #Wait for table deletion to complete
    waiter = dynamodb_client.get_waiter('table_not_exists')
    waiter.wait(TableName=target_ddb_name)
    print('Table deleted.')
except dynamodb_client.exceptions.ResourceNotFoundException:
    print('Table already deleted / does not exist.')
    pass

print('Creating table: ' + target_ddb_name + ' ...')

table = dynamodb_client.create_table(
    TableName=target_ddb_name,
    KeySchema=[
        {
            'AttributeName': 'PK',
            'KeyType': 'HASH'  # Partition key
        },
        {
            'AttributeName': 'SK',
            'KeyType': 'RANGE'  # Sort key
        }
    ],
    AttributeDefinitions=attribute_definitions,
    GlobalSecondaryIndexes=global_secondary_indexes,
    BillingMode='PAY_PER_REQUEST'
)

waiter = dynamodb_client.get_waiter('table_exists')
waiter.wait(TableName=target_ddb_name)

print('Table created.')
```

## Best practices
<a name="copy-amazon-dynamodb-tables-across-accounts-using-a-custom-implementation-best-practices"></a>

**Temporary credentials**

As a security best practice, while accessing AWS services programmatically, avoid using the `AWS_ACCESS_KEY_ID` and `AWS_SECRET_ACCESS_KEY` of an IAM user because these are long-term credentials. Always try to use temporary credentials to access AWS services programmatically.

As an example, a developer hardcodes the `AWS_ACCESS_KEY_ID` and `AWS_SECRET_ACCESS_KEY` of an IAM user in the application during development but fails to remove the hardcoded values before pushing changes to code repository. These exposed credentials can be used by unintended or malicious users, which can have serious implications (especially if the exposed credentials have admin privileges). These exposed credentials should be deactivated or deleted immediately by using the IAM console or AWS Command Line Interface (AWS CLI).

To get temporary credentials for programmatic access to AWS services, use AWS STS. Temporary credentials are valid only for the specified time (from 15 minutes up to 36 hours). The maximum allowed duration of temporary credentials varies depending on such factors as role settings and role chaining. For more information about AWS STS, see the [documentation](https://docs.aws.amazon.com/STS/latest/APIReference/welcome.html).

## Epics
<a name="copy-amazon-dynamodb-tables-across-accounts-using-a-custom-implementation-epics"></a>

### Set up DynamoDB tables
<a name="set-up-dynamodb-tables"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Create DynamoDB tables. | Create DynamoDB tables, with indexes, in both source and target AWS accounts.<br />Set the capacity provisioning as on-demand mode, which allows DynamoDB to scale read/write capacities dynamically based on the workload. <br />Alternatively, you can use provisioned capacity with 4000 RCUs and 4000 WCUs. | App developer, DBA, Migration engineer |
| Populate the source table. | Populate the DynamoDB table in the source account with test data. Having at least 50 MB or more of test data helps you to see the peak and average RCUs consumed during table copy. You can then change the capacity provisioning as needed. | App developer, DBA, Migration engineer |

### Set up credentials to access the DynamoDB tables
<a name="set-up-credentials-to-access-the-dynamodb-tables"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Create IAM roles to access the source and target DynamoDB tables. | Create an IAM role in the source account with permissions to access (read) the DynamoDB table in the source account.<br />Add the source account as a trusted entity for this role.<br />Create an IAM role in the target account with permissions to access (create, read, update, delete) the DynamoDB table in the target account.  <br />Add the target account as a trusted entity for this role. | App developer, AWS DevOps |

### Copy table data from one account to another
<a name="copy-table-data-from-one-account-to-another"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Get temporary credentials for the IAM roles. | Get temporary credentials for IAM role created in source account.<br />Get temporary credentials for IAM role created in target account.<br />One way to get the temporary credentials for the IAM role is to use AWS STS from the AWS CLI.<pre>aws sts assume-role --role-arn arn:aws:iam::<account-id>:role/<role-name> --role-session-name <session-name> --profile <profile-name></pre><br />Use the appropriate AWS profile (corresponding to the source or target account).<br />For more information about different ways to get temporary credentials, see the following:+ [AWS Security Token Service API Reference](https://docs.aws.amazon.com/STS/latest/APIReference/welcome.html)<br />+ [Getting IAM role credentials for CLI access](https://docs.aws.amazon.com/singlesignon/latest/userguide/howtogetcredentials.html) | App developer, Migration engineer |
| Initialize the DynamoDB clients for source and target DynamoDB access. | Initialize the DynamoDB clients, which are provided by the AWS SDK, for the source and target DynamoDB tables.+ For the source DynamoDB client, use the temporary credentials fetched from the source account.<br />+ For the target DynamoDB client, use the temporary credentials fetched from the target account.<br />For more information about making requests by using IAM temporary credentials, see the [AWS documentation](https://docs.aws.amazon.com/AmazonS3/latest/userguide/AuthUsingTempSessionToken.html). | App developer |
| Drop and recreate the target table. | Delete and recreate the target DynamoDB table (along with indexes) in the target account, using the target account DynamoDB client.<br />Deleting all records from a DynamoDB table is a costly operation because it consumes provisioned WCUs. Deleting and recreating the table avoids those extra costs.<br />You can add indexes to a table after you create it, but this takes 2–5 minutes longer. Creating indexes during table creation, by passing the indexes collection to the `createTable` call, is more efficient. | App developer |
| Perform the table copy. | Repeat the following steps until all data are copied:+ Perform a scan on the table in the source account, using the source DynamoDB client. Each DynamoDB scan retrieves only 1 MB of data from the table, so you must repeat this operation until all items, or records, are read.<br />+ For each set of scanned items, write the items to the table in the target account, with the target DynamoDB client, using the `BatchWriteItem` call in AWS SDK for DynamoDB. This reduces the number of `PutItem` requests made to DynamoDB. <br />+ `BatchWriteItem` has a limitation of 25 writes or puts, or up to 16 MB. You must add logic to accumulate scanned items in counts of 25 before calling `BatchWriteItem`. `BatchWriteItem` returns a list of items that could not be successfully copied. Using this list, add retry logic to perform another `BatchWriteItem` call with only those items that did not succeed.<br />For more information, see the reference implementation in C\# (for dropping, creating, and populating tables) in the *Attachments* section. An example table config JavaScript Object Notation (JSON) file is also attached. | App developer |

## Related resources
<a name="copy-amazon-dynamodb-tables-across-accounts-using-a-custom-implementation-resources"></a>
+ [Amazon DynamoDB documentation](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/Introduction.html)
+ [Creating an IAM user in your AWS account](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_users_create.html)
+ [AWS SDKs](https://aws.amazon.com/tools/)
+ [Using temporary credentials with AWS resources](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_temp_use-resources.html)

## Additional information
<a name="copy-amazon-dynamodb-tables-across-accounts-using-a-custom-implementation-additional"></a>

This pattern was implemented using C\# to copy a DynamoDB table with 200,000 items (average item size of 5 KB and table size of 250 MB). The target DynamoDB table was set up with provisioned capacity of 4000 RCUs and 4000 WCUs.

The complete table copy operation (from source account to target account), including dropping and recreating the table, took 5 minutes. Total capacity units consumed: 30,000 RCUs and approximately 400,000 WCUs.

For more information on DynamoDB capacity modes, see [Read/Write capacity mode](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/HowItWorks.ReadWriteCapacityMode.html) in the AWS documentation.

## Attachments
<a name="attachments-ba8175be-9809-4c2e-b2d1-6b9180ed056c"></a>

To access additional content that is associated with this document, download and unzip the following file: [attachment.zip](samples/p-attach/ba8175be-9809-4c2e-b2d1-6b9180ed056c/attachments/attachment.zip)
