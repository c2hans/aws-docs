---
source_url: https://docs.aws.amazon.com/chatbot/latest/APIReference/API_ConfiguredTeam.html
---

# ConfiguredTeam
<a name="API_ConfiguredTeam"></a>

A Microsoft Teams team that is authorized with Amazon Q Developer.

## Contents
<a name="API_ConfiguredTeam_Contents"></a>

 ** TeamId **   <a name="qdevinchatapps-Type-ConfiguredTeam-TeamId"></a>
 The ID of the Microsoft Teams authorized with Amazon Q Developer.
To get the team ID, you must perform the initial authorization flow with Microsoft Teams in the Amazon Q Developer console. Then you can copy and paste the team ID from the console. For more information, see [Step 1: Configure a Microsoft Teams client](https://docs.aws.amazon.com/chatbot/latest/adminguide/teams-setup.html#teams-client-setup) in the * Amazon Q Developer Administrator Guide*.
Type: String
Length Constraints: Fixed length of 36.
Pattern: `[0-9A-Fa-f]{8}(?:-[0-9A-Fa-f]{4}){3}-[0-9A-Fa-f]{12}`
Required: Yes

 ** TenantId **   <a name="qdevinchatapps-Type-ConfiguredTeam-TenantId"></a>
The ID of the Microsoft Teams tenant.
Type: String
Length Constraints: Fixed length of 36.
Pattern: `[0-9A-Fa-f]{8}(?:-[0-9A-Fa-f]{4}){3}-[0-9A-Fa-f]{12}`
Required: Yes

 ** State **   <a name="qdevinchatapps-Type-ConfiguredTeam-State"></a>
Either `ENABLED` or `DISABLED`. The resource returns `DISABLED` if the organization's Amazon Q Developer policy has explicitly denied that configuration. For example, if Amazon Chime is disabled.
Type: String
Pattern: `(ENABLED|DISABLED)`
Required: No

 ** StateReason **   <a name="qdevinchatapps-Type-ConfiguredTeam-StateReason"></a>
Provided if State is `DISABLED`. Provides context as to why the resource is disabled.
Type: String
Required: No

 ** TeamName **   <a name="qdevinchatapps-Type-ConfiguredTeam-TeamName"></a>
The name of the Microsoft Teams Team.
Type: String
Length Constraints: Fixed length of 36.
Pattern: `[0-9A-Fa-f]{8}(?:-[0-9A-Fa-f]{4}){3}-[0-9A-Fa-f]{12}`
Required: No

## See Also
<a name="API_ConfiguredTeam_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/chatbot-2017-10-11/ConfiguredTeam)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/chatbot-2017-10-11/ConfiguredTeam)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/chatbot-2017-10-11/ConfiguredTeam)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Q Developer in chat applications. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query chatbot` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
