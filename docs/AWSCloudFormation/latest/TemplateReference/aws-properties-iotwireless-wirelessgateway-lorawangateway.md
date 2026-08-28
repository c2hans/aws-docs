---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-iotwireless-wirelessgateway-lorawangateway.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::IoTWireless::WirelessGateway LoRaWANGateway
<a name="aws-properties-iotwireless-wirelessgateway-lorawangateway"></a>

LoRaWAN wireless gateway object.

## Syntax
<a name="aws-properties-iotwireless-wirelessgateway-lorawangateway-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-iotwireless-wirelessgateway-lorawangateway-syntax.json"></a>

```
{
  "[GatewayEui](#cfn-iotwireless-wirelessgateway-lorawangateway-gatewayeui)" : {{String}},
  "[RfRegion](#cfn-iotwireless-wirelessgateway-lorawangateway-rfregion)" : {{String}}
}
```

### YAML
<a name="aws-properties-iotwireless-wirelessgateway-lorawangateway-syntax.yaml"></a>

```
  [GatewayEui](#cfn-iotwireless-wirelessgateway-lorawangateway-gatewayeui): {{String}}
  [RfRegion](#cfn-iotwireless-wirelessgateway-lorawangateway-rfregion): {{String}}
```

## Properties
<a name="aws-properties-iotwireless-wirelessgateway-lorawangateway-properties"></a>

`GatewayEui`  <a name="cfn-iotwireless-wirelessgateway-lorawangateway-gatewayeui"></a>
The gateway's EUI value.
*Required*: Yes
*Type*: String
*Pattern*: `^(([0-9A-Fa-f]{2}-){7}|([0-9A-Fa-f]{2}:){7}|([0-9A-Fa-f]{2}\s){7}|([0-9A-Fa-f]{2}){7})([0-9A-Fa-f]{2})$`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`RfRegion`  <a name="cfn-iotwireless-wirelessgateway-lorawangateway-rfregion"></a>
The frequency band (RFRegion) value.
*Required*: Yes
*Type*: String
*Maximum*: `64`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
