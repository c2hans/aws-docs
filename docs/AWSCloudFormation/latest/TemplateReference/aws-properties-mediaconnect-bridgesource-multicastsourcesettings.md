---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-mediaconnect-bridgesource-multicastsourcesettings.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::MediaConnect::BridgeSource MulticastSourceSettings
<a name="aws-properties-mediaconnect-bridgesource-multicastsourcesettings"></a>

The settings related to the multicast source.

## Syntax
<a name="aws-properties-mediaconnect-bridgesource-multicastsourcesettings-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-mediaconnect-bridgesource-multicastsourcesettings-syntax.json"></a>

```
{
  "[MulticastSourceIp](#cfn-mediaconnect-bridgesource-multicastsourcesettings-multicastsourceip)" : {{String}}
}
```

### YAML
<a name="aws-properties-mediaconnect-bridgesource-multicastsourcesettings-syntax.yaml"></a>

```
  [MulticastSourceIp](#cfn-mediaconnect-bridgesource-multicastsourcesettings-multicastsourceip): {{String}}
```

## Properties
<a name="aws-properties-mediaconnect-bridgesource-multicastsourcesettings-properties"></a>

`MulticastSourceIp`  <a name="cfn-mediaconnect-bridgesource-multicastsourcesettings-multicastsourceip"></a>
 The IP address of the source for source-specific multicast (SSM).
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
