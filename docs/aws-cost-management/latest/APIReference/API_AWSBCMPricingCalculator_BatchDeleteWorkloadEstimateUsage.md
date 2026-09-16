---
source_url: https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_AWSBCMPricingCalculator_BatchDeleteWorkloadEstimateUsage.html
---

# BatchDeleteWorkloadEstimateUsage
<a name="API_AWSBCMPricingCalculator_BatchDeleteWorkloadEstimateUsage"></a>

 Delete usage that you have created in a Workload estimate. You can only delete usage that you had added and cannot model deletion (or removal) of a existing usage. If you want model removal of an existing usage, see [ BatchUpdateWorkloadEstimateUsage](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_AWSBCMPricingCalculator_BatchUpdateWorkloadEstimateUsage.html).

**Note**
The `BatchDeleteWorkloadEstimateUsage` operation doesn't have its own IAM permission. To authorize this operation for AWS principals, include the permission `bcm-pricing-calculator:DeleteWorkloadEstimateUsage` in your policies.

## Request Syntax
<a name="API_AWSBCMPricingCalculator_BatchDeleteWorkloadEstimateUsage_RequestSyntax"></a>

```
{
   "ids": [ "{{string}}" ],
   "workloadEstimateId": "{{string}}"
}
```

## Request Parameters
<a name="API_AWSBCMPricingCalculator_BatchDeleteWorkloadEstimateUsage_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [ids](#API_AWSBCMPricingCalculator_BatchDeleteWorkloadEstimateUsage_RequestSyntax) **   <a name="awscostmanagement-AWSBCMPricingCalculator_BatchDeleteWorkloadEstimateUsage-request-ids"></a>
 List of usage that you want to delete from the Workload estimate.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 25 items.
Length Constraints: Fixed length of 36.
Pattern: `[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}`
Required: Yes

 ** [workloadEstimateId](#API_AWSBCMPricingCalculator_BatchDeleteWorkloadEstimateUsage_RequestSyntax) **   <a name="awscostmanagement-AWSBCMPricingCalculator_BatchDeleteWorkloadEstimateUsage-request-workloadEstimateId"></a>
 The ID of the Workload estimate for which you want to delete the modeled usage.
Type: String
Length Constraints: Fixed length of 36.
Pattern: `[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}`
Required: Yes

## Response Syntax
<a name="API_AWSBCMPricingCalculator_BatchDeleteWorkloadEstimateUsage_ResponseSyntax"></a>

```
{
   "errors": [
      {
         "errorCode": "string",
         "errorMessage": "string",
         "id": "string"
      }
   ]
}
```

## Response Elements
<a name="API_AWSBCMPricingCalculator_BatchDeleteWorkloadEstimateUsage_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [errors](#API_AWSBCMPricingCalculator_BatchDeleteWorkloadEstimateUsage_ResponseSyntax) **   <a name="awscostmanagement-AWSBCMPricingCalculator_BatchDeleteWorkloadEstimateUsage-response-errors"></a>
 Returns the list of errors reason and the usage item keys that cannot be deleted from the Workload estimate.
Type: Array of [BatchDeleteWorkloadEstimateUsageError](API_AWSBCMPricingCalculator_BatchDeleteWorkloadEstimateUsageError.md) objects

## Errors
<a name="API_AWSBCMPricingCalculator_BatchDeleteWorkloadEstimateUsage_Errors"></a>

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
<a name="API_AWSBCMPricingCalculator_BatchDeleteWorkloadEstimateUsage_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/bcm-pricing-calculator-2024-06-19/BatchDeleteWorkloadEstimateUsage)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/bcm-pricing-calculator-2024-06-19/BatchDeleteWorkloadEstimateUsage)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bcm-pricing-calculator-2024-06-19/BatchDeleteWorkloadEstimateUsage)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/bcm-pricing-calculator-2024-06-19/BatchDeleteWorkloadEstimateUsage)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bcm-pricing-calculator-2024-06-19/BatchDeleteWorkloadEstimateUsage)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/bcm-pricing-calculator-2024-06-19/BatchDeleteWorkloadEstimateUsage)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/bcm-pricing-calculator-2024-06-19/BatchDeleteWorkloadEstimateUsage)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/bcm-pricing-calculator-2024-06-19/BatchDeleteWorkloadEstimateUsage)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/bcm-pricing-calculator-2024-06-19/BatchDeleteWorkloadEstimateUsage)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bcm-pricing-calculator-2024-06-19/BatchDeleteWorkloadEstimateUsage)
