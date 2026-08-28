---
source_url: https://docs.aws.amazon.com/devopsagent/latest/APIReference/API_SlackConfiguration.html
---

# SlackConfiguration
<a name="API_SlackConfiguration"></a>

Configuration for Slack workspace integration.

## Contents
<a name="API_SlackConfiguration_Contents"></a>

 ** transmissionTarget **   <a name="devopsagent-Type-SlackConfiguration-transmissionTarget"></a>
Transmission targets for agent notifications
Type: [SlackTransmissionTarget](API_SlackTransmissionTarget.md) object
Required: Yes

 ** workspaceId **   <a name="devopsagent-Type-SlackConfiguration-workspaceId"></a>
Associated Slack workspace ID
Type: String
Pattern: `[TE][A-Z0-9]+`
Required: Yes

 ** workspaceName **   <a name="devopsagent-Type-SlackConfiguration-workspaceName"></a>
Associated Slack workspace name
Type: String
Required: Yes

## See Also
<a name="API_SlackConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/devops-agent-2026-01-01/SlackConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/devops-agent-2026-01-01/SlackConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/devops-agent-2026-01-01/SlackConfiguration)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS DevOps Agent. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query devopsagent` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
