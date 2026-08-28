---
source_url: https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_media-pipelines-chime_KeywordMatchConfiguration.html
---

# KeywordMatchConfiguration
<a name="API_media-pipelines-chime_KeywordMatchConfiguration"></a>

A structure that contains the settings for a keyword match task.

## Contents
<a name="API_media-pipelines-chime_KeywordMatchConfiguration_Contents"></a>

 ** Keywords **   <a name="chimesdk-Type-media-pipelines-chime_KeywordMatchConfiguration-Keywords"></a>
The keywords or phrases that you want to match.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 10 items.
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `^[\s0-9a-zA-Z'-]+`
Required: Yes

 ** RuleName **   <a name="chimesdk-Type-media-pipelines-chime_KeywordMatchConfiguration-RuleName"></a>
The name of the keyword match rule.
Type: String
Length Constraints: Minimum length of 2. Maximum length of 64.
Pattern: `^[0-9a-zA-Z._-]+`
Required: Yes

 ** Negate **   <a name="chimesdk-Type-media-pipelines-chime_KeywordMatchConfiguration-Negate"></a>
Matches keywords or phrases on their presence or absence. If set to `TRUE`, the rule matches when all the specified keywords or phrases are absent. Default: `FALSE`.
Type: Boolean
Required: No

## See Also
<a name="API_media-pipelines-chime_KeywordMatchConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/chime-sdk-media-pipelines-2021-07-15/KeywordMatchConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/chime-sdk-media-pipelines-2021-07-15/KeywordMatchConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/chime-sdk-media-pipelines-2021-07-15/KeywordMatchConfiguration)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Chime SDK. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query chime-sdk` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
