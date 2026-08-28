---
source_url: https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_CoverageNormalizedUnits.html
---

# CoverageNormalizedUnits
<a name="API_CoverageNormalizedUnits"></a>

The amount of instance usage, in normalized units. You can use normalized units to see your EC2 usage for multiple sizes of instances in a uniform way. For example, suppose that you run an xlarge instance and a 2xlarge instance. If you run both instances for the same amount of time, the 2xlarge instance uses twice as much of your reservation as the xlarge instance, even though both instances show only one instance-hour. When you use normalized units instead of instance-hours, the xlarge instance used 8 normalized units, and the 2xlarge instance used 16 normalized units.

For more information, see [Modifying Reserved Instances](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ri-modifying.html) in the *Amazon Elastic Compute Cloud User Guide for Linux Instances*.

## Contents
<a name="API_CoverageNormalizedUnits_Contents"></a>

 ** CoverageNormalizedUnitsPercentage **   <a name="awscostmanagement-Type-CoverageNormalizedUnits-CoverageNormalizedUnitsPercentage"></a>
The percentage of your used instance normalized units that a reservation covers.
Type: String
Required: No

 ** OnDemandNormalizedUnits **   <a name="awscostmanagement-Type-CoverageNormalizedUnits-OnDemandNormalizedUnits"></a>
The number of normalized units that are covered by On-Demand Instances instead of a reservation.
Type: String
Required: No

 ** ReservedNormalizedUnits **   <a name="awscostmanagement-Type-CoverageNormalizedUnits-ReservedNormalizedUnits"></a>
The number of normalized units that a reservation covers.
Type: String
Required: No

 ** TotalRunningNormalizedUnits **   <a name="awscostmanagement-Type-CoverageNormalizedUnits-TotalRunningNormalizedUnits"></a>
The total number of normalized units that you used.
Type: String
Required: No

## See Also
<a name="API_CoverageNormalizedUnits_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ce-2017-10-25/CoverageNormalizedUnits)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ce-2017-10-25/CoverageNormalizedUnits)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ce-2017-10-25/CoverageNormalizedUnits)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Billing and Cost Management. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query aws-cost-management` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
