---
source_url: https://docs.aws.amazon.com/glue/latest/webapi/API_GroupFilters.html
---

# GroupFilters
<a name="API_GroupFilters"></a>

Specifies a group of filters with a logical operator that determines how the filters are combined to evaluate routing conditions.

## Contents
<a name="API_GroupFilters_Contents"></a>

 ** Filters **   <a name="Glue-Type-GroupFilters-Filters"></a>
A list of filter expressions that define the conditions for this group.
Type: Array of [FilterExpression](API_FilterExpression.md) objects
Required: Yes

 ** GroupName **   <a name="Glue-Type-GroupFilters-GroupName"></a>
The name of the filter group.
Type: String
Pattern: `[A-Za-z0-9_-]*`
Required: Yes

 ** LogicalOperator **   <a name="Glue-Type-GroupFilters-LogicalOperator"></a>
The logical operator used to combine the filters in this group. Determines whether all filters must match (AND) or any filter can match (OR).
Type: String
Valid Values: `AND | OR`
Required: Yes

## See Also
<a name="API_GroupFilters_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/glue-2017-03-31/GroupFilters)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/glue-2017-03-31/GroupFilters)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/glue-2017-03-31/GroupFilters)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Glue. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query glue` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
