---
source_url: https://docs.aws.amazon.com/outposts/latest/APIReference/API_GetOutpostBillingInformation.html
---

# GetOutpostBillingInformation
<a name="API_GetOutpostBillingInformation"></a>

Gets current and historical billing information about the specified Outpost.

## Request Syntax
<a name="API_GetOutpostBillingInformation_RequestSyntax"></a>

```
GET /outpost/{{OutpostIdentifier}}/billing-information?MaxResults={{MaxResults}}&NextToken={{NextToken}} HTTP/1.1
```

## URI Request Parameters
<a name="API_GetOutpostBillingInformation_RequestParameters"></a>

The request uses the following URI parameters.

 ** [MaxResults](#API_GetOutpostBillingInformation_RequestSyntax) **   <a name="outposts-GetOutpostBillingInformation-request-uri-MaxResults"></a>
The maximum page size.
Valid Range: Minimum value of 1. Maximum value of 1000.

 ** [NextToken](#API_GetOutpostBillingInformation_RequestSyntax) **   <a name="outposts-GetOutpostBillingInformation-request-uri-NextToken"></a>
The pagination token.
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `^(\d+)##(\S+)$`

 ** [OutpostIdentifier](#API_GetOutpostBillingInformation_RequestSyntax) **   <a name="outposts-GetOutpostBillingInformation-request-uri-OutpostIdentifier"></a>
The ID or ARN of the Outpost.
Length Constraints: Minimum length of 1. Maximum length of 180.
Pattern: `^(arn:aws([a-z-]+)?:outposts:[a-z\d-]+:\d{12}:outpost/)?op-[a-f0-9]{17}$`
Required: Yes

## Request Body
<a name="API_GetOutpostBillingInformation_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_GetOutpostBillingInformation_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "ContractEndDate": "string",
   "NextToken": "string",
   "PaymentOption": "string",
   "PaymentTerm": "string",
   "Subscriptions": [
      {
         "BeginDate": number,
         "Currency": "string",
         "EndDate": number,
         "MonthlyRecurringPrice": number,
         "OrderIds": [ "string" ],
         "SubscriptionId": "string",
         "SubscriptionStatus": "string",
         "SubscriptionType": "string",
         "UpfrontPrice": number
      }
   ]
}
```

## Response Elements
<a name="API_GetOutpostBillingInformation_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [ContractEndDate](#API_GetOutpostBillingInformation_ResponseSyntax) **   <a name="outposts-GetOutpostBillingInformation-response-ContractEndDate"></a>
The date the current contract term ends for the specified Outpost. You must start the renewal or decommission process at least 5 business days before the current term for your AWS Outposts ends. Failing to complete these steps at least 5 business days before the current term ends might result in unanticipated charges.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1000.
Pattern: `^[\S \n]+$`

 ** [NextToken](#API_GetOutpostBillingInformation_ResponseSyntax) **   <a name="outposts-GetOutpostBillingInformation-response-NextToken"></a>
The pagination token.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `^(\d+)##(\S+)$`

 ** [PaymentOption](#API_GetOutpostBillingInformation_ResponseSyntax) **   <a name="outposts-GetOutpostBillingInformation-response-PaymentOption"></a>
The payment option.
Type: String
Valid Values: `ALL_UPFRONT | NO_UPFRONT | PARTIAL_UPFRONT`

 ** [PaymentTerm](#API_GetOutpostBillingInformation_ResponseSyntax) **   <a name="outposts-GetOutpostBillingInformation-response-PaymentTerm"></a>
The payment term.
Type: String
Valid Values: `THREE_YEARS | ONE_YEAR | FIVE_YEARS`

 ** [Subscriptions](#API_GetOutpostBillingInformation_ResponseSyntax) **   <a name="outposts-GetOutpostBillingInformation-response-Subscriptions"></a>
The subscription details for the specified Outpost.
Type: Array of [Subscription](API_Subscription.md) objects

## Errors
<a name="API_GetOutpostBillingInformation_Errors"></a>

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

## Examples
<a name="API_GetOutpostBillingInformation_Examples"></a>

### Example
<a name="API_GetOutpostBillingInformation_Example_1"></a>

This example displays information about the subscription for the specified Outpost.

#### Sample Request
<a name="API_GetOutpostBillingInformation_Example_1_Request"></a>

```
aws outposts get-outpost-billing-information --outpost-identifier op-1234567890example"
```

#### Sample Response
<a name="API_GetOutpostBillingInformation_Example_1_Response"></a>

```
{
  "Subscriptions": [
    {
      "SubscriptionId": "1234567890",
      "SubscriptionType": "ORIGINAL",
      "SubscriptionStatus": "ACTIVE",
      "OrderIds": [
        "oo-00000000000000000"
      ],
      "BeginDate": "Tue Jul 18 16:09:01 UTC 2024",
      "EndDate": "Fri Jul 17 16:09:01 UTC 2026",
      "Currency": "USD",
      "MonthlyRecurringPrice": 100.12,
      "UpfrontPrice": 1000.10
    }
  ],
  "ContractEndDate": "Fri Jul 17 16:09:01 UTC 2026",
  "PaymentTerm": "THREE_YEARS",
  "PaymentOption": "PARTIAL_UPFRONT"
}
```

## See Also
<a name="API_GetOutpostBillingInformation_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/outposts-2019-12-03/GetOutpostBillingInformation)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/outposts-2019-12-03/GetOutpostBillingInformation)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/outposts-2019-12-03/GetOutpostBillingInformation)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/outposts-2019-12-03/GetOutpostBillingInformation)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/outposts-2019-12-03/GetOutpostBillingInformation)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/outposts-2019-12-03/GetOutpostBillingInformation)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/outposts-2019-12-03/GetOutpostBillingInformation)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/outposts-2019-12-03/GetOutpostBillingInformation)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/outposts-2019-12-03/GetOutpostBillingInformation)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/outposts-2019-12-03/GetOutpostBillingInformation)
