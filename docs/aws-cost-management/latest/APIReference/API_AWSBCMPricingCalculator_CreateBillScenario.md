---
source_url: https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_AWSBCMPricingCalculator_CreateBillScenario.html
---

# CreateBillScenario
<a name="API_AWSBCMPricingCalculator_CreateBillScenario"></a>

 Creates a new bill scenario to model potential changes to AWS usage and costs.

## Request Syntax
<a name="API_AWSBCMPricingCalculator_CreateBillScenario_RequestSyntax"></a>

```
{
   "clientToken": "{{string}}",
   "costCategoryGroupSharingPreferenceArn": "{{string}}",
   "groupSharingPreference": "{{string}}",
   "name": "{{string}}",
   "tags": {
      "{{string}}" : "{{string}}"
   }
}
```

## Request Parameters
<a name="API_AWSBCMPricingCalculator_CreateBillScenario_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [clientToken](#API_AWSBCMPricingCalculator_CreateBillScenario_RequestSyntax) **   <a name="awscostmanagement-AWSBCMPricingCalculator_CreateBillScenario-request-clientToken"></a>
 A unique, case-sensitive identifier to ensure idempotency of the request.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[\u0021-\u007E]+`
Required: No

 ** [costCategoryGroupSharingPreferenceArn](#API_AWSBCMPricingCalculator_CreateBillScenario_RequestSyntax) **   <a name="awscostmanagement-AWSBCMPricingCalculator_CreateBillScenario-request-costCategoryGroupSharingPreferenceArn"></a>
The arn of the cost category used in the reserved and prioritized group sharing.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:aws[-a-z0-9]*:ce::[0-9]{12}:costcategory/[a-f0-9-]{36}`
Required: No

 ** [groupSharingPreference](#API_AWSBCMPricingCalculator_CreateBillScenario_RequestSyntax) **   <a name="awscostmanagement-AWSBCMPricingCalculator_CreateBillScenario-request-groupSharingPreference"></a>
The setting for the reserved instance and savings plans group sharing used in this estimate.
Type: String
Valid Values: `OPEN | PRIORITIZED | RESTRICTED`
Required: No

 ** [name](#API_AWSBCMPricingCalculator_CreateBillScenario_RequestSyntax) **   <a name="awscostmanagement-AWSBCMPricingCalculator_CreateBillScenario-request-name"></a>
 A descriptive name for the bill scenario.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 64.
Pattern: `[a-zA-Z0-9-]+`
Required: Yes

 ** [tags](#API_AWSBCMPricingCalculator_CreateBillScenario_RequestSyntax) **   <a name="awscostmanagement-AWSBCMPricingCalculator_CreateBillScenario-request-tags"></a>
 The tags to apply to the bill scenario.
Type: String to string map
Map Entries: Minimum number of 0 items. Maximum number of 200 items.
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Key Pattern: `[\w\s:+=@/-]+`
Value Length Constraints: Minimum length of 0. Maximum length of 256.
Value Pattern: `[\w\s:+=@/-]*`
Required: No

## Response Syntax
<a name="API_AWSBCMPricingCalculator_CreateBillScenario_ResponseSyntax"></a>

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
<a name="API_AWSBCMPricingCalculator_CreateBillScenario_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [billInterval](#API_AWSBCMPricingCalculator_CreateBillScenario_ResponseSyntax) **   <a name="awscostmanagement-AWSBCMPricingCalculator_CreateBillScenario-response-billInterval"></a>
 The time period covered by the bill scenario.
Type: [BillInterval](API_AWSBCMPricingCalculator_BillInterval.md) object

 ** [costCategoryGroupSharingPreferenceArn](#API_AWSBCMPricingCalculator_CreateBillScenario_ResponseSyntax) **   <a name="awscostmanagement-AWSBCMPricingCalculator_CreateBillScenario-response-costCategoryGroupSharingPreferenceArn"></a>
The arn of the cost category used in the reserved and prioritized group sharing.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:aws[-a-z0-9]*:ce::[0-9]{12}:costcategory/[a-f0-9-]{36}`

 ** [createdAt](#API_AWSBCMPricingCalculator_CreateBillScenario_ResponseSyntax) **   <a name="awscostmanagement-AWSBCMPricingCalculator_CreateBillScenario-response-createdAt"></a>
 The timestamp when the bill scenario was created.
Type: Timestamp

 ** [expiresAt](#API_AWSBCMPricingCalculator_CreateBillScenario_ResponseSyntax) **   <a name="awscostmanagement-AWSBCMPricingCalculator_CreateBillScenario-response-expiresAt"></a>
 The timestamp when the bill scenario will expire.
Type: Timestamp

 ** [failureMessage](#API_AWSBCMPricingCalculator_CreateBillScenario_ResponseSyntax) **   <a name="awscostmanagement-AWSBCMPricingCalculator_CreateBillScenario-response-failureMessage"></a>
 An error message if the bill scenario creation failed.
Type: String

 ** [groupSharingPreference](#API_AWSBCMPricingCalculator_CreateBillScenario_ResponseSyntax) **   <a name="awscostmanagement-AWSBCMPricingCalculator_CreateBillScenario-response-groupSharingPreference"></a>
The setting for the reserved instance and savings plans group sharing used in this estimate.
Type: String
Valid Values: `OPEN | PRIORITIZED | RESTRICTED`

 ** [id](#API_AWSBCMPricingCalculator_CreateBillScenario_ResponseSyntax) **   <a name="awscostmanagement-AWSBCMPricingCalculator_CreateBillScenario-response-id"></a>
 The unique identifier for the created bill scenario.
Type: String
Length Constraints: Fixed length of 36.
Pattern: `[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}`

 ** [name](#API_AWSBCMPricingCalculator_CreateBillScenario_ResponseSyntax) **   <a name="awscostmanagement-AWSBCMPricingCalculator_CreateBillScenario-response-name"></a>
 The name of the created bill scenario.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 64.
Pattern: `[a-zA-Z0-9-]+`

 ** [status](#API_AWSBCMPricingCalculator_CreateBillScenario_ResponseSyntax) **   <a name="awscostmanagement-AWSBCMPricingCalculator_CreateBillScenario-response-status"></a>
 The current status of the bill scenario.
Type: String
Valid Values: `READY | LOCKED | FAILED | STALE`

## Errors
<a name="API_AWSBCMPricingCalculator_CreateBillScenario_Errors"></a>

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
<a name="API_AWSBCMPricingCalculator_CreateBillScenario_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/bcm-pricing-calculator-2024-06-19/CreateBillScenario)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/bcm-pricing-calculator-2024-06-19/CreateBillScenario)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bcm-pricing-calculator-2024-06-19/CreateBillScenario)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/bcm-pricing-calculator-2024-06-19/CreateBillScenario)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bcm-pricing-calculator-2024-06-19/CreateBillScenario)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/bcm-pricing-calculator-2024-06-19/CreateBillScenario)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/bcm-pricing-calculator-2024-06-19/CreateBillScenario)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/bcm-pricing-calculator-2024-06-19/CreateBillScenario)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/bcm-pricing-calculator-2024-06-19/CreateBillScenario)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bcm-pricing-calculator-2024-06-19/CreateBillScenario)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Billing and Cost Management. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query aws-cost-management` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
