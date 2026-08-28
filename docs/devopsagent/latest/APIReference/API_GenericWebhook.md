---
source_url: https://docs.aws.amazon.com/devopsagent/latest/APIReference/API_GenericWebhook.html
---

# GenericWebhook
<a name="API_GenericWebhook"></a>

Generic webhook configuration for services that support webhook notifications.

## Contents
<a name="API_GenericWebhook_Contents"></a>

 ** apiKey **   <a name="devopsagent-Type-GenericWebhook-apiKey"></a>
API Key for API Key webhook authentication
Type: String
Length Constraints: Minimum length of 1.
Required: No

 ** webhookId **   <a name="devopsagent-Type-GenericWebhook-webhookId"></a>
The unique webhook identifier
Type: String
Required: No

 ** webhookSecret **   <a name="devopsagent-Type-GenericWebhook-webhookSecret"></a>
The webhook secret for authentication
Type: String
Required: No

 ** webhookType **   <a name="devopsagent-Type-GenericWebhook-webhookType"></a>
The webhook authentication type
Type: String
Valid Values: `hmac | apikey | gitlab | pagerduty`
Required: No

 ** webhookUrl **   <a name="devopsagent-Type-GenericWebhook-webhookUrl"></a>
The webhook URL endpoint
Type: String
Required: No

## See Also
<a name="API_GenericWebhook_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/devops-agent-2026-01-01/GenericWebhook)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/devops-agent-2026-01-01/GenericWebhook)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/devops-agent-2026-01-01/GenericWebhook)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS DevOps Agent. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query devopsagent` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
