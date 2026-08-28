---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-mediaconnect-routerinput-mergerouterinputconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::MediaConnect::RouterInput MergeRouterInputConfiguration
<a name="aws-properties-mediaconnect-routerinput-mergerouterinputconfiguration"></a>

Configuration settings for a merge router input that combines two input sources.

## Syntax
<a name="aws-properties-mediaconnect-routerinput-mergerouterinputconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-mediaconnect-routerinput-mergerouterinputconfiguration-syntax.json"></a>

```
{
  "[MergeRecoveryWindowMilliseconds](#cfn-mediaconnect-routerinput-mergerouterinputconfiguration-mergerecoverywindowmilliseconds)" : {{Integer}},
  "[NetworkInterfaceArn](#cfn-mediaconnect-routerinput-mergerouterinputconfiguration-networkinterfacearn)" : {{String}},
  "[ProtocolConfigurations](#cfn-mediaconnect-routerinput-mergerouterinputconfiguration-protocolconfigurations)" : {{[ MergeRouterInputProtocolConfiguration, ... ]}}
}
```

### YAML
<a name="aws-properties-mediaconnect-routerinput-mergerouterinputconfiguration-syntax.yaml"></a>

```
  [MergeRecoveryWindowMilliseconds](#cfn-mediaconnect-routerinput-mergerouterinputconfiguration-mergerecoverywindowmilliseconds): {{Integer}}
  [NetworkInterfaceArn](#cfn-mediaconnect-routerinput-mergerouterinputconfiguration-networkinterfacearn): {{String}}
  [ProtocolConfigurations](#cfn-mediaconnect-routerinput-mergerouterinputconfiguration-protocolconfigurations): {{
    - MergeRouterInputProtocolConfiguration}}
```

## Properties
<a name="aws-properties-mediaconnect-routerinput-mergerouterinputconfiguration-properties"></a>

`MergeRecoveryWindowMilliseconds`  <a name="cfn-mediaconnect-routerinput-mergerouterinputconfiguration-mergerecoverywindowmilliseconds"></a>
The time window in milliseconds for merging the two input sources.
*Required*: Yes
*Type*: Integer
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`NetworkInterfaceArn`  <a name="cfn-mediaconnect-routerinput-mergerouterinputconfiguration-networkinterfacearn"></a>
The ARN of the network interface to use for this merge router input.
*Required*: Yes
*Type*: String
*Pattern*: `^arn:(aws[a-zA-Z-]*):mediaconnect:[a-z0-9-]+:[0-9]{12}:routerNetworkInterface:[a-z0-9]{12}$`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ProtocolConfigurations`  <a name="cfn-mediaconnect-routerinput-mergerouterinputconfiguration-protocolconfigurations"></a>
A list of exactly two protocol configurations for the merge input sources. Both must use the same protocol type.
*Required*: Yes
*Type*: Array of [MergeRouterInputProtocolConfiguration](aws-properties-mediaconnect-routerinput-mergerouterinputprotocolconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
