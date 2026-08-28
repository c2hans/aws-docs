---
source_url: https://docs.aws.amazon.com/glue/latest/webapi/API_SchemaColumn.html
---

# SchemaColumn
<a name="API_SchemaColumn"></a>

A key-value pair representing a column and data type that this transform can run against. The `Schema` parameter of the `MLTransform` may contain up to 100 of these structures.

## Contents
<a name="API_SchemaColumn_Contents"></a>

 ** DataType **   <a name="Glue-Type-SchemaColumn-DataType"></a>
The type of data in the column.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 131072.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\t]*`
Required: No

 ** Name **   <a name="Glue-Type-SchemaColumn-Name"></a>
The name of the column.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\t]*`
Required: No

## See Also
<a name="API_SchemaColumn_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/glue-2017-03-31/SchemaColumn)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/glue-2017-03-31/SchemaColumn)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/glue-2017-03-31/SchemaColumn)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Glue. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query glue` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
