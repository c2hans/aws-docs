---
source_url: https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_ResourcesCompositeFilter.html
---

# ResourcesCompositeFilter
<a name="API_ResourcesCompositeFilter"></a>

Enables the creation of criteria for AWS resources in Security Hub CSPM.

## Contents
<a name="API_ResourcesCompositeFilter_Contents"></a>

 ** DateFilters **   <a name="securityhub-Type-ResourcesCompositeFilter-DateFilters"></a>
Enables filtering based on date and timestamp field values.
Type: Array of [ResourcesDateFilter](API_ResourcesDateFilter.md) objects
Required: No

 ** MapFilters **   <a name="securityhub-Type-ResourcesCompositeFilter-MapFilters"></a>
Enables filtering based on map-based field values.
Type: Array of [ResourcesMapFilter](API_ResourcesMapFilter.md) objects
Required: No

 ** NestedCompositeFilters **   <a name="securityhub-Type-ResourcesCompositeFilter-NestedCompositeFilters"></a>
 Provides an additional level of filtering, creating a three-layer nested structure. The first layer is a `CompositeFilters` array with a `CompositeOperator` (`AND`/`OR`). The second layer is a `CompositeFilter` object that contains direct filters and `NestedCompositeFilters`. The third layer is `NestedCompositeFilters`, which contains additional filter conditions.
Type: Array of [ResourcesCompositeFilter](#API_ResourcesCompositeFilter) objects
Required: No

 ** NumberFilters **   <a name="securityhub-Type-ResourcesCompositeFilter-NumberFilters"></a>
Enables filtering based on numerical field values.
Type: Array of [ResourcesNumberFilter](API_ResourcesNumberFilter.md) objects
Required: No

 ** Operator **   <a name="securityhub-Type-ResourcesCompositeFilter-Operator"></a>
The logical operator used to combine multiple filter conditions.
Type: String
Valid Values: `AND | OR`
Required: No

 ** StringFilters **   <a name="securityhub-Type-ResourcesCompositeFilter-StringFilters"></a>
Enables filtering based on string field values.
Type: Array of [ResourcesStringFilter](API_ResourcesStringFilter.md) objects
Required: No

## See Also
<a name="API_ResourcesCompositeFilter_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securityhub-2018-10-26/ResourcesCompositeFilter)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securityhub-2018-10-26/ResourcesCompositeFilter)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securityhub-2018-10-26/ResourcesCompositeFilter)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Security Hub. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query securityhub` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
