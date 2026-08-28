---
source_url: https://docs.aws.amazon.com/application-discovery/latest/APIReference/API_AgentInfo.html
---

# AgentInfo
<a name="API_AgentInfo"></a>

Information about agents associated with the user’s AWS account. Information includes agent IDs, IP addresses, media access control (MAC) addresses, agent or collector status, hostname where the agent resides, and agent version for each agent.

## Contents
<a name="API_AgentInfo_Contents"></a>

 ** agentId **   <a name="DiscServ-Type-AgentInfo-agentId"></a>
The agent or collector ID.
Type: String
Length Constraints: Minimum length of 10. Maximum length of 20.
Pattern: `\S+`
Required: No

 ** agentNetworkInfoList **   <a name="DiscServ-Type-AgentInfo-agentNetworkInfoList"></a>
Network details about the host where the agent or collector resides.
Type: Array of [AgentNetworkInfo](API_AgentNetworkInfo.md) objects
Required: No

 ** agentType **   <a name="DiscServ-Type-AgentInfo-agentType"></a>
Type of agent.
Type: String
Length Constraints: Maximum length of 10000.
Pattern: `[\s\S]*`
Required: No

 ** collectionStatus **   <a name="DiscServ-Type-AgentInfo-collectionStatus"></a>
Status of the collection process for an agent.
Type: String
Length Constraints: Maximum length of 10000.
Pattern: `[\s\S]*`
Required: No

 ** connectorId **   <a name="DiscServ-Type-AgentInfo-connectorId"></a>
The ID of the connector.
Type: String
Length Constraints: Maximum length of 10000.
Pattern: `[\s\S]*`
Required: No

 ** health **   <a name="DiscServ-Type-AgentInfo-health"></a>
The health of the agent.
Type: String
Valid Values: `HEALTHY | UNHEALTHY | RUNNING | UNKNOWN | BLACKLISTED | SHUTDOWN`
Required: No

 ** hostName **   <a name="DiscServ-Type-AgentInfo-hostName"></a>
The name of the host where the agent or collector resides. The host can be a server or virtual machine.
Type: String
Length Constraints: Maximum length of 10000.
Pattern: `[\s\S]*`
Required: No

 ** lastHealthPingTime **   <a name="DiscServ-Type-AgentInfo-lastHealthPingTime"></a>
Time since agent health was reported.
Type: String
Length Constraints: Maximum length of 10000.
Pattern: `[\s\S]*`
Required: No

 ** registeredTime **   <a name="DiscServ-Type-AgentInfo-registeredTime"></a>
Agent's first registration timestamp in UTC.
Type: String
Length Constraints: Maximum length of 10000.
Pattern: `[\s\S]*`
Required: No

 ** version **   <a name="DiscServ-Type-AgentInfo-version"></a>
The agent or collector version.
Type: String
Length Constraints: Maximum length of 10000.
Pattern: `[\s\S]*`
Required: No

## See Also
<a name="API_AgentInfo_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/discovery-2015-11-01/AgentInfo)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/discovery-2015-11-01/AgentInfo)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/discovery-2015-11-01/AgentInfo)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Application Discovery Service. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query application-discovery` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
