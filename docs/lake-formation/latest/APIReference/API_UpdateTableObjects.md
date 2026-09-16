---
source_url: https://docs.aws.amazon.com/lake-formation/latest/APIReference/API_UpdateTableObjects.html
---

# UpdateTableObjects
<a name="API_UpdateTableObjects"></a>

Updates the manifest of Amazon S3 objects that make up the specified governed table.

## Request Syntax
<a name="API_UpdateTableObjects_RequestSyntax"></a>

```
POST /UpdateTableObjects HTTP/1.1
Content-type: application/json

{
   "CatalogId": "{{string}}",
   "DatabaseName": "{{string}}",
   "TableName": "{{string}}",
   "TransactionId": "{{string}}",
   "WriteOperations": [
      {
         "AddObject": {
            "ETag": "{{string}}",
            "PartitionValues": [ "{{string}}" ],
            "Size": {{number}},
            "Uri": "{{string}}"
         },
         "DeleteObject": {
            "ETag": "{{string}}",
            "PartitionValues": [ "{{string}}" ],
            "Uri": "{{string}}"
         }
      }
   ]
}
```

## URI Request Parameters
<a name="API_UpdateTableObjects_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_UpdateTableObjects_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [CatalogId](#API_UpdateTableObjects_RequestSyntax) **   <a name="lakeformation-UpdateTableObjects-request-CatalogId"></a>
The catalog containing the governed table to update. Defaults to the caller’s account ID.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\t]*`
Required: No

 ** [DatabaseName](#API_UpdateTableObjects_RequestSyntax) **   <a name="lakeformation-UpdateTableObjects-request-DatabaseName"></a>
The database containing the governed table to update.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\t]*`
Required: Yes

 ** [TableName](#API_UpdateTableObjects_RequestSyntax) **   <a name="lakeformation-UpdateTableObjects-request-TableName"></a>
The governed table to update.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\t]*`
Required: Yes

 ** [TransactionId](#API_UpdateTableObjects_RequestSyntax) **   <a name="lakeformation-UpdateTableObjects-request-TransactionId"></a>
The transaction at which to do the write.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\p{L}\p{N}\p{P}]*`
Required: No

 ** [WriteOperations](#API_UpdateTableObjects_RequestSyntax) **   <a name="lakeformation-UpdateTableObjects-request-WriteOperations"></a>
A list of `WriteOperation` objects that define an object to add to or delete from the manifest for a governed table.
Type: Array of [WriteOperation](API_WriteOperation.md) objects
Array Members: Minimum number of 1 item. Maximum number of 100 items.
Required: Yes

## Response Syntax
<a name="API_UpdateTableObjects_ResponseSyntax"></a>

```
HTTP/1.1 200
```

## Response Elements
<a name="API_UpdateTableObjects_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_UpdateTableObjects_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ConcurrentModificationException **
Two processes are trying to modify a resource simultaneously.
 ** Message **
A message describing the problem.
HTTP Status Code: 400

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

 ** TransactionCommitInProgressException **
Contains details about an error related to a transaction commit that was in progress.
 ** Message **
A message describing the error.
HTTP Status Code: 400

 ** TransactionCommittedException **
Contains details about an error where the specified transaction has already been committed and cannot be used for `UpdateTableObjects`.
 ** Message **
A message describing the error.
HTTP Status Code: 400

## See Also
<a name="API_UpdateTableObjects_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/lakeformation-2017-03-31/UpdateTableObjects)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/lakeformation-2017-03-31/UpdateTableObjects)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/lakeformation-2017-03-31/UpdateTableObjects)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/lakeformation-2017-03-31/UpdateTableObjects)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/lakeformation-2017-03-31/UpdateTableObjects)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/lakeformation-2017-03-31/UpdateTableObjects)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/lakeformation-2017-03-31/UpdateTableObjects)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/lakeformation-2017-03-31/UpdateTableObjects)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/lakeformation-2017-03-31/UpdateTableObjects)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/lakeformation-2017-03-31/UpdateTableObjects)
