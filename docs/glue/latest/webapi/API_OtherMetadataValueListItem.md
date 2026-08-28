---
source_url: https://docs.aws.amazon.com/glue/latest/webapi/API_OtherMetadataValueListItem.html
---

# OtherMetadataValueListItem
<a name="API_OtherMetadataValueListItem"></a>

A structure containing other metadata for a schema version belonging to the same metadata key.

## Contents
<a name="API_OtherMetadataValueListItem_Contents"></a>

 ** CreatedTime **   <a name="Glue-Type-OtherMetadataValueListItem-CreatedTime"></a>
The time at which the entry was created.
Type: String
Required: No

 ** MetadataValue **   <a name="Glue-Type-OtherMetadataValueListItem-MetadataValue"></a>
The metadata key’s corresponding value for the other metadata belonging to the same metadata key.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[a-zA-Z0-9+-=._./@]+`
Required: No

## See Also
<a name="API_OtherMetadataValueListItem_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/glue-2017-03-31/OtherMetadataValueListItem)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/glue-2017-03-31/OtherMetadataValueListItem)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/glue-2017-03-31/OtherMetadataValueListItem)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Glue. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query glue` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
