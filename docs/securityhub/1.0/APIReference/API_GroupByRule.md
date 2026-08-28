---
source_url: https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_GroupByRule.html
---

# GroupByRule
<a name="API_GroupByRule"></a>

Defines the how the finding attribute should be grouped.

## Contents
<a name="API_GroupByRule_Contents"></a>

 ** GroupByField **   <a name="securityhub-Type-GroupByRule-GroupByField"></a>
The attribute by which filtered findings should be grouped.
Type: String
Valid Values: `activity_name | cloud.account.uid | cloud.provider | cloud.region | compliance.assessments.name | compliance.status | compliance.control | finding_info.title | finding_info.related_events.traits.category | finding_info.types | metadata.product.name | metadata.product.uid | resources.type | resources.cloud_partition | resources.name | resources.owner.account.uid | resources.owner.org.uid | resources.owner.account.name | resources.provider | resources.region | resources.uid | severity | status | vulnerabilities.fix_coverage | class_name | vulnerabilities.affected_packages.name | finding_info.analytic.name | compliance.standards | cloud.account.name | vendor_attributes.severity | metadata.product.vendor_name`
Required: Yes

 ** Filters **   <a name="securityhub-Type-GroupByRule-Filters"></a>
The criteria used to select which security findings should be included in the grouping operation.
Type: [OcsfFindingFilters](API_OcsfFindingFilters.md) object
Required: No

## See Also
<a name="API_GroupByRule_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securityhub-2018-10-26/GroupByRule)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securityhub-2018-10-26/GroupByRule)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securityhub-2018-10-26/GroupByRule)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Security Hub. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query securityhub` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
