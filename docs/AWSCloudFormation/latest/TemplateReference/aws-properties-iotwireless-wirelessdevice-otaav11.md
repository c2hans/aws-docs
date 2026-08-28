---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-iotwireless-wirelessdevice-otaav11.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::IoTWireless::WirelessDevice OtaaV11
<a name="aws-properties-iotwireless-wirelessdevice-otaav11"></a>

OTAA device object for v1.1 for create APIs.

## Syntax
<a name="aws-properties-iotwireless-wirelessdevice-otaav11-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-iotwireless-wirelessdevice-otaav11-syntax.json"></a>

```
{
  "[AppKey](#cfn-iotwireless-wirelessdevice-otaav11-appkey)" : {{String}},
  "[JoinEui](#cfn-iotwireless-wirelessdevice-otaav11-joineui)" : {{String}},
  "[NwkKey](#cfn-iotwireless-wirelessdevice-otaav11-nwkkey)" : {{String}}
}
```

### YAML
<a name="aws-properties-iotwireless-wirelessdevice-otaav11-syntax.yaml"></a>

```
  [AppKey](#cfn-iotwireless-wirelessdevice-otaav11-appkey): {{String}}
  [JoinEui](#cfn-iotwireless-wirelessdevice-otaav11-joineui): {{String}}
  [NwkKey](#cfn-iotwireless-wirelessdevice-otaav11-nwkkey): {{String}}
```

## Properties
<a name="aws-properties-iotwireless-wirelessdevice-otaav11-properties"></a>

`AppKey`  <a name="cfn-iotwireless-wirelessdevice-otaav11-appkey"></a>
The AppKey is a secret key, which you should handle in a similar way as you would an application password. You can protect the AppKey value by storing it in the AWS Secrets Manager and use the [secretsmanager](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/dynamic-references.html#dynamic-references-secretsmanager) to reference this value.
*Required*: Yes
*Type*: String
*Pattern*: `[a-fA-F0-9]{32}`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`JoinEui`  <a name="cfn-iotwireless-wirelessdevice-otaav11-joineui"></a>
The JoinEUI value.
*Required*: Yes
*Type*: String
*Pattern*: `[a-fA-F0-9]{16}`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`NwkKey`  <a name="cfn-iotwireless-wirelessdevice-otaav11-nwkkey"></a>
The NwkKey is a secret key, which you should handle in a similar way as you would an application password. You can protect the NwkKey value by storing it in the AWS Secrets Manager and use the [secretsmanager](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/dynamic-references.html#dynamic-references-secretsmanager) to reference this value.
*Required*: Yes
*Type*: String
*Pattern*: `[a-fA-F0-9]{32}`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
