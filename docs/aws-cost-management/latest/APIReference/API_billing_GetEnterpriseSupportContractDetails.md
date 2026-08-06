---
source_url: https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_billing_GetEnterpriseSupportContractDetails.html
---

# GetEnterpriseSupportContractDetails
<a name="API_billing_GetEnterpriseSupportContractDetails"></a>

Returns Enterprise Support contract details.

## Request Syntax
<a name="API_billing_GetEnterpriseSupportContractDetails_RequestSyntax"></a>

```
{
   "billingMonth": "{{string}}"
}
```

## Request Parameters
<a name="API_billing_GetEnterpriseSupportContractDetails_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [billingMonth](#API_billing_GetEnterpriseSupportContractDetails_RequestSyntax) **   <a name="awscostmanagement-billing_GetEnterpriseSupportContractDetails-request-billingMonth"></a>
The billing month in YYYY-MM format. This must be a month in the past.
Type: String
Pattern: `\d{4}-(0[1-9]|1[0-2])`
Required: Yes

## Response Syntax
<a name="API_billing_GetEnterpriseSupportContractDetails_ResponseSyntax"></a>

```
{
   "additionalSupportCharge": [
      {
         "amount": "string",
         "chargeType": "string",
         "description": "string"
      }
   ],
   "additionalSupportEligibleUsageSpend": [
      {
         "amount": "string",
         "chargeType": "string",
         "description": "string"
      }
   ],
   "chargedPayerAccountIds": [
      {
         "accountId": "string",
         "chargePercentage": "string"
      }
   ],
   "contractPayerAccountIds": [
      {
         "accountId": "string",
         "isGdn": boolean
      }
   ],
   "isContractActive": boolean,
   "pricingPlans": [
      {
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
      }
   ],
   "supportAllocationMethod": "string",
   "supportProrateStartDate": number,
   "supportReservedInstanceAmortizationStartDate": number,
   "supportReservedInstanceTreatmentMethod": "string",
   "supportSavingsPlansAmortizationStartDate": number,
   "supportSavingsPlansTreatmentMethod": "string"
}
```

