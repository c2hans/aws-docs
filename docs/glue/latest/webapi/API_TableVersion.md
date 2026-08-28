---
source_url: https://docs.aws.amazon.com/glue/latest/webapi/API_TableVersion.html
---

# TableVersion
<a name="API_TableVersion"></a>

Specifies a version of a table.

## Contents
<a name="API_TableVersion_Contents"></a>

 ** Table **   <a name="Glue-Type-TableVersion-Table"></a>
The table in question.
Type: [Table](API_Table.md) object
Required: No

 ** VersionId **   <a name="Glue-Type-TableVersion-VersionId"></a>
The ID value that identifies this table version. A `VersionId` is a string representation of an integer. Each version is incremented by 1.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\t]*`
Required: No

## See Also
<a name="API_TableVersion_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/glue-2017-03-31/TableVersion)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/glue-2017-03-31/TableVersion)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/glue-2017-03-31/TableVersion)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Glue. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query glue` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
