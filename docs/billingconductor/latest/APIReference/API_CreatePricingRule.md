---
source_url: https://docs.aws.amazon.com/billingconductor/latest/APIReference/API_CreatePricingRule.html
---

# CreatePricingRule
<a name="API_CreatePricingRule"></a>

 Creates a pricing rule can be associated to a pricing plan, or a set of pricing plans.

## Request Syntax
<a name="API_CreatePricingRule_RequestSyntax"></a>

```
POST /create-pricing-rule HTTP/1.1
X-Amzn-Client-Token: {{ClientToken}}
Content-type: application/json

{
   "BillingEntity": "{{string}}",
   "Description": "{{string}}",
   "ModifierPercentage": {{number}},
   "Name": "{{string}}",
   "Operation": "{{string}}",
   "Scope": "{{string}}",
   "Service": "{{string}}",
   "Tags": {
      "{{string}}" : "{{string}}"
   },
   "Tiering": {
      "CustomTiers": [
         {
            "BeginRangeInclusive": {{number}},
            "EndRangeExclusive": {{number}},
            "RateValue": {{number}}
         }
      ],
      "FreeTier": {
         "Activated": {{boolean}}
      }
   },
   "Type": "{{string}}",
   "UsageType": "{{string}}"
}
```

## URI Request Parameters
<a name="API_CreatePricingRule_RequestParameters"></a>

The request uses the following URI parameters.

 ** [ClientToken](#API_CreatePricingRule_RequestSyntax) **   <a name="billingconductor-CreatePricingRule-request-ClientToken"></a>
A unique, case-sensitive identifier that you specify to ensure idempotency of the request. Idempotency ensures that an API request completes no more than one time. With an idempotent request, if the original request completes successfully, any subsequent retries complete successfully without performing any further actions.
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[a-zA-Z0-9-]+`

## Request Body
<a name="API_CreatePricingRule_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [BillingEntity](#API_CreatePricingRule_RequestSyntax) **   <a name="billingconductor-CreatePricingRule-request-BillingEntity"></a>
 The seller of services provided by AWS, their affiliates, or third-party providers selling services via AWS Marketplace.
Type: String
Pattern: `[a-zA-Z0-9() ]+`
Required: No

 ** [Description](#API_CreatePricingRule_RequestSyntax) **   <a name="billingconductor-CreatePricingRule-request-Description"></a>
 The pricing rule description.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Required: No

 ** [ModifierPercentage](#API_CreatePricingRule_RequestSyntax) **   <a name="billingconductor-CreatePricingRule-request-ModifierPercentage"></a>
A percentage modifier that's applied on the public pricing rates. Your entry will be rounded to the nearest 2 decimal places.
Type: Double
Valid Range: Minimum value of 0.
Required: No

 ** [Name](#API_CreatePricingRule_RequestSyntax) **   <a name="billingconductor-CreatePricingRule-request-Name"></a>
 The pricing rule name. The names must be unique to each pricing rule.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[a-zA-Z0-9_\+=\.\-@]+`
Required: Yes

 ** [Operation](#API_CreatePricingRule_RequestSyntax) **   <a name="billingconductor-CreatePricingRule-request-Operation"></a>
 Operation is the specific AWS action covered by this line item. This describes the specific usage of the line item.
 If the `Scope` attribute is set to `SKU`, this attribute indicates which operation the `PricingRule` is modifying. For example, a value of `RunInstances:0202` indicates the operation of running an Amazon EC2 instance.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `\S+`
Required: No

 ** [Scope](#API_CreatePricingRule_RequestSyntax) **   <a name="billingconductor-CreatePricingRule-request-Scope"></a>
 The scope of pricing rule that indicates if it's globally applicable, or it's service-specific.
Type: String
Valid Values: `GLOBAL | SERVICE | BILLING_ENTITY | SKU`
Required: Yes

 ** [Service](#API_CreatePricingRule_RequestSyntax) **   <a name="billingconductor-CreatePricingRule-request-Service"></a>
 If the `Scope` attribute is set to `SERVICE` or `SKU`, the attribute indicates which service the `PricingRule` is applicable for.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[a-zA-Z0-9]+`
Required: No

 ** [Tags](#API_CreatePricingRule_RequestSyntax) **   <a name="billingconductor-CreatePricingRule-request-Tags"></a>
 A map that contains tag keys and tag values that are attached to a pricing rule.
Type: String to string map
Map Entries: Maximum number of 200 items.
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Value Length Constraints: Minimum length of 0. Maximum length of 256.
Required: No

 ** [Tiering](#API_CreatePricingRule_RequestSyntax) **   <a name="billingconductor-CreatePricingRule-request-Tiering"></a>
 The set of tiering configurations for the pricing rule.
Type: [CreateTieringInput](API_CreateTieringInput.md) object
Required: No

 ** [Type](#API_CreatePricingRule_RequestSyntax) **   <a name="billingconductor-CreatePricingRule-request-Type"></a>
 The type of pricing rule.
Type: String
Valid Values: `MARKUP | DISCOUNT | TIERING`
Required: Yes

 ** [UsageType](#API_CreatePricingRule_RequestSyntax) **   <a name="billingconductor-CreatePricingRule-request-UsageType"></a>
 Usage type is the unit that each service uses to measure the usage of a specific type of resource.
If the `Scope` attribute is set to `SKU`, this attribute indicates which usage type the `PricingRule` is modifying. For example, `USW2-BoxUsage:m2.2xlarge` describes an` M2 High Memory Double Extra Large` instance in the US West (Oregon) Region.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `\S+`
Required: No

## Response Syntax
<a name="API_CreatePricingRule_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "Arn": "string"
}
```

## Response Elements
<a name="API_CreatePricingRule_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Arn](#API_CreatePricingRule_ResponseSyntax) **   <a name="billingconductor-CreatePricingRule-response-Arn"></a>
 The Amazon Resource Name (ARN) of the created pricing rule.
Type: String
Pattern: `(arn:aws(-cn)?:billingconductor::[0-9]{12}:pricingrule/)?[a-zA-Z0-9]{10}`

## Errors
<a name="API_CreatePricingRule_Errors"></a>

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
<a name="API_CreatePricingRule_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/billingconductor-2021-07-30/CreatePricingRule)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/billingconductor-2021-07-30/CreatePricingRule)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/billingconductor-2021-07-30/CreatePricingRule)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/billingconductor-2021-07-30/CreatePricingRule)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/billingconductor-2021-07-30/CreatePricingRule)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/billingconductor-2021-07-30/CreatePricingRule)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/billingconductor-2021-07-30/CreatePricingRule)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/billingconductor-2021-07-30/CreatePricingRule)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/billingconductor-2021-07-30/CreatePricingRule)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/billingconductor-2021-07-30/CreatePricingRule)
