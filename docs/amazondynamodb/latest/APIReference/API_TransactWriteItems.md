---
source_url: https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_TransactWriteItems.html
---

# TransactWriteItems
<a name="API_TransactWriteItems"></a>

 `TransactWriteItems` is a synchronous write operation that groups up to 100 action requests. These actions can target items in different tables, but not in different AWS accounts or Regions, and no two actions can target the same item. For example, you cannot both `ConditionCheck` and `Update` the same item. The aggregate size of the items in the transaction cannot exceed 4 MB.

The actions are completed atomically so that either all of them succeed, or all of them fail. They are defined by the following objects:
+  `Put`  —   Initiates a `PutItem` operation to write a new item. This structure specifies the primary key of the item to be written, the name of the table to write it in, an optional condition expression that must be satisfied for the write to succeed, a list of the item's attributes, and a field indicating whether to retrieve the item's attributes if the condition is not met.
+  `Update`  —   Initiates an `UpdateItem` operation to update an existing item. This structure specifies the primary key of the item to be updated, the name of the table where it resides, an optional condition expression that must be satisfied for the update to succeed, an expression that defines one or more attributes to be updated, and a field indicating whether to retrieve the item's attributes if the condition is not met.
+  `Delete`  —   Initiates a `DeleteItem` operation to delete an existing item. This structure specifies the primary key of the item to be deleted, the name of the table where it resides, an optional condition expression that must be satisfied for the deletion to succeed, and a field indicating whether to retrieve the item's attributes if the condition is not met.
+  `ConditionCheck`  —   Applies a condition to an item that is not being modified by the transaction. This structure specifies the primary key of the item to be checked, the name of the table where it resides, a condition expression that must be satisfied for the transaction to succeed, and a field indicating whether to retrieve the item's attributes if the condition is not met.

DynamoDB rejects the entire `TransactWriteItems` request if any of the following is true:
+ A condition in one of the condition expressions is not met.
+ An ongoing operation is in the process of updating the same item.
+ There is insufficient provisioned capacity for the transaction to be completed.
+ An item size becomes too large (bigger than 400 KB), a local secondary index (LSI) becomes too large, or a similar validation error occurs because of changes made by the transaction.
+ The aggregate size of the items in the transaction exceeds 4 MB.
+ There is a user error, such as an invalid data format.

## Request Syntax
<a name="API_TransactWriteItems_RequestSyntax"></a>

