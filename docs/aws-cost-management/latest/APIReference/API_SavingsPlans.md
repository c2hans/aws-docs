---
source_url: https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_SavingsPlans.html
---

# SavingsPlans
<a name="API_SavingsPlans"></a>

The Savings Plans commitment details.

## Contents
<a name="API_SavingsPlans_Contents"></a>

 ** InstanceFamily **   <a name="awscostmanagement-Type-SavingsPlans-InstanceFamily"></a>
The instance family of the Savings Plans commitment.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Pattern: `[\S\s]*`
Required: No

 ** OfferingId **   <a name="awscostmanagement-Type-SavingsPlans-OfferingId"></a>
The unique ID that's used to distinguish Savings Plans commitments from one another.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Pattern: `[\S\s]*`
Required: No

 ** PaymentOption **   <a name="awscostmanagement-Type-SavingsPlans-PaymentOption"></a>
The payment option for the Savings Plans commitment.
Type: String
Valid Values: `NO_UPFRONT | PARTIAL_UPFRONT | ALL_UPFRONT | LIGHT_UTILIZATION | MEDIUM_UTILIZATION | HEAVY_UTILIZATION`
Required: No

 ** Region **   <a name="awscostmanagement-Type-SavingsPlans-Region"></a>
The Region associated with the Savings Plans commitment.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Pattern: `[\S\s]*`
Required: No

 ** SavingsPlansCommitment **   <a name="awscostmanagement-Type-SavingsPlans-SavingsPlansCommitment"></a>
The Savings Plans commitment.
Type: Double
Valid Range: Minimum value of 0.001. Maximum value of 5000.
Required: No

 ** SavingsPlansType **   <a name="awscostmanagement-Type-SavingsPlans-SavingsPlansType"></a>
The Savings Plans type.
Type: String
Valid Values: `COMPUTE_SP | EC2_INSTANCE_SP | SAGEMAKER_SP | DATABASE_SP`
Required: No

 ** TermInYears **   <a name="awscostmanagement-Type-SavingsPlans-TermInYears"></a>
The term that you want the Savings Plans commitment for.
Type: String
Valid Values: `ONE_YEAR | THREE_YEARS`
Required: No

## See Also
<a name="API_SavingsPlans_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ce-2017-10-25/SavingsPlans)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ce-2017-10-25/SavingsPlans)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ce-2017-10-25/SavingsPlans)
