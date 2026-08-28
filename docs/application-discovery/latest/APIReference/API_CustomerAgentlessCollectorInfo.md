---
source_url: https://docs.aws.amazon.com/application-discovery/latest/APIReference/API_CustomerAgentlessCollectorInfo.html
---

# CustomerAgentlessCollectorInfo
<a name="API_CustomerAgentlessCollectorInfo"></a>

**Important**
 AWS Application Discovery Service is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see [AWS Application Discovery Service availability change](https://docs.aws.amazon.com/application-discovery/latest/userguide/application-discovery-service-availability-change.html).

The inventory data for installed Agentless Collector collectors.

## Contents
<a name="API_CustomerAgentlessCollectorInfo_Contents"></a>

 ** activeAgentlessCollectors **   <a name="DiscServ-Type-CustomerAgentlessCollectorInfo-activeAgentlessCollectors"></a>
The number of active Agentless Collector collectors.
Type: Integer
Required: Yes

 ** denyListedAgentlessCollectors **   <a name="DiscServ-Type-CustomerAgentlessCollectorInfo-denyListedAgentlessCollectors"></a>
The number of deny-listed Agentless Collector collectors.
Type: Integer
Required: Yes

 ** healthyAgentlessCollectors **   <a name="DiscServ-Type-CustomerAgentlessCollectorInfo-healthyAgentlessCollectors"></a>
The number of healthy Agentless Collector collectors.
Type: Integer
Required: Yes

 ** shutdownAgentlessCollectors **   <a name="DiscServ-Type-CustomerAgentlessCollectorInfo-shutdownAgentlessCollectors"></a>
The number of Agentless Collector collectors with `SHUTDOWN` status.
Type: Integer
Required: Yes

 ** totalAgentlessCollectors **   <a name="DiscServ-Type-CustomerAgentlessCollectorInfo-totalAgentlessCollectors"></a>
 The total number of Agentless Collector collectors.
Type: Integer
Required: Yes

 ** unhealthyAgentlessCollectors **   <a name="DiscServ-Type-CustomerAgentlessCollectorInfo-unhealthyAgentlessCollectors"></a>
 The number of unhealthy Agentless Collector collectors.
Type: Integer
Required: Yes

 ** unknownAgentlessCollectors **   <a name="DiscServ-Type-CustomerAgentlessCollectorInfo-unknownAgentlessCollectors"></a>
 The number of unknown Agentless Collector collectors.
Type: Integer
Required: Yes

## See Also
<a name="API_CustomerAgentlessCollectorInfo_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/discovery-2015-11-01/CustomerAgentlessCollectorInfo)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/discovery-2015-11-01/CustomerAgentlessCollectorInfo)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/discovery-2015-11-01/CustomerAgentlessCollectorInfo)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Application Discovery Service. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query application-discovery` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
