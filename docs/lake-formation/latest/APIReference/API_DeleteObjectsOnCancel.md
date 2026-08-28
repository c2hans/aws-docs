---
source_url: https://docs.aws.amazon.com/lake-formation/latest/APIReference/API_DeleteObjectsOnCancel.html
---

# DeleteObjectsOnCancel
<a name="API_DeleteObjectsOnCancel"></a>

For a specific governed table, provides a list of Amazon S3 objects that will be written during the current transaction and that can be automatically deleted if the transaction is canceled. Without this call, no Amazon S3 objects are automatically deleted when a transaction cancels.

 The AWS Glue ETL library function `write_dynamic_frame.from_catalog()` includes an option to automatically call `DeleteObjectsOnCancel` before writes. For more information, see [Rolling Back Amazon S3 Writes](https://docs.aws.amazon.com/lake-formation/latest/dg/transactions-data-operations.html#rolling-back-writes).

## Request Syntax
<a name="API_DeleteObjectsOnCancel_RequestSyntax"></a>

```
POST /DeleteObjectsOnCancel HTTP/1.1
Content-type: application/json

{
   "CatalogId": "{{string}}",
   "DatabaseName": "{{string}}",
   "Objects": [
      {
         "ETag": "{{string}}",
         "Uri": "{{string}}"
      }
   ],
   "TableName": "{{string}}",
   "TransactionId": "{{string}}"
}
```

## URI Request Parameters
<a name="API_DeleteObjectsOnCancel_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_DeleteObjectsOnCancel_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [CatalogId](#API_DeleteObjectsOnCancel_RequestSyntax) **   <a name="lakeformation-DeleteObjectsOnCancel-request-CatalogId"></a>
The AWS Glue data catalog that contains the governed table. Defaults to the current account ID.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\t]*`
Required: No

 ** [DatabaseName](#API_DeleteObjectsOnCancel_RequestSyntax) **   <a name="lakeformation-DeleteObjectsOnCancel-request-DatabaseName"></a>
The database that contains the governed table.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\t]*`
Required: Yes

 ** [Objects](#API_DeleteObjectsOnCancel_RequestSyntax) **   <a name="lakeformation-DeleteObjectsOnCancel-request-Objects"></a>
A list of VirtualObject structures, which indicates the Amazon S3 objects to be deleted if the transaction cancels.
Type: Array of [VirtualObject](API_VirtualObject.md) objects
Array Members: Minimum number of 1 item. Maximum number of 100 items.
Required: Yes

 ** [TableName](#API_DeleteObjectsOnCancel_RequestSyntax) **   <a name="lakeformation-DeleteObjectsOnCancel-request-TableName"></a>
The name of the governed table.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\t]*`
Required: Yes

 ** [TransactionId](#API_DeleteObjectsOnCancel_RequestSyntax) **   <a name="lakeformation-DeleteObjectsOnCancel-request-TransactionId"></a>
ID of the transaction that the writes occur in.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\p{L}\p{N}\p{P}]*`
Required: Yes

## Response Syntax
<a name="API_DeleteObjectsOnCancel_ResponseSyntax"></a>

```
HTTP/1.1 200
```

## Response Elements
<a name="API_DeleteObjectsOnCancel_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_DeleteObjectsOnCancel_Errors"></a>

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

 ** TransactionCommittedException **
Contains details about an error where the specified transaction has already been committed and cannot be used for `UpdateTableObjects`.
 ** Message **
A message describing the error.
HTTP Status Code: 400

## See Also
<a name="API_DeleteObjectsOnCancel_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/lakeformation-2017-03-31/DeleteObjectsOnCancel)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/lakeformation-2017-03-31/DeleteObjectsOnCancel)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/lakeformation-2017-03-31/DeleteObjectsOnCancel)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/lakeformation-2017-03-31/DeleteObjectsOnCancel)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/lakeformation-2017-03-31/DeleteObjectsOnCancel)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/lakeformation-2017-03-31/DeleteObjectsOnCancel)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/lakeformation-2017-03-31/DeleteObjectsOnCancel)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/lakeformation-2017-03-31/DeleteObjectsOnCancel)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/lakeformation-2017-03-31/DeleteObjectsOnCancel)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/lakeformation-2017-03-31/DeleteObjectsOnCancel)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Lake Formation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query lake-formation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
