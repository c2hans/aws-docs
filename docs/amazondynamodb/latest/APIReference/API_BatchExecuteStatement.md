---
source_url: https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_BatchExecuteStatement.html
---

# BatchExecuteStatement
<a name="API_BatchExecuteStatement"></a>

This operation allows you to perform batch reads or writes on data stored in DynamoDB, using PartiQL. Each read statement in a `BatchExecuteStatement` must specify an equality condition on all key attributes. This enforces that each `SELECT` statement in a batch returns at most a single item. For more information, see [Running batch operations with PartiQL for DynamoDB ](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/ql-reference.multiplestatements.batching.html).

**Note**
The entire batch must consist of either read statements or write statements, you cannot mix both in one batch.

**Important**
A HTTP 200 response does not mean that all statements in the BatchExecuteStatement succeeded. Error details for individual statements can be found under the [Error](https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_BatchStatementResponse.html#DDB-Type-BatchStatementResponse-Error) field of the `BatchStatementResponse` for each statement.

## Request Syntax
<a name="API_BatchExecuteStatement_RequestSyntax"></a>

```
{
   "ReturnConsumedCapacity": "{{string}}",
   "Statements": [
      {
         "ConsistentRead": {{boolean}},
         "Parameters": [
            {
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
         ],
         "ReturnValuesOnConditionCheckFailure": "{{string}}",
         "Statement": "{{string}}"
      }
   ]
}
```

## Request Parameters
<a name="API_BatchExecuteStatement_RequestParameters"></a>

The request accepts the following data in JSON format.

**Note**
In the following list, the required parameters are described first.

 ** [Statements](#API_BatchExecuteStatement_RequestSyntax) **   <a name="DDB-BatchExecuteStatement-request-Statements"></a>
The list of PartiQL statements representing the batch to run.
Type: Array of [BatchStatementRequest](API_BatchStatementRequest.md) objects
Array Members: Minimum number of 1 item. Maximum number of 25 items.
Required: Yes

 ** [ReturnConsumedCapacity](#API_BatchExecuteStatement_RequestSyntax) **   <a name="DDB-BatchExecuteStatement-request-ReturnConsumedCapacity"></a>
Determines the level of detail about either provisioned or on-demand throughput consumption that is returned in the response:
+  `INDEXES` - The response includes the aggregate `ConsumedCapacity` for the operation, together with `ConsumedCapacity` for each table and secondary index that was accessed.

  Note that some operations, such as `GetItem` and `BatchGetItem`, do not access any indexes at all. In these cases, specifying `INDEXES` will only return `ConsumedCapacity` information for table(s).
+  `TOTAL` - The response includes only the aggregate `ConsumedCapacity` for the operation.
+  `NONE` - No `ConsumedCapacity` details are included in the response.
Type: String
Valid Values: `INDEXES | TOTAL | NONE`
Required: No

## Response Syntax
<a name="API_BatchExecuteStatement_ResponseSyntax"></a>

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
         "WriteCapacityUnits": number
      }
   ],
   "Responses": [
      {
         "Error": {
            "Code": "string",
            "Item": {
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
            "Message": "string"
         },
         "Item": {
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
         "TableName": "string"
      }
   ]
}
```

## Response Elements
<a name="API_BatchExecuteStatement_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [ConsumedCapacity](#API_BatchExecuteStatement_ResponseSyntax) **   <a name="DDB-BatchExecuteStatement-response-ConsumedCapacity"></a>
The capacity units consumed by the entire operation. The values of the list are ordered according to the ordering of the statements.
Type: Array of [ConsumedCapacity](API_ConsumedCapacity.md) objects

 ** [Responses](#API_BatchExecuteStatement_ResponseSyntax) **   <a name="DDB-BatchExecuteStatement-response-Responses"></a>
The response to each PartiQL statement in the batch. The values of the list are ordered according to the ordering of the request statements.
Type: Array of [BatchStatementResponse](API_BatchStatementResponse.md) objects

## Errors
<a name="API_BatchExecuteStatement_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InternalServerError **
An error occurred on the server side.
 ** message **
The server encountered an internal error trying to fulfill the request.
HTTP Status Code: 500

 ** RequestLimitExceeded **
Throughput exceeds the current throughput quota for your account. For detailed information about why the request was throttled and the ARN of the impacted resource, find the [ThrottlingReason](https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_ThrottlingReason.html) field in the returned exception. Contact [Support](https://aws.amazon.com/support) to request a quota increase.
 ** ThrottlingReasons **
A list of [ThrottlingReason](https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_ThrottlingReason.html) that provide detailed diagnostic information about why the request was throttled.
HTTP Status Code: 400

 ** ThrottlingException **
The request was denied due to request throttling. For detailed information about why the request was throttled and the ARN of the impacted resource, find the [ThrottlingReason](https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_ThrottlingReason.html) field in the returned exception.
 ** throttlingReasons **
A list of [ThrottlingReason](https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_ThrottlingReason.html) that provide detailed diagnostic information about why the request was throttled.
HTTP Status Code: 400

## See Also
<a name="API_BatchExecuteStatement_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/dynamodb-2012-08-10/BatchExecuteStatement)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/dynamodb-2012-08-10/BatchExecuteStatement)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/dynamodb-2012-08-10/BatchExecuteStatement)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/dynamodb-2012-08-10/BatchExecuteStatement)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/dynamodb-2012-08-10/BatchExecuteStatement)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/dynamodb-2012-08-10/BatchExecuteStatement)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/dynamodb-2012-08-10/BatchExecuteStatement)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/dynamodb-2012-08-10/BatchExecuteStatement)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/dynamodb-2012-08-10/BatchExecuteStatement)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/dynamodb-2012-08-10/BatchExecuteStatement)
