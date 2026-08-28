---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-mediaconnect-routerinput-failoverrouterinputconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::MediaConnect::RouterInput FailoverRouterInputConfiguration
<a name="aws-properties-mediaconnect-routerinput-failoverrouterinputconfiguration"></a>

Configuration settings for a failover router input that allows switching between two input sources.

## Syntax
<a name="aws-properties-mediaconnect-routerinput-failoverrouterinputconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-mediaconnect-routerinput-failoverrouterinputconfiguration-syntax.json"></a>

```
{
  "[NetworkInterfaceArn](#cfn-mediaconnect-routerinput-failoverrouterinputconfiguration-networkinterfacearn)" : {{String}},
  "[PrimarySourceIndex](#cfn-mediaconnect-routerinput-failoverrouterinputconfiguration-primarysourceindex)" : {{Integer}},
  "[ProtocolConfigurations](#cfn-mediaconnect-routerinput-failoverrouterinputconfiguration-protocolconfigurations)" : {{[ FailoverRouterInputProtocolConfiguration, ... ]}},
  "[SourcePriorityMode](#cfn-mediaconnect-routerinput-failoverrouterinputconfiguration-sourceprioritymode)" : {{String}}
}
```

### YAML
<a name="aws-properties-mediaconnect-routerinput-failoverrouterinputconfiguration-syntax.yaml"></a>

```
  [NetworkInterfaceArn](#cfn-mediaconnect-routerinput-failoverrouterinputconfiguration-networkinterfacearn): {{String}}
  [PrimarySourceIndex](#cfn-mediaconnect-routerinput-failoverrouterinputconfiguration-primarysourceindex): {{Integer}}
  [ProtocolConfigurations](#cfn-mediaconnect-routerinput-failoverrouterinputconfiguration-protocolconfigurations): {{
    - FailoverRouterInputProtocolConfiguration}}
  [SourcePriorityMode](#cfn-mediaconnect-routerinput-failoverrouterinputconfiguration-sourceprioritymode): {{String}}
```

## Properties
<a name="aws-properties-mediaconnect-routerinput-failoverrouterinputconfiguration-properties"></a>

`NetworkInterfaceArn`  <a name="cfn-mediaconnect-routerinput-failoverrouterinputconfiguration-networkinterfacearn"></a>
The ARN of the network interface to use for this failover router input.
*Required*: Yes
*Type*: String
*Pattern*: `^arn:(aws[a-zA-Z-]*):mediaconnect:[a-z0-9-]+:[0-9]{12}:routerNetworkInterface:[a-z0-9]{12}$`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`PrimarySourceIndex`  <a name="cfn-mediaconnect-routerinput-failoverrouterinputconfiguration-primarysourceindex"></a>
The index (0 or 1) that specifies which source in the protocol configurations list is currently active. Used to control which of the two failover sources is currently selected. This field is ignored when sourcePriorityMode is set to NO\_PRIORITY
*Required*: No
*Type*: Integer
*Minimum*: `0`
*Maximum*: `1`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ProtocolConfigurations`  <a name="cfn-mediaconnect-routerinput-failoverrouterinputconfiguration-protocolconfigurations"></a>
A list of exactly two protocol configurations for the failover input sources. Both must use the same protocol type.
*Required*: Yes
*Type*: Array of [FailoverRouterInputProtocolConfiguration](aws-properties-mediaconnect-routerinput-failoverrouterinputprotocolconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SourcePriorityMode`  <a name="cfn-mediaconnect-routerinput-failoverrouterinputconfiguration-sourceprioritymode"></a>
The mode for determining source priority in failover configurations.
*Required*: Yes
*Type*: String
*Allowed values*: `NO_PRIORITY | PRIMARY_SECONDARY`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
