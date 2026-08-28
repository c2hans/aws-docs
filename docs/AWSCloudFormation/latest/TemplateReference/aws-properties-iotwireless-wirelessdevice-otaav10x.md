---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-iotwireless-wirelessdevice-otaav10x.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::IoTWireless::WirelessDevice OtaaV10x
<a name="aws-properties-iotwireless-wirelessdevice-otaav10x"></a>

OTAA device object for v1.0.x

## Syntax
<a name="aws-properties-iotwireless-wirelessdevice-otaav10x-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-iotwireless-wirelessdevice-otaav10x-syntax.json"></a>

```
{
  "[AppEui](#cfn-iotwireless-wirelessdevice-otaav10x-appeui)" : {{String}},
  "[AppKey](#cfn-iotwireless-wirelessdevice-otaav10x-appkey)" : {{String}}
}
```

### YAML
<a name="aws-properties-iotwireless-wirelessdevice-otaav10x-syntax.yaml"></a>

```
  [AppEui](#cfn-iotwireless-wirelessdevice-otaav10x-appeui): {{String}}
  [AppKey](#cfn-iotwireless-wirelessdevice-otaav10x-appkey): {{String}}
```

## Properties
<a name="aws-properties-iotwireless-wirelessdevice-otaav10x-properties"></a>

`AppEui`  <a name="cfn-iotwireless-wirelessdevice-otaav10x-appeui"></a>
The AppEUI value. You specify this value when using LoRaWAN versions v1.0.2 or v1.0.3.
*Required*: Yes
*Type*: String
*Pattern*: `[a-fA-F0-9]{16}`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`AppKey`  <a name="cfn-iotwireless-wirelessdevice-otaav10x-appkey"></a>
The AppKey value.
*Required*: Yes
*Type*: String
*Pattern*: `[a-fA-F0-9]{32}`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
