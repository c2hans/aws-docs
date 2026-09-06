---
source_url: https://docs.aws.amazon.com/lake-formation/latest/APIReference/API_ListTransactions.html
---

# ListTransactions
<a name="API_ListTransactions"></a>

Returns metadata about transactions and their status. To prevent the response from growing indefinitely, only uncommitted transactions and those available for time-travel queries are returned.

This operation can help you identify uncommitted transactions or to get information about transactions.

## Request Syntax
<a name="API_ListTransactions_RequestSyntax"></a>

```
POST /ListTransactions HTTP/1.1
Content-type: application/json

{
   "CatalogId": "{{string}}",
   "MaxResults": {{number}},
   "NextToken": "{{string}}",
   "StatusFilter": "{{string}}"
}
```

## URI Request Parameters
<a name="API_ListTransactions_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_ListTransactions_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [CatalogId](#API_ListTransactions_RequestSyntax) **   <a name="lakeformation-ListTransactions-request-CatalogId"></a>
The catalog for which to list transactions. Defaults to the account ID of the caller.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\t]*`
Required: No

 ** [MaxResults](#API_ListTransactions_RequestSyntax) **   <a name="lakeformation-ListTransactions-request-MaxResults"></a>
The maximum number of transactions to return in a single call.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 1000.
Required: No

 ** [NextToken](#API_ListTransactions_RequestSyntax) **   <a name="lakeformation-ListTransactions-request-NextToken"></a>
A continuation token if this is not the first call to retrieve transactions.
Type: String
Length Constraints: Maximum length of 4096.
Required: No

 ** [StatusFilter](#API_ListTransactions_RequestSyntax) **   <a name="lakeformation-ListTransactions-request-StatusFilter"></a>
 A filter indicating the status of transactions to return. Options are ALL \| COMPLETED \| COMMITTED \| ABORTED \| ACTIVE. The default is `ALL`.
Type: String
Valid Values: `ALL | COMPLETED | ACTIVE | COMMITTED | ABORTED`
Required: No

## Response Syntax
<a name="API_ListTransactions_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "NextToken": "string",
   "Transactions": [
      {
         "TransactionEndTime": number,
         "TransactionId": "string",
         "TransactionStartTime": number,
         "TransactionStatus": "string"
      }
   ]
}
```

## Response Elements
<a name="API_ListTransactions_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [NextToken](#API_ListTransactions_ResponseSyntax) **   <a name="lakeformation-ListTransactions-response-NextToken"></a>
A continuation token indicating whether additional data is available.
Type: String
Length Constraints: Maximum length of 4096.

 ** [Transactions](#API_ListTransactions_ResponseSyntax) **   <a name="lakeformation-ListTransactions-response-Transactions"></a>
A list of transactions. The record for each transaction is a `TransactionDescription` object.
Type: Array of [TransactionDescription](API_TransactionDescription.md) objects

## Errors
<a name="API_ListTransactions_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

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
<a name="API_ListTransactions_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/lakeformation-2017-03-31/ListTransactions)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/lakeformation-2017-03-31/ListTransactions)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/lakeformation-2017-03-31/ListTransactions)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/lakeformation-2017-03-31/ListTransactions)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/lakeformation-2017-03-31/ListTransactions)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/lakeformation-2017-03-31/ListTransactions)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/lakeformation-2017-03-31/ListTransactions)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/lakeformation-2017-03-31/ListTransactions)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/lakeformation-2017-03-31/ListTransactions)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/lakeformation-2017-03-31/ListTransactions)
