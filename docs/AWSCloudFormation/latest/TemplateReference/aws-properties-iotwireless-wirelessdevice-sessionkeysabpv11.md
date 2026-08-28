---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-iotwireless-wirelessdevice-sessionkeysabpv11.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::IoTWireless::WirelessDevice SessionKeysAbpV11
<a name="aws-properties-iotwireless-wirelessdevice-sessionkeysabpv11"></a>

Session keys for ABP v1.1.

## Syntax
<a name="aws-properties-iotwireless-wirelessdevice-sessionkeysabpv11-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-iotwireless-wirelessdevice-sessionkeysabpv11-syntax.json"></a>

```
{
  "[AppSKey](#cfn-iotwireless-wirelessdevice-sessionkeysabpv11-appskey)" : {{String}},
  "[FNwkSIntKey](#cfn-iotwireless-wirelessdevice-sessionkeysabpv11-fnwksintkey)" : {{String}},
  "[NwkSEncKey](#cfn-iotwireless-wirelessdevice-sessionkeysabpv11-nwksenckey)" : {{String}},
  "[SNwkSIntKey](#cfn-iotwireless-wirelessdevice-sessionkeysabpv11-snwksintkey)" : {{String}}
}
```

### YAML
<a name="aws-properties-iotwireless-wirelessdevice-sessionkeysabpv11-syntax.yaml"></a>

```
  [AppSKey](#cfn-iotwireless-wirelessdevice-sessionkeysabpv11-appskey): {{String}}
  [FNwkSIntKey](#cfn-iotwireless-wirelessdevice-sessionkeysabpv11-fnwksintkey): {{String}}
  [NwkSEncKey](#cfn-iotwireless-wirelessdevice-sessionkeysabpv11-nwksenckey): {{String}}
  [SNwkSIntKey](#cfn-iotwireless-wirelessdevice-sessionkeysabpv11-snwksintkey): {{String}}
```

## Properties
<a name="aws-properties-iotwireless-wirelessdevice-sessionkeysabpv11-properties"></a>

`AppSKey`  <a name="cfn-iotwireless-wirelessdevice-sessionkeysabpv11-appskey"></a>
The AppSKey is a secret key, which you should handle in a similar way as you would an application password. You can protect the AppSKey value by storing it in the AWS Secrets Manager and use the [secretsmanager](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/dynamic-references.html#dynamic-references-secretsmanager) to reference this value.
*Required*: Yes
*Type*: String
*Pattern*: `[a-fA-F0-9]{32}`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`FNwkSIntKey`  <a name="cfn-iotwireless-wirelessdevice-sessionkeysabpv11-fnwksintkey"></a>
The FNwkSIntKey is a secret key, which you should handle in a similar way as you would an application password. You can protect the FNwkSIntKey value by storing it in the AWS Secrets Manager and use the [secretsmanager](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/dynamic-references.html#dynamic-references-secretsmanager) to reference this value.
*Required*: Yes
*Type*: String
*Pattern*: `[a-fA-F0-9]{32}`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`NwkSEncKey`  <a name="cfn-iotwireless-wirelessdevice-sessionkeysabpv11-nwksenckey"></a>
The NwkSEncKey is a secret key, which you should handle in a similar way as you would an application password. You can protect the NwkSEncKey value by storing it in the AWS Secrets Manager and use the [secretsmanager](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/dynamic-references.html#dynamic-references-secretsmanager) to reference this value.
*Required*: Yes
*Type*: String
*Pattern*: `[a-fA-F0-9]{32}`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SNwkSIntKey`  <a name="cfn-iotwireless-wirelessdevice-sessionkeysabpv11-snwksintkey"></a>
The SNwkSIntKey is a secret key, which you should handle in a similar way as you would an application password. You can protect the SNwkSIntKey value by storing it in the AWS Secrets Manager and use the [secretsmanager](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/dynamic-references.html#dynamic-references-secretsmanager) to reference this value.
*Required*: Yes
*Type*: String
*Pattern*: `[a-fA-F0-9]{32}`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
