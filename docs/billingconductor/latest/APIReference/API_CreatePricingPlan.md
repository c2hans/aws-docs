---
source_url: https://docs.aws.amazon.com/billingconductor/latest/APIReference/API_CreatePricingPlan.html
---

# CreatePricingPlan
<a name="API_CreatePricingPlan"></a>

Creates a pricing plan that is used for computing AWS charges for billing groups.

## Request Syntax
<a name="API_CreatePricingPlan_RequestSyntax"></a>

```
POST /create-pricing-plan HTTP/1.1
X-Amzn-Client-Token: {{ClientToken}}
Content-type: application/json

{
   "Description": "{{string}}",
   "Name": "{{string}}",
   "PricingRuleArns": [ "{{string}}" ],
   "Tags": {
      "{{string}}" : "{{string}}"
   }
}
```

## URI Request Parameters
<a name="API_CreatePricingPlan_RequestParameters"></a>

The request uses the following URI parameters.

 ** [ClientToken](#API_CreatePricingPlan_RequestSyntax) **   <a name="billingconductor-CreatePricingPlan-request-ClientToken"></a>
A unique, case-sensitive identifier that you specify to ensure idempotency of the request. Idempotency ensures that an API request completes no more than one time. With an idempotent request, if the original request completes successfully, any subsequent retries complete successfully without performing any further actions.
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[a-zA-Z0-9-]+`

## Request Body
<a name="API_CreatePricingPlan_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [Description](#API_CreatePricingPlan_RequestSyntax) **   <a name="billingconductor-CreatePricingPlan-request-Description"></a>
The description of the pricing plan.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Required: No

 ** [Name](#API_CreatePricingPlan_RequestSyntax) **   <a name="billingconductor-CreatePricingPlan-request-Name"></a>
The name of the pricing plan. The names must be unique to each pricing plan.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[a-zA-Z0-9_\+=\.\-@]+`
Required: Yes

 ** [PricingRuleArns](#API_CreatePricingPlan_RequestSyntax) **   <a name="billingconductor-CreatePricingPlan-request-PricingRuleArns"></a>
 A list of Amazon Resource Names (ARNs) that define the pricing plan parameters.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 30 items.
Pattern: `(arn:aws(-cn)?:billingconductor::[0-9]{12}:pricingrule/)?[a-zA-Z0-9]{10}`
Required: No

 ** [Tags](#API_CreatePricingPlan_RequestSyntax) **   <a name="billingconductor-CreatePricingPlan-request-Tags"></a>
 A map that contains tag keys and tag values that are attached to a pricing plan.
Type: String to string map
Map Entries: Maximum number of 200 items.
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Value Length Constraints: Minimum length of 0. Maximum length of 256.
Required: No

## Response Syntax
<a name="API_CreatePricingPlan_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "Arn": "string"
}
```

## Response Elements
<a name="API_CreatePricingPlan_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Arn](#API_CreatePricingPlan_ResponseSyntax) **   <a name="billingconductor-CreatePricingPlan-response-Arn"></a>
The Amazon Resource Name (ARN) of the created pricing plan.
Type: String
Pattern: `(arn:aws(-cn)?:billingconductor::(aws|[0-9]{12}):pricingplan/)?(BasicPricingPlan|Passthrough|[a-zA-Z0-9]{10})`

## Errors
<a name="API_CreatePricingPlan_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You do not have sufficient access to perform this action.
HTTP Status Code: 403

 ** ConflictException **
You can cause an inconsistent state by updating or deleting a resource.
 ** Reason **
Reason for the inconsistent state.
 ** ResourceId **
Identifier of the resource in use.
 ** ResourceType **
Type of the resource in use.
HTTP Status Code: 409

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

 ** ServiceLimitExceededException **
The request would cause a service limit to exceed.
 ** LimitCode **
The unique code identifier of the service limit that is being exceeded.
 ** ResourceId **
Identifier of the resource affected.
 ** ResourceType **
Type of the resource affected.
 ** ServiceCode **
The unique code for the service of the limit that is being exceeded.
HTTP Status Code: 402

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
<a name="API_CreatePricingPlan_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/billingconductor-2021-07-30/CreatePricingPlan)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/billingconductor-2021-07-30/CreatePricingPlan)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/billingconductor-2021-07-30/CreatePricingPlan)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/billingconductor-2021-07-30/CreatePricingPlan)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/billingconductor-2021-07-30/CreatePricingPlan)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/billingconductor-2021-07-30/CreatePricingPlan)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/billingconductor-2021-07-30/CreatePricingPlan)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/billingconductor-2021-07-30/CreatePricingPlan)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/billingconductor-2021-07-30/CreatePricingPlan)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/billingconductor-2021-07-30/CreatePricingPlan)
