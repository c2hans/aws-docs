---
source_url: https://docs.aws.amazon.com/glue/latest/webapi/API_Union.html
---

# Union
<a name="API_Union"></a>

Specifies a transform that combines the rows from two or more datasets into a single result.

## Contents
<a name="API_Union_Contents"></a>

 ** Inputs **   <a name="Glue-Type-Union-Inputs"></a>
The node ID inputs to the transform.
Type: Array of strings
Array Members: Fixed number of 2 items.
Pattern: `[A-Za-z0-9_-]*`
Required: Yes

 ** Name **   <a name="Glue-Type-Union-Name"></a>
The name of the transform node.
Type: String
Pattern: `([^\r\n])*`
Required: Yes

 ** UnionType **   <a name="Glue-Type-Union-UnionType"></a>
Indicates the type of Union transform.
Specify `ALL` to join all rows from data sources to the resulting DynamicFrame. The resulting union does not remove duplicate rows.
Specify `DISTINCT` to remove duplicate rows in the resulting DynamicFrame.
Type: String
Valid Values: `ALL | DISTINCT`
Required: Yes

## See Also
<a name="API_Union_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/glue-2017-03-31/Union)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/glue-2017-03-31/Union)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/glue-2017-03-31/Union)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Glue. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query glue` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
