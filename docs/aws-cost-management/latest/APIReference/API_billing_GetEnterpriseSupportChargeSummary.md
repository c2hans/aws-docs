---
source_url: https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_billing_GetEnterpriseSupportChargeSummary.html
---

# GetEnterpriseSupportChargeSummary
<a name="API_billing_GetEnterpriseSupportChargeSummary"></a>

Returns a summary of Enterprise Support data aggregated across all accounts in the Enterprise Support profile.

## Request Syntax
<a name="API_billing_GetEnterpriseSupportChargeSummary_RequestSyntax"></a>

```
{
   "billingMonth": "{{string}}"
}
```

## Request Parameters
<a name="API_billing_GetEnterpriseSupportChargeSummary_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [billingMonth](#API_billing_GetEnterpriseSupportChargeSummary_RequestSyntax) **   <a name="awscostmanagement-billing_GetEnterpriseSupportChargeSummary-request-billingMonth"></a>
The billing month in YYYY-MM format. This must be a month in the past.
Type: String
Pattern: `\d{4}-(0[1-9]|1[0-2])`
Required: Yes

## Response Syntax
<a name="API_billing_GetEnterpriseSupportChargeSummary_ResponseSyntax"></a>

```
{
   "billDate": number,
   "billingMonth": "string",
   "billingPeriodEndDate": number,
   "billingPeriodStartDate": number,
   "isEstimated": boolean,
   "payerAccountId": "string",
   "supportCharge": "string",
   "supportChargePercentage": "string",
   "supportDiscount": "string",
   "supportEffectivePricingPlan": {
      "description": "string",
      "discountAppliesToMinimumCharge": boolean,
      "endDate": number,
      "minimumCharge": "string",
      "name": "string",
      "planDiscountPercent": "string",
      "pricingPlanId": "string",
      "startDate": number,
      "tiered": "string",
      "tiers": [
         {
            "additionalPercentageOfAggregateCharges": "string",
            "aggregateChargesAdjustment": "string",
            "baseCharge": "string",
            "increment": "string",
            "incremental": boolean,
            "incrementCharge": "string",
            "tierMaximum": "string",
            "tierMinimum": "string"
         }
      ]
   },
   "totalSupportCharge": "string",
   "totalSupportEligibleReservedInstanceSpend": "string",
   "totalSupportEligibleSavingsPlanSpend": "string",
   "totalSupportEligibleSpend": "string",
   "totalSupportEligibleUsageSpend": "string"
}
```

