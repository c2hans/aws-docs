---
source_url: https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_ResourcesFilters.html
---

# ResourcesFilters
<a name="API_ResourcesFilters"></a>

Enables filtering of AWS resources based on data.

## Contents
<a name="API_ResourcesFilters_Contents"></a>

 ** CompositeFilters **   <a name="securityhub-Type-ResourcesFilters-CompositeFilters"></a>
A collection of complex filtering conditions that can be applied to AWS resources.
Type: Array of [ResourcesCompositeFilter](API_ResourcesCompositeFilter.md) objects
Required: No

 ** CompositeOperator **   <a name="securityhub-Type-ResourcesFilters-CompositeOperator"></a>
The logical operator used to combine multiple filter conditions in the structure.
Type: String
Valid Values: `AND | OR`
Required: No

## See Also
<a name="API_ResourcesFilters_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securityhub-2018-10-26/ResourcesFilters)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securityhub-2018-10-26/ResourcesFilters)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securityhub-2018-10-26/ResourcesFilters)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Security Hub. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query securityhub` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
