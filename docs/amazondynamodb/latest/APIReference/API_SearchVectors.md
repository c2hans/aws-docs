---
source_url: https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_SearchVectors.html
---

# SearchVectors
<a name="API_SearchVectors"></a>

Performs a vector similarity search on a vector index associated with an Amazon DynamoDB table, and returns the most similar items sorted by similarity score based on the distance function configured for the index.

Score interpretation depends on the distance function:
+  `COSINE` - Returns the items with the *k smallest* scores. Scores range from 0 (identical) to 2 (opposite). Lower scores indicate higher similarity.
+  `EUCLIDEAN` - Returns the items with the *k smallest* scores. Scores represent the Euclidean distance between vectors. Lower scores indicate higher similarity.
+  `DOT_PRODUCT` - Returns the items with the *k highest* scores. Higher scores indicate higher similarity.

## Request Syntax
<a name="API_SearchVectors_RequestSyntax"></a>

```
{
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
   "IndexName": "{{string}}",
   "ProjectionExpression": "{{string}}",
   "ReturnConsumedCapacity": "{{string}}",
   "SearchConditionExpression": "{{string}}",
   "SearchVector": [
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
   "TableName": "{{string}}",
   "TopK": {{number}}
}
```

## Request Parameters
<a name="API_SearchVectors_RequestParameters"></a>

The request accepts the following data in JSON format.

**Note**
In the following list, the required parameters are described first.

 ** [IndexName](#API_SearchVectors_RequestSyntax) **   <a name="DDB-SearchVectors-request-IndexName"></a>
The name of the vector index to search. The index must be in the `ACTIVE` state.
Type: String
Length Constraints: Minimum length of 3. Maximum length of 255.
Pattern: `[a-zA-Z0-9_.-]+`
Required: Yes

 ** [SearchVector](#API_SearchVectors_RequestSyntax) **   <a name="DDB-SearchVectors-request-SearchVector"></a>
The search vector to compare against the indexed vectors. Each element is a 32-bit IEEE-754 floating point number, provided in DynamoDB list format.
The number of dimensions must match the number of dimensions configured for the vector index.
Type: Array of [AttributeValue](API_AttributeValue.md) objects
Array Members: Minimum number of 1 item. Maximum number of 4096 items.
Required: Yes

 ** [TableName](#API_SearchVectors_RequestSyntax) **   <a name="DDB-SearchVectors-request-TableName"></a>
The name or Amazon Resource Name (ARN) of the table containing the vector index.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Required: Yes

 ** [TopK](#API_SearchVectors_RequestSyntax) **   <a name="DDB-SearchVectors-request-TopK"></a>
The number of most similar results to return. Valid values range from 1 to 100, inclusive.
Type: Integer
Valid Range: Minimum value of 1.
Required: Yes

 ** [ExpressionAttributeNames](#API_SearchVectors_RequestSyntax) **   <a name="DDB-SearchVectors-request-ExpressionAttributeNames"></a>
One or more substitution tokens for attribute names in an expression. Use the `#` character in an expression to dereference an attribute name.
Type: String to string map
Value Length Constraints: Maximum length of 65535.
Required: No

 ** [ExpressionAttributeValues](#API_SearchVectors_RequestSyntax) **   <a name="DDB-SearchVectors-request-ExpressionAttributeValues"></a>
One or more values that can be substituted in an expression. Use the `:` character in an expression to dereference an attribute value.
Type: String to [AttributeValue](API_AttributeValue.md) object map
Required: No

 ** [ProjectionExpression](#API_SearchVectors_RequestSyntax) **   <a name="DDB-SearchVectors-request-ProjectionExpression"></a>
A string that identifies one or more attributes to retrieve from the index. Separate attribute names with commas. If not specified, the operation returns all attributes projected into the vector index.
Only attributes projected into the vector index can be retrieved.
Type: String
Required: No

 ** [ReturnConsumedCapacity](#API_SearchVectors_RequestSyntax) **   <a name="DDB-SearchVectors-request-ReturnConsumedCapacity"></a>
Determines the level of detail about either provisioned or on-demand throughput consumption that is returned in the response:
+  `INDEXES` - The response includes the aggregate `ConsumedCapacity` for the operation, together with `ConsumedCapacity` for each table and secondary index that was accessed.

  Note that some operations, such as `GetItem` and `BatchGetItem`, do not access any indexes at all. In these cases, specifying `INDEXES` will only return `ConsumedCapacity` information for table(s).
+  `TOTAL` - The response includes only the aggregate `ConsumedCapacity` for the operation.
+  `NONE` - No `ConsumedCapacity` details are included in the response.
Type: String
Valid Values: `INDEXES | TOTAL | NONE`
Required: No

 ** [SearchConditionExpression](#API_SearchVectors_RequestSyntax) **   <a name="DDB-SearchVectors-request-SearchConditionExpression"></a>
A condition expression used to filter the vector search results. The expression can reference attributes defined in the vector index search schema, including `HASH` and `INLINE_FILTER` key elements.
The `HASH` and `INLINE_FILTER` attributes support only the equality operator (`=`). You can reference only top-level attributes from the search schema.
Type: String
Required: No

## Response Syntax
<a name="API_SearchVectors_ResponseSyntax"></a>

```
{
   "ConsumedCapacity": {
      "VectorSearchRequestBytes": number,
      "VectorWriteRequestBytes": number
   },
   "SearchResults": [
      {
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
         "Score": number
      }
   ]
}
```

## Response Elements
<a name="API_SearchVectors_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [ConsumedCapacity](#API_SearchVectors_ResponseSyntax) **   <a name="DDB-SearchVectors-response-ConsumedCapacity"></a>
The capacity units consumed by the `SearchVectors` operation. Contains `VectorSearchRequestBytes`, which represents the vector search capacity consumed.
Type: [VectorCapacity](API_VectorCapacity.md) object

 ** [SearchResults](#API_SearchVectors_ResponseSyntax) **   <a name="DDB-SearchVectors-response-SearchResults"></a>
A list of items returned by the vector similarity search, sorted by similarity with the most similar item first. Each item contains the projected attributes and a similarity score.
Type: Array of [SearchResultItem](API_SearchResultItem.md) objects

## Errors
<a name="API_SearchVectors_Errors"></a>

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

## See Also
<a name="API_SearchVectors_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/dynamodb-2012-08-10/SearchVectors)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/dynamodb-2012-08-10/SearchVectors)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/dynamodb-2012-08-10/SearchVectors)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/dynamodb-2012-08-10/SearchVectors)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/dynamodb-2012-08-10/SearchVectors)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/dynamodb-2012-08-10/SearchVectors)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/dynamodb-2012-08-10/SearchVectors)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/dynamodb-2012-08-10/SearchVectors)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/dynamodb-2012-08-10/SearchVectors)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/dynamodb-2012-08-10/SearchVectors)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon DynamoDB. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query amazondynamodb` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
