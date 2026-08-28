---
source_url: https://docs.aws.amazon.com/devopsagent/latest/APIReference/API_SlackChannel.html
---

# SlackChannel
<a name="API_SlackChannel"></a>

Represents a Slack channel with its ID and optional name.

## Contents
<a name="API_SlackChannel_Contents"></a>

 ** channelId **   <a name="devopsagent-Type-SlackChannel-channelId"></a>
Slack channel ID
Type: String
Length Constraints: Minimum length of 8. Maximum length of 16.
Pattern: `[CGD][A-Z0-9]+`
Required: Yes

 ** channelName **   <a name="devopsagent-Type-SlackChannel-channelName"></a>
Slack channel name
Type: String
Required: No

## See Also
<a name="API_SlackChannel_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/devops-agent-2026-01-01/SlackChannel)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/devops-agent-2026-01-01/SlackChannel)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/devops-agent-2026-01-01/SlackChannel)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS DevOps Agent. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query devopsagent` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
