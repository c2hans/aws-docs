---
source_url: https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_AWSBCMPricingCalculator_ListBillEstimateInputCommitmentModifications.html
---

# ListBillEstimateInputCommitmentModifications
<a name="API_AWSBCMPricingCalculator_ListBillEstimateInputCommitmentModifications"></a>

 Lists the input commitment modifications associated with a bill estimate.

## Request Syntax
<a name="API_AWSBCMPricingCalculator_ListBillEstimateInputCommitmentModifications_RequestSyntax"></a>

```
{
   "billEstimateId": "{{string}}",
   "maxResults": {{number}},
   "nextToken": "{{string}}"
}
```

## Request Parameters
<a name="API_AWSBCMPricingCalculator_ListBillEstimateInputCommitmentModifications_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [billEstimateId](#API_AWSBCMPricingCalculator_ListBillEstimateInputCommitmentModifications_RequestSyntax) **   <a name="awscostmanagement-AWSBCMPricingCalculator_ListBillEstimateInputCommitmentModifications-request-billEstimateId"></a>
 The unique identifier of the bill estimate to list input commitment modifications for.
Type: String
Length Constraints: Fixed length of 36.
Pattern: `[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}`
Required: Yes

 ** [maxResults](#API_AWSBCMPricingCalculator_ListBillEstimateInputCommitmentModifications_RequestSyntax) **   <a name="awscostmanagement-AWSBCMPricingCalculator_ListBillEstimateInputCommitmentModifications-request-maxResults"></a>
 The maximum number of results to return per page.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 25.
Required: No

 ** [nextToken](#API_AWSBCMPricingCalculator_ListBillEstimateInputCommitmentModifications_RequestSyntax) **   <a name="awscostmanagement-AWSBCMPricingCalculator_ListBillEstimateInputCommitmentModifications-request-nextToken"></a>
 A token to retrieve the next page of results.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 2048.
Pattern: `[\S\s]*`
Required: No

## Response Syntax
<a name="API_AWSBCMPricingCalculator_ListBillEstimateInputCommitmentModifications_ResponseSyntax"></a>

```
{
   "items": [
      {
         "commitmentAction": { ... },
         "group": "string",
         "id": "string",
         "usageAccountId": "string"
      }
   ],
   "nextToken": "string"
}
```

## Response Elements
<a name="API_AWSBCMPricingCalculator_ListBillEstimateInputCommitmentModifications_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [items](#API_AWSBCMPricingCalculator_ListBillEstimateInputCommitmentModifications_ResponseSyntax) **   <a name="awscostmanagement-AWSBCMPricingCalculator_ListBillEstimateInputCommitmentModifications-response-items"></a>
 The list of input commitment modifications associated with the bill estimate.
Type: Array of [BillEstimateInputCommitmentModificationSummary](API_AWSBCMPricingCalculator_BillEstimateInputCommitmentModificationSummary.md) objects

 ** [nextToken](#API_AWSBCMPricingCalculator_ListBillEstimateInputCommitmentModifications_ResponseSyntax) **   <a name="awscostmanagement-AWSBCMPricingCalculator_ListBillEstimateInputCommitmentModifications-response-nextToken"></a>
 A token to retrieve the next page of results, if any.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 2048.
Pattern: `[\S\s]*`

## Errors
<a name="API_AWSBCMPricingCalculator_ListBillEstimateInputCommitmentModifications_Errors"></a>

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
<a name="API_AWSBCMPricingCalculator_ListBillEstimateInputCommitmentModifications_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/bcm-pricing-calculator-2024-06-19/ListBillEstimateInputCommitmentModifications)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/bcm-pricing-calculator-2024-06-19/ListBillEstimateInputCommitmentModifications)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bcm-pricing-calculator-2024-06-19/ListBillEstimateInputCommitmentModifications)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/bcm-pricing-calculator-2024-06-19/ListBillEstimateInputCommitmentModifications)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bcm-pricing-calculator-2024-06-19/ListBillEstimateInputCommitmentModifications)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/bcm-pricing-calculator-2024-06-19/ListBillEstimateInputCommitmentModifications)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/bcm-pricing-calculator-2024-06-19/ListBillEstimateInputCommitmentModifications)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/bcm-pricing-calculator-2024-06-19/ListBillEstimateInputCommitmentModifications)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/bcm-pricing-calculator-2024-06-19/ListBillEstimateInputCommitmentModifications)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bcm-pricing-calculator-2024-06-19/ListBillEstimateInputCommitmentModifications)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Billing and Cost Management. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query aws-cost-management` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
