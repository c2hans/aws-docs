---
source_url: https://docs.aws.amazon.com/glue/latest/webapi/API_MetadataKeyValuePair.html
---

# MetadataKeyValuePair
<a name="API_MetadataKeyValuePair"></a>

A structure containing a key value pair for metadata.

## Contents
<a name="API_MetadataKeyValuePair_Contents"></a>

 ** MetadataKey **   <a name="Glue-Type-MetadataKeyValuePair-MetadataKey"></a>
A metadata key.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[a-zA-Z0-9+-=._./@]+`
Required: No

 ** MetadataValue **   <a name="Glue-Type-MetadataKeyValuePair-MetadataValue"></a>
A metadata key’s corresponding value.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[a-zA-Z0-9+-=._./@]+`
Required: No

## See Also
<a name="API_MetadataKeyValuePair_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/glue-2017-03-31/MetadataKeyValuePair)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/glue-2017-03-31/MetadataKeyValuePair)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/glue-2017-03-31/MetadataKeyValuePair)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Glue. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query glue` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
