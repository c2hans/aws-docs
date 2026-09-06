---
source_url: https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_AWSBCMPricingCalculator_GetWorkloadEstimate.html
---

# GetWorkloadEstimate
<a name="API_AWSBCMPricingCalculator_GetWorkloadEstimate"></a>

 Retrieves details of a specific workload estimate.

## Request Syntax
<a name="API_AWSBCMPricingCalculator_GetWorkloadEstimate_RequestSyntax"></a>

```
{
   "identifier": "{{string}}"
}
```

## Request Parameters
<a name="API_AWSBCMPricingCalculator_GetWorkloadEstimate_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [identifier](#API_AWSBCMPricingCalculator_GetWorkloadEstimate_RequestSyntax) **   <a name="awscostmanagement-AWSBCMPricingCalculator_GetWorkloadEstimate-request-identifier"></a>
 The unique identifier of the workload estimate to retrieve.
Type: String
Length Constraints: Fixed length of 36.
Pattern: `[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}`
Required: Yes

## Response Syntax
<a name="API_AWSBCMPricingCalculator_GetWorkloadEstimate_ResponseSyntax"></a>

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
<a name="API_AWSBCMPricingCalculator_GetWorkloadEstimate_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [costCurrency](#API_AWSBCMPricingCalculator_GetWorkloadEstimate_ResponseSyntax) **   <a name="awscostmanagement-AWSBCMPricingCalculator_GetWorkloadEstimate-response-costCurrency"></a>
 The currency of the estimated cost.
Type: String
Valid Values: `USD`

 ** [createdAt](#API_AWSBCMPricingCalculator_GetWorkloadEstimate_ResponseSyntax) **   <a name="awscostmanagement-AWSBCMPricingCalculator_GetWorkloadEstimate-response-createdAt"></a>
 The timestamp when the workload estimate was created.
Type: Timestamp

 ** [expiresAt](#API_AWSBCMPricingCalculator_GetWorkloadEstimate_ResponseSyntax) **   <a name="awscostmanagement-AWSBCMPricingCalculator_GetWorkloadEstimate-response-expiresAt"></a>
 The timestamp when the workload estimate will expire.
Type: Timestamp

 ** [failureMessage](#API_AWSBCMPricingCalculator_GetWorkloadEstimate_ResponseSyntax) **   <a name="awscostmanagement-AWSBCMPricingCalculator_GetWorkloadEstimate-response-failureMessage"></a>
 An error message if the workload estimate retrieval failed.
Type: String

 ** [id](#API_AWSBCMPricingCalculator_GetWorkloadEstimate_ResponseSyntax) **   <a name="awscostmanagement-AWSBCMPricingCalculator_GetWorkloadEstimate-response-id"></a>
 The unique identifier of the retrieved workload estimate.
Type: String
Length Constraints: Fixed length of 36.
Pattern: `[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}`

 ** [name](#API_AWSBCMPricingCalculator_GetWorkloadEstimate_ResponseSyntax) **   <a name="awscostmanagement-AWSBCMPricingCalculator_GetWorkloadEstimate-response-name"></a>
 The name of the retrieved workload estimate.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 64.
Pattern: `[a-zA-Z0-9-]+`

 ** [rateTimestamp](#API_AWSBCMPricingCalculator_GetWorkloadEstimate_ResponseSyntax) **   <a name="awscostmanagement-AWSBCMPricingCalculator_GetWorkloadEstimate-response-rateTimestamp"></a>
 The timestamp of the pricing rates used for the estimate.
Type: Timestamp

 ** [rateType](#API_AWSBCMPricingCalculator_GetWorkloadEstimate_ResponseSyntax) **   <a name="awscostmanagement-AWSBCMPricingCalculator_GetWorkloadEstimate-response-rateType"></a>
 The type of pricing rates used for the estimate.
Type: String
Valid Values: `BEFORE_DISCOUNTS | AFTER_DISCOUNTS | AFTER_DISCOUNTS_AND_COMMITMENTS`

 ** [status](#API_AWSBCMPricingCalculator_GetWorkloadEstimate_ResponseSyntax) **   <a name="awscostmanagement-AWSBCMPricingCalculator_GetWorkloadEstimate-response-status"></a>
 The current status of the workload estimate.
Type: String
Valid Values: `UPDATING | VALID | INVALID | ACTION_NEEDED`

 ** [totalCost](#API_AWSBCMPricingCalculator_GetWorkloadEstimate_ResponseSyntax) **   <a name="awscostmanagement-AWSBCMPricingCalculator_GetWorkloadEstimate-response-totalCost"></a>
 The total estimated cost for the workload.
Type: Double

## Errors
<a name="API_AWSBCMPricingCalculator_GetWorkloadEstimate_Errors"></a>

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
<a name="API_AWSBCMPricingCalculator_GetWorkloadEstimate_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/bcm-pricing-calculator-2024-06-19/GetWorkloadEstimate)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/bcm-pricing-calculator-2024-06-19/GetWorkloadEstimate)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bcm-pricing-calculator-2024-06-19/GetWorkloadEstimate)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/bcm-pricing-calculator-2024-06-19/GetWorkloadEstimate)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bcm-pricing-calculator-2024-06-19/GetWorkloadEstimate)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/bcm-pricing-calculator-2024-06-19/GetWorkloadEstimate)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/bcm-pricing-calculator-2024-06-19/GetWorkloadEstimate)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/bcm-pricing-calculator-2024-06-19/GetWorkloadEstimate)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/bcm-pricing-calculator-2024-06-19/GetWorkloadEstimate)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bcm-pricing-calculator-2024-06-19/GetWorkloadEstimate)
