---
source_url: https://docs.aws.amazon.com/glue/latest/webapi/API_GlueStudioSchemaColumn.html
---

# GlueStudioSchemaColumn
<a name="API_GlueStudioSchemaColumn"></a>

Specifies a single column in a AWS Glue schema definition.

## Contents
<a name="API_GlueStudioSchemaColumn_Contents"></a>

 ** Name **   <a name="Glue-Type-GlueStudioSchemaColumn-Name"></a>
The name of the column in the AWS Glue Studio schema.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\t]*`
Required: Yes

 ** GlueStudioType **   <a name="Glue-Type-GlueStudioSchemaColumn-GlueStudioType"></a>
The data type of the column as defined in AWS Glue Studio.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 131072.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\t]*`
Required: No

 ** Type **   <a name="Glue-Type-GlueStudioSchemaColumn-Type"></a>
The hive type for this column in the AWS Glue Studio schema.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 131072.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\t]*`
Required: No

## See Also
<a name="API_GlueStudioSchemaColumn_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/glue-2017-03-31/GlueStudioSchemaColumn)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/glue-2017-03-31/GlueStudioSchemaColumn)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/glue-2017-03-31/GlueStudioSchemaColumn)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Glue. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query glue` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
