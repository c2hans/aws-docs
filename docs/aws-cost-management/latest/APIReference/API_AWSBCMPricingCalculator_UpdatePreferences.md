---
source_url: https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_AWSBCMPricingCalculator_UpdatePreferences.html
---

# UpdatePreferences
<a name="API_AWSBCMPricingCalculator_UpdatePreferences"></a>

 Updates the preferences for AWS Pricing Calculator.

## Request Syntax
<a name="API_AWSBCMPricingCalculator_UpdatePreferences_RequestSyntax"></a>

```
{
   "managementAccountRateTypeSelections": [ "{{string}}" ],
   "memberAccountRateTypeSelections": [ "{{string}}" ],
   "standaloneAccountRateTypeSelections": [ "{{string}}" ]
}
```

## Request Parameters
<a name="API_AWSBCMPricingCalculator_UpdatePreferences_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [managementAccountRateTypeSelections](#API_AWSBCMPricingCalculator_UpdatePreferences_RequestSyntax) **   <a name="awscostmanagement-AWSBCMPricingCalculator_UpdatePreferences-request-managementAccountRateTypeSelections"></a>
 The updated preferred rate types for the management account.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 3 items.
Valid Values: `BEFORE_DISCOUNTS | AFTER_DISCOUNTS | AFTER_DISCOUNTS_AND_COMMITMENTS`
Required: No

 ** [memberAccountRateTypeSelections](#API_AWSBCMPricingCalculator_UpdatePreferences_RequestSyntax) **   <a name="awscostmanagement-AWSBCMPricingCalculator_UpdatePreferences-request-memberAccountRateTypeSelections"></a>
 The updated preferred rate types for member accounts.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 3 items.
Valid Values: `BEFORE_DISCOUNTS | AFTER_DISCOUNTS | AFTER_DISCOUNTS_AND_COMMITMENTS`
Required: No

 ** [standaloneAccountRateTypeSelections](#API_AWSBCMPricingCalculator_UpdatePreferences_RequestSyntax) **   <a name="awscostmanagement-AWSBCMPricingCalculator_UpdatePreferences-request-standaloneAccountRateTypeSelections"></a>
 The updated preferred rate types for a standalone account.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 3 items.
Valid Values: `BEFORE_DISCOUNTS | AFTER_DISCOUNTS | AFTER_DISCOUNTS_AND_COMMITMENTS`
Required: No

## Response Syntax
<a name="API_AWSBCMPricingCalculator_UpdatePreferences_ResponseSyntax"></a>

```
{
   "managementAccountRateTypeSelections": [ "string" ],
   "memberAccountRateTypeSelections": [ "string" ],
   "standaloneAccountRateTypeSelections": [ "string" ]
}
```

## Response Elements
<a name="API_AWSBCMPricingCalculator_UpdatePreferences_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [managementAccountRateTypeSelections](#API_AWSBCMPricingCalculator_UpdatePreferences_ResponseSyntax) **   <a name="awscostmanagement-AWSBCMPricingCalculator_UpdatePreferences-response-managementAccountRateTypeSelections"></a>
 The updated preferred rate types for the management account.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 3 items.
Valid Values: `BEFORE_DISCOUNTS | AFTER_DISCOUNTS | AFTER_DISCOUNTS_AND_COMMITMENTS`

 ** [memberAccountRateTypeSelections](#API_AWSBCMPricingCalculator_UpdatePreferences_ResponseSyntax) **   <a name="awscostmanagement-AWSBCMPricingCalculator_UpdatePreferences-response-memberAccountRateTypeSelections"></a>
 The updated preferred rate types for member accounts.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 3 items.
Valid Values: `BEFORE_DISCOUNTS | AFTER_DISCOUNTS | AFTER_DISCOUNTS_AND_COMMITMENTS`

 ** [standaloneAccountRateTypeSelections](#API_AWSBCMPricingCalculator_UpdatePreferences_ResponseSyntax) **   <a name="awscostmanagement-AWSBCMPricingCalculator_UpdatePreferences-response-standaloneAccountRateTypeSelections"></a>
 The updated preferred rate types for a standalone account.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 3 items.
Valid Values: `BEFORE_DISCOUNTS | AFTER_DISCOUNTS | AFTER_DISCOUNTS_AND_COMMITMENTS`

## Errors
<a name="API_AWSBCMPricingCalculator_UpdatePreferences_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
 You do not have sufficient access to perform this action.
HTTP Status Code: 400

 ** DataUnavailableException **
 The requested data is currently unavailable.
HTTP Status Code: 400

 ** InternalServerException **
 An internal error has occurred. Retry your request, but if the problem persists, contact AWS support.
 ** retryAfterSeconds **
 An internal error has occurred. Retry your request, but if the problem persists, contact AWS support.
HTTP Status Code: 500

 ** ServiceQuotaExceededException **
 The request would cause you to exceed your service quota.
 ** quotaCode **
 The quota code that was exceeded.
 ** resourceId **
 The identifier of the resource that exceeded quota.
 ** resourceType **
 The type of the resource that exceeded quota.
 ** serviceCode **
 The service code that exceeded quota.
HTTP Status Code: 400

 ** ThrottlingException **
 The request was denied due to request throttling.
 ** quotaCode **
The quota code that exceeded the throttling limit.
 ** retryAfterSeconds **
The service code that exceeded the throttling limit. Retry your request, but if the problem persists, contact AWS support.
 ** serviceCode **
The service code that exceeded the throttling limit.
HTTP Status Code: 400

 ** ValidationException **
 The input provided fails to satisfy the constraints specified by an AWS service.
 ** fieldList **
 The list of fields that are invalid.
 ** reason **
 The reason for the validation exception.
HTTP Status Code: 400

## See Also
<a name="API_AWSBCMPricingCalculator_UpdatePreferences_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/bcm-pricing-calculator-2024-06-19/UpdatePreferences)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/bcm-pricing-calculator-2024-06-19/UpdatePreferences)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bcm-pricing-calculator-2024-06-19/UpdatePreferences)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/bcm-pricing-calculator-2024-06-19/UpdatePreferences)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bcm-pricing-calculator-2024-06-19/UpdatePreferences)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/bcm-pricing-calculator-2024-06-19/UpdatePreferences)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/bcm-pricing-calculator-2024-06-19/UpdatePreferences)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/bcm-pricing-calculator-2024-06-19/UpdatePreferences)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/bcm-pricing-calculator-2024-06-19/UpdatePreferences)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bcm-pricing-calculator-2024-06-19/UpdatePreferences)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Billing and Cost Management. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query aws-cost-management` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
