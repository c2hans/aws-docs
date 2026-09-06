---
source_url: https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_AWSBCMPricingCalculator_CreateWorkloadEstimate.html
---

# CreateWorkloadEstimate
<a name="API_AWSBCMPricingCalculator_CreateWorkloadEstimate"></a>

 Creates a new workload estimate to model costs for a specific workload.

## Request Syntax
<a name="API_AWSBCMPricingCalculator_CreateWorkloadEstimate_RequestSyntax"></a>

```
{
   "clientToken": "{{string}}",
   "name": "{{string}}",
   "rateType": "{{string}}",
   "tags": {
      "{{string}}" : "{{string}}"
   }
}
```

## Request Parameters
<a name="API_AWSBCMPricingCalculator_CreateWorkloadEstimate_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [clientToken](#API_AWSBCMPricingCalculator_CreateWorkloadEstimate_RequestSyntax) **   <a name="awscostmanagement-AWSBCMPricingCalculator_CreateWorkloadEstimate-request-clientToken"></a>
 A unique, case-sensitive identifier to ensure idempotency of the request.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[\u0021-\u007E]+`
Required: No

 ** [name](#API_AWSBCMPricingCalculator_CreateWorkloadEstimate_RequestSyntax) **   <a name="awscostmanagement-AWSBCMPricingCalculator_CreateWorkloadEstimate-request-name"></a>
 A descriptive name for the workload estimate.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 64.
Pattern: `[a-zA-Z0-9-]+`
Required: Yes

 ** [rateType](#API_AWSBCMPricingCalculator_CreateWorkloadEstimate_RequestSyntax) **   <a name="awscostmanagement-AWSBCMPricingCalculator_CreateWorkloadEstimate-request-rateType"></a>
 The type of pricing rates to use for the estimate.
Type: String
Valid Values: `BEFORE_DISCOUNTS | AFTER_DISCOUNTS | AFTER_DISCOUNTS_AND_COMMITMENTS`
Required: No

 ** [tags](#API_AWSBCMPricingCalculator_CreateWorkloadEstimate_RequestSyntax) **   <a name="awscostmanagement-AWSBCMPricingCalculator_CreateWorkloadEstimate-request-tags"></a>
 The tags to apply to the workload estimate.
Type: String to string map
Map Entries: Minimum number of 0 items. Maximum number of 200 items.
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Key Pattern: `[\w\s:+=@/-]+`
Value Length Constraints: Minimum length of 0. Maximum length of 256.
Value Pattern: `[\w\s:+=@/-]*`
Required: No

## Response Syntax
<a name="API_AWSBCMPricingCalculator_CreateWorkloadEstimate_ResponseSyntax"></a>

```
{
   "costCurrency": "string",
   "createdAt": number,
   "expiresAt": number,
   "failureMessage": "string",
   "id": "string",
   "name": "string",
   "rateTimestamp": number,
   "rateType": "string",
   "status": "string",
   "totalCost": number
}
```

## Response Elements
<a name="API_AWSBCMPricingCalculator_CreateWorkloadEstimate_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [costCurrency](#API_AWSBCMPricingCalculator_CreateWorkloadEstimate_ResponseSyntax) **   <a name="awscostmanagement-AWSBCMPricingCalculator_CreateWorkloadEstimate-response-costCurrency"></a>
 The currency of the estimated cost.
Type: String
Valid Values: `USD`

 ** [createdAt](#API_AWSBCMPricingCalculator_CreateWorkloadEstimate_ResponseSyntax) **   <a name="awscostmanagement-AWSBCMPricingCalculator_CreateWorkloadEstimate-response-createdAt"></a>
 The timestamp when the workload estimate was created.
Type: Timestamp

 ** [expiresAt](#API_AWSBCMPricingCalculator_CreateWorkloadEstimate_ResponseSyntax) **   <a name="awscostmanagement-AWSBCMPricingCalculator_CreateWorkloadEstimate-response-expiresAt"></a>
 The timestamp when the workload estimate will expire.
Type: Timestamp

 ** [failureMessage](#API_AWSBCMPricingCalculator_CreateWorkloadEstimate_ResponseSyntax) **   <a name="awscostmanagement-AWSBCMPricingCalculator_CreateWorkloadEstimate-response-failureMessage"></a>
 An error message if the workload estimate creation failed.
Type: String

 ** [id](#API_AWSBCMPricingCalculator_CreateWorkloadEstimate_ResponseSyntax) **   <a name="awscostmanagement-AWSBCMPricingCalculator_CreateWorkloadEstimate-response-id"></a>
 The unique identifier for the created workload estimate.
Type: String
Length Constraints: Fixed length of 36.
Pattern: `[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}`

 ** [name](#API_AWSBCMPricingCalculator_CreateWorkloadEstimate_ResponseSyntax) **   <a name="awscostmanagement-AWSBCMPricingCalculator_CreateWorkloadEstimate-response-name"></a>
 The name of the created workload estimate.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 64.
Pattern: `[a-zA-Z0-9-]+`

 ** [rateTimestamp](#API_AWSBCMPricingCalculator_CreateWorkloadEstimate_ResponseSyntax) **   <a name="awscostmanagement-AWSBCMPricingCalculator_CreateWorkloadEstimate-response-rateTimestamp"></a>
 The timestamp of the pricing rates used for the estimate.
Type: Timestamp

 ** [rateType](#API_AWSBCMPricingCalculator_CreateWorkloadEstimate_ResponseSyntax) **   <a name="awscostmanagement-AWSBCMPricingCalculator_CreateWorkloadEstimate-response-rateType"></a>
 The type of pricing rates used for the estimate.
Type: String
Valid Values: `BEFORE_DISCOUNTS | AFTER_DISCOUNTS | AFTER_DISCOUNTS_AND_COMMITMENTS`

 ** [status](#API_AWSBCMPricingCalculator_CreateWorkloadEstimate_ResponseSyntax) **   <a name="awscostmanagement-AWSBCMPricingCalculator_CreateWorkloadEstimate-response-status"></a>
 The current status of the workload estimate.
Type: String
Valid Values: `UPDATING | VALID | INVALID | ACTION_NEEDED`

 ** [totalCost](#API_AWSBCMPricingCalculator_CreateWorkloadEstimate_ResponseSyntax) **   <a name="awscostmanagement-AWSBCMPricingCalculator_CreateWorkloadEstimate-response-totalCost"></a>
 The total estimated cost for the workload.
Type: Double

## Errors
<a name="API_AWSBCMPricingCalculator_CreateWorkloadEstimate_Errors"></a>

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
<a name="API_AWSBCMPricingCalculator_CreateWorkloadEstimate_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/bcm-pricing-calculator-2024-06-19/CreateWorkloadEstimate)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/bcm-pricing-calculator-2024-06-19/CreateWorkloadEstimate)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bcm-pricing-calculator-2024-06-19/CreateWorkloadEstimate)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/bcm-pricing-calculator-2024-06-19/CreateWorkloadEstimate)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bcm-pricing-calculator-2024-06-19/CreateWorkloadEstimate)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/bcm-pricing-calculator-2024-06-19/CreateWorkloadEstimate)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/bcm-pricing-calculator-2024-06-19/CreateWorkloadEstimate)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/bcm-pricing-calculator-2024-06-19/CreateWorkloadEstimate)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/bcm-pricing-calculator-2024-06-19/CreateWorkloadEstimate)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bcm-pricing-calculator-2024-06-19/CreateWorkloadEstimate)
