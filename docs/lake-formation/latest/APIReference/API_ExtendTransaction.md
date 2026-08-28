---
source_url: https://docs.aws.amazon.com/lake-formation/latest/APIReference/API_ExtendTransaction.html
---

# ExtendTransaction
<a name="API_ExtendTransaction"></a>

Indicates to the service that the specified transaction is still active and should not be treated as idle and aborted.

Write transactions that remain idle for a long period are automatically aborted unless explicitly extended.

## Request Syntax
<a name="API_ExtendTransaction_RequestSyntax"></a>

```
POST /ExtendTransaction HTTP/1.1
Content-type: application/json

{
   "TransactionId": "{{string}}"
}
```

## URI Request Parameters
<a name="API_ExtendTransaction_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_ExtendTransaction_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [TransactionId](#API_ExtendTransaction_RequestSyntax) **   <a name="lakeformation-ExtendTransaction-request-TransactionId"></a>
The transaction to extend.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\p{L}\p{N}\p{P}]*`
Required: No

## Response Syntax
<a name="API_ExtendTransaction_ResponseSyntax"></a>

```
HTTP/1.1 200
```

## Response Elements
<a name="API_ExtendTransaction_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_ExtendTransaction_Errors"></a>

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
<a name="API_ExtendTransaction_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/lakeformation-2017-03-31/ExtendTransaction)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/lakeformation-2017-03-31/ExtendTransaction)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/lakeformation-2017-03-31/ExtendTransaction)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/lakeformation-2017-03-31/ExtendTransaction)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/lakeformation-2017-03-31/ExtendTransaction)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/lakeformation-2017-03-31/ExtendTransaction)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/lakeformation-2017-03-31/ExtendTransaction)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/lakeformation-2017-03-31/ExtendTransaction)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/lakeformation-2017-03-31/ExtendTransaction)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/lakeformation-2017-03-31/ExtendTransaction)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Lake Formation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query lake-formation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
