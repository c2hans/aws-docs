---
source_url: https://docs.aws.amazon.com/devopsagent/latest/APIReference/API_MSTeamsConfiguration.html
---

# MSTeamsConfiguration
<a name="API_MSTeamsConfiguration"></a>

Configuration for connecting a Microsoft Teams team to the DevOps Agent service. Use this configuration to specify which team to connect and how to route agent notifications to channels within that team.

## Contents
<a name="API_MSTeamsConfiguration_Contents"></a>

 ** teamId **   <a name="devopsagent-Type-MSTeamsConfiguration-teamId"></a>
The identifier of the Microsoft Teams team to connect to the DevOps Agent service.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 36.
Pattern: `[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}`
Required: Yes

 ** teamName **   <a name="devopsagent-Type-MSTeamsConfiguration-teamName"></a>
The name of the Microsoft Teams team to connect to the DevOps Agent service.
Type: String
Required: Yes

 ** transmissionTarget **   <a name="devopsagent-Type-MSTeamsConfiguration-transmissionTarget"></a>
The Microsoft Teams channels that receive agent notifications.
Type: [MSTeamsTransmissionTarget](API_MSTeamsTransmissionTarget.md) object
Required: Yes

## See Also
<a name="API_MSTeamsConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/devops-agent-2026-01-01/MSTeamsConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/devops-agent-2026-01-01/MSTeamsConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/devops-agent-2026-01-01/MSTeamsConfiguration)
