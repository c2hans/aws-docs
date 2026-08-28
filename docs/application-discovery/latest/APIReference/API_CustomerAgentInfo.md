---
source_url: https://docs.aws.amazon.com/application-discovery/latest/APIReference/API_CustomerAgentInfo.html
---

# CustomerAgentInfo
<a name="API_CustomerAgentInfo"></a>

Inventory data for installed discovery agents.

## Contents
<a name="API_CustomerAgentInfo_Contents"></a>

 ** activeAgents **   <a name="DiscServ-Type-CustomerAgentInfo-activeAgents"></a>
Number of active discovery agents.
Type: Integer
Required: Yes

 ** blackListedAgents **   <a name="DiscServ-Type-CustomerAgentInfo-blackListedAgents"></a>
Number of blacklisted discovery agents.
Type: Integer
Required: Yes

 ** healthyAgents **   <a name="DiscServ-Type-CustomerAgentInfo-healthyAgents"></a>
Number of healthy discovery agents
Type: Integer
Required: Yes

 ** shutdownAgents **   <a name="DiscServ-Type-CustomerAgentInfo-shutdownAgents"></a>
Number of discovery agents with status SHUTDOWN.
Type: Integer
Required: Yes

 ** totalAgents **   <a name="DiscServ-Type-CustomerAgentInfo-totalAgents"></a>
Total number of discovery agents.
Type: Integer
Required: Yes

 ** unhealthyAgents **   <a name="DiscServ-Type-CustomerAgentInfo-unhealthyAgents"></a>
Number of unhealthy discovery agents.
Type: Integer
Required: Yes

 ** unknownAgents **   <a name="DiscServ-Type-CustomerAgentInfo-unknownAgents"></a>
Number of unknown discovery agents.
Type: Integer
Required: Yes

## See Also
<a name="API_CustomerAgentInfo_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/discovery-2015-11-01/CustomerAgentInfo)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/discovery-2015-11-01/CustomerAgentInfo)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/discovery-2015-11-01/CustomerAgentInfo)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Application Discovery Service. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query application-discovery` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