## Response Elements
<a name="API_billing_GetEnterpriseSupportChargeSummary_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [billDate](#API_billing_GetEnterpriseSupportChargeSummary_ResponseSyntax) **   <a name="awscostmanagement-billing_GetEnterpriseSupportChargeSummary-response-billDate"></a>
The date the bill was generated.
Type: Timestamp

 ** [billingMonth](#API_billing_GetEnterpriseSupportChargeSummary_ResponseSyntax) **   <a name="awscostmanagement-billing_GetEnterpriseSupportChargeSummary-response-billingMonth"></a>
The billing month in YYYY-MM format. This must be a month in the past.
Type: String
Pattern: `\d{4}-(0[1-9]|1[0-2])`

 ** [billingPeriodEndDate](#API_billing_GetEnterpriseSupportChargeSummary_ResponseSyntax) **   <a name="awscostmanagement-billing_GetEnterpriseSupportChargeSummary-response-billingPeriodEndDate"></a>
The end date of the billing period.
Type: Timestamp

 ** [billingPeriodStartDate](#API_billing_GetEnterpriseSupportChargeSummary_ResponseSyntax) **   <a name="awscostmanagement-billing_GetEnterpriseSupportChargeSummary-response-billingPeriodStartDate"></a>
The start date of the billing period.
Type: Timestamp

 ** [isEstimated](#API_billing_GetEnterpriseSupportChargeSummary_ResponseSyntax) **   <a name="awscostmanagement-billing_GetEnterpriseSupportChargeSummary-response-isEstimated"></a>
When true, the Support charge amount is estimated. When false, the Support charge amount is finalized.
Type: Boolean

 ** [payerAccountId](#API_billing_GetEnterpriseSupportChargeSummary_ResponseSyntax) **   <a name="awscostmanagement-billing_GetEnterpriseSupportChargeSummary-response-payerAccountId"></a>
The payer account ID that is authorized to view Enterprise Support data for all accounts in its Support profile.
Type: String
Pattern: `[0-9]{12}`

 ** [supportCharge](#API_billing_GetEnterpriseSupportChargeSummary_ResponseSyntax) **   <a name="awscostmanagement-billing_GetEnterpriseSupportChargeSummary-response-supportCharge"></a>
The Support charge amount for the account.
Type: String

 ** [supportChargePercentage](#API_billing_GetEnterpriseSupportChargeSummary_ResponseSyntax) **   <a name="awscostmanagement-billing_GetEnterpriseSupportChargeSummary-response-supportChargePercentage"></a>
The percentage applied to the total Support-eligible spend to calculate the total Support charge across all accounts in the Support profile.
Type: String

 ** [supportDiscount](#API_billing_GetEnterpriseSupportChargeSummary_ResponseSyntax) **   <a name="awscostmanagement-billing_GetEnterpriseSupportChargeSummary-response-supportDiscount"></a>
The support discount amount.
Type: String

 ** [supportEffectivePricingPlan](#API_billing_GetEnterpriseSupportChargeSummary_ResponseSyntax) **   <a name="awscostmanagement-billing_GetEnterpriseSupportChargeSummary-response-supportEffectivePricingPlan"></a>
The effective pricing plan used for the support charge calculation.
Type: [PricingPlan](API_billing_PricingPlan.md) object

 ** [totalSupportCharge](#API_billing_GetEnterpriseSupportChargeSummary_ResponseSyntax) **   <a name="awscostmanagement-billing_GetEnterpriseSupportChargeSummary-response-totalSupportCharge"></a>
The total Support charge amount for all accounts in the Support profile.
Type: String

 ** [totalSupportEligibleReservedInstanceSpend](#API_billing_GetEnterpriseSupportChargeSummary_ResponseSyntax) **   <a name="awscostmanagement-billing_GetEnterpriseSupportChargeSummary-response-totalSupportEligibleReservedInstanceSpend"></a>
The total Support-eligible Reserved Instance spend from all accounts in the Support profile.
Type: String

 ** [totalSupportEligibleSavingsPlanSpend](#API_billing_GetEnterpriseSupportChargeSummary_ResponseSyntax) **   <a name="awscostmanagement-billing_GetEnterpriseSupportChargeSummary-response-totalSupportEligibleSavingsPlanSpend"></a>
The total Support-eligible Savings Plan spend from all accounts in the Support profile.
Type: String

 ** [totalSupportEligibleSpend](#API_billing_GetEnterpriseSupportChargeSummary_ResponseSyntax) **   <a name="awscostmanagement-billing_GetEnterpriseSupportChargeSummary-response-totalSupportEligibleSpend"></a>
The total Support-eligible Spend from all accounts in the Support profile. This includes eligible spend from usage of Amazon Web Services, Reserved Instances, and Savings Plans.
Type: String

 ** [totalSupportEligibleUsageSpend](#API_billing_GetEnterpriseSupportChargeSummary_ResponseSyntax) **   <a name="awscostmanagement-billing_GetEnterpriseSupportChargeSummary-response-totalSupportEligibleUsageSpend"></a>
The total Support-eligible spend from usage of Amazon Web Services from all accounts in the Support profile.
Type: String

## Errors
<a name="API_billing_GetEnterpriseSupportChargeSummary_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You don't have sufficient access to perform this action.
HTTP Status Code: 400

 ** InternalServerException **
The request processing failed because of an unknown error, exception, or failure.
HTTP Status Code: 500

 ** ResourceNotFoundException **
 The specified ARN in the request doesn't exist.
 ** resourceId **
 Value is a list of resource IDs that were not found.
 ** resourceType **
 Value is the type of resource that was not found.
HTTP Status Code: 400

 ** ThrottlingException **
The request was denied due to request throttling.
HTTP Status Code: 400

 ** ValidationException **
The input fails to satisfy the constraints specified by an AWS service.
 ** fieldList **
The input fails to satisfy the constraints specified by an AWS service.
 ** reason **
The input fails to satisfy the constraints specified by an AWS service.
HTTP Status Code: 400

## See Also
<a name="API_billing_GetEnterpriseSupportChargeSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/billing-2023-09-07/GetEnterpriseSupportChargeSummary)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/billing-2023-09-07/GetEnterpriseSupportChargeSummary)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/billing-2023-09-07/GetEnterpriseSupportChargeSummary)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/billing-2023-09-07/GetEnterpriseSupportChargeSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/billing-2023-09-07/GetEnterpriseSupportChargeSummary)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/billing-2023-09-07/GetEnterpriseSupportChargeSummary)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/billing-2023-09-07/GetEnterpriseSupportChargeSummary)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/billing-2023-09-07/GetEnterpriseSupportChargeSummary)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/billing-2023-09-07/GetEnterpriseSupportChargeSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/billing-2023-09-07/GetEnterpriseSupportChargeSummary)
