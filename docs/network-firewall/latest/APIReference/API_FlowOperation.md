---
source_url: https://docs.aws.amazon.com/network-firewall/latest/APIReference/API_FlowOperation.html
---

# FlowOperation
<a name="API_FlowOperation"></a>

Contains information about a flow operation, such as related statuses, unique identifiers, and all filters defined in the operation.

Flow operations let you manage the flows tracked in the flow table, also known as the firewall table.

A flow is network traffic that is monitored by a firewall, either by stateful or stateless rules. For traffic to be considered part of a flow, it must share Destination, DestinationPort, Direction, Protocol, Source, and SourcePort.

## Contents
<a name="API_FlowOperation_Contents"></a>

 ** FlowFilters **   <a name="networkfirewall-Type-FlowOperation-FlowFilters"></a>
Defines the scope a flow operation. You can use up to 20 filters to configure a single flow operation.
Type: Array of [FlowFilter](API_FlowFilter.md) objects
Required: No

 ** MinimumFlowAgeInSeconds **   <a name="networkfirewall-Type-FlowOperation-MinimumFlowAgeInSeconds"></a>
The reqested `FlowOperation` ignores flows with an age (in seconds) lower than `MinimumFlowAgeInSeconds`. You provide this for start commands.
Type: Integer
Required: No

## See Also
<a name="API_FlowOperation_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/network-firewall-2020-11-12/FlowOperation)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/network-firewall-2020-11-12/FlowOperation)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/network-firewall-2020-11-12/FlowOperation)
