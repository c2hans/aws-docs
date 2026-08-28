---
source_url: https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_CurrentInstance.html
---

# CurrentInstance
<a name="API_CurrentInstance"></a>

Context about the current instance.

## Contents
<a name="API_CurrentInstance_Contents"></a>

 ** CurrencyCode **   <a name="awscostmanagement-Type-CurrentInstance-CurrencyCode"></a>
The currency code that AWS used to calculate the costs for this instance.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Pattern: `[\S\s]*`
Required: No

 ** InstanceName **   <a name="awscostmanagement-Type-CurrentInstance-InstanceName"></a>
The name that you given an instance. This field shows as blank if you haven't given the instance a name.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Pattern: `[\S\s]*`
Required: No

 ** MonthlyCost **   <a name="awscostmanagement-Type-CurrentInstance-MonthlyCost"></a>
The current On-Demand cost of operating this instance on a monthly basis.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Pattern: `[\S\s]*`
Required: No

 ** OnDemandHoursInLookbackPeriod **   <a name="awscostmanagement-Type-CurrentInstance-OnDemandHoursInLookbackPeriod"></a>
The number of hours during the lookback period that's billed at On-Demand rates.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Pattern: `[\S\s]*`
Required: No

 ** ReservationCoveredHoursInLookbackPeriod **   <a name="awscostmanagement-Type-CurrentInstance-ReservationCoveredHoursInLookbackPeriod"></a>
The number of hours during the lookback period that's covered by reservations.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Pattern: `[\S\s]*`
Required: No

 ** ResourceDetails **   <a name="awscostmanagement-Type-CurrentInstance-ResourceDetails"></a>
Details about the resource and utilization.
Type: [ResourceDetails](API_ResourceDetails.md) object
Required: No

 ** ResourceId **   <a name="awscostmanagement-Type-CurrentInstance-ResourceId"></a>
Resource ID of the current instance.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Pattern: `[\S\s]*`
Required: No

 ** ResourceUtilization **   <a name="awscostmanagement-Type-CurrentInstance-ResourceUtilization"></a>
Utilization information of the current instance during the lookback period.
Type: [ResourceUtilization](API_ResourceUtilization.md) object
Required: No

 ** SavingsPlansCoveredHoursInLookbackPeriod **   <a name="awscostmanagement-Type-CurrentInstance-SavingsPlansCoveredHoursInLookbackPeriod"></a>
The number of hours during the lookback period that's covered by Savings Plans.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Pattern: `[\S\s]*`
Required: No

 ** Tags **   <a name="awscostmanagement-Type-CurrentInstance-Tags"></a>
Cost allocation resource tags that are applied to the instance.
Type: Array of [TagValues](API_TagValues.md) objects
Required: No

 ** TotalRunningHoursInLookbackPeriod **   <a name="awscostmanagement-Type-CurrentInstance-TotalRunningHoursInLookbackPeriod"></a>
The total number of hours that the instance ran during the lookback period.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Pattern: `[\S\s]*`
Required: No

## See Also
<a name="API_CurrentInstance_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ce-2017-10-25/CurrentInstance)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ce-2017-10-25/CurrentInstance)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ce-2017-10-25/CurrentInstance)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Billing and Cost Management. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query aws-cost-management` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
