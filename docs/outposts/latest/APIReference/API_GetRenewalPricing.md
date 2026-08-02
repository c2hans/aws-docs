---
source_url: https://docs.aws.amazon.com/outposts/latest/APIReference/API_GetRenewalPricing.html
---

# GetRenewalPricing
<a name="API_GetRenewalPricing"></a>

Gets all available renewal pricing options for the specified Outpost.

## Request Syntax
<a name="API_GetRenewalPricing_RequestSyntax"></a>

```
GET /outpost/{{OutpostIdentifier}}/renewal-pricing HTTP/1.1
```

## URI Request Parameters
<a name="API_GetRenewalPricing_RequestParameters"></a>

The request uses the following URI parameters.

 ** [OutpostIdentifier](#API_GetRenewalPricing_RequestSyntax) **   <a name="outposts-GetRenewalPricing-request-uri-OutpostIdentifier"></a>
The ID or ARN of the Outpost.
Length Constraints: Minimum length of 1. Maximum length of 180.
Pattern: `^(arn:aws([a-z-]+)?:outposts:[a-z\d-]+:\d{12}:outpost/)?op-[a-f0-9]{17}$`
Required: Yes

## Request Body
<a name="API_GetRenewalPricing_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_GetRenewalPricing_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "PricingOptions": [
      {
         "PricingType": "string",
         "SubscriptionPricingDetails": {
            "Currency": "string",
            "MonthlyRecurringPrice": number,
            "PaymentOption": "string",
            "PaymentTerm": "string",
            "UpfrontPrice": number
         }
      }
   ],
   "PricingResult": "string"
}
```

## Response Elements
<a name="API_GetRenewalPricing_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [PricingOptions](#API_GetRenewalPricing_ResponseSyntax) **   <a name="outposts-GetRenewalPricing-response-PricingOptions"></a>
The pricing options for the specified Outpost.
Type: Array of [PricingOption](API_PricingOption.md) objects
Array Members: Maximum number of 9 items.

 ** [PricingResult](#API_GetRenewalPricing_ResponseSyntax) **   <a name="outposts-GetRenewalPricing-response-PricingResult"></a>
The result of the pricing request.
Type: String
Valid Values: `PRICED | UNABLE_TO_PRICE`

## Errors
<a name="API_GetRenewalPricing_Errors"></a>

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
<a name="API_GetRenewalPricing_Examples"></a>

### Example
<a name="API_GetRenewalPricing_Example_1"></a>

This example displays the available renewal pricing options for the specified Outpost.

#### Sample Request
<a name="API_GetRenewalPricing_Example_1_Request"></a>

```
aws outposts get-renewal-pricing --outpost-identifier op-1234567890example
```

#### Sample Response
<a name="API_GetRenewalPricing_Example_1_Response"></a>

```
{
  "PricingResult": "PRICED",
  "PricingOptions": [
    {
      "PricingType": "SUBSCRIPTION",
      "SubscriptionPricingDetails": {
        "PaymentOption": "ALL_UPFRONT",
        "PaymentTerm": "ONE_YEAR",
        "UpfrontPrice": 12000.00,
        "MonthlyRecurringPrice": 0.0,
        "Currency": "USD"
      }
    },
    {
      "PricingType": "SUBSCRIPTION",
      "SubscriptionPricingDetails": {
        "PaymentOption": "NO_UPFRONT",
        "PaymentTerm": "ONE_YEAR",
        "UpfrontPrice": 0.0,
        "MonthlyRecurringPrice": 1100.00,
        "Currency": "USD"
      }
    }
  ]
}
```

## See Also
<a name="API_GetRenewalPricing_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/outposts-2019-12-03/GetRenewalPricing)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/outposts-2019-12-03/GetRenewalPricing)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/outposts-2019-12-03/GetRenewalPricing)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/outposts-2019-12-03/GetRenewalPricing)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/outposts-2019-12-03/GetRenewalPricing)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/outposts-2019-12-03/GetRenewalPricing)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/outposts-2019-12-03/GetRenewalPricing)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/outposts-2019-12-03/GetRenewalPricing)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/outposts-2019-12-03/GetRenewalPricing)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/outposts-2019-12-03/GetRenewalPricing)
