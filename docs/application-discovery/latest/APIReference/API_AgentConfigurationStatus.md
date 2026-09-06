---
source_url: https://docs.aws.amazon.com/application-discovery/latest/APIReference/API_AgentConfigurationStatus.html
---

# AgentConfigurationStatus
<a name="API_AgentConfigurationStatus"></a>

Information about agents that were instructed to start collecting data. Information includes the agent ID, a description of the operation, and whether the agent configuration was updated.

## Contents
<a name="API_AgentConfigurationStatus_Contents"></a>

 ** agentId **   <a name="DiscServ-Type-AgentConfigurationStatus-agentId"></a>
The agent ID.
Type: String
Length Constraints: Maximum length of 10000.
Pattern: `[\s\S]*`
Required: No

 ** description **   <a name="DiscServ-Type-AgentConfigurationStatus-description"></a>
A description of the operation performed.
Type: String
Length Constraints: Maximum length of 10000.
Pattern: `[\s\S]*`
Required: No

 ** operationSucceeded **   <a name="DiscServ-Type-AgentConfigurationStatus-operationSucceeded"></a>
Information about the status of the `StartDataCollection` and `StopDataCollection` operations. The system has recorded the data collection operation. The agent receives this command the next time it polls for a new command.
Type: Boolean
Required: No

## See Also
<a name="API_AgentConfigurationStatus_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/discovery-2015-11-01/AgentConfigurationStatus)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/discovery-2015-11-01/AgentConfigurationStatus)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/discovery-2015-11-01/AgentConfigurationStatus)