```
{
   "ClientRequestToken": "{{string}}",
   "ReturnConsumedCapacity": "{{string}}",
   "ReturnItemCollectionMetrics": "{{string}}",
   "TransactItems": [
      {
         "ConditionCheck": {
            "ConditionExpression": "{{string}}",
            "ExpressionAttributeNames": {
               "{{string}}" : "{{string}}"
            },
            "ExpressionAttributeValues": {
               "{{string}}" : {
                  "B": {{blob}},
                  "BOOL": {{boolean}},
                  "BS": [ {{blob}} ],
                  "L": [
                     "AttributeValue"
                  ],
                  "M": {
                     "{{string}}" : "AttributeValue"
                  },
                  "N": "{{string}}",
                  "NS": [ "{{string}}" ],
                  "NULL": {{boolean}},
                  "S": "{{string}}",
                  "SS": [ "{{string}}" ]
               }
            },
            "Key": {
               "{{string}}" : {
                  "B": {{blob}},
                  "BOOL": {{boolean}},
                  "BS": [ {{blob}} ],
                  "L": [
                     "AttributeValue"
                  ],
                  "M": {
                     "{{string}}" : "AttributeValue"
                  },
                  "N": "{{string}}",
                  "NS": [ "{{string}}" ],
                  "NULL": {{boolean}},
                  "S": "{{string}}",
                  "SS": [ "{{string}}" ]
               }
            },
            "ReturnValuesOnConditionCheckFailure": "{{string}}",
            "TableName": "{{string}}"
         },
         "Delete": {
            "ConditionExpression": "{{string}}",
            "ExpressionAttributeNames": {
               "{{string}}" : "{{string}}"
            },
            "ExpressionAttributeValues": {
               "{{string}}" : {
                  "B": {{blob}},
                  "BOOL": {{boolean}},
                  "BS": [ {{blob}} ],
                  "L": [
                     "AttributeValue"
                  ],
                  "M": {
                     "{{string}}" : "AttributeValue"
                  },
                  "N": "{{string}}",
                  "NS": [ "{{string}}" ],
                  "NULL": {{boolean}},
                  "S": "{{string}}",
                  "SS": [ "{{string}}" ]
               }
            },
            "Key": {
               "{{string}}" : {
                  "B": {{blob}},
                  "BOOL": {{boolean}},
                  "BS": [ {{blob}} ],
                  "L": [
                     "AttributeValue"
                  ],
                  "M": {
                     "{{string}}" : "AttributeValue"
                  },
                  "N": "{{string}}",
                  "NS": [ "{{string}}" ],
                  "NULL": {{boolean}},
                  "S": "{{string}}",
                  "SS": [ "{{string}}" ]
               }
            },
            "ReturnValuesOnConditionCheckFailure": "{{string}}",
            "TableName": "{{string}}"
         },
         "Put": {
            "ConditionExpression": "{{string}}",
            "ExpressionAttributeNames": {
               "{{string}}" : "{{string}}"
            },
            "ExpressionAttributeValues": {
               "{{string}}" : {
                  "B": {{blob}},
                  "BOOL": {{boolean}},
                  "BS": [ {{blob}} ],
                  "L": [
                     "AttributeValue"
                  ],
                  "M": {
                     "{{string}}" : "AttributeValue"
                  },
                  "N": "{{string}}",
                  "NS": [ "{{string}}" ],
                  "NULL": {{boolean}},
                  "S": "{{string}}",
                  "SS": [ "{{string}}" ]
               }
            },
            "Item": {
               "{{string}}" : {
                  "B": {{blob}},
                  "BOOL": {{boolean}},
                  "BS": [ {{blob}} ],
                  "L": [
                     "AttributeValue"
                  ],
                  "M": {
                     "{{string}}" : "AttributeValue"
                  },
                  "N": "{{string}}",
                  "NS": [ "{{string}}" ],
                  "NULL": {{boolean}},
                  "S": "{{string}}",
                  "SS": [ "{{string}}" ]
               }
            },
            "ReturnValuesOnConditionCheckFailure": "{{string}}",
            "TableName": "{{string}}"
         },
         "Update": {
            "ConditionExpression": "{{string}}",
            "ExpressionAttributeNames": {
               "{{string}}" : "{{string}}"
            },
            "ExpressionAttributeValues": {
               "{{string}}" : {
                  "B": {{blob}},
                  "BOOL": {{boolean}},
                  "BS": [ {{blob}} ],
                  "L": [
                     "AttributeValue"
                  ],
                  "M": {
                     "{{string}}" : "AttributeValue"
                  },
                  "N": "{{string}}",
                  "NS": [ "{{string}}" ],
                  "NULL": {{boolean}},
                  "S": "{{string}}",
                  "SS": [ "{{string}}" ]
               }
            },
            "Key": {
               "{{string}}" : {
                  "B": {{blob}},
                  "BOOL": {{boolean}},
                  "BS": [ {{blob}} ],
                  "L": [
                     "AttributeValue"
                  ],
                  "M": {
                     "{{string}}" : "AttributeValue"
                  },
                  "N": "{{string}}",
                  "NS": [ "{{string}}" ],
                  "NULL": {{boolean}},
                  "S": "{{string}}",
                  "SS": [ "{{string}}" ]
               }
            },
            "ReturnValuesOnConditionCheckFailure": "{{string}}",
            "TableName": "{{string}}",
            "UpdateExpression": "{{string}}"
         }
      }
   ]
}
```

## Request Parameters
<a name="API_TransactWriteItems_RequestParameters"></a>

The request accepts the following data in JSON format.

