---
source_url: https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_CoverageHours.html
---

# CoverageHours
<a name="API_CoverageHours"></a>

How long a running instance either used a reservation or was On-Demand.

## Contents
<a name="API_CoverageHours_Contents"></a>

 ** CoverageHoursPercentage **   <a name="awscostmanagement-Type-CoverageHours-CoverageHoursPercentage"></a>
The percentage of instance hours that a reservation covered.
Type: String
Required: No

 ** OnDemandHours **   <a name="awscostmanagement-Type-CoverageHours-OnDemandHours"></a>
The number of instance running hours that On-Demand Instances covered.
Type: String
Required: No

 ** ReservedHours **   <a name="awscostmanagement-Type-CoverageHours-ReservedHours"></a>
The number of instance running hours that reservations covered.
Type: String
Required: No

 ** TotalRunningHours **   <a name="awscostmanagement-Type-CoverageHours-TotalRunningHours"></a>
The total instance usage, in hours.
Type: String
Required: No

## See Also
<a name="API_CoverageHours_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ce-2017-10-25/CoverageHours)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ce-2017-10-25/CoverageHours)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ce-2017-10-25/CoverageHours)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Billing and Cost Management. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query aws-cost-management` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
