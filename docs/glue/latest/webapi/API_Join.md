---
source_url: https://docs.aws.amazon.com/glue/latest/webapi/API_Join.html
---

# Join
<a name="API_Join"></a>

Specifies a transform that joins two datasets into one dataset using a comparison phrase on the specified data property keys. You can use inner, outer, left, right, left semi, and left anti joins.

## Contents
<a name="API_Join_Contents"></a>

 ** Columns **   <a name="Glue-Type-Join-Columns"></a>
A list of the two columns to be joined.
Type: Array of [JoinColumn](API_JoinColumn.md) objects
Array Members: Fixed number of 2 items.
Required: Yes

 ** Inputs **   <a name="Glue-Type-Join-Inputs"></a>
The data inputs identified by their node names.
Type: Array of strings
Array Members: Fixed number of 2 items.
Pattern: `[A-Za-z0-9_-]*`
Required: Yes

 ** JoinType **   <a name="Glue-Type-Join-JoinType"></a>
Specifies the type of join to be performed on the datasets.
Type: String
Valid Values: `equijoin | left | right | outer | leftsemi | leftanti`
Required: Yes

 ** Name **   <a name="Glue-Type-Join-Name"></a>
The name of the transform node.
Type: String
Pattern: `([^\r\n])*`
Required: Yes

## See Also
<a name="API_Join_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/glue-2017-03-31/Join)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/glue-2017-03-31/Join)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/glue-2017-03-31/Join)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Glue. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query glue` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
