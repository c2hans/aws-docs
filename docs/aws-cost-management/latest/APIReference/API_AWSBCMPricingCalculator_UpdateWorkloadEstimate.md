---
source_url: https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_AWSBCMPricingCalculator_UpdateWorkloadEstimate.html
---

# UpdateWorkloadEstimate
<a name="API_AWSBCMPricingCalculator_UpdateWorkloadEstimate"></a>

 Updates an existing workload estimate.

## Request Syntax
<a name="API_AWSBCMPricingCalculator_UpdateWorkloadEstimate_RequestSyntax"></a>

```
{
   "expiresAt": {{number}},
   "identifier": "{{string}}",
   "name": "{{string}}"
}
```

## Request Parameters
<a name="API_AWSBCMPricingCalculator_UpdateWorkloadEstimate_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [expiresAt](#API_AWSBCMPricingCalculator_UpdateWorkloadEstimate_RequestSyntax) **   <a name="awscostmanagement-AWSBCMPricingCalculator_UpdateWorkloadEstimate-request-expiresAt"></a>
 The new expiration date for the workload estimate.
Type: Timestamp
Required: No

 ** [identifier](#API_AWSBCMPricingCalculator_UpdateWorkloadEstimate_RequestSyntax) **   <a name="awscostmanagement-AWSBCMPricingCalculator_UpdateWorkloadEstimate-request-identifier"></a>
 The unique identifier of the workload estimate to update.
Type: String
Length Constraints: Fixed length of 36.
Pattern: `[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}`
Required: Yes

 ** [name](#API_AWSBCMPricingCalculator_UpdateWorkloadEstimate_RequestSyntax) **   <a name="awscostmanagement-AWSBCMPricingCalculator_UpdateWorkloadEstimate-request-name"></a>
 The new name for the workload estimate.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 64.
Pattern: `[a-zA-Z0-9-]+`
Required: No

## Response Syntax
<a name="API_AWSBCMPricingCalculator_UpdateWorkloadEstimate_ResponseSyntax"></a>

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
<a name="API_AWSBCMPricingCalculator_UpdateWorkloadEstimate_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [costCurrency](#API_AWSBCMPricingCalculator_UpdateWorkloadEstimate_ResponseSyntax) **   <a name="awscostmanagement-AWSBCMPricingCalculator_UpdateWorkloadEstimate-response-costCurrency"></a>
 The currency of the updated estimated cost.
Type: String
Valid Values: `USD`

 ** [createdAt](#API_AWSBCMPricingCalculator_UpdateWorkloadEstimate_ResponseSyntax) **   <a name="awscostmanagement-AWSBCMPricingCalculator_UpdateWorkloadEstimate-response-createdAt"></a>
 The timestamp when the workload estimate was originally created.
Type: Timestamp

 ** [expiresAt](#API_AWSBCMPricingCalculator_UpdateWorkloadEstimate_ResponseSyntax) **   <a name="awscostmanagement-AWSBCMPricingCalculator_UpdateWorkloadEstimate-response-expiresAt"></a>
 The updated expiration timestamp for the workload estimate.
Type: Timestamp

 ** [failureMessage](#API_AWSBCMPricingCalculator_UpdateWorkloadEstimate_ResponseSyntax) **   <a name="awscostmanagement-AWSBCMPricingCalculator_UpdateWorkloadEstimate-response-failureMessage"></a>
 An error message if the workload estimate update failed.
Type: String

 ** [id](#API_AWSBCMPricingCalculator_UpdateWorkloadEstimate_ResponseSyntax) **   <a name="awscostmanagement-AWSBCMPricingCalculator_UpdateWorkloadEstimate-response-id"></a>
 The unique identifier of the updated workload estimate.
Type: String
Length Constraints: Fixed length of 36.
Pattern: `[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}`

 ** [name](#API_AWSBCMPricingCalculator_UpdateWorkloadEstimate_ResponseSyntax) **   <a name="awscostmanagement-AWSBCMPricingCalculator_UpdateWorkloadEstimate-response-name"></a>
 The updated name of the workload estimate.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 64.
Pattern: `[a-zA-Z0-9-]+`

 ** [rateTimestamp](#API_AWSBCMPricingCalculator_UpdateWorkloadEstimate_ResponseSyntax) **   <a name="awscostmanagement-AWSBCMPricingCalculator_UpdateWorkloadEstimate-response-rateTimestamp"></a>
 The timestamp of the pricing rates used for the updated estimate.
Type: Timestamp

 ** [rateType](#API_AWSBCMPricingCalculator_UpdateWorkloadEstimate_ResponseSyntax) **   <a name="awscostmanagement-AWSBCMPricingCalculator_UpdateWorkloadEstimate-response-rateType"></a>
 The type of pricing rates used for the updated estimate.
Type: String
Valid Values: `BEFORE_DISCOUNTS | AFTER_DISCOUNTS | AFTER_DISCOUNTS_AND_COMMITMENTS`

 ** [status](#API_AWSBCMPricingCalculator_UpdateWorkloadEstimate_ResponseSyntax) **   <a name="awscostmanagement-AWSBCMPricingCalculator_UpdateWorkloadEstimate-response-status"></a>
 The current status of the updated workload estimate.
Type: String
Valid Values: `UPDATING | VALID | INVALID | ACTION_NEEDED`

 ** [totalCost](#API_AWSBCMPricingCalculator_UpdateWorkloadEstimate_ResponseSyntax) **   <a name="awscostmanagement-AWSBCMPricingCalculator_UpdateWorkloadEstimate-response-totalCost"></a>
 The updated total estimated cost for the workload.
Type: Double

## Errors
<a name="API_AWSBCMPricingCalculator_UpdateWorkloadEstimate_Errors"></a>

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
<a name="API_AWSBCMPricingCalculator_UpdateWorkloadEstimate_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/bcm-pricing-calculator-2024-06-19/UpdateWorkloadEstimate)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/bcm-pricing-calculator-2024-06-19/UpdateWorkloadEstimate)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bcm-pricing-calculator-2024-06-19/UpdateWorkloadEstimate)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/bcm-pricing-calculator-2024-06-19/UpdateWorkloadEstimate)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bcm-pricing-calculator-2024-06-19/UpdateWorkloadEstimate)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/bcm-pricing-calculator-2024-06-19/UpdateWorkloadEstimate)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/bcm-pricing-calculator-2024-06-19/UpdateWorkloadEstimate)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/bcm-pricing-calculator-2024-06-19/UpdateWorkloadEstimate)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/bcm-pricing-calculator-2024-06-19/UpdateWorkloadEstimate)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bcm-pricing-calculator-2024-06-19/UpdateWorkloadEstimate)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Billing and Cost Management. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query aws-cost-management` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
