---
source_url: https://docs.aws.amazon.com/partner-central/latest/APIReference/API_prm_Tag.html
---

# Tag
<a name="API_prm_Tag"></a>

A key-value pair used for organizing and managing resources through metadata tags.

## Contents
<a name="API_prm_Tag_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** Key **   <a name="AWSPartnerCentral-Type-prm_Tag-Key"></a>
The key portion of the tag.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[^\x00-\x1F\x7F]+`
Required: Yes

 ** Value **   <a name="AWSPartnerCentral-Type-prm_Tag-Value"></a>
The value portion of the tag.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Pattern: `[^\x00-\x1F\x7F]*`
Required: Yes

## See Also
<a name="API_prm_Tag_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/partnercentral-revenue-measurement-2022-07-26/Tag)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/partnercentral-revenue-measurement-2022-07-26/Tag)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/partnercentral-revenue-measurement-2022-07-26/Tag)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Partner Central. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query partner-central` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
