---
source_url: https://docs.aws.amazon.com/lake-formation/latest/APIReference/API_StartTransaction.html
---

# StartTransaction
<a name="API_StartTransaction"></a>

Starts a new transaction and returns its transaction ID. Transaction IDs are opaque objects that you can use to identify a transaction.

## Request Syntax
<a name="API_StartTransaction_RequestSyntax"></a>

```
POST /StartTransaction HTTP/1.1
Content-type: application/json

{
   "TransactionType": "{{string}}"
}
```

## URI Request Parameters
<a name="API_StartTransaction_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_StartTransaction_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [TransactionType](#API_StartTransaction_RequestSyntax) **   <a name="lakeformation-StartTransaction-request-TransactionType"></a>
Indicates whether this transaction should be read only or read and write. Writes made using a read-only transaction ID will be rejected. Read-only transactions do not need to be committed.
Type: String
Valid Values: `READ_AND_WRITE | READ_ONLY`
Required: No

## Response Syntax
<a name="API_StartTransaction_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "TransactionId": "string"
}
```

## Response Elements
<a name="API_StartTransaction_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [TransactionId](#API_StartTransaction_ResponseSyntax) **   <a name="lakeformation-StartTransaction-response-TransactionId"></a>
An opaque identifier for the transaction.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\p{L}\p{N}\p{P}]*`

## Errors
<a name="API_StartTransaction_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InternalServiceException **
An internal service error occurred.
 ** Message **
A message describing the problem.
HTTP Status Code: 500

 ** OperationTimeoutException **
The operation timed out.
 ** Message **
A message describing the problem.
HTTP Status Code: 400

## See Also
<a name="API_StartTransaction_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/lakeformation-2017-03-31/StartTransaction)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/lakeformation-2017-03-31/StartTransaction)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/lakeformation-2017-03-31/StartTransaction)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/lakeformation-2017-03-31/StartTransaction)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/lakeformation-2017-03-31/StartTransaction)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/lakeformation-2017-03-31/StartTransaction)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/lakeformation-2017-03-31/StartTransaction)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/lakeformation-2017-03-31/StartTransaction)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/lakeformation-2017-03-31/StartTransaction)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/lakeformation-2017-03-31/StartTransaction)
