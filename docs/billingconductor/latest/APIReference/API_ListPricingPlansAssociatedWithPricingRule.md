---
source_url: https://docs.aws.amazon.com/billingconductor/latest/APIReference/API_ListPricingPlansAssociatedWithPricingRule.html
---

# ListPricingPlansAssociatedWithPricingRule
<a name="API_ListPricingPlansAssociatedWithPricingRule"></a>

 A list of the pricing plans that are associated with a pricing rule.

## Request Syntax
<a name="API_ListPricingPlansAssociatedWithPricingRule_RequestSyntax"></a>

```
POST /list-pricing-plans-associated-with-pricing-rule HTTP/1.1
Content-type: application/json

{
   "BillingPeriod": "{{string}}",
   "MaxResults": {{number}},
   "NextToken": "{{string}}",
   "PricingRuleArn": "{{string}}"
}
```

## URI Request Parameters
<a name="API_ListPricingPlansAssociatedWithPricingRule_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_ListPricingPlansAssociatedWithPricingRule_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [BillingPeriod](#API_ListPricingPlansAssociatedWithPricingRule_RequestSyntax) **   <a name="billingconductor-ListPricingPlansAssociatedWithPricingRule-request-BillingPeriod"></a>
 The pricing plan billing period for which associations will be listed.
Type: String
Pattern: `\d{4}-(0?[1-9]|1[012])`
Required: No

 ** [MaxResults](#API_ListPricingPlansAssociatedWithPricingRule_RequestSyntax) **   <a name="billingconductor-ListPricingPlansAssociatedWithPricingRule-request-MaxResults"></a>
 The optional maximum number of pricing rule associations to retrieve.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 100.
Required: No

 ** [NextToken](#API_ListPricingPlansAssociatedWithPricingRule_RequestSyntax) **   <a name="billingconductor-ListPricingPlansAssociatedWithPricingRule-request-NextToken"></a>
 The optional pagination token returned by a previous call.
Type: String
Required: No

 ** [PricingRuleArn](#API_ListPricingPlansAssociatedWithPricingRule_RequestSyntax) **   <a name="billingconductor-ListPricingPlansAssociatedWithPricingRule-request-PricingRuleArn"></a>
 The pricing rule Amazon Resource Name (ARN) for which associations will be listed.
Type: String
Pattern: `(arn:aws(-cn)?:billingconductor::[0-9]{12}:pricingrule/)?[a-zA-Z0-9]{10}`
Required: Yes

## Response Syntax
<a name="API_ListPricingPlansAssociatedWithPricingRule_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "BillingPeriod": "string",
   "NextToken": "string",
   "PricingPlanArns": [ "string" ],
   "PricingRuleArn": "string"
}
```

## Response Elements
<a name="API_ListPricingPlansAssociatedWithPricingRule_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [BillingPeriod](#API_ListPricingPlansAssociatedWithPricingRule_ResponseSyntax) **   <a name="billingconductor-ListPricingPlansAssociatedWithPricingRule-response-BillingPeriod"></a>
 The pricing plan billing period for which associations will be listed.
Type: String
Pattern: `\d{4}-(0?[1-9]|1[012])`

 ** [NextToken](#API_ListPricingPlansAssociatedWithPricingRule_ResponseSyntax) **   <a name="billingconductor-ListPricingPlansAssociatedWithPricingRule-response-NextToken"></a>
 The pagination token to be used on subsequent calls.
Type: String

 ** [PricingPlanArns](#API_ListPricingPlansAssociatedWithPricingRule_ResponseSyntax) **   <a name="billingconductor-ListPricingPlansAssociatedWithPricingRule-response-PricingPlanArns"></a>
 The list containing pricing plans that are associated with the requested pricing rule.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 100 items.
Pattern: `(arn:aws(-cn)?:billingconductor::(aws|[0-9]{12}):pricingplan/)?(BasicPricingPlan|Passthrough|[a-zA-Z0-9]{10})`

 ** [PricingRuleArn](#API_ListPricingPlansAssociatedWithPricingRule_ResponseSyntax) **   <a name="billingconductor-ListPricingPlansAssociatedWithPricingRule-response-PricingRuleArn"></a>
 The pricing rule Amazon Resource Name (ARN) for which associations will be listed.
Type: String
Pattern: `(arn:aws(-cn)?:billingconductor::[0-9]{12}:pricingrule/)?[a-zA-Z0-9]{10}`

## Errors
<a name="API_ListPricingPlansAssociatedWithPricingRule_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You do not have sufficient access to perform this action.
HTTP Status Code: 403

 ** InternalServerException **
An unexpected error occurred while processing a request.
 ** RetryAfterSeconds **
Number of seconds you can retry after the call.
HTTP Status Code: 500

 ** ResourceNotFoundException **
The request references a resource that doesn't exist.
 ** ResourceId **
Resource identifier that was not found.
 ** ResourceType **
Resource type that was not found.
HTTP Status Code: 404

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
<a name="API_ListPricingPlansAssociatedWithPricingRule_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/billingconductor-2021-07-30/ListPricingPlansAssociatedWithPricingRule)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/billingconductor-2021-07-30/ListPricingPlansAssociatedWithPricingRule)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/billingconductor-2021-07-30/ListPricingPlansAssociatedWithPricingRule)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/billingconductor-2021-07-30/ListPricingPlansAssociatedWithPricingRule)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/billingconductor-2021-07-30/ListPricingPlansAssociatedWithPricingRule)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/billingconductor-2021-07-30/ListPricingPlansAssociatedWithPricingRule)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/billingconductor-2021-07-30/ListPricingPlansAssociatedWithPricingRule)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/billingconductor-2021-07-30/ListPricingPlansAssociatedWithPricingRule)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/billingconductor-2021-07-30/ListPricingPlansAssociatedWithPricingRule)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/billingconductor-2021-07-30/ListPricingPlansAssociatedWithPricingRule)
