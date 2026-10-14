---
source_url: https://docs.aws.amazon.com/resilience-hub/v2/APIReference/API_DevOpsAgentConfigurationView.html
---

# DevOpsAgentConfigurationView
<a name="API_DevOpsAgentConfigurationView"></a>

The current DevOps Agent integration state for a service. Read operations return this state.

## Contents
<a name="API_DevOpsAgentConfigurationView_Contents"></a>

 ** agentSpaceArn **   <a name="ngresiliencehub-Type-DevOpsAgentConfigurationView-agentSpaceArn"></a>
The ARN of the linked DevOps Agent Agent Space.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `arn:aws[a-zA-Z-]*:aidevops:[a-z0-9-]+:[0-9]{12}:agentspace/[a-zA-Z0-9-]{1,64}`
Required: No

 ** agentSpaceId **   <a name="ngresiliencehub-Type-DevOpsAgentConfigurationView-agentSpaceId"></a>
The identifier of the linked DevOps Agent Agent Space.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[a-zA-Z0-9-]{1,64}`
Required: No

 ** connectedAt **   <a name="ngresiliencehub-Type-DevOpsAgentConfigurationView-connectedAt"></a>
The timestamp when the service successfully connected to the DevOps Agent Agent Space.
Type: Timestamp
Required: No

 ** operatorAppUrl **   <a name="ngresiliencehub-Type-DevOpsAgentConfigurationView-operatorAppUrl"></a>
The URL of the DevOps Agent Operator App for the linked Agent Space. This URL is present when the connection status is CONNECTED.
Type: String
Required: No

 ** region **   <a name="ngresiliencehub-Type-DevOpsAgentConfigurationView-region"></a>
The AWS Region of the linked DevOps Agent Agent Space.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[a-z0-9-]+`
Required: No

 ** status **   <a name="ngresiliencehub-Type-DevOpsAgentConfigurationView-status"></a>
The connection status of the DevOps Agent integration for this service. Valid values:
+ CONNECTING - The service is being connected to the Agent Space.
+ CONNECTED - The service is connected to the Agent Space.
+ DISCONNECTED - The service is not connected to an Agent Space.
+ FAILED - The connection attempt failed. See statusReason for details.
Type: String
Valid Values: `CONNECTING | CONNECTED | DISCONNECTED | FAILED`
Required: No

 ** statusReason **   <a name="ngresiliencehub-Type-DevOpsAgentConfigurationView-statusReason"></a>
A human-readable explanation of the current connection status. This field explains the status when the connection fails.
Type: String
Required: No

## See Also
<a name="API_DevOpsAgentConfigurationView_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/resiliencehubv2-2026-02-17/DevOpsAgentConfigurationView)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/resiliencehubv2-2026-02-17/DevOpsAgentConfigurationView)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/resiliencehubv2-2026-02-17/DevOpsAgentConfigurationView)
