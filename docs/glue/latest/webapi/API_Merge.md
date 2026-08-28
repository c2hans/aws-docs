---
source_url: https://docs.aws.amazon.com/glue/latest/webapi/API_Merge.html
---

# Merge
<a name="API_Merge"></a>

Specifies a transform that merges a `DynamicFrame` with a staging `DynamicFrame` based on the specified primary keys to identify records. Duplicate records (records with the same primary keys) are not de-duplicated.

## Contents
<a name="API_Merge_Contents"></a>

 ** Inputs **   <a name="Glue-Type-Merge-Inputs"></a>
The data inputs identified by their node names.
Type: Array of strings
Array Members: Fixed number of 2 items.
Pattern: `[A-Za-z0-9_-]*`
Required: Yes

 ** Name **   <a name="Glue-Type-Merge-Name"></a>
The name of the transform node.
Type: String
Pattern: `([^\r\n])*`
Required: Yes

 ** PrimaryKeys **   <a name="Glue-Type-Merge-PrimaryKeys"></a>
The list of primary key fields to match records from the source and staging dynamic frames.
Type: Array of arrays of strings
Pattern: `([\u0009\u000B\u000C\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF])*`
Required: Yes

 ** Source **   <a name="Glue-Type-Merge-Source"></a>
The source `DynamicFrame` that will be merged with a staging `DynamicFrame`.
Type: String
Pattern: `[A-Za-z0-9_-]*`
Required: Yes

## See Also
<a name="API_Merge_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/glue-2017-03-31/Merge)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/glue-2017-03-31/Merge)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/glue-2017-03-31/Merge)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Glue. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query glue` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
