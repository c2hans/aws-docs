---
source_url: https://docs.aws.amazon.com/lake-formation/latest/APIReference/API_DescribeTransaction.html
---

# DescribeTransaction
<a name="API_DescribeTransaction"></a>

Returns the details of a single transaction.

## Request Syntax
<a name="API_DescribeTransaction_RequestSyntax"></a>

```
POST /DescribeTransaction HTTP/1.1
Content-type: application/json

{
   "TransactionId": "{{string}}"
}
```

## URI Request Parameters
<a name="API_DescribeTransaction_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_DescribeTransaction_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [TransactionId](#API_DescribeTransaction_RequestSyntax) **   <a name="lakeformation-DescribeTransaction-request-TransactionId"></a>
The transaction for which to return status.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\p{L}\p{N}\p{P}]*`
Required: Yes

## Response Syntax
<a name="API_DescribeTransaction_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "TransactionDescription": {
      "TransactionEndTime": number,
      "TransactionId": "string",
      "TransactionStartTime": number,
      "TransactionStatus": "string"
   }
}
```

## Response Elements
<a name="API_DescribeTransaction_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [TransactionDescription](#API_DescribeTransaction_ResponseSyntax) **   <a name="lakeformation-DescribeTransaction-response-TransactionDescription"></a>
Returns a `TransactionDescription` object containing information about the transaction.
Type: [TransactionDescription](API_TransactionDescription.md) object

## Errors
<a name="API_DescribeTransaction_Errors"></a>

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

## See Also
<a name="API_DescribeTransaction_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/lakeformation-2017-03-31/DescribeTransaction)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/lakeformation-2017-03-31/DescribeTransaction)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/lakeformation-2017-03-31/DescribeTransaction)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/lakeformation-2017-03-31/DescribeTransaction)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/lakeformation-2017-03-31/DescribeTransaction)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/lakeformation-2017-03-31/DescribeTransaction)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/lakeformation-2017-03-31/DescribeTransaction)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/lakeformation-2017-03-31/DescribeTransaction)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/lakeformation-2017-03-31/DescribeTransaction)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/lakeformation-2017-03-31/DescribeTransaction)
