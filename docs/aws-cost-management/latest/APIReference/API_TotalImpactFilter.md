---
source_url: https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_TotalImpactFilter.html
---

# TotalImpactFilter
<a name="API_TotalImpactFilter"></a>

Filters cost anomalies based on the total impact.

## Contents
<a name="API_TotalImpactFilter_Contents"></a>

 ** NumericOperator **   <a name="awscostmanagement-Type-TotalImpactFilter-NumericOperator"></a>
The comparing value that's used in the filter.
Type: String
Valid Values: `EQUAL | GREATER_THAN_OR_EQUAL | LESS_THAN_OR_EQUAL | GREATER_THAN | LESS_THAN | BETWEEN`
Required: Yes

 ** StartValue **   <a name="awscostmanagement-Type-TotalImpactFilter-StartValue"></a>
The lower bound dollar value that's used in the filter.
Type: Double
Required: Yes

 ** EndValue **   <a name="awscostmanagement-Type-TotalImpactFilter-EndValue"></a>
The upper bound dollar value that's used in the filter.
Type: Double
Required: No

## See Also
<a name="API_TotalImpactFilter_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ce-2017-10-25/TotalImpactFilter)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ce-2017-10-25/TotalImpactFilter)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ce-2017-10-25/TotalImpactFilter)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Billing and Cost Management. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query aws-cost-management` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