**Note**
In the following list, the required parameters are described first.

 ** [TransactItems](#API_TransactWriteItems_RequestSyntax) **   <a name="DDB-TransactWriteItems-request-TransactItems"></a>
An ordered array of up to 100 `TransactWriteItem` objects, each of which contains a `ConditionCheck`, `Put`, `Update`, or `Delete` object. These can operate on items in different tables, but the tables must reside in the same AWS account and Region, and no two of them can operate on the same item.
Type: Array of [TransactWriteItem](API_TransactWriteItem.md) objects
Array Members: Minimum number of 1 item. Maximum number of 100 items.
Required: Yes

 ** [ClientRequestToken](#API_TransactWriteItems_RequestSyntax) **   <a name="DDB-TransactWriteItems-request-ClientRequestToken"></a>
Providing a `ClientRequestToken` makes the call to `TransactWriteItems` idempotent, meaning that multiple identical calls have the same effect as one single call.
Although multiple identical calls using the same client request token produce the same result on the server (no side effects), the responses to the calls might not be the same. If the `ReturnConsumedCapacity` parameter is set, then the initial `TransactWriteItems` call returns the amount of write capacity units consumed in making the changes. Subsequent `TransactWriteItems` calls with the same client token return the number of read capacity units consumed in reading the item.
A client request token is valid for 10 minutes after the first request that uses it is completed. After 10 minutes, any request with the same client token is treated as a new request. Do not resubmit the same request with the same client token for more than 10 minutes, or the result might not be idempotent.
If you submit a request with the same client token but a change in other parameters within the 10-minute idempotency window, DynamoDB returns an `IdempotentParameterMismatch` exception.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 36.
Required: No

 ** [ReturnConsumedCapacity](#API_TransactWriteItems_RequestSyntax) **   <a name="DDB-TransactWriteItems-request-ReturnConsumedCapacity"></a>
Determines the level of detail about either provisioned or on-demand throughput consumption that is returned in the response:
+  `INDEXES` - The response includes the aggregate `ConsumedCapacity` for the operation, together with `ConsumedCapacity` for each table and secondary index that was accessed.

  Note that some operations, such as `GetItem` and `BatchGetItem`, do not access any indexes at all. In these cases, specifying `INDEXES` will only return `ConsumedCapacity` information for table(s).
+  `TOTAL` - The response includes only the aggregate `ConsumedCapacity` for the operation.
+  `NONE` - No `ConsumedCapacity` details are included in the response.
Type: String
Valid Values: `INDEXES | TOTAL | NONE`
Required: No

 ** [ReturnItemCollectionMetrics](#API_TransactWriteItems_RequestSyntax) **   <a name="DDB-TransactWriteItems-request-ReturnItemCollectionMetrics"></a>
Determines whether item collection metrics are returned. If set to `SIZE`, the response includes statistics about item collections (if any), that were modified during the operation and are returned in the response. If set to `NONE` (the default), no statistics are returned.
Type: String
Valid Values: `SIZE | NONE`
Required: No

## Response Syntax
<a name="API_TransactWriteItems_ResponseSyntax"></a>

```
{
   "ConsumedCapacity": [
      {
         "CapacityUnits": number,
         "GlobalSecondaryIndexes": {
            "string" : {
               "CapacityUnits": number,
               "ReadCapacityUnits": number,
               "WriteCapacityUnits": number
            }
         },
         "LocalSecondaryIndexes": {
            "string" : {
               "CapacityUnits": number,
               "ReadCapacityUnits": number,
               "WriteCapacityUnits": number
            }
         },
         "ReadCapacityUnits": number,
         "Table": {
            "CapacityUnits": number,
            "ReadCapacityUnits": number,
            "WriteCapacityUnits": number
         },
         "TableName": "string",
         "VectorIndexes": {
            "string" : {
               "VectorSearchRequestBytes": number,
               "VectorWriteRequestBytes": number
            }
         },
         "WriteCapacityUnits": number
      }
   ],
   "ItemCollectionMetrics": {
      "string" : [
         {
            "ItemCollectionKey": {
               "string" : {
                  "B": blob,
                  "BOOL": boolean,
                  "BS": [ blob ],
                  "L": [
                     "AttributeValue"
                  ],
                  "M": {
                     "string" : "AttributeValue"
                  },
                  "N": "string",
                  "NS": [ "string" ],
                  "NULL": boolean,
                  "S": "string",
                  "SS": [ "string" ]
               }
            },
            "SizeEstimateRangeGB": [ number ]
         }
      ]
   }
}
```

## Response Elements
<a name="API_TransactWriteItems_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [ConsumedCapacity](#API_TransactWriteItems_ResponseSyntax) **   <a name="DDB-TransactWriteItems-response-ConsumedCapacity"></a>
The capacity units consumed by the entire `TransactWriteItems` operation. The values of the list are ordered according to the ordering of the `TransactItems` request parameter.
If the table has vector indexes, each element also includes a `VectorIndexes` field with `VectorWriteRequestBytes` consumed for each affected vector index.
Type: Array of [ConsumedCapacity](API_ConsumedCapacity.md) objects

 ** [ItemCollectionMetrics](#API_TransactWriteItems_ResponseSyntax) **   <a name="DDB-TransactWriteItems-response-ItemCollectionMetrics"></a>
A list of tables that were processed by `TransactWriteItems` and, for each table, information about any item collections that were affected by individual `UpdateItem`, `PutItem`, or `DeleteItem` operations.
Type: String to array of [ItemCollectionMetrics](API_ItemCollectionMetrics.md) objects map
Key Length Constraints: Minimum length of 1. Maximum length of 1024.

## Errors
<a name="API_TransactWriteItems_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** IdempotentParameterMismatchException **
DynamoDB rejected the request because you retried a request with a different payload but with an idempotent token that was already used.
HTTP Status Code: 400

 ** InternalServerError **
An error occurred on the server side.
 ** message **
The server encountered an internal error trying to fulfill the request.
HTTP Status Code: 500

 ** ProvisionedThroughputExceededException **
The request was denied due to request throttling. For detailed information about why the request was throttled and the ARN of the impacted resource, find the [ThrottlingReason](https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_ThrottlingReason.html) field in the returned exception. The AWS SDKs for DynamoDB automatically retry requests that receive this exception. Your request is eventually successful, unless your retry queue is too large to finish. Reduce the frequency of requests and use exponential backoff. For more information, go to [Error Retries and Exponential Backoff](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/Programming.Errors.html#Programming.Errors.RetryAndBackoff) in the *Amazon DynamoDB Developer Guide*.
 ** message **
You exceeded your maximum allowed provisioned throughput.
 ** ThrottlingReasons **
A list of [ThrottlingReason](https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_ThrottlingReason.html) that provide detailed diagnostic information about why the request was throttled.
HTTP Status Code: 400

 ** RequestLimitExceeded **
Throughput exceeds the current throughput quota for your account. For detailed information about why the request was throttled and the ARN of the impacted resource, find the [ThrottlingReason](https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_ThrottlingReason.html) field in the returned exception. Contact [Support](https://aws.amazon.com/support) to request a quota increase.
 ** ThrottlingReasons **
A list of [ThrottlingReason](https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_ThrottlingReason.html) that provide detailed diagnostic information about why the request was throttled.
HTTP Status Code: 400

 ** ResourceNotFoundException **
The operation tried to access a nonexistent table or index. The resource might not be specified correctly, or its status might not be `ACTIVE`.
 ** message **
The resource which is being requested does not exist.
HTTP Status Code: 400

 ** ThrottlingException **
The request was denied due to request throttling. For detailed information about why the request was throttled and the ARN of the impacted resource, find the [ThrottlingReason](https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_ThrottlingReason.html) field in the returned exception.
 ** throttlingReasons **
A list of [ThrottlingReason](https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_ThrottlingReason.html) that provide detailed diagnostic information about why the request was throttled.
HTTP Status Code: 400

 ** TransactionCanceledException **
The entire transaction request was canceled.
DynamoDB cancels a `TransactWriteItems` request under the following circumstances:
+ A condition in one of the condition expressions is not met.
+ A table in the `TransactWriteItems` request is in a different account or region.
+ More than one action in the `TransactWriteItems` operation targets the same item.
+ There is insufficient provisioned capacity for the transaction to be completed.
+ An item size becomes too large (larger than 400 KB), or a local secondary index (LSI) becomes too large, or a similar validation error occurs because of changes made by the transaction.
+ There is a user error, such as an invalid data format.
+  There is an ongoing `TransactWriteItems` operation that conflicts with a concurrent `TransactWriteItems` request. In this case the `TransactWriteItems` operation fails with a `TransactionCanceledException`.
DynamoDB cancels a `TransactGetItems` request under the following circumstances:
+ There is an ongoing `TransactGetItems` operation that conflicts with a concurrent `PutItem`, `UpdateItem`, `DeleteItem` or `TransactWriteItems` request. In this case the `TransactGetItems` operation fails with a `TransactionCanceledException`.
+ A table in the `TransactGetItems` request is in a different account or region.
+ There is insufficient provisioned capacity for the transaction to be completed.
+ There is a user error, such as an invalid data format.
DynamoDB lists the cancellation reasons on the `CancellationReasons` property. Transaction cancellation reasons are ordered in the order of requested items, if an item has no error it will have `None` code and `Null` message. The `None` code is returned as the literal string `"None"`, not a null or absent value; the message field is omitted entirely for an item that has no error. This is important to note when using an SDK that surfaces the code as an optional or nullable type.
Cancellation reason codes and possible error messages:
+ No Errors:
  + Code: `None`
  + Message: `null`
+ Conditional Check Failed:
  + Code: `ConditionalCheckFailed`
  + Message: The conditional request failed.
+ Item Collection Size Limit Exceeded:
  + Code: `ItemCollectionSizeLimitExceeded`
  + Message: Collection size exceeded.
+ Transaction Conflict:
  + Code: `TransactionConflict`
  + Message: Transaction is ongoing for the item.
+ Provisioned Throughput Exceeded:
  + Code: `ProvisionedThroughputExceeded`
  + Messages:
    + The level of configured provisioned throughput for the table was exceeded. Consider increasing your provisioning level with the UpdateTable API.
**Note**
This Message is received when provisioned throughput is exceeded is on a provisioned DynamoDB table.
    + The level of configured provisioned throughput for one or more global secondary indexes of the table was exceeded. Consider increasing your provisioning level for the under-provisioned global secondary indexes with the UpdateTable API.
**Note**
This message is returned when provisioned throughput is exceeded is on a provisioned GSI.
+ Throttling Error:
  + Code: `ThrottlingError`
  + Messages:
    + Throughput exceeds the current capacity of your table or index. DynamoDB is automatically scaling your table or index so please try again shortly. If exceptions persist, check if you have a hot key: https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/bp-partition-key-design.html.
**Note**
This message is returned when writes get throttled on an On-Demand table as DynamoDB is automatically scaling the table.
    + Throughput exceeds the current capacity for one or more global secondary indexes. DynamoDB is automatically scaling your index so please try again shortly.
**Note**
This message is returned when writes get throttled on an On-Demand GSI as DynamoDB is automatically scaling the GSI.
+ Validation Error:
  + Code: `ValidationError`
  + Messages:
    + One or more parameter values were invalid.
    + The update expression attempted to update the secondary index key beyond allowed size limits.
    + The update expression attempted to update the secondary index key to unsupported type.
    + An operand in the update expression has an incorrect data type.
    + Item size to update has exceeded the maximum allowed size.
    + Number overflow. Attempting to store a number with magnitude larger than supported range.
    + Type mismatch for attribute to update.
    + Nesting Levels have exceeded supported limits.
    + The document path provided in the update expression is invalid for update.
    + The provided expression refers to an attribute that does not exist in the item.
 ** CancellationReasons **
A list of cancellation reasons.
HTTP Status Code: 400

 ** TransactionInProgressException **
The transaction with the given request token is already in progress.
 Recommended Settings
 This is a general recommendation for handling the `TransactionInProgressException`. These settings help ensure that the client retries will trigger completion of the ongoing `TransactWriteItems` request.
+  Set `clientExecutionTimeout` to a value that allows at least one retry to be processed after 5 seconds have elapsed since the first attempt for the `TransactWriteItems` operation.
+  Set `socketTimeout` to a value a little lower than the `requestTimeout` setting.
+  `requestTimeout` should be set based on the time taken for the individual retries of a single HTTP request for your use case, but setting it to 1 second or higher should work well to reduce chances of retries and `TransactionInProgressException` errors.
+  Use exponential backoff when retrying and tune backoff if needed.
 Assuming [default retry policy](https://github.com/aws/aws-sdk-java/blob/fd409dee8ae23fb8953e0bb4dbde65536a7e0514/aws-java-sdk-core/src/main/java/com/amazonaws/retry/PredefinedRetryPolicies.java#L97), example timeout settings based on the guidelines above are as follows:
Example timeline:
+ 0-1000 first attempt
+ 1000-1500 first sleep/delay (default retry policy uses 500 ms as base delay for 4xx errors)
+ 1500-2500 second attempt
+ 2500-3500 second sleep/delay (500 \* 2, exponential backoff)
+ 3500-4500 third attempt
+ 4500-6500 third sleep/delay (500 \* 2^2)
+ 6500-7500 fourth attempt (this can trigger inline recovery since 5 seconds have elapsed since the first attempt reached TC)
HTTP Status Code: 400

## See Also
<a name="API_TransactWriteItems_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/dynamodb-2012-08-10/TransactWriteItems)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/dynamodb-2012-08-10/TransactWriteItems)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/dynamodb-2012-08-10/TransactWriteItems)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/dynamodb-2012-08-10/TransactWriteItems)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/dynamodb-2012-08-10/TransactWriteItems)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/dynamodb-2012-08-10/TransactWriteItems)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/dynamodb-2012-08-10/TransactWriteItems)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/dynamodb-2012-08-10/TransactWriteItems)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/dynamodb-2012-08-10/TransactWriteItems)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/dynamodb-2012-08-10/TransactWriteItems)
