---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-iotwireless-wirelessdevice-abpv11.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::IoTWireless::WirelessDevice AbpV11
<a name="aws-properties-iotwireless-wirelessdevice-abpv11"></a>

ABP device object for create APIs for v1.1.

## Syntax
<a name="aws-properties-iotwireless-wirelessdevice-abpv11-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-iotwireless-wirelessdevice-abpv11-syntax.json"></a>

```
{
  "[DevAddr](#cfn-iotwireless-wirelessdevice-abpv11-devaddr)" : {{String}},
  "[SessionKeys](#cfn-iotwireless-wirelessdevice-abpv11-sessionkeys)" : {{SessionKeysAbpV11}}
}
```

### YAML
<a name="aws-properties-iotwireless-wirelessdevice-abpv11-syntax.yaml"></a>

```
  [DevAddr](#cfn-iotwireless-wirelessdevice-abpv11-devaddr): {{String}}
  [SessionKeys](#cfn-iotwireless-wirelessdevice-abpv11-sessionkeys): {{
    SessionKeysAbpV11}}
```

## Properties
<a name="aws-properties-iotwireless-wirelessdevice-abpv11-properties"></a>

`DevAddr`  <a name="cfn-iotwireless-wirelessdevice-abpv11-devaddr"></a>
The DevAddr value.
*Required*: Yes
*Type*: String
*Pattern*: `[a-fA-F0-9]{8}`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SessionKeys`  <a name="cfn-iotwireless-wirelessdevice-abpv11-sessionkeys"></a>
Session keys for ABP v1.1.
*Required*: Yes
*Type*: [SessionKeysAbpV11](aws-properties-iotwireless-wirelessdevice-sessionkeysabpv11.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
