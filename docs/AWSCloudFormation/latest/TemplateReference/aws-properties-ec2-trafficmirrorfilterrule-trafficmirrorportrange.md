---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-ec2-trafficmirrorfilterrule-trafficmirrorportrange.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::EC2::TrafficMirrorFilterRule TrafficMirrorPortRange
<a name="aws-properties-ec2-trafficmirrorfilterrule-trafficmirrorportrange"></a>

Describes the Traffic Mirror port range.

## Syntax
<a name="aws-properties-ec2-trafficmirrorfilterrule-trafficmirrorportrange-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-ec2-trafficmirrorfilterrule-trafficmirrorportrange-syntax.json"></a>

```
{
  "[FromPort](#cfn-ec2-trafficmirrorfilterrule-trafficmirrorportrange-fromport)" : {{Integer}},
  "[ToPort](#cfn-ec2-trafficmirrorfilterrule-trafficmirrorportrange-toport)" : {{Integer}}
}
```

### YAML
<a name="aws-properties-ec2-trafficmirrorfilterrule-trafficmirrorportrange-syntax.yaml"></a>

```
  [FromPort](#cfn-ec2-trafficmirrorfilterrule-trafficmirrorportrange-fromport): {{Integer}}
  [ToPort](#cfn-ec2-trafficmirrorfilterrule-trafficmirrorportrange-toport): {{Integer}}
```

## Properties
<a name="aws-properties-ec2-trafficmirrorfilterrule-trafficmirrorportrange-properties"></a>

`FromPort`  <a name="cfn-ec2-trafficmirrorfilterrule-trafficmirrorportrange-fromport"></a>
The start of the Traffic Mirror port range. This applies to the TCP and UDP protocols.
*Required*: Yes
*Type*: Integer
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ToPort`  <a name="cfn-ec2-trafficmirrorfilterrule-trafficmirrorportrange-toport"></a>
The end of the Traffic Mirror port range. This applies to the TCP and UDP protocols.
*Required*: Yes
*Type*: Integer
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
