---
source_url: https://docs.aws.amazon.com/opensearch-service/latest/APIReference/API_osis_Tag.html
---

# Tag
<a name="API_osis_Tag"></a>

A tag (key-value pair) for an OpenSearch Ingestion pipeline.

## Contents
<a name="API_osis_Tag_Contents"></a>

 ** Key **   <a name="opensearchservice-Type-osis_Tag-Key"></a>
The tag key. Tag keys must be unique for the pipeline to which they are attached.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `.*`
Required: Yes

 ** Value **   <a name="opensearchservice-Type-osis_Tag-Value"></a>
The value assigned to the corresponding tag key. Tag values can be null and don't have to be unique in a tag set. For example, you can have a key value pair in a tag set of `project : Trinity` and `cost-center : Trinity`
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Pattern: `.*`
Required: Yes

## See Also
<a name="API_osis_Tag_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/osis-2022-01-01/Tag)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/osis-2022-01-01/Tag)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/osis-2022-01-01/Tag)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon OpenSearch Service. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query opensearch-service` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
