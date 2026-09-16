---
source_url: https://docs.aws.amazon.com/lake-formation/latest/APIReference/API_GetTableObjects.html
---

# GetTableObjects
<a name="API_GetTableObjects"></a>

Returns the set of Amazon S3 objects that make up the specified governed table. A transaction ID or timestamp can be specified for time-travel queries.

## Request Syntax
<a name="API_GetTableObjects_RequestSyntax"></a>

```
POST /GetTableObjects HTTP/1.1
Content-type: application/json

{
   "CatalogId": "{{string}}",
   "DatabaseName": "{{string}}",
   "MaxResults": {{number}},
   "NextToken": "{{string}}",
   "PartitionPredicate": "{{string}}",
   "QueryAsOfTime": {{number}},
   "TableName": "{{string}}",
   "TransactionId": "{{string}}"
}
```

## URI Request Parameters
<a name="API_GetTableObjects_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_GetTableObjects_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [CatalogId](#API_GetTableObjects_RequestSyntax) **   <a name="lakeformation-GetTableObjects-request-CatalogId"></a>
The catalog containing the governed table. Defaults to the caller’s account.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\t]*`
Required: No

 ** [DatabaseName](#API_GetTableObjects_RequestSyntax) **   <a name="lakeformation-GetTableObjects-request-DatabaseName"></a>
The database containing the governed table.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\t]*`
Required: Yes

 ** [MaxResults](#API_GetTableObjects_RequestSyntax) **   <a name="lakeformation-GetTableObjects-request-MaxResults"></a>
Specifies how many values to return in a page.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 1000.
Required: No

 ** [NextToken](#API_GetTableObjects_RequestSyntax) **   <a name="lakeformation-GetTableObjects-request-NextToken"></a>
A continuation token if this is not the first call to retrieve these objects.
Type: String
Length Constraints: Maximum length of 4096.
Required: No

 ** [PartitionPredicate](#API_GetTableObjects_RequestSyntax) **   <a name="lakeformation-GetTableObjects-request-PartitionPredicate"></a>
A predicate to filter the objects returned based on the partition keys defined in the governed table.
+ The comparison operators supported are: =, >, <, >=, <=
+ The logical operators supported are: AND
+ The data types supported are integer, long, date(yyyy-MM-dd), timestamp(yyyy-MM-dd HH:mm:ssXXX or yyyy-MM-dd HH:mm:ss"), string and decimal.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 2048.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\r\n\t]*`
Required: No

 ** [QueryAsOfTime](#API_GetTableObjects_RequestSyntax) **   <a name="lakeformation-GetTableObjects-request-QueryAsOfTime"></a>
The time as of when to read the governed table contents. If not set, the most recent transaction commit time is used. Cannot be specified along with `TransactionId`.
Type: Timestamp
Required: No

 ** [TableName](#API_GetTableObjects_RequestSyntax) **   <a name="lakeformation-GetTableObjects-request-TableName"></a>
The governed table for which to retrieve objects.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\t]*`
Required: Yes

 ** [TransactionId](#API_GetTableObjects_RequestSyntax) **   <a name="lakeformation-GetTableObjects-request-TransactionId"></a>
The transaction ID at which to read the governed table contents. If this transaction has aborted, an error is returned. If not set, defaults to the most recent committed transaction. Cannot be specified along with `QueryAsOfTime`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\p{L}\p{N}\p{P}]*`
Required: No

## Response Syntax
<a name="API_GetTableObjects_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "NextToken": "string",
   "Objects": [
      {
         "Objects": [
            {
               "ETag": "string",
               "Size": number,
               "Uri": "string"
            }
         ],
         "PartitionValues": [ "string" ]
      }
   ]
}
```

## Response Elements
<a name="API_GetTableObjects_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [NextToken](#API_GetTableObjects_ResponseSyntax) **   <a name="lakeformation-GetTableObjects-response-NextToken"></a>
A continuation token indicating whether additional data is available.
Type: String
Length Constraints: Maximum length of 4096.

 ** [Objects](#API_GetTableObjects_ResponseSyntax) **   <a name="lakeformation-GetTableObjects-response-Objects"></a>
A list of objects organized by partition keys.
Type: Array of [PartitionObjects](API_PartitionObjects.md) objects

## Errors
<a name="API_GetTableObjects_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** EntityNotFoundException **
A specified entity does not exist.
 ** Message **
A message describing the problem.
HTTP Status Code: 400

 ** InternalServiceException **
An internal service error occurred.
 ** Message **
A message describing the problem.
HTTP Status Code: 500

 ** InvalidInputException **
The input provided was not valid.
 ** Message **
A message describing the problem.
HTTP Status Code: 400

 ** OperationTimeoutException **
The operation timed out.
 ** Message **
A message describing the problem.
HTTP Status Code: 400

 ** ResourceNotReadyException **
Contains details about an error related to a resource which is not ready for a transaction.
 ** Message **
A message describing the error.
HTTP Status Code: 400

 ** TransactionCanceledException **
Contains details about an error related to a transaction that was cancelled.
 ** Message **
A message describing the error.
HTTP Status Code: 400

 ** TransactionCommittedException **
Contains details about an error where the specified transaction has already been committed and cannot be used for `UpdateTableObjects`.
 ** Message **
A message describing the error.
HTTP Status Code: 400

## See Also
<a name="API_GetTableObjects_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/lakeformation-2017-03-31/GetTableObjects)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/lakeformation-2017-03-31/GetTableObjects)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/lakeformation-2017-03-31/GetTableObjects)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/lakeformation-2017-03-31/GetTableObjects)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/lakeformation-2017-03-31/GetTableObjects)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/lakeformation-2017-03-31/GetTableObjects)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/lakeformation-2017-03-31/GetTableObjects)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/lakeformation-2017-03-31/GetTableObjects)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/lakeformation-2017-03-31/GetTableObjects)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/lakeformation-2017-03-31/GetTableObjects)
