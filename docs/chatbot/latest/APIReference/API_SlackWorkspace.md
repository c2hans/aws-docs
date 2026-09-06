---
source_url: https://docs.aws.amazon.com/chatbot/latest/APIReference/API_SlackWorkspace.html
---

# SlackWorkspace
<a name="API_SlackWorkspace"></a>

A Slack workspace.

## Contents
<a name="API_SlackWorkspace_Contents"></a>

 ** SlackTeamId **   <a name="qdevinchatapps-Type-SlackWorkspace-SlackTeamId"></a>
The ID of the Slack workspace authorized with Amazon Q Developer.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[0-9A-Z]{1,255}`
Required: Yes

 ** SlackTeamName **   <a name="qdevinchatapps-Type-SlackWorkspace-SlackTeamName"></a>
The name of the Slack workspace.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Required: Yes

 ** State **   <a name="qdevinchatapps-Type-SlackWorkspace-State"></a>
Either `ENABLED` or `DISABLED`. The resource returns `DISABLED` if the organization's Amazon Q Developer policy has explicitly denied that configuration. For example, if Amazon Chime is disabled.
Type: String
Pattern: `(ENABLED|DISABLED)`
Required: No

 ** StateReason **   <a name="qdevinchatapps-Type-SlackWorkspace-StateReason"></a>
Provided if State is `DISABLED`. Provides context as to why the resource is disabled.
Type: String
Required: No

## See Also
<a name="API_SlackWorkspace_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/chatbot-2017-10-11/SlackWorkspace)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/chatbot-2017-10-11/SlackWorkspace)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/chatbot-2017-10-11/SlackWorkspace)
