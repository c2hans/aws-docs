---
source_url: https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_PutItem.html
---

# PutItem
<a name="API_PutItem"></a>

Creates a new item, or replaces an old item with a new item. If an item that has the same primary key as the new item already exists in the specified table, the new item completely replaces the existing item. You can perform a conditional put operation (add a new item if one with the specified primary key doesn't exist), or replace an existing item if it has certain attribute values. You can return the item's attribute values in the same operation, using the `ReturnValues` parameter.

When you add an item, the primary key attributes are the only required attributes.

Empty String and Binary attribute values are allowed. Attribute values of type String and Binary must have a length greater than zero if the attribute is used as a key attribute for a table or index. Set type attributes cannot be empty.

Invalid Requests with empty values will be rejected with a `ValidationException` exception.

**Note**
To prevent a new item from replacing an existing item, use a conditional expression that contains the `attribute_not_exists` function with the name of the attribute being used as the partition key for the table. Since every record must contain that attribute, the `attribute_not_exists` function will only succeed if no matching item exists.

**Note**
To determine whether `PutItem` overwrote an existing item, use `ReturnValues` set to `ALL_OLD`. If the response includes the `Attributes` element, an existing item was overwritten.

For more information about `PutItem`, see [Working with Items](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/WorkingWithItems.html) in the *Amazon DynamoDB Developer Guide*.

## Request Syntax
<a name="API_PutItem_RequestSyntax"></a>

```
{
   "ConditionalOperator": "{{string}}",
   "ConditionExpression": "{{string}}",
   "Expected": {
      "{{string}}" : {
         "AttributeValueList": [
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
         "ComparisonOperator": "{{string}}",
         "Exists": {{boolean}},
         "Value": {
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
      }
   },
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
   "ReturnConsumedCapacity": "{{string}}",
   "ReturnItemCollectionMetrics": "{{string}}",
   "ReturnValues": "{{string}}",
   "ReturnValuesOnConditionCheckFailure": "{{string}}",
   "TableName": "{{string}}"
}
```

## Request Parameters
<a name="API_PutItem_RequestParameters"></a>

The request accepts the following data in JSON format.

**Note**
In the following list, the required parameters are described first.

 ** [Item](#API_PutItem_RequestSyntax) **   <a name="DDB-PutItem-request-Item"></a>
A map of attribute name/value pairs, one for each attribute. Only the primary key attributes are required; you can optionally provide other attribute name-value pairs for the item.
You must provide all of the attributes for the primary key. For example, with a simple primary key, you only need to provide a value for the partition key. For a composite primary key, you must provide both values for both the partition key and the sort key.
If you specify any attributes that are part of an index key, then the data types for those attributes must match those of the schema in the table's attribute definition.
If the table has vector indexes, the following validations apply to write operations. A violation of any of these constraints results in a `ValidationException`:
+ The vector attribute must be a list of numbers with dimensions matching the index configuration.
+ Vector values must fit in 32-bit IEEE-754 floating point format (f32).
+ Partition key and inline filter attributes defined in the search schema must have data types matching the index schema definition.
Empty String and Binary attribute values are allowed. Attribute values of type String and Binary must have a length greater than zero if the attribute is used as a key attribute for a table or index.
For more information about primary keys, see [Primary Key](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/HowItWorks.CoreComponents.html#HowItWorks.CoreComponents.PrimaryKey) in the *Amazon DynamoDB Developer Guide*.
Each element in the `Item` map is an `AttributeValue` object.
Type: String to [AttributeValue](API_AttributeValue.md) object map
Key Length Constraints: Maximum length of 65535.
Required: Yes

 ** [TableName](#API_PutItem_RequestSyntax) **   <a name="DDB-PutItem-request-TableName"></a>
The name of the table to contain the item. You can also provide the Amazon Resource Name (ARN) of the table in this parameter.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Required: Yes

 ** [ConditionalOperator](#API_PutItem_RequestSyntax) **   <a name="DDB-PutItem-request-ConditionalOperator"></a>
This is a legacy parameter. Use `ConditionExpression` instead. For more information, see [ConditionalOperator](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/LegacyConditionalParameters.ConditionalOperator.html) in the *Amazon DynamoDB Developer Guide*.
Type: String
Valid Values: `AND | OR`
Required: No

 ** [ConditionExpression](#API_PutItem_RequestSyntax) **   <a name="DDB-PutItem-request-ConditionExpression"></a>
A condition that must be satisfied in order for a conditional `PutItem` operation to succeed.
An expression can contain any of the following:
+ Functions: `attribute_exists | attribute_not_exists | attribute_type | contains | begins_with | size`

  These function names are case-sensitive.
+ Comparison operators: `= | <> | < | > | <= | >= | BETWEEN | IN `
+  Logical operators: `AND | OR | NOT`
For more information on condition expressions, see [Condition Expressions](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/Expressions.SpecifyingConditions.html) in the *Amazon DynamoDB Developer Guide*.
Type: String
Required: No

 ** [Expected](#API_PutItem_RequestSyntax) **   <a name="DDB-PutItem-request-Expected"></a>
This is a legacy parameter. Use `ConditionExpression` instead. For more information, see [Expected](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/LegacyConditionalParameters.Expected.html) in the *Amazon DynamoDB Developer Guide*.
Type: String to [ExpectedAttributeValue](API_ExpectedAttributeValue.md) object map
Key Length Constraints: Maximum length of 65535.
Required: No

 ** [ExpressionAttributeNames](#API_PutItem_RequestSyntax) **   <a name="DDB-PutItem-request-ExpressionAttributeNames"></a>
One or more substitution tokens for attribute names in an expression. The following are some use cases for using `ExpressionAttributeNames`:
+ To access an attribute whose name conflicts with a DynamoDB reserved word.
+ To create a placeholder for repeating occurrences of an attribute name in an expression.
+ To prevent special characters in an attribute name from being misinterpreted in an expression.
Use the **\#** character in an expression to dereference an attribute name. For example, consider the following attribute name:
+  `Percentile`
The name of this attribute conflicts with a reserved word, so it cannot be used directly in an expression. (For the complete list of reserved words, see [Reserved Words](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/ReservedWords.html) in the *Amazon DynamoDB Developer Guide*). To work around this, you could specify the following for `ExpressionAttributeNames`:
+  `{"#P":"Percentile"}`
You could then use this substitution in an expression, as in this example:
+  `#P = :val`
Tokens that begin with the **:** character are *expression attribute values*, which are placeholders for the actual value at runtime.
For more information on expression attribute names, see [Specifying Item Attributes](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/Expressions.AccessingItemAttributes.html) in the *Amazon DynamoDB Developer Guide*.
Type: String to string map
Value Length Constraints: Maximum length of 65535.
Required: No

 ** [ExpressionAttributeValues](#API_PutItem_RequestSyntax) **   <a name="DDB-PutItem-request-ExpressionAttributeValues"></a>
One or more values that can be substituted in an expression.
Use the **:** (colon) character in an expression to dereference an attribute value. For example, suppose that you wanted to check whether the value of the *ProductStatus* attribute was one of the following:
 `Available | Backordered | Discontinued`
You would first need to specify `ExpressionAttributeValues` as follows:
 `{ ":avail":{"S":"Available"}, ":back":{"S":"Backordered"}, ":disc":{"S":"Discontinued"} }`
You could then use these values in an expression, such as this:
 `ProductStatus IN (:avail, :back, :disc)`
For more information on expression attribute values, see [Condition Expressions](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/Expressions.SpecifyingConditions.html) in the *Amazon DynamoDB Developer Guide*.
Type: String to [AttributeValue](API_AttributeValue.md) object map
Required: No

 ** [ReturnConsumedCapacity](#API_PutItem_RequestSyntax) **   <a name="DDB-PutItem-request-ReturnConsumedCapacity"></a>
Determines the level of detail about either provisioned or on-demand throughput consumption that is returned in the response:
+  `INDEXES` - The response includes the aggregate `ConsumedCapacity` for the operation, together with `ConsumedCapacity` for each table and secondary index that was accessed.

  Note that some operations, such as `GetItem` and `BatchGetItem`, do not access any indexes at all. In these cases, specifying `INDEXES` will only return `ConsumedCapacity` information for table(s).
+  `TOTAL` - The response includes only the aggregate `ConsumedCapacity` for the operation.
+  `NONE` - No `ConsumedCapacity` details are included in the response.
Type: String
Valid Values: `INDEXES | TOTAL | NONE`
Required: No

 ** [ReturnItemCollectionMetrics](#API_PutItem_RequestSyntax) **   <a name="DDB-PutItem-request-ReturnItemCollectionMetrics"></a>
Determines whether item collection metrics are returned. If set to `SIZE`, the response includes statistics about item collections, if any, that were modified during the operation are returned in the response. If set to `NONE` (the default), no statistics are returned.
Type: String
Valid Values: `SIZE | NONE`
Required: No

 ** [ReturnValues](#API_PutItem_RequestSyntax) **   <a name="DDB-PutItem-request-ReturnValues"></a>
Use `ReturnValues` if you want to get the item attributes as they appeared before they were updated with the `PutItem` request. For `PutItem`, the valid values are:
+  `NONE` - If `ReturnValues` is not specified, or if its value is `NONE`, then nothing is returned. (This setting is the default for `ReturnValues`.)
+  `ALL_OLD` - If `PutItem` overwrote an attribute name-value pair, then the content of the old item is returned.
The values returned are strongly consistent.
There is no additional cost associated with requesting a return value aside from the small network and processing overhead of receiving a larger response. No read capacity units are consumed.
The `ReturnValues` parameter is used by several DynamoDB operations; however, `PutItem` does not recognize any values other than `NONE` or `ALL_OLD`.
Type: String
Valid Values: `NONE | ALL_OLD | UPDATED_OLD | ALL_NEW | UPDATED_NEW`
Required: No

 ** [ReturnValuesOnConditionCheckFailure](#API_PutItem_RequestSyntax) **   <a name="DDB-PutItem-request-ReturnValuesOnConditionCheckFailure"></a>
An optional parameter that returns the item attributes for a `PutItem` operation that failed a condition check.
There is no additional cost associated with requesting a return value aside from the small network and processing overhead of receiving a larger response. No read capacity units are consumed.
Type: String
Valid Values: `ALL_OLD | NONE`
Required: No

## Response Syntax
<a name="API_PutItem_ResponseSyntax"></a>

```
{
   "Attributes": {
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
   "ConsumedCapacity": {
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
   },
   "ItemCollectionMetrics": {
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
}
```

## Response Elements
<a name="API_PutItem_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Attributes](#API_PutItem_ResponseSyntax) **   <a name="DDB-PutItem-response-Attributes"></a>
The attribute values as they appeared before the `PutItem` operation, but only if `ReturnValues` is specified as `ALL_OLD` in the request. Each element consists of an attribute name and an attribute value.
Type: String to [AttributeValue](API_AttributeValue.md) object map
Key Length Constraints: Maximum length of 65535.

 ** [ConsumedCapacity](#API_PutItem_ResponseSyntax) **   <a name="DDB-PutItem-response-ConsumedCapacity"></a>
The capacity units consumed by the `PutItem` operation. The data returned includes the total provisioned throughput consumed, along with statistics for the table and any indexes involved in the operation. `ConsumedCapacity` is only returned if the `ReturnConsumedCapacity` parameter was specified. For more information, see [Capacity unity consumption for write operations](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/read-write-operations.html#write-operation-consumption) in the *Amazon DynamoDB Developer Guide*.
If the table has vector indexes, the response includes a `VectorIndexes` field with `VectorWriteRequestBytes` consumed for each affected vector index.
Type: [ConsumedCapacity](API_ConsumedCapacity.md) object

 ** [ItemCollectionMetrics](#API_PutItem_ResponseSyntax) **   <a name="DDB-PutItem-response-ItemCollectionMetrics"></a>
Information about item collections, if any, that were affected by the `PutItem` operation. `ItemCollectionMetrics` is only returned if the `ReturnItemCollectionMetrics` parameter was specified. If the table does not have any local secondary indexes, this information is not returned in the response.
Each `ItemCollectionMetrics` element consists of:
+  `ItemCollectionKey` - The partition key value of the item collection. This is the same as the partition key value of the item itself.
+  `SizeEstimateRangeGB` - An estimate of item collection size, in gigabytes. This value is a two-element array containing a lower bound and an upper bound for the estimate. The estimate includes the size of all the items in the table, plus the size of all attributes projected into all of the local secondary indexes on that table. Use this estimate to measure whether a local secondary index is approaching its size limit.

  The estimate is subject to change over time; therefore, do not rely on the precision or accuracy of the estimate.
Type: [ItemCollectionMetrics](API_ItemCollectionMetrics.md) object

## Errors
<a name="API_PutItem_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ConditionalCheckFailedException **
A condition specified in the operation failed to be evaluated.
 ** Item **
Item which caused the `ConditionalCheckFailedException`.
 ** message **
The conditional request failed.
HTTP Status Code: 400

 ** InternalServerError **
An error occurred on the server side.
 ** message **
The server encountered an internal error trying to fulfill the request.
HTTP Status Code: 500

 ** ItemCollectionSizeLimitExceededException **
An item collection is too large. This exception is only returned for tables that have one or more local secondary indexes.
 ** message **
The total size of an item collection has exceeded the maximum limit of 10 gigabytes.
HTTP Status Code: 400

 ** ProvisionedThroughputExceededException **
The request was denied due to request throttling. For detailed information about why the request was throttled and the ARN of the impacted resource, find the [ThrottlingReason](https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_ThrottlingReason.html) field in the returned exception. The AWS SDKs for DynamoDB automatically retry requests that receive this exception. Your request is eventually successful, unless your retry queue is too large to finish. Reduce the frequency of requests and use exponential backoff. For more information, go to [Error Retries and Exponential Backoff](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/Programming.Errors.html#Programming.Errors.RetryAndBackoff) in the *Amazon DynamoDB Developer Guide*.
 ** message **
You exceeded your maximum allowed provisioned throughput.
 ** ThrottlingReasons **
A list of [ThrottlingReason](https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_ThrottlingReason.html) that provide detailed diagnostic information about why the request was throttled.
HTTP Status Code: 400

 ** ReplicatedWriteConflictException **
The request was rejected because one or more items in the request are being modified by a request in another Region.
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

 ** TransactionConflictException **
Operation was rejected because there is an ongoing transaction for the item.
HTTP Status Code: 400

## Examples
<a name="API_PutItem_Examples"></a>

### Put an Item
<a name="API_PutItem_Example_1"></a>

The following example puts a new item into the `Thread` table, but only if there is not already an item in the table with the same key.

#### Sample Request
<a name="API_PutItem_Example_1_Request"></a>

```
POST / HTTP/1.1
Host: dynamodb.<region>.<domain>;
Accept-Encoding: identity
Content-Length: <PayloadSizeBytes>
User-Agent: <UserAgentString>
Content-Type: application/x-amz-json-1.0
Authorization: AWS4-HMAC-SHA256 Credential=<Credential>, SignedHeaders=<Headers>, Signature=<Signature>
X-Amz-Date: <Date>
X-Amz-Target: DynamoDB_20120810.PutItem

{
    "TableName": "Thread",
    "Item": {
        "LastPostDateTime": {
            "S": "201303190422"
        },
        "Tags": {
            "SS": ["Update","Multiple Items","HelpMe"]
        },
        "ForumName": {
            "S": "Amazon DynamoDB"
        },
        "Message": {
            "S": "I want to update multiple items in a single call. What's the best way to do that?"
        },
        "Subject": {
            "S": "How do I update multiple items?"
        },
        "LastPostedBy": {
            "S": "fred@example.com"
        }
    },
    "ConditionExpression": "ForumName <> :f and Subject <> :s",
    "ExpressionAttributeValues": {
        ":f": {"S": "Amazon DynamoDB"},
        ":s": {"S": "How do I update multiple items?"}
    }
}
```

#### Sample Response
<a name="API_PutItem_Example_1_Response"></a>

```
HTTP/1.1 200 OK
x-amzn-RequestId: <RequestId>
x-amz-crc32: <Checksum>
Content-Type: application/x-amz-json-1.0
Content-Length: <PayloadSizeBytes>
Date: <Date>
{
}
```

## See Also
<a name="API_PutItem_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/dynamodb-2012-08-10/PutItem)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/dynamodb-2012-08-10/PutItem)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/dynamodb-2012-08-10/PutItem)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/dynamodb-2012-08-10/PutItem)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/dynamodb-2012-08-10/PutItem)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/dynamodb-2012-08-10/PutItem)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/dynamodb-2012-08-10/PutItem)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/dynamodb-2012-08-10/PutItem)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/dynamodb-2012-08-10/PutItem)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/dynamodb-2012-08-10/PutItem)
