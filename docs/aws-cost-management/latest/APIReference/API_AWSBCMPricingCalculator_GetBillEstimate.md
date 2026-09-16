---
source_url: https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_AWSBCMPricingCalculator_GetBillEstimate.html
---

# GetBillEstimate
<a name="API_AWSBCMPricingCalculator_GetBillEstimate"></a>

 Retrieves details of a specific bill estimate.

## Request Syntax
<a name="API_AWSBCMPricingCalculator_GetBillEstimate_RequestSyntax"></a>

```
{
   "identifier": "{{string}}"
}
```

## Request Parameters
<a name="API_AWSBCMPricingCalculator_GetBillEstimate_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [identifier](#API_AWSBCMPricingCalculator_GetBillEstimate_RequestSyntax) **   <a name="awscostmanagement-AWSBCMPricingCalculator_GetBillEstimate-request-identifier"></a>
 The unique identifier of the bill estimate to retrieve.
Type: String
Length Constraints: Fixed length of 36.
Pattern: `[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}`
Required: Yes

## Response Syntax
<a name="API_AWSBCMPricingCalculator_GetBillEstimate_ResponseSyntax"></a>

```
{
   "billInterval": {
      "end": number,
      "start": number
   },
   "costCategoryGroupSharingPreferenceArn": "string",
   "costCategoryGroupSharingPreferenceEffectiveDate": number,
   "costSummary": {
      "serviceCostDifferences": {
         "string" : {
            "estimatedCost": {
               "amount": number,
               "currency": "string"
            },
            "historicalCost": {
               "amount": number,
               "currency": "string"
            }
         }
      },
      "totalCostDifference": {
         "estimatedCost": {
            "amount": number,
            "currency": "string"
         },
         "historicalCost": {
            "amount": number,
            "currency": "string"
         }
      }
   },
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
<a name="API_AWSBCMPricingCalculator_GetBillEstimate_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [billInterval](#API_AWSBCMPricingCalculator_GetBillEstimate_ResponseSyntax) **   <a name="awscostmanagement-AWSBCMPricingCalculator_GetBillEstimate-response-billInterval"></a>
 The time period covered by the bill estimate.
Type: [BillInterval](API_AWSBCMPricingCalculator_BillInterval.md) object

 ** [costCategoryGroupSharingPreferenceArn](#API_AWSBCMPricingCalculator_GetBillEstimate_ResponseSyntax) **   <a name="awscostmanagement-AWSBCMPricingCalculator_GetBillEstimate-response-costCategoryGroupSharingPreferenceArn"></a>
The arn of the cost category used in the reserved and prioritized group sharing.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:aws[-a-z0-9]*:ce::[0-9]{12}:costcategory/[a-f0-9-]{36}`

 ** [costCategoryGroupSharingPreferenceEffectiveDate](#API_AWSBCMPricingCalculator_GetBillEstimate_ResponseSyntax) **   <a name="awscostmanagement-AWSBCMPricingCalculator_GetBillEstimate-response-costCategoryGroupSharingPreferenceEffectiveDate"></a>
Timestamp of the effective date of the cost category used in the group sharing settings.
Type: Timestamp

 ** [costSummary](#API_AWSBCMPricingCalculator_GetBillEstimate_ResponseSyntax) **   <a name="awscostmanagement-AWSBCMPricingCalculator_GetBillEstimate-response-costSummary"></a>
 A summary of the estimated costs.
Type: [BillEstimateCostSummary](API_AWSBCMPricingCalculator_BillEstimateCostSummary.md) object

 ** [createdAt](#API_AWSBCMPricingCalculator_GetBillEstimate_ResponseSyntax) **   <a name="awscostmanagement-AWSBCMPricingCalculator_GetBillEstimate-response-createdAt"></a>
 The timestamp when the bill estimate was created.
Type: Timestamp

 ** [expiresAt](#API_AWSBCMPricingCalculator_GetBillEstimate_ResponseSyntax) **   <a name="awscostmanagement-AWSBCMPricingCalculator_GetBillEstimate-response-expiresAt"></a>
 The timestamp when the bill estimate will expire.
Type: Timestamp

 ** [failureMessage](#API_AWSBCMPricingCalculator_GetBillEstimate_ResponseSyntax) **   <a name="awscostmanagement-AWSBCMPricingCalculator_GetBillEstimate-response-failureMessage"></a>
 An error message if the bill estimate retrieval failed.
Type: String

 ** [groupSharingPreference](#API_AWSBCMPricingCalculator_GetBillEstimate_ResponseSyntax) **   <a name="awscostmanagement-AWSBCMPricingCalculator_GetBillEstimate-response-groupSharingPreference"></a>
The setting for the reserved instance and savings plans group sharing used in this estimate.
Type: String
Valid Values: `OPEN | PRIORITIZED | RESTRICTED`

 ** [id](#API_AWSBCMPricingCalculator_GetBillEstimate_ResponseSyntax) **   <a name="awscostmanagement-AWSBCMPricingCalculator_GetBillEstimate-response-id"></a>
 The unique identifier of the retrieved bill estimate.
Type: String
Length Constraints: Fixed length of 36.
Pattern: `[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}`

 ** [name](#API_AWSBCMPricingCalculator_GetBillEstimate_ResponseSyntax) **   <a name="awscostmanagement-AWSBCMPricingCalculator_GetBillEstimate-response-name"></a>
 The name of the retrieved bill estimate.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 64.
Pattern: `[a-zA-Z0-9-]+`

 ** [status](#API_AWSBCMPricingCalculator_GetBillEstimate_ResponseSyntax) **   <a name="awscostmanagement-AWSBCMPricingCalculator_GetBillEstimate-response-status"></a>
 The current status of the bill estimate.
Type: String
Valid Values: `IN_PROGRESS | COMPLETE | FAILED`

## Errors
<a name="API_AWSBCMPricingCalculator_GetBillEstimate_Errors"></a>

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
<a name="API_AWSBCMPricingCalculator_GetBillEstimate_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/bcm-pricing-calculator-2024-06-19/GetBillEstimate)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/bcm-pricing-calculator-2024-06-19/GetBillEstimate)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bcm-pricing-calculator-2024-06-19/GetBillEstimate)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/bcm-pricing-calculator-2024-06-19/GetBillEstimate)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bcm-pricing-calculator-2024-06-19/GetBillEstimate)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/bcm-pricing-calculator-2024-06-19/GetBillEstimate)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/bcm-pricing-calculator-2024-06-19/GetBillEstimate)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/bcm-pricing-calculator-2024-06-19/GetBillEstimate)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/bcm-pricing-calculator-2024-06-19/GetBillEstimate)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bcm-pricing-calculator-2024-06-19/GetBillEstimate)