## Response Elements
<a name="API_billing_GetEnterpriseSupportContractDetails_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [additionalSupportCharge](#API_billing_GetEnterpriseSupportContractDetails_ResponseSyntax) **   <a name="awscostmanagement-billing_GetEnterpriseSupportContractDetails-response-additionalSupportCharge"></a>
Any Additional support charges applied to the contract.
Type: Array of [AdditionalCharge](API_billing_AdditionalCharge.md) objects
Array Members: Minimum number of 0 items. Maximum number of 50 items.

 ** [additionalSupportEligibleUsageSpend](#API_billing_GetEnterpriseSupportContractDetails_ResponseSyntax) **   <a name="awscostmanagement-billing_GetEnterpriseSupportContractDetails-response-additionalSupportEligibleUsageSpend"></a>
Any Additional support-eligible usage spend charges.
Type: Array of [AdditionalCharge](API_billing_AdditionalCharge.md) objects
Array Members: Minimum number of 0 items. Maximum number of 50 items.

 ** [chargedPayerAccountIds](#API_billing_GetEnterpriseSupportContractDetails_ResponseSyntax) **   <a name="awscostmanagement-billing_GetEnterpriseSupportContractDetails-response-chargedPayerAccountIds"></a>
The list of payer accounts and their charge allocation percentages.
Type: Array of [ChargeAccount](API_billing_ChargeAccount.md) objects
Array Members: Minimum number of 0 items. Maximum number of 1000 items.

 ** [contractPayerAccountIds](#API_billing_GetEnterpriseSupportContractDetails_ResponseSyntax) **   <a name="awscostmanagement-billing_GetEnterpriseSupportContractDetails-response-contractPayerAccountIds"></a>
The list of accounts covered by the Enterprise Support contract.
Type: Array of [ContractAccount](API_billing_ContractAccount.md) objects
Array Members: Minimum number of 0 items. Maximum number of 2000 items.

 ** [isContractActive](#API_billing_GetEnterpriseSupportContractDetails_ResponseSyntax) **   <a name="awscostmanagement-billing_GetEnterpriseSupportContractDetails-response-isContractActive"></a>
When true, the Enterprise Support contract is active. When false, the Enterprise Support Contract is inactive.
Type: Boolean

 ** [pricingPlans](#API_billing_GetEnterpriseSupportContractDetails_ResponseSyntax) **   <a name="awscostmanagement-billing_GetEnterpriseSupportContractDetails-response-pricingPlans"></a>
The pricing plans associated with this Enterprise Support contract.
Type: Array of [PricingPlan](API_billing_PricingPlan.md) objects
Array Members: Minimum number of 0 items. Maximum number of 10 items.

 ** [supportAllocationMethod](#API_billing_GetEnterpriseSupportContractDetails_ResponseSyntax) **   <a name="awscostmanagement-billing_GetEnterpriseSupportContractDetails-response-supportAllocationMethod"></a>
The method used to distribute the total Support charge amount across each account in the Support profile. Valid values: Proportional, Fixed\_Percentage. Proportional means support charges are distributed to each account in proportion to its eligible Spend. Fixed\_Percentage means support charges are distributed across accounts according to pre-configured percentages from the contract.
Type: String

 ** [supportProrateStartDate](#API_billing_GetEnterpriseSupportContractDetails_ResponseSyntax) **   <a name="awscostmanagement-billing_GetEnterpriseSupportContractDetails-response-supportProrateStartDate"></a>
The start date for accounts subscribed or unsubscribed to Support billing during the billing month.
Type: Timestamp

 ** [supportReservedInstanceAmortizationStartDate](#API_billing_GetEnterpriseSupportContractDetails_ResponseSyntax) **   <a name="awscostmanagement-billing_GetEnterpriseSupportContractDetails-response-supportReservedInstanceAmortizationStartDate"></a>
When supportReservedInstanceTreatmentMethod = AmortizedCustom, only amortized fees for Reserved Instances purchased on or after this date are included in the calculation. This field is Null for all other treatment methods.
Type: Timestamp

 ** [supportReservedInstanceTreatmentMethod](#API_billing_GetEnterpriseSupportContractDetails_ResponseSyntax) **   <a name="awscostmanagement-billing_GetEnterpriseSupportContractDetails-response-supportReservedInstanceTreatmentMethod"></a>
The method used to include Reserved Instance (RI) fees in the Enterprise Support charge calculation. Valid values: None (RI fees excluded from Support-eligible spend), Upfront (full upfront RI fees included in month of purchase), Amortized (RI fees spread over commitment term for RIs purchased on or after Support subscription start date), AmortizedCustom (same as Amortized but only for RIs purchased on or after a specified custom start date), AmortizedAll (RI fees amortized for all active RIs including those purchased before Support subscription started).
Type: String

 ** [supportSavingsPlansAmortizationStartDate](#API_billing_GetEnterpriseSupportContractDetails_ResponseSyntax) **   <a name="awscostmanagement-billing_GetEnterpriseSupportContractDetails-response-supportSavingsPlansAmortizationStartDate"></a>
This is applicable when supportSavingsPlansTreatmentMethod = Amortized and is Null for all other methods. It shows the start date from which Savings Plan fees are included in Support Eligible Spend.
Type: Timestamp

 ** [supportSavingsPlansTreatmentMethod](#API_billing_GetEnterpriseSupportContractDetails_ResponseSyntax) **   <a name="awscostmanagement-billing_GetEnterpriseSupportContractDetails-response-supportSavingsPlansTreatmentMethod"></a>
The method used to include Savings Plans fees in Enterprise Support charge calculations. Valid values: None (Savings Plan fees excluded from Support-eligible spend), Upfront (full upfront Savings Plan fees included in month of purchase), Amortized (Savings Plan fees spread over commitment term for Savings Plans purchased on or after Support subscription start date), AmortizedCustom (same as Amortized but only for Savings Plans purchased on or after a specified custom start date), AmortizedAll (Savings Plan fees amortized for all active Savings Plans including those purchased before Support subscription started).
Type: String

## Errors
<a name="API_billing_GetEnterpriseSupportContractDetails_Errors"></a>

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
<a name="API_billing_GetEnterpriseSupportContractDetails_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/billing-2023-09-07/GetEnterpriseSupportContractDetails)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/billing-2023-09-07/GetEnterpriseSupportContractDetails)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/billing-2023-09-07/GetEnterpriseSupportContractDetails)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/billing-2023-09-07/GetEnterpriseSupportContractDetails)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/billing-2023-09-07/GetEnterpriseSupportContractDetails)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/billing-2023-09-07/GetEnterpriseSupportContractDetails)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/billing-2023-09-07/GetEnterpriseSupportContractDetails)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/billing-2023-09-07/GetEnterpriseSupportContractDetails)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/billing-2023-09-07/GetEnterpriseSupportContractDetails)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/billing-2023-09-07/GetEnterpriseSupportContractDetails)
