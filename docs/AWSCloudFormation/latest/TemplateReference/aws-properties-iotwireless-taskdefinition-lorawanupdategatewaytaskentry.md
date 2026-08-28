---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-iotwireless-taskdefinition-lorawanupdategatewaytaskentry.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::IoTWireless::TaskDefinition LoRaWANUpdateGatewayTaskEntry
<a name="aws-properties-iotwireless-taskdefinition-lorawanupdategatewaytaskentry"></a>

LoRaWANUpdateGatewayTaskEntry object.

## Syntax
<a name="aws-properties-iotwireless-taskdefinition-lorawanupdategatewaytaskentry-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-iotwireless-taskdefinition-lorawanupdategatewaytaskentry-syntax.json"></a>

```
{
  "[CurrentVersion](#cfn-iotwireless-taskdefinition-lorawanupdategatewaytaskentry-currentversion)" : {{LoRaWANGatewayVersion}},
  "[UpdateVersion](#cfn-iotwireless-taskdefinition-lorawanupdategatewaytaskentry-updateversion)" : {{LoRaWANGatewayVersion}}
}
```

### YAML
<a name="aws-properties-iotwireless-taskdefinition-lorawanupdategatewaytaskentry-syntax.yaml"></a>

```
  [CurrentVersion](#cfn-iotwireless-taskdefinition-lorawanupdategatewaytaskentry-currentversion): {{
    LoRaWANGatewayVersion}}
  [UpdateVersion](#cfn-iotwireless-taskdefinition-lorawanupdategatewaytaskentry-updateversion): {{
    LoRaWANGatewayVersion}}
```

## Properties
<a name="aws-properties-iotwireless-taskdefinition-lorawanupdategatewaytaskentry-properties"></a>

`CurrentVersion`  <a name="cfn-iotwireless-taskdefinition-lorawanupdategatewaytaskentry-currentversion"></a>
The version of the gateways that should receive the update.
*Required*: No
*Type*: [LoRaWANGatewayVersion](aws-properties-iotwireless-taskdefinition-lorawangatewayversion.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`UpdateVersion`  <a name="cfn-iotwireless-taskdefinition-lorawanupdategatewaytaskentry-updateversion"></a>
The firmware version to update the gateway to.
*Required*: No
*Type*: [LoRaWANGatewayVersion](aws-properties-iotwireless-taskdefinition-lorawangatewayversion.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
