---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-gamelift-fleet-playergatewayconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::GameLift::Fleet PlayerGatewayConfiguration
<a name="aws-properties-gamelift-fleet-playergatewayconfiguration"></a>

Configuration settings for player gateway. Use these settings to specify advanced options for how player gateway handles connections.

## Syntax
<a name="aws-properties-gamelift-fleet-playergatewayconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-gamelift-fleet-playergatewayconfiguration-syntax.json"></a>

```
{
  "[GameServerIpProtocolSupported](#cfn-gamelift-fleet-playergatewayconfiguration-gameserveripprotocolsupported)" : {{String}}
}
```

### YAML
<a name="aws-properties-gamelift-fleet-playergatewayconfiguration-syntax.yaml"></a>

```
  [GameServerIpProtocolSupported](#cfn-gamelift-fleet-playergatewayconfiguration-gameserveripprotocolsupported): {{String}}
```

## Properties
<a name="aws-properties-gamelift-fleet-playergatewayconfiguration-properties"></a>

`GameServerIpProtocolSupported`  <a name="cfn-gamelift-fleet-playergatewayconfiguration-gameserveripprotocolsupported"></a>
The IP protocol that your game servers support for player connections through player gateway. If the value is set to `IPv4`, GameLift will install and execute a lightweight IP translation software on fleet instances to receive and transform incoming IPv6 traffic to IPv4. If the value is set to `DUAL_STACK`, the lightweight IP translation software will not be installed on fleet instances. `DUAL_STACK` provides slightly better performance than `IPv4`.
*Required*: No
*Type*: String
*Allowed values*: `IPv4 | DUAL_STACK`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
