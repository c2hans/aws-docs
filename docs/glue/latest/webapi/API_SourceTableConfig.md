---
source_url: https://docs.aws.amazon.com/glue/latest/webapi/API_SourceTableConfig.html
---

# SourceTableConfig
<a name="API_SourceTableConfig"></a>

Properties used by the source leg to process data from the source.

## Contents
<a name="API_SourceTableConfig_Contents"></a>

 ** Fields **   <a name="Glue-Type-SourceTableConfig-Fields"></a>
A list of fields used for column-level filtering. Currently unsupported.
Type: Array of strings
Length Constraints: Minimum length of 1. Maximum length of 128.
Required: No

 ** FilterPredicate **   <a name="Glue-Type-SourceTableConfig-FilterPredicate"></a>
A condition clause used for row-level filtering. Currently unsupported.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Required: No

 ** PrimaryKey **   <a name="Glue-Type-SourceTableConfig-PrimaryKey"></a>
Provide the primary key set for this table. Currently supported specifically for SAP `EntityOf` entities upon request. Contact AWS Support to make this feature available.
Type: Array of strings
Length Constraints: Minimum length of 1. Maximum length of 128.
Required: No

 ** RecordUpdateField **   <a name="Glue-Type-SourceTableConfig-RecordUpdateField"></a>
Incremental pull timestamp-based field. Currently unsupported.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Required: No

## See Also
<a name="API_SourceTableConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/glue-2017-03-31/SourceTableConfig)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/glue-2017-03-31/SourceTableConfig)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/glue-2017-03-31/SourceTableConfig)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Glue. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query glue` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
