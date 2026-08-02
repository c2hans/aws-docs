---
source_url: https://docs.aws.amazon.com/appsync/latest/eventapi/dynamodb-function-reference.html
---

# AWS AppSync JavaScript function reference for DynamoDB
<a name="dynamodb-function-reference"></a>

The Amazon DynamoDB functions allow you to use JavaScript to store and retrieve data in existing Amazon DynamoDB tables in your account. This section describes the request and response handlers for supported DynamoDB operations.
+  [GetItem](dynamodb-getitem.md) — The GetItem request lets you tell the DynamoDB function to make a GetItem request to DynamoDB, and enables you to specify the key of the item in DynamoDB and whether to use a consistent read.
+  [PutItem](dynamodb-putitem.md) — The PutItem request lets you tell the DynamoDB function to make a PutItem request to DynamoDB, and enables you to specify the key of the item in DynamoDB, the full contents of the item (composed of key and attributeValues), and conditions for the operation to succeed.
+  [UpdateItem](dynamodb-updateitem.md) — The UpdateItem request enables you to tell the DynamoDB function to make a UpdateItem request to DynamoDB and allows you to specify the key of the item in DynamoDB, an update expression describing how to update the item in DynamoDB, and conditions for the operation to succeed.
+  [DeleteItem](dynamodb-deleteitem.md) — The DeleteItem request lets you tell the DynamoDB function to make a DeleteItem request to DynamoDB, and enables you to specify the key of the item in DynamoDB and conditions for the operation to succeed.
+  [Query](dynamodb-query.md) — The Query request object lets you tell the handler to make a Query request to DynamoDB, and enables you to specify the key expression, which index to use, additional filters, how many items to return, whether to use consistent reads, query direction (forward or backward), and pagination tokens.
+  [Scan](dynamodb-scan.md) — The Scan request lets you tell the DynamoDB function to make a Scan request to DynamoDB, and enables you to specify a filter to exclude results, which index to use, how many items to return, whether to use consistent reads, pagination tokens, and parallel scans.
+  [BatchGetItem](dynamodb-batchgetitem.md) — The BatchGetItem request object lets you tell the DynamoDB function to make a BatchGetItem request to DynamoDB to retrieve multiple items, potentially across multiple tables. For this request object, you must specify the table names to retrieve the items from and the keys of the items to retrieve from each table.
+  [BatchDeleteItem](dynamodb-batchdeleteitem.md) — The BatchDeleteItem request object lets you tell the DynamoDB function to make a BatchWriteItem request to DynamoDB to delete multiple items, potentially across multiple tables. For this request object, you must specify the table names to delete the items from and the keys of the items to delete from each table.
+  [BatchPutItem](dynamodb-batchputitem.md) — The BatchPutItem request object lets you tell the DynamoDB function to make a BatchWriteItem request to DynamoDB to put multiple items, potentially across multiple tables. For this request object, you must specify the table names to put the items in and the full items to put in each table.
+  [TransactGetItems](dynamodb-transactgetitems.md) — The TransactGetItems request object lets you to tell the DynamoDB function to make a TransactGetItems request to DynamoDB to retrieve multiple items, potentially across multiple tables. For this request object, you must specify the table name of each request item to retrieve the item from and the key of each request item to retrieve from each table.
+  [TransactWriteItems](dynamodb-transactwriteitems.md) — The TransactWriteItems request object lets you tell the DynamoDB function to make a TransactWriteItems request to DynamoDB to write multiple items, potentially to multiple tables. For this request object, you must specify the destination table name of each request item, the operation of each request item to perform, and the key of each request item to write.
+  [Type system (request mapping)](dynamodb-typed-values-request.md) — Learn more about how DynamoDB typing is integrated into AWS AppSync requests.
+  [Type system (response mapping)](dynamodb-typed-values-responses.md) — Learn more about how DynamoDB types are converted automatically to JSON in a response payload.
+  [Filters](dynamodb-filter.md) — Learn more about filters for query and scan operations.
+  [Condition expressions](dynamodb-condition-expressions.md) — Learn more about condition expressions for PutItem, UpdateItem, and DeleteItem operations.
+  [Transaction condition expressions](dynamodb-transaction-condition-expressions.md) — Learn more about condition expressions for TransactWriteItems operations.
+  [Projections](dynamodb-projections.md) — Learn more about how to specify attributes in read operations.
