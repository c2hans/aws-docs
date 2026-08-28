---
source_url: https://docs.aws.amazon.com/glue/latest/webapi/API_Filter.html
---

# Filter
<a name="API_Filter"></a>

Specifies a transform that splits a dataset into two, based on a filter condition.

## Contents
<a name="API_Filter_Contents"></a>

 ** Filters **   <a name="Glue-Type-Filter-Filters"></a>
Specifies a filter expression.
Type: Array of [FilterExpression](API_FilterExpression.md) objects
Required: Yes

 ** Inputs **   <a name="Glue-Type-Filter-Inputs"></a>
The data inputs identified by their node names.
Type: Array of strings
Array Members: Fixed number of 1 item.
Pattern: `[A-Za-z0-9_-]*`
Required: Yes

 ** LogicalOperator **   <a name="Glue-Type-Filter-LogicalOperator"></a>
The operator used to filter rows by comparing the key value to a specified value.
Type: String
Valid Values: `AND | OR`
Required: Yes

 ** Name **   <a name="Glue-Type-Filter-Name"></a>
The name of the transform node.
Type: String
Pattern: `([^\r\n])*`
Required: Yes

## See Also
<a name="API_Filter_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/glue-2017-03-31/Filter)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/glue-2017-03-31/Filter)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/glue-2017-03-31/Filter)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Glue. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query glue` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
