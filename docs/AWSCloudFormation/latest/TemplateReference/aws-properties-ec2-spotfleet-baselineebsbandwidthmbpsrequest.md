---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-ec2-spotfleet-baselineebsbandwidthmbpsrequest.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::EC2::SpotFleet BaselineEbsBandwidthMbpsRequest
<a name="aws-properties-ec2-spotfleet-baselineebsbandwidthmbpsrequest"></a>

The minimum and maximum baseline bandwidth to Amazon EBS, in Mbps. For more information, see [Amazon EBS–optimized instances](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ebs-optimized.html) in the *Amazon EC2 User Guide*.

## Syntax
<a name="aws-properties-ec2-spotfleet-baselineebsbandwidthmbpsrequest-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-ec2-spotfleet-baselineebsbandwidthmbpsrequest-syntax.json"></a>

```
{
  "[Max](#cfn-ec2-spotfleet-baselineebsbandwidthmbpsrequest-max)" : {{Integer}},
  "[Min](#cfn-ec2-spotfleet-baselineebsbandwidthmbpsrequest-min)" : {{Integer}}
}
```

### YAML
<a name="aws-properties-ec2-spotfleet-baselineebsbandwidthmbpsrequest-syntax.yaml"></a>

```
  [Max](#cfn-ec2-spotfleet-baselineebsbandwidthmbpsrequest-max): {{Integer}}
  [Min](#cfn-ec2-spotfleet-baselineebsbandwidthmbpsrequest-min): {{Integer}}
```

## Properties
<a name="aws-properties-ec2-spotfleet-baselineebsbandwidthmbpsrequest-properties"></a>

`Max`  <a name="cfn-ec2-spotfleet-baselineebsbandwidthmbpsrequest-max"></a>
The maximum baseline bandwidth, in Mbps. To specify no maximum limit, omit this parameter.
*Required*: No
*Type*: Integer
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Min`  <a name="cfn-ec2-spotfleet-baselineebsbandwidthmbpsrequest-min"></a>
The minimum baseline bandwidth, in Mbps. To specify no minimum limit, omit this parameter.
*Required*: No
*Type*: Integer
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
