---
source_url: https://docs.aws.amazon.com/billingconductor/latest/APIReference/API_UpdatePricingRule.html
---

# UpdatePricingRule
<a name="API_UpdatePricingRule"></a>

 Updates an existing pricing rule.

## Request Syntax
<a name="API_UpdatePricingRule_RequestSyntax"></a>

```
PUT /update-pricing-rule HTTP/1.1
Content-type: application/json

{
   "Arn": "{{string}}",
   "Description": "{{string}}",
   "ModifierPercentage": {{number}},
   "Name": "{{string}}",
   "Tiering": {
      "FreeTier": {
         "Activated": {{boolean}}
      }
   },
   "Type": "{{string}}"
}
```

## URI Request Parameters
<a name="API_UpdatePricingRule_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_UpdatePricingRule_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [Arn](#API_UpdatePricingRule_RequestSyntax) **   <a name="billingconductor-UpdatePricingRule-request-Arn"></a>
 The Amazon Resource Name (ARN) of the pricing rule to update.
Type: String
Pattern: `(arn:aws(-cn)?:billingconductor::[0-9]{12}:pricingrule/)?[a-zA-Z0-9]{10}`
Required: Yes

 ** [Description](#API_UpdatePricingRule_RequestSyntax) **   <a name="billingconductor-UpdatePricingRule-request-Description"></a>
 The new description for the pricing rule.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Required: No

 ** [ModifierPercentage](#API_UpdatePricingRule_RequestSyntax) **   <a name="billingconductor-UpdatePricingRule-request-ModifierPercentage"></a>
 The new modifier to show pricing plan rates as a percentage. Your entry will be rounded to the nearest 2 decimal places.
Type: Double
Valid Range: Minimum value of 0.
Required: No

 ** [Name](#API_UpdatePricingRule_RequestSyntax) **   <a name="billingconductor-UpdatePricingRule-request-Name"></a>
 The new name of the pricing rule. The name must be unique to each pricing rule.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[a-zA-Z0-9_\+=\.\-@]+`
Required: No

 ** [Tiering](#API_UpdatePricingRule_RequestSyntax) **   <a name="billingconductor-UpdatePricingRule-request-Tiering"></a>
 The set of tiering configurations for the pricing rule.
Type: [UpdateTieringInput](API_UpdateTieringInput.md) object
Required: No

 ** [Type](#API_UpdatePricingRule_RequestSyntax) **   <a name="billingconductor-UpdatePricingRule-request-Type"></a>
 The new pricing rule type.
Type: String
Valid Values: `MARKUP | DISCOUNT | TIERING`
Required: No

## Response Syntax
<a name="API_UpdatePricingRule_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "Arn": "string",
   "AssociatedPricingPlanCount": number,
   "BillingEntity": "string",
   "Description": "string",
   "LastModifiedTime": number,
   "ModifierPercentage": number,
   "Name": "string",
   "Operation": "string",
   "Scope": "string",
   "Service": "string",
   "Tiering": {
      "FreeTier": {
         "Activated": boolean
      }
   },
   "Type": "string",
   "UsageType": "string"
}
```

## Response Elements
<a name="API_UpdatePricingRule_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Arn](#API_UpdatePricingRule_ResponseSyntax) **   <a name="billingconductor-UpdatePricingRule-response-Arn"></a>
 The Amazon Resource Name (ARN) of the successfully updated pricing rule.
Type: String
Pattern: `(arn:aws(-cn)?:billingconductor::[0-9]{12}:pricingrule/)?[a-zA-Z0-9]{10}`

 ** [AssociatedPricingPlanCount](#API_UpdatePricingRule_ResponseSyntax) **   <a name="billingconductor-UpdatePricingRule-response-AssociatedPricingPlanCount"></a>
 The pricing plans count that this pricing rule is associated with.
Type: Long
Valid Range: Minimum value of 0.

 ** [BillingEntity](#API_UpdatePricingRule_ResponseSyntax) **   <a name="billingconductor-UpdatePricingRule-response-BillingEntity"></a>
 The seller of services provided by AWS, their affiliates, or third-party providers selling services via AWS Marketplace.
Type: String
Pattern: `[a-zA-Z0-9() ]+`

 ** [Description](#API_UpdatePricingRule_ResponseSyntax) **   <a name="billingconductor-UpdatePricingRule-response-Description"></a>
 The new description for the pricing rule.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.

 ** [LastModifiedTime](#API_UpdatePricingRule_ResponseSyntax) **   <a name="billingconductor-UpdatePricingRule-response-LastModifiedTime"></a>
 The most recent time the pricing rule was modified.
Type: Long

 ** [ModifierPercentage](#API_UpdatePricingRule_ResponseSyntax) **   <a name="billingconductor-UpdatePricingRule-response-ModifierPercentage"></a>
 The new modifier to show pricing plan rates as a percentage.
Type: Double
Valid Range: Minimum value of 0.

 ** [Name](#API_UpdatePricingRule_ResponseSyntax) **   <a name="billingconductor-UpdatePricingRule-response-Name"></a>
 The new name of the pricing rule. The name must be unique to each pricing rule.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[a-zA-Z0-9_\+=\.\-@]+`

 ** [Operation](#API_UpdatePricingRule_ResponseSyntax) **   <a name="billingconductor-UpdatePricingRule-response-Operation"></a>
Operation refers to the specific AWS covered by this line item. This describes the specific usage of the line item.
 If the `Scope` attribute is set to `SKU`, this attribute indicates which operation the `PricingRule` is modifying. For example, a value of `RunInstances:0202` indicates the operation of running an Amazon EC2 instance.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `\S+`

 ** [Scope](#API_UpdatePricingRule_ResponseSyntax) **   <a name="billingconductor-UpdatePricingRule-response-Scope"></a>
 The scope of pricing rule that indicates if it's globally applicable, or it's service-specific.
Type: String
Valid Values: `GLOBAL | SERVICE | BILLING_ENTITY | SKU`

 ** [Service](#API_UpdatePricingRule_ResponseSyntax) **   <a name="billingconductor-UpdatePricingRule-response-Service"></a>
 If the `Scope` attribute is set to `SERVICE`, the attribute indicates which service the `PricingRule` is applicable for.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[a-zA-Z0-9]+`

 ** [Tiering](#API_UpdatePricingRule_ResponseSyntax) **   <a name="billingconductor-UpdatePricingRule-response-Tiering"></a>
 The set of tiering configurations for the pricing rule.
Type: [UpdateTieringInput](API_UpdateTieringInput.md) object

 ** [Type](#API_UpdatePricingRule_ResponseSyntax) **   <a name="billingconductor-UpdatePricingRule-response-Type"></a>
 The new pricing rule type.
Type: String
Valid Values: `MARKUP | DISCOUNT | TIERING`

 ** [UsageType](#API_UpdatePricingRule_ResponseSyntax) **   <a name="billingconductor-UpdatePricingRule-response-UsageType"></a>
Usage type is the unit that each service uses to measure the usage of a specific type of resource.
If the `Scope` attribute is set to `SKU`, this attribute indicates which usage type the `PricingRule` is modifying. For example, `USW2-BoxUsage:m2.2xlarge` describes an `M2 High Memory Double Extra Large` instance in the US West (Oregon) Region.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `\S+`

## Errors
<a name="API_UpdatePricingRule_Errors"></a>

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
<a name="API_UpdatePricingRule_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/billingconductor-2021-07-30/UpdatePricingRule)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/billingconductor-2021-07-30/UpdatePricingRule)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/billingconductor-2021-07-30/UpdatePricingRule)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/billingconductor-2021-07-30/UpdatePricingRule)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/billingconductor-2021-07-30/UpdatePricingRule)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/billingconductor-2021-07-30/UpdatePricingRule)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/billingconductor-2021-07-30/UpdatePricingRule)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/billingconductor-2021-07-30/UpdatePricingRule)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/billingconductor-2021-07-30/UpdatePricingRule)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/billingconductor-2021-07-30/UpdatePricingRule)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Billing Conductor. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query billingconductor` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
