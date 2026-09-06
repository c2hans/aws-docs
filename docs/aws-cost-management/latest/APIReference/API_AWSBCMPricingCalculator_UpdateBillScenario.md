---
source_url: https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_AWSBCMPricingCalculator_UpdateBillScenario.html
---

# UpdateBillScenario
<a name="API_AWSBCMPricingCalculator_UpdateBillScenario"></a>

 Updates an existing bill scenario.

## Request Syntax
<a name="API_AWSBCMPricingCalculator_UpdateBillScenario_RequestSyntax"></a>

```
{
   "costCategoryGroupSharingPreferenceArn": "{{string}}",
   "expiresAt": {{number}},
   "groupSharingPreference": "{{string}}",
   "identifier": "{{string}}",
   "name": "{{string}}"
}
```

## Request Parameters
<a name="API_AWSBCMPricingCalculator_UpdateBillScenario_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [costCategoryGroupSharingPreferenceArn](#API_AWSBCMPricingCalculator_UpdateBillScenario_RequestSyntax) **   <a name="awscostmanagement-AWSBCMPricingCalculator_UpdateBillScenario-request-costCategoryGroupSharingPreferenceArn"></a>
The arn of the cost category used in the reserved and prioritized group sharing.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:aws[-a-z0-9]*:ce::[0-9]{12}:costcategory/[a-f0-9-]{36}`
Required: No

 ** [expiresAt](#API_AWSBCMPricingCalculator_UpdateBillScenario_RequestSyntax) **   <a name="awscostmanagement-AWSBCMPricingCalculator_UpdateBillScenario-request-expiresAt"></a>
 The new expiration date for the bill scenario.
Type: Timestamp
Required: No

 ** [groupSharingPreference](#API_AWSBCMPricingCalculator_UpdateBillScenario_RequestSyntax) **   <a name="awscostmanagement-AWSBCMPricingCalculator_UpdateBillScenario-request-groupSharingPreference"></a>
The setting for the reserved instance and savings plans group sharing used in this estimate.
Type: String
Valid Values: `OPEN | PRIORITIZED | RESTRICTED`
Required: No

 ** [identifier](#API_AWSBCMPricingCalculator_UpdateBillScenario_RequestSyntax) **   <a name="awscostmanagement-AWSBCMPricingCalculator_UpdateBillScenario-request-identifier"></a>
 The unique identifier of the bill scenario to update.
Type: String
Length Constraints: Fixed length of 36.
Pattern: `[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}`
Required: Yes

 ** [name](#API_AWSBCMPricingCalculator_UpdateBillScenario_RequestSyntax) **   <a name="awscostmanagement-AWSBCMPricingCalculator_UpdateBillScenario-request-name"></a>
 The new name for the bill scenario.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 64.
Pattern: `[a-zA-Z0-9-]+`
Required: No

## Response Syntax
<a name="API_AWSBCMPricingCalculator_UpdateBillScenario_ResponseSyntax"></a>

```
{
   "billInterval": {
      "end": number,
      "start": number
   },
   "costCategoryGroupSharingPreferenceArn": "string",
   "createdAt": number,
   "expiresAt": number,
   "failureMessage": "string",
   "groupSharingPreference": "string",
   "id": "string",
   "name": "string",
   "status": "string"
}
```

## Response Elements
<a name="API_AWSBCMPricingCalculator_UpdateBillScenario_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [billInterval](#API_AWSBCMPricingCalculator_UpdateBillScenario_ResponseSyntax) **   <a name="awscostmanagement-AWSBCMPricingCalculator_UpdateBillScenario-response-billInterval"></a>
 The time period covered by the updated bill scenario.
Type: [BillInterval](API_AWSBCMPricingCalculator_BillInterval.md) object

 ** [costCategoryGroupSharingPreferenceArn](#API_AWSBCMPricingCalculator_UpdateBillScenario_ResponseSyntax) **   <a name="awscostmanagement-AWSBCMPricingCalculator_UpdateBillScenario-response-costCategoryGroupSharingPreferenceArn"></a>
The arn of the cost category used in the reserved and prioritized group sharing.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:aws[-a-z0-9]*:ce::[0-9]{12}:costcategory/[a-f0-9-]{36}`

 ** [createdAt](#API_AWSBCMPricingCalculator_UpdateBillScenario_ResponseSyntax) **   <a name="awscostmanagement-AWSBCMPricingCalculator_UpdateBillScenario-response-createdAt"></a>
 The timestamp when the bill scenario was originally created.
Type: Timestamp

 ** [expiresAt](#API_AWSBCMPricingCalculator_UpdateBillScenario_ResponseSyntax) **   <a name="awscostmanagement-AWSBCMPricingCalculator_UpdateBillScenario-response-expiresAt"></a>
 The updated expiration timestamp for the bill scenario.
Type: Timestamp

 ** [failureMessage](#API_AWSBCMPricingCalculator_UpdateBillScenario_ResponseSyntax) **   <a name="awscostmanagement-AWSBCMPricingCalculator_UpdateBillScenario-response-failureMessage"></a>
 An error message if the bill scenario update failed.
Type: String

 ** [groupSharingPreference](#API_AWSBCMPricingCalculator_UpdateBillScenario_ResponseSyntax) **   <a name="awscostmanagement-AWSBCMPricingCalculator_UpdateBillScenario-response-groupSharingPreference"></a>
The setting for the reserved instance and savings plans group sharing used in this estimate.
Type: String
Valid Values: `OPEN | PRIORITIZED | RESTRICTED`

 ** [id](#API_AWSBCMPricingCalculator_UpdateBillScenario_ResponseSyntax) **   <a name="awscostmanagement-AWSBCMPricingCalculator_UpdateBillScenario-response-id"></a>
 The unique identifier of the updated bill scenario.
Type: String
Length Constraints: Fixed length of 36.
Pattern: `[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}`

 ** [name](#API_AWSBCMPricingCalculator_UpdateBillScenario_ResponseSyntax) **   <a name="awscostmanagement-AWSBCMPricingCalculator_UpdateBillScenario-response-name"></a>
 The updated name of the bill scenario.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 64.
Pattern: `[a-zA-Z0-9-]+`

 ** [status](#API_AWSBCMPricingCalculator_UpdateBillScenario_ResponseSyntax) **   <a name="awscostmanagement-AWSBCMPricingCalculator_UpdateBillScenario-response-status"></a>
 The current status of the updated bill scenario.
Type: String
Valid Values: `READY | LOCKED | FAILED | STALE`

## Errors
<a name="API_AWSBCMPricingCalculator_UpdateBillScenario_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
 You do not have sufficient access to perform this action.
HTTP Status Code: 400

 ** ConflictException **
 The request could not be processed because of conflict in the current state of the resource.
 ** resourceId **
 The identifier of the resource that was not found.
 ** resourceType **
 The type of the resource that was not found.
HTTP Status Code: 400

 ** DataUnavailableException **
 The requested data is currently unavailable.
HTTP Status Code: 400

 ** InternalServerException **
 An internal error has occurred. Retry your request, but if the problem persists, contact AWS support.
 ** retryAfterSeconds **
 An internal error has occurred. Retry your request, but if the problem persists, contact AWS support.
HTTP Status Code: 500

 ** ResourceNotFoundException **
 The specified resource was not found.
 ** resourceId **
 The identifier of the resource that was not found.
 ** resourceType **
 The type of the resource that was not found.
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
<a name="API_AWSBCMPricingCalculator_UpdateBillScenario_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/bcm-pricing-calculator-2024-06-19/UpdateBillScenario)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/bcm-pricing-calculator-2024-06-19/UpdateBillScenario)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bcm-pricing-calculator-2024-06-19/UpdateBillScenario)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/bcm-pricing-calculator-2024-06-19/UpdateBillScenario)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bcm-pricing-calculator-2024-06-19/UpdateBillScenario)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/bcm-pricing-calculator-2024-06-19/UpdateBillScenario)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/bcm-pricing-calculator-2024-06-19/UpdateBillScenario)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/bcm-pricing-calculator-2024-06-19/UpdateBillScenario)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/bcm-pricing-calculator-2024-06-19/UpdateBillScenario)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bcm-pricing-calculator-2024-06-19/UpdateBillScenario)
