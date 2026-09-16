---
source_url: https://docs.aws.amazon.com/billingconductor/latest/APIReference/API_ListPricingRules.html
---

# ListPricingRules
<a name="API_ListPricingRules"></a>

 Describes a pricing rule that can be associated to a pricing plan, or set of pricing plans.

## Request Syntax
<a name="API_ListPricingRules_RequestSyntax"></a>

```
POST /list-pricing-rules HTTP/1.1
Content-type: application/json

{
   "BillingPeriod": "{{string}}",
   "Filters": {
      "Arns": [ "{{string}}" ]
   },
   "MaxResults": {{number}},
   "NextToken": "{{string}}"
}
```

## URI Request Parameters
<a name="API_ListPricingRules_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_ListPricingRules_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [BillingPeriod](#API_ListPricingRules_RequestSyntax) **   <a name="billingconductor-ListPricingRules-request-BillingPeriod"></a>
 The preferred billing period to get the pricing plan.
Type: String
Pattern: `\d{4}-(0?[1-9]|1[012])`
Required: No

 ** [Filters](#API_ListPricingRules_RequestSyntax) **   <a name="billingconductor-ListPricingRules-request-Filters"></a>
 A `DescribePricingRuleFilter` that specifies the Amazon Resource Name (ARNs) of pricing rules to retrieve pricing rules information.
Type: [ListPricingRulesFilter](API_ListPricingRulesFilter.md) object
Required: No

 ** [MaxResults](#API_ListPricingRules_RequestSyntax) **   <a name="billingconductor-ListPricingRules-request-MaxResults"></a>
 The maximum number of pricing rules to retrieve.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 100.
Required: No

 ** [NextToken](#API_ListPricingRules_RequestSyntax) **   <a name="billingconductor-ListPricingRules-request-NextToken"></a>
 The pagination token that's used on subsequent call to get pricing rules.
Type: String
Required: No

## Response Syntax
<a name="API_ListPricingRules_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "BillingPeriod": "string",
   "NextToken": "string",
   "PricingRules": [
      {
         "Arn": "string",
         "AssociatedPricingPlanCount": number,
         "BillingEntity": "string",
         "CreationTime": number,
         "Description": "string",
         "LastModifiedTime": number,
         "ModifierPercentage": number,
         "Name": "string",
         "Operation": "string",
         "Scope": "string",
         "Service": "string",
         "Tiering": {
            "CustomTiers": [
               {
                  "BeginRangeInclusive": number,
                  "EndRangeExclusive": number,
                  "RateValue": number
               }
            ],
            "FreeTier": {
               "Activated": boolean
            }
         },
         "Type": "string",
         "UsageType": "string"
      }
   ]
}
```

## Response Elements
<a name="API_ListPricingRules_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [BillingPeriod](#API_ListPricingRules_ResponseSyntax) **   <a name="billingconductor-ListPricingRules-response-BillingPeriod"></a>
 The billing period for which the described pricing rules are applicable.
Type: String
Pattern: `\d{4}-(0?[1-9]|1[012])`

 ** [NextToken](#API_ListPricingRules_ResponseSyntax) **   <a name="billingconductor-ListPricingRules-response-NextToken"></a>
 The pagination token that's used on subsequent calls to get pricing rules.
Type: String

 ** [PricingRules](#API_ListPricingRules_ResponseSyntax) **   <a name="billingconductor-ListPricingRules-response-PricingRules"></a>
 A list containing the described pricing rules.
Type: Array of [PricingRuleListElement](API_PricingRuleListElement.md) objects

## Errors
<a name="API_ListPricingRules_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You do not have sufficient access to perform this action.
HTTP Status Code: 403

 ** InternalServerException **
An unexpected error occurred while processing a request.
 ** RetryAfterSeconds **
Number of seconds you can retry after the call.
HTTP Status Code: 500

 ** ThrottlingException **
The request was denied due to request throttling.
 ** RetryAfterSeconds **
Number of seconds you can safely retry after the call.
HTTP Status Code: 429

 ** ValidationException **
The input doesn't match with the constraints specified by AWS services.
 ** Fields **
The fields that caused the error, if applicable.
 ** Reason **
The reason the request's validation failed.
HTTP Status Code: 400

## See Also
<a name="API_ListPricingRules_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/billingconductor-2021-07-30/ListPricingRules)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/billingconductor-2021-07-30/ListPricingRules)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/billingconductor-2021-07-30/ListPricingRules)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/billingconductor-2021-07-30/ListPricingRules)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/billingconductor-2021-07-30/ListPricingRules)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/billingconductor-2021-07-30/ListPricingRules)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/billingconductor-2021-07-30/ListPricingRules)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/billingconductor-2021-07-30/ListPricingRules)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/billingconductor-2021-07-30/ListPricingRules)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/billingconductor-2021-07-30/ListPricingRules)
