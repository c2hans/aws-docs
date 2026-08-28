---
source_url: https://docs.aws.amazon.com/sdk-for-cpp/v1/developer-guide/examples-dynamodb-tables.html
---

# Working with Tables in DynamoDB
<a name="examples-dynamodb-tables"></a>

Tables are the containers for all items in a DynamoDB database. Before you can add or remove data from DynamoDB, you must create a table.

For each table, you must define:
+ A table *name* that is unique for your AWS account and AWS Region.
+ A *primary key* for which every value must be unique. No two items in your table can have the same primary key value.

  A primary key can be *simple*, consisting of a single partition (HASH) key, or *composite*, consisting of a partition and a sort (RANGE) key.

  Each key value has an associated *data type*, enumerated by the [ScalarAttributeType](https://docs.aws.amazon.com/sdk-for-cpp/latest/api/aws-cpp-sdk-dynamodb/html/namespace_aws_1_1_dynamo_d_b_1_1_model.html#a4b39ae66214e022d3737079d071e4bcb.html) class. The key value can be binary (B), numeric (N), or a string (S). For more information, see [Naming Rules and Data Types](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/HowItWorks.NamingRulesDataTypes.html) in the Amazon DynamoDB Developer Guide.
+  *Provisioned throughput* values that define the number of reserved read/write capacity units for the table.
**Note**
 [Amazon DynamoDB pricing](https://aws.amazon.com/dynamodb/pricing/) is based on the provisioned throughput values that you set on your tables, so reserve only as much capacity as you think you’ll need for your table.
Provisioned throughput for a table can be modified at any time, so you can adjust capacity if your needs change.

## Create a Table
<a name="dynamodb-create-table"></a>

Use the [DynamoDB client](https://docs.aws.amazon.com/sdk-for-cpp/latest/api/aws-cpp-sdk-dynamodb/html/class_aws_1_1_dynamo_d_b_1_1_dynamo_d_b_client.html) `CreateTable` method to create a new DynamoDB table. You need to construct table attributes and a table schema, both of which are used to identify the primary key of your table. You must also supply initial provisioned throughput values and a table name. `CreateTable` is an asynchronous operation. `GetTableStatus` will return CREATING until the table is ACTIVE and ready for use.

### Create a Table with a Simple Primary Key
<a name="dynamodb-create-table-simple"></a>

This code creates a table with a simple primary key (“Name”).

 **Includes**

```
#include <aws/core/Aws.h>
#include <aws/dynamodb/DynamoDBClient.h>
#include <aws/dynamodb/model/AttributeDefinition.h>
#include <aws/dynamodb/model/CreateTableRequest.h>
#include <aws/dynamodb/model/KeySchemaElement.h>
#include <aws/dynamodb/model/ProvisionedThroughput.h>
#include <aws/dynamodb/model/ScalarAttributeType.h>
#include <iostream>
```

 **Code**

```
//! Create an Amazon DynamoDB table.
/*!
  \sa createTable()
  \param tableName: Name for the DynamoDB table.
  \param primaryKey: Primary key for the DynamoDB table.
  \param clientConfiguration: AWS client configuration.
  \return bool: Function succeeded.
 */
bool AwsDoc::DynamoDB::createTable(const Aws::String &tableName,
                                   const Aws::String &primaryKey,
                                   const Aws::Client::ClientConfiguration &clientConfiguration) {
    Aws::DynamoDB::DynamoDBClient dynamoClient(clientConfiguration);

    std::cout << "Creating table " << tableName <<
              " with a simple primary key: \"" << primaryKey << "\"." << std::endl;

    Aws::DynamoDB::Model::CreateTableRequest request;

    Aws::DynamoDB::Model::AttributeDefinition hashKey;
    hashKey.SetAttributeName(primaryKey);
    hashKey.SetAttributeType(Aws::DynamoDB::Model::ScalarAttributeType::S);
    request.AddAttributeDefinitions(hashKey);

    Aws::DynamoDB::Model::KeySchemaElement keySchemaElement;
    keySchemaElement.WithAttributeName(primaryKey).WithKeyType(
            Aws::DynamoDB::Model::KeyType::HASH);
    request.AddKeySchema(keySchemaElement);

    Aws::DynamoDB::Model::ProvisionedThroughput throughput;
    throughput.WithReadCapacityUnits(5).WithWriteCapacityUnits(5);
    request.SetProvisionedThroughput(throughput);
    request.SetTableName(tableName);

    const Aws::DynamoDB::Model::CreateTableOutcome &outcome = dynamoClient.CreateTable(
            request);
    if (outcome.IsSuccess()) {
        std::cout << "Table \""
                  << outcome.GetResult().GetTableDescription().GetTableName() <<
                  " created!" << std::endl;
    }
    else {
        std::cerr << "Failed to create table: " << outcome.GetError().GetMessage()
                  << std::endl;
        return false;
    }

    return waitTableActive(tableName, dynamoClient);
}
```

See the [complete example](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/cpp/example_code/dynamodb/create_table.cpp).

### Create a Table with a Composite Primary Key
<a name="dynamodb-create-table-composite"></a>

Add another [AttributeDefinition](https://docs.aws.amazon.com/sdk-for-cpp/latest/api/aws-cpp-sdk-dynamodb/html/class_aws_1_1_dynamo_d_b_1_1_model_1_1_attribute_definition.html) and [KeySchemaElement](https://docs.aws.amazon.com/sdk-for-cpp/latest/api/aws-cpp-sdk-dynamodb/html/class_aws_1_1_dynamo_d_b_1_1_model_1_1_key_schema_element.html) to [CreateTableRequest](https://docs.aws.amazon.com/sdk-for-cpp/latest/api/aws-cpp-sdk-dynamodb/html/class_aws_1_1_dynamo_d_b_1_1_model_1_1_create_table_request.html).

 **Includes**

```
#include <aws/core/Aws.h>
#include <aws/dynamodb/DynamoDBClient.h>
#include <aws/dynamodb/model/AttributeDefinition.h>
#include <aws/dynamodb/model/CreateTableRequest.h>
#include <aws/dynamodb/model/KeySchemaElement.h>
#include <aws/dynamodb/model/ProvisionedThroughput.h>
#include <aws/dynamodb/model/ScalarAttributeType.h>
#include <iostream>
```

 **Code**

```
//! Create an Amazon DynamoDB table with a composite key.
/*!
  \sa createTableWithCompositeKey()
  \param tableName: Name for the DynamoDB table.
  \param partitionKey: Name for the partition (hash) key.
  \param sortKey: Name for the sort (range) key.
  \param clientConfiguration: AWS client configuration.
  \return bool: Function succeeded.
 */
bool AwsDoc::DynamoDB::createTableWithCompositeKey(const Aws::String &tableName,
                                                   const Aws::String &partitionKey,
                                                   const Aws::String &sortKey,
                                                   const Aws::Client::ClientConfiguration &clientConfiguration) {
    Aws::DynamoDB::DynamoDBClient dynamoClient(clientConfiguration);

    std::cout << "Creating table " << tableName <<
              " with a composite primary key:\n" \
            "* " << partitionKey << " - partition key\n" \
            "* " << sortKey << " - sort key\n";

    Aws::DynamoDB::Model::CreateTableRequest request;

    Aws::DynamoDB::Model::AttributeDefinition hashKey1, hashKey2;
    hashKey1.WithAttributeName(partitionKey).WithAttributeType(
            Aws::DynamoDB::Model::ScalarAttributeType::S);
    request.AddAttributeDefinitions(hashKey1);
    hashKey2.WithAttributeName(sortKey).WithAttributeType(
            Aws::DynamoDB::Model::ScalarAttributeType::S);
    request.AddAttributeDefinitions(hashKey2);

    Aws::DynamoDB::Model::KeySchemaElement keySchemaElement1, keySchemaElement2;
    keySchemaElement1.WithAttributeName(partitionKey).WithKeyType(
            Aws::DynamoDB::Model::KeyType::HASH);
    request.AddKeySchema(keySchemaElement1);
    keySchemaElement2.WithAttributeName(sortKey).WithKeyType(
            Aws::DynamoDB::Model::KeyType::RANGE);
    request.AddKeySchema(keySchemaElement2);

    Aws::DynamoDB::Model::ProvisionedThroughput throughput;
    throughput.WithReadCapacityUnits(5).WithWriteCapacityUnits(5);
    request.SetProvisionedThroughput(throughput);

    request.SetTableName(tableName);

    const Aws::DynamoDB::Model::CreateTableOutcome &outcome = dynamoClient.CreateTable(
            request);
    if (outcome.IsSuccess()) {
        std::cout << "Table \""
                  << outcome.GetResult().GetTableDescription().GetTableName() <<
                  "\" was created!" << std::endl;
    }
    else {
        std::cerr << "Failed to create table:" << outcome.GetError().GetMessage()
                  << std::endl;
        return false;
    }

    return waitTableActive(tableName, dynamoClient);
}
```

See the [complete example](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/cpp/example_code/dynamodb/create_table_composite_key.cpp) on GitHub.

## List Tables
<a name="dynamodb-list-tables"></a>

You can list the tables in a particular region by calling the [DynamoDB client](https://docs.aws.amazon.com/sdk-for-cpp/latest/api/aws-cpp-sdk-dynamodb/html/class_aws_1_1_dynamo_d_b_1_1_dynamo_d_b_client.html) `ListTables` method.

 **Includes**

```
#include <aws/core/Aws.h>
#include <aws/core/utils/Outcome.h>
#include <aws/dynamodb/DynamoDBClient.h>
#include <aws/dynamodb/model/ListTablesRequest.h>
#include <aws/dynamodb/model/ListTablesResult.h>
#include <iostream>
```

 **Code**

```
//! List the Amazon DynamoDB tables for the current AWS account.
/*!
  \sa listTables()
  \param clientConfiguration: AWS client configuration.
  \return bool: Function succeeded.
 */

bool AwsDoc::DynamoDB::listTables(
        const Aws::Client::ClientConfiguration &clientConfiguration) {
    Aws::DynamoDB::DynamoDBClient dynamoClient(clientConfiguration);

    Aws::DynamoDB::Model::ListTablesRequest listTablesRequest;
    listTablesRequest.SetLimit(50);
    do {
        const Aws::DynamoDB::Model::ListTablesOutcome &outcome = dynamoClient.ListTables(
                listTablesRequest);
        if (!outcome.IsSuccess()) {
            std::cout << "Error: " << outcome.GetError().GetMessage() << std::endl;
            return false;
        }

        for (const auto &tableName: outcome.GetResult().GetTableNames())
            std::cout << tableName << std::endl;
        listTablesRequest.SetExclusiveStartTableName(
                outcome.GetResult().GetLastEvaluatedTableName());

    } while (!listTablesRequest.GetExclusiveStartTableName().empty());

    return true;
}
```

By default, up to 100 tables are returned per call. Use `GetExclusiveStartTableName` on the returned [ListTablesOutcome](https://docs.aws.amazon.com/sdk-for-cpp/latest/api/aws-cpp-sdk-dynamodb/html/class_aws_1_1_dynamo_d_b_1_1_dynamo_d_b_client.html) object to get the last table that was evaluated. You can use this value to start the listing after the last returned value of the previous listing.

See the [complete example](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/cpp/example_code/dynamodb/list_tables.cpp).

## Retrieve Information about a Table
<a name="dynamodb-describe-table"></a>

You can find out more about a table by calling the [DynamoDB client](https://docs.aws.amazon.com/sdk-for-cpp/latest/api/aws-cpp-sdk-dynamodb/html/class_aws_1_1_dynamo_d_b_1_1_dynamo_d_b_client.html) `DescribeTable` method.

 **Includes**

```
#include <aws/core/Aws.h>
#include <aws/dynamodb/DynamoDBClient.h>
#include <aws/dynamodb/model/DescribeTableRequest.h>
#include <iostream>
```

 **Code**

```
//! Describe an Amazon DynamoDB table.
/*!
  \sa describeTable()
  \param tableName: The DynamoDB table name.
  \param clientConfiguration: AWS client configuration.
  \return bool: Function succeeded.
*/
bool AwsDoc::DynamoDB::describeTable(const Aws::String &tableName,
                                     const Aws::Client::ClientConfiguration &clientConfiguration) {
    Aws::DynamoDB::DynamoDBClient dynamoClient(clientConfiguration);

    Aws::DynamoDB::Model::DescribeTableRequest request;
    request.SetTableName(tableName);

    const Aws::DynamoDB::Model::DescribeTableOutcome &outcome = dynamoClient.DescribeTable(
            request);

    if (outcome.IsSuccess()) {
        const Aws::DynamoDB::Model::TableDescription &td = outcome.GetResult().GetTable();
        std::cout << "Table name  : " << td.GetTableName() << std::endl;
        std::cout << "Table ARN   : " << td.GetTableArn() << std::endl;
        std::cout << "Status      : "
                  << Aws::DynamoDB::Model::TableStatusMapper::GetNameForTableStatus(
                          td.GetTableStatus()) << std::endl;
        std::cout << "Item count  : " << td.GetItemCount() << std::endl;
        std::cout << "Size (bytes): " << td.GetTableSizeBytes() << std::endl;

        const Aws::DynamoDB::Model::ProvisionedThroughputDescription &ptd = td.GetProvisionedThroughput();
        std::cout << "Throughput" << std::endl;
        std::cout << "  Read Capacity : " << ptd.GetReadCapacityUnits() << std::endl;
        std::cout << "  Write Capacity: " << ptd.GetWriteCapacityUnits() << std::endl;

        const Aws::Vector<Aws::DynamoDB::Model::AttributeDefinition> &ad = td.GetAttributeDefinitions();
        std::cout << "Attributes" << std::endl;
        for (const auto &a: ad)
            std::cout << "  " << a.GetAttributeName() << " (" <<
                      Aws::DynamoDB::Model::ScalarAttributeTypeMapper::GetNameForScalarAttributeType(
                              a.GetAttributeType()) <<
                      ")" << std::endl;
    }
    else {
        std::cerr << "Failed to describe table: " << outcome.GetError().GetMessage();
    }

    return outcome.IsSuccess();
}
```

See the [complete example](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/cpp/example_code/dynamodb/describe_table.cpp) on GitHub.

## Modify a Table
<a name="dynamodb-update-table"></a>

You can modify your table’s provisioned throughput values at any time by calling the [DynamoDB client](https://docs.aws.amazon.com/sdk-for-cpp/latest/api/aws-cpp-sdk-dynamodb/html/class_aws_1_1_dynamo_d_b_1_1_dynamo_d_b_client.html) `UpdateTable` method.

 **Includes**

```
#include <aws/core/Aws.h>
#include <aws/core/utils/Outcome.h>
#include <aws/dynamodb/DynamoDBClient.h>
#include <aws/dynamodb/model/ProvisionedThroughput.h>
#include <aws/dynamodb/model/UpdateTableRequest.h>
#include <iostream>
```

 **Code**

```
//! Update a DynamoDB table.
/*!
  \sa updateTable()
  \param tableName: Name for the DynamoDB table.
  \param readCapacity: Provisioned read capacity.
  \param writeCapacity: Provisioned write capacity.
  \param clientConfiguration: AWS client configuration.
  \return bool: Function succeeded.
 */
bool AwsDoc::DynamoDB::updateTable(const Aws::String &tableName,
                                   long long readCapacity, long long writeCapacity,
                                   const Aws::Client::ClientConfiguration &clientConfiguration) {
    Aws::DynamoDB::DynamoDBClient dynamoClient(clientConfiguration);

    std::cout << "Updating " << tableName << " with new provisioned throughput values"
              << std::endl;
    std::cout << "Read capacity : " << readCapacity << std::endl;
    std::cout << "Write capacity: " << writeCapacity << std::endl;

    Aws::DynamoDB::Model::UpdateTableRequest request;
    Aws::DynamoDB::Model::ProvisionedThroughput provisionedThroughput;
    provisionedThroughput.WithReadCapacityUnits(readCapacity).WithWriteCapacityUnits(
            writeCapacity);
    request.WithProvisionedThroughput(provisionedThroughput).WithTableName(tableName);

    const Aws::DynamoDB::Model::UpdateTableOutcome &outcome = dynamoClient.UpdateTable(
            request);
    if (outcome.IsSuccess()) {
        std::cout << "Successfully updated the table." << std::endl;
    } else {
        const Aws::DynamoDB::DynamoDBError &error = outcome.GetError();
        if (error.GetErrorType() == Aws::DynamoDB::DynamoDBErrors::VALIDATION &&
            error.GetMessage().find("The provisioned throughput for the table will not change") != std::string::npos) {
            std::cout << "The provisioned throughput for the table will not change." << std::endl;
        } else {
            std::cerr << outcome.GetError().GetMessage() << std::endl;
            return false;
        }
    }

    return waitTableActive(tableName, dynamoClient);
}
```

See the [complete example](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/cpp/example_code/dynamodb/update_table.cpp).

## Delete a Table
<a name="dynamodb-delete-table"></a>

Call the [DynamoDB client](https://docs.aws.amazon.com/sdk-for-cpp/latest/api/aws-cpp-sdk-dynamodb/html/class_aws_1_1_dynamo_d_b_1_1_dynamo_d_b_client.html) `DeleteTable` method and pass it the table’s name.

 **Includes**

```
#include <aws/core/Aws.h>
#include <aws/dynamodb/DynamoDBClient.h>
#include <aws/dynamodb/model/DeleteTableRequest.h>
#include <iostream>
```

 **Code**

```
//! Delete an Amazon DynamoDB table.
/*!
  \sa deleteTable()
  \param tableName: The DynamoDB table name.
  \param clientConfiguration: AWS client configuration.
  \return bool: Function succeeded.
*/
bool AwsDoc::DynamoDB::deleteTable(const Aws::String &tableName,
                                   const Aws::Client::ClientConfiguration &clientConfiguration) {
    Aws::DynamoDB::DynamoDBClient dynamoClient(clientConfiguration);

    Aws::DynamoDB::Model::DeleteTableRequest request;
    request.SetTableName(tableName);

    const Aws::DynamoDB::Model::DeleteTableOutcome &result = dynamoClient.DeleteTable(
            request);
    if (result.IsSuccess()) {
        std::cout << "Your table \""
                  << result.GetResult().GetTableDescription().GetTableName()
                  << " was deleted.\n";
    }
    else {
        std::cerr << "Failed to delete table: " << result.GetError().GetMessage()
                  << std::endl;
    }

    return result.IsSuccess();
}
```

See the [complete example](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/cpp/example_code/dynamodb/delete_table.cpp) on GitHub.

## More Info
<a name="more-info"></a>
+  [Guidelines for Working with Tables](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/GuidelinesForTables.html) in the Amazon DynamoDB Developer Guide
+  [Working with Tables in DynamoDB](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/WorkingWithTables.html) in the Amazon DynamoDB Developer Guide

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS SDK for C++. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sdk-for-cpp` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
