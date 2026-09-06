---
source_url: https://docs.aws.amazon.com/systems-manager/latest/APIReference/API_NodeAggregator.html
---

# NodeAggregator
<a name="API_NodeAggregator"></a>

One or more aggregators for viewing counts of nodes using different dimensions.

## Contents
<a name="API_NodeAggregator_Contents"></a>

 ** AggregatorType **   <a name="systemsmanager-Type-NodeAggregator-AggregatorType"></a>
The aggregator type for limiting a node summary. Currently, only `Count` is supported.
Type: String
Valid Values: `Count`
Required: Yes

 ** AttributeName **   <a name="systemsmanager-Type-NodeAggregator-AttributeName"></a>
The name of a node attribute on which to limit the count of nodes.
Type: String
Valid Values: `AgentVersion | PlatformName | PlatformType | PlatformVersion | Region | ResourceType | SourceType | AvailabilityZone`
Required: Yes

 ** TypeName **   <a name="systemsmanager-Type-NodeAggregator-TypeName"></a>
The data type name to use for viewing counts of nodes. Currently, only `Instance` is supported.
Type: String
Valid Values: `Instance`
Required: Yes

 ** Aggregators **   <a name="systemsmanager-Type-NodeAggregator-Aggregators"></a>
Information about aggregators used to refine a node summary.
Type: Array of [NodeAggregator](#API_NodeAggregator) objects
Array Members: Minimum number of 1 item. Maximum number of 2 items.
Required: No

## See Also
<a name="API_NodeAggregator_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ssm-2014-11-06/NodeAggregator)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ssm-2014-11-06/NodeAggregator)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ssm-2014-11-06/NodeAggregator)
