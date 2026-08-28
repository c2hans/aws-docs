---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-mediaconnect-flowoutput-destinationconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::MediaConnect::FlowOutput DestinationConfiguration
<a name="aws-properties-mediaconnect-flowoutput-destinationconfiguration"></a>

 The transport parameters that you want to associate with an outbound media stream.

## Syntax
<a name="aws-properties-mediaconnect-flowoutput-destinationconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-mediaconnect-flowoutput-destinationconfiguration-syntax.json"></a>

```
{
  "[DestinationIp](#cfn-mediaconnect-flowoutput-destinationconfiguration-destinationip)" : {{String}},
  "[DestinationPort](#cfn-mediaconnect-flowoutput-destinationconfiguration-destinationport)" : {{Integer}},
  "[Interface](#cfn-mediaconnect-flowoutput-destinationconfiguration-interface)" : {{Interface}}
}
```

### YAML
<a name="aws-properties-mediaconnect-flowoutput-destinationconfiguration-syntax.yaml"></a>

```
  [DestinationIp](#cfn-mediaconnect-flowoutput-destinationconfiguration-destinationip): {{String}}
  [DestinationPort](#cfn-mediaconnect-flowoutput-destinationconfiguration-destinationport): {{Integer}}
  [Interface](#cfn-mediaconnect-flowoutput-destinationconfiguration-interface): {{
    Interface}}
```

## Properties
<a name="aws-properties-mediaconnect-flowoutput-destinationconfiguration-properties"></a>

`DestinationIp`  <a name="cfn-mediaconnect-flowoutput-destinationconfiguration-destinationip"></a>
The IP address where you want MediaConnect to send contents of the media stream.
*Required*: Yes
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`DestinationPort`  <a name="cfn-mediaconnect-flowoutput-destinationconfiguration-destinationport"></a>
 The port that you want MediaConnect to use when it distributes the media stream to the output.
*Required*: Yes
*Type*: Integer
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Interface`  <a name="cfn-mediaconnect-flowoutput-destinationconfiguration-interface"></a>
 The VPC interface that you want to use for the media stream associated with the output.
*Required*: Yes
*Type*: [Interface](aws-properties-mediaconnect-flowoutput-interface.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
