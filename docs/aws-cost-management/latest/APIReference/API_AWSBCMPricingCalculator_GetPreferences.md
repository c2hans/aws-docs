---
source_url: https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_AWSBCMPricingCalculator_GetPreferences.html
---

# GetPreferences
<a name="API_AWSBCMPricingCalculator_GetPreferences"></a>

 Retrieves the current preferences for AWS Pricing Calculator.

## Response Syntax
<a name="API_AWSBCMPricingCalculator_GetPreferences_ResponseSyntax"></a>

```
{
   "managementAccountRateTypeSelections": [ "string" ],
   "memberAccountRateTypeSelections": [ "string" ],
   "standaloneAccountRateTypeSelections": [ "string" ]
}
```

## Response Elements
<a name="API_AWSBCMPricingCalculator_GetPreferences_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [managementAccountRateTypeSelections](#API_AWSBCMPricingCalculator_GetPreferences_ResponseSyntax) **   <a name="awscostmanagement-AWSBCMPricingCalculator_GetPreferences-response-managementAccountRateTypeSelections"></a>
 The preferred rate types for the management account.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 3 items.
Valid Values: `BEFORE_DISCOUNTS | AFTER_DISCOUNTS | AFTER_DISCOUNTS_AND_COMMITMENTS`

 ** [memberAccountRateTypeSelections](#API_AWSBCMPricingCalculator_GetPreferences_ResponseSyntax) **   <a name="awscostmanagement-AWSBCMPricingCalculator_GetPreferences-response-memberAccountRateTypeSelections"></a>
 The preferred rate types for member accounts.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 3 items.
Valid Values: `BEFORE_DISCOUNTS | AFTER_DISCOUNTS | AFTER_DISCOUNTS_AND_COMMITMENTS`

 ** [standaloneAccountRateTypeSelections](#API_AWSBCMPricingCalculator_GetPreferences_ResponseSyntax) **   <a name="awscostmanagement-AWSBCMPricingCalculator_GetPreferences-response-standaloneAccountRateTypeSelections"></a>
 The preferred rate types for a standalone account.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 3 items.
Valid Values: `BEFORE_DISCOUNTS | AFTER_DISCOUNTS | AFTER_DISCOUNTS_AND_COMMITMENTS`

## Errors
<a name="API_AWSBCMPricingCalculator_GetPreferences_Errors"></a>

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
<a name="API_AWSBCMPricingCalculator_GetPreferences_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/bcm-pricing-calculator-2024-06-19/GetPreferences)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/bcm-pricing-calculator-2024-06-19/GetPreferences)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bcm-pricing-calculator-2024-06-19/GetPreferences)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/bcm-pricing-calculator-2024-06-19/GetPreferences)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bcm-pricing-calculator-2024-06-19/GetPreferences)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/bcm-pricing-calculator-2024-06-19/GetPreferences)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/bcm-pricing-calculator-2024-06-19/GetPreferences)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/bcm-pricing-calculator-2024-06-19/GetPreferences)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/bcm-pricing-calculator-2024-06-19/GetPreferences)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bcm-pricing-calculator-2024-06-19/GetPreferences)
