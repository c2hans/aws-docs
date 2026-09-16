---
source_url: https://docs.aws.amazon.com/outposts/latest/APIReference/API_CreateRenewal.html
---

# CreateRenewal
<a name="API_CreateRenewal"></a>

Creates a renewal contract for the specified Outpost.

## Request Syntax
<a name="API_CreateRenewal_RequestSyntax"></a>

```
POST /renewals HTTP/1.1
Content-type: application/json

{
   "ClientToken": "{{string}}",
   "OutpostIdentifier": "{{string}}",
   "PaymentOption": "{{string}}",
   "PaymentTerm": "{{string}}"
}
```

## URI Request Parameters
<a name="API_CreateRenewal_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_CreateRenewal_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [ClientToken](#API_CreateRenewal_RequestSyntax) **   <a name="outposts-CreateRenewal-request-ClientToken"></a>
A unique, case-sensitive identifier that you provide to ensure the idempotency of the request.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `^.*$`
Required: No

 ** [OutpostIdentifier](#API_CreateRenewal_RequestSyntax) **   <a name="outposts-CreateRenewal-request-OutpostIdentifier"></a>
The ID or ARN of the Outpost.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 180.
Pattern: `^(arn:aws([a-z-]+)?:outposts:[a-z\d-]+:\d{12}:outpost/)?op-[a-f0-9]{17}$`
Required: Yes

 ** [PaymentOption](#API_CreateRenewal_RequestSyntax) **   <a name="outposts-CreateRenewal-request-PaymentOption"></a>
The payment option.
Type: String
Valid Values: `ALL_UPFRONT | NO_UPFRONT | PARTIAL_UPFRONT`
Required: Yes

 ** [PaymentTerm](#API_CreateRenewal_RequestSyntax) **   <a name="outposts-CreateRenewal-request-PaymentTerm"></a>
The payment term.
Type: String
Valid Values: `THREE_YEARS | ONE_YEAR | FIVE_YEARS`
Required: Yes

## Response Syntax
<a name="API_CreateRenewal_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "Currency": "string",
   "MonthlyRecurringPrice": number,
   "OutpostId": "string",
   "PaymentOption": "string",
   "PaymentTerm": "string",
   "UpfrontPrice": number
}
```

## Response Elements
<a name="API_CreateRenewal_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Currency](#API_CreateRenewal_ResponseSyntax) **   <a name="outposts-CreateRenewal-response-Currency"></a>
The currency of the renewal price.
Type: String
Valid Values: `USD`

 ** [MonthlyRecurringPrice](#API_CreateRenewal_ResponseSyntax) **   <a name="outposts-CreateRenewal-response-MonthlyRecurringPrice"></a>
The monthly recurring price of the renewal.
Type: Float

 ** [OutpostId](#API_CreateRenewal_ResponseSyntax) **   <a name="outposts-CreateRenewal-response-OutpostId"></a>
The ID of the Outpost.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 20.
Pattern: `^op-[a-f0-9]{17}$`

 ** [PaymentOption](#API_CreateRenewal_ResponseSyntax) **   <a name="outposts-CreateRenewal-response-PaymentOption"></a>
The payment option.
Type: String
Valid Values: `ALL_UPFRONT | NO_UPFRONT | PARTIAL_UPFRONT`

 ** [PaymentTerm](#API_CreateRenewal_ResponseSyntax) **   <a name="outposts-CreateRenewal-response-PaymentTerm"></a>
The payment term.
Type: String
Valid Values: `THREE_YEARS | ONE_YEAR | FIVE_YEARS`

 ** [UpfrontPrice](#API_CreateRenewal_ResponseSyntax) **   <a name="outposts-CreateRenewal-response-UpfrontPrice"></a>
The upfront price of the renewal.
Type: Float

## Errors
<a name="API_CreateRenewal_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You do not have permission to perform this operation.
HTTP Status Code: 403

 ** InternalServerException **
An internal error has occurred.
HTTP Status Code: 500

 ** NotFoundException **
The specified request is not valid.
HTTP Status Code: 404

 ** ValidationException **
A parameter is not valid.
HTTP Status Code: 400

## Examples
<a name="API_CreateRenewal_Examples"></a>

### Example
<a name="API_CreateRenewal_Example_1"></a>

This example creates a renewal for the specified Outpost.

#### Sample Request
<a name="API_CreateRenewal_Example_1_Request"></a>

```
aws outposts create-renewal --outpost-identifier op-1234567890example --payment-option ALL_UPFRONT --payment-term ONE_YEAR
```

#### Sample Response
<a name="API_CreateRenewal_Example_1_Response"></a>

```
{
  "PaymentOption": "ALL_UPFRONT",
  "PaymentTerm": "ONE_YEAR",
  "OutpostId": "op-1234567890example",
  "UpfrontPrice": 12000.00,
  "MonthlyRecurringPrice": 0.0,
  "Currency": "USD"
}
```

## See Also
<a name="API_CreateRenewal_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/outposts-2019-12-03/CreateRenewal)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/outposts-2019-12-03/CreateRenewal)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/outposts-2019-12-03/CreateRenewal)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/outposts-2019-12-03/CreateRenewal)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/outposts-2019-12-03/CreateRenewal)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/outposts-2019-12-03/CreateRenewal)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/outposts-2019-12-03/CreateRenewal)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/outposts-2019-12-03/CreateRenewal)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/outposts-2019-12-03/CreateRenewal)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/outposts-2019-12-03/CreateRenewal)
