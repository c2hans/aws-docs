---
source_url: https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_AWSBCMPricingCalculator_BatchCreateBillScenarioCommitmentModification.html
---

# BatchCreateBillScenarioCommitmentModification
<a name="API_AWSBCMPricingCalculator_BatchCreateBillScenarioCommitmentModification"></a>

 Create Compute Savings Plans, EC2 Instance Savings Plans, or EC2 Reserved Instances commitments that you want to model in a Bill Scenario.

**Note**
The `BatchCreateBillScenarioCommitmentModification` operation doesn't have its own IAM permission. To authorize this operation for AWS principals, include the permission `bcm-pricing-calculator:CreateBillScenarioCommitmentModification` in your policies.

## Request Syntax
<a name="API_AWSBCMPricingCalculator_BatchCreateBillScenarioCommitmentModification_RequestSyntax"></a>

```
{
   "billScenarioId": "{{string}}",
   "clientToken": "{{string}}",
   "commitmentModifications": [
      {
         "commitmentAction": { ... },
         "group": "{{string}}",
         "key": "{{string}}",
         "usageAccountId": "{{string}}"
      }
   ]
}
```

## Request Parameters
<a name="API_AWSBCMPricingCalculator_BatchCreateBillScenarioCommitmentModification_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [billScenarioId](#API_AWSBCMPricingCalculator_BatchCreateBillScenarioCommitmentModification_RequestSyntax) **   <a name="awscostmanagement-AWSBCMPricingCalculator_BatchCreateBillScenarioCommitmentModification-request-billScenarioId"></a>
 The ID of the Bill Scenario for which you want to create the modeled commitment.
Type: String
Length Constraints: Fixed length of 36.
Pattern: `[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}`
Required: Yes

 ** [clientToken](#API_AWSBCMPricingCalculator_BatchCreateBillScenarioCommitmentModification_RequestSyntax) **   <a name="awscostmanagement-AWSBCMPricingCalculator_BatchCreateBillScenarioCommitmentModification-request-clientToken"></a>
 A unique, case-sensitive identifier that you provide to ensure the idempotency of the request.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[\u0021-\u007E]+`
Required: No

 ** [commitmentModifications](#API_AWSBCMPricingCalculator_BatchCreateBillScenarioCommitmentModification_RequestSyntax) **   <a name="awscostmanagement-AWSBCMPricingCalculator_BatchCreateBillScenarioCommitmentModification-request-commitmentModifications"></a>
 List of commitments that you want to model in the Bill Scenario.
Type: Array of [BatchCreateBillScenarioCommitmentModificationEntry](API_AWSBCMPricingCalculator_BatchCreateBillScenarioCommitmentModificationEntry.md) objects
Array Members: Minimum number of 1 item. Maximum number of 25 items.
Required: Yes

## Response Syntax
<a name="API_AWSBCMPricingCalculator_BatchCreateBillScenarioCommitmentModification_ResponseSyntax"></a>

```
{
   "errors": [
      {
         "errorCode": "string",
         "errorMessage": "string",
         "key": "string"
      }
   ],
   "items": [
      {
         "commitmentAction": { ... },
         "group": "string",
         "id": "string",
         "key": "string",
         "usageAccountId": "string"
      }
   ]
}
```

## Response Elements
<a name="API_AWSBCMPricingCalculator_BatchCreateBillScenarioCommitmentModification_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [errors](#API_AWSBCMPricingCalculator_BatchCreateBillScenarioCommitmentModification_ResponseSyntax) **   <a name="awscostmanagement-AWSBCMPricingCalculator_BatchCreateBillScenarioCommitmentModification-response-errors"></a>
 Returns the list of errors reason and the commitment item keys that cannot be created in the Bill Scenario.
Type: Array of [BatchCreateBillScenarioCommitmentModificationError](API_AWSBCMPricingCalculator_BatchCreateBillScenarioCommitmentModificationError.md) objects

 ** [items](#API_AWSBCMPricingCalculator_BatchCreateBillScenarioCommitmentModification_ResponseSyntax) **   <a name="awscostmanagement-AWSBCMPricingCalculator_BatchCreateBillScenarioCommitmentModification-response-items"></a>
 Returns the list of successful commitment line items that were created for the Bill Scenario.
Type: Array of [BatchCreateBillScenarioCommitmentModificationItem](API_AWSBCMPricingCalculator_BatchCreateBillScenarioCommitmentModificationItem.md) objects

## Errors
<a name="API_AWSBCMPricingCalculator_BatchCreateBillScenarioCommitmentModification_Errors"></a>

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
<a name="API_AWSBCMPricingCalculator_BatchCreateBillScenarioCommitmentModification_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/bcm-pricing-calculator-2024-06-19/BatchCreateBillScenarioCommitmentModification)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/bcm-pricing-calculator-2024-06-19/BatchCreateBillScenarioCommitmentModification)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bcm-pricing-calculator-2024-06-19/BatchCreateBillScenarioCommitmentModification)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/bcm-pricing-calculator-2024-06-19/BatchCreateBillScenarioCommitmentModification)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bcm-pricing-calculator-2024-06-19/BatchCreateBillScenarioCommitmentModification)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/bcm-pricing-calculator-2024-06-19/BatchCreateBillScenarioCommitmentModification)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/bcm-pricing-calculator-2024-06-19/BatchCreateBillScenarioCommitmentModification)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/bcm-pricing-calculator-2024-06-19/BatchCreateBillScenarioCommitmentModification)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/bcm-pricing-calculator-2024-06-19/BatchCreateBillScenarioCommitmentModification)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bcm-pricing-calculator-2024-06-19/BatchCreateBillScenarioCommitmentModification)
