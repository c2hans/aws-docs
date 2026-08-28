---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-ec2-ec2fleet-networkbandwidthgbpsrequest.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::EC2::EC2Fleet NetworkBandwidthGbpsRequest
<a name="aws-properties-ec2-ec2fleet-networkbandwidthgbpsrequest"></a>

The minimum and maximum amount of network bandwidth, in gigabits per second (Gbps).

**Note**
Setting the minimum bandwidth does not guarantee that your instance will achieve the minimum bandwidth. Amazon EC2 will identify instance types that support the specified minimum bandwidth, but the actual bandwidth of your instance might go below the specified minimum at times. For more information, see [Available instance bandwidth](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-instance-network-bandwidth.html#available-instance-bandwidth) in the *Amazon EC2 User Guide*.

## Syntax
<a name="aws-properties-ec2-ec2fleet-networkbandwidthgbpsrequest-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-ec2-ec2fleet-networkbandwidthgbpsrequest-syntax.json"></a>

```
{
  "[Max](#cfn-ec2-ec2fleet-networkbandwidthgbpsrequest-max)" : {{Number}},
  "[Min](#cfn-ec2-ec2fleet-networkbandwidthgbpsrequest-min)" : {{Number}}
}
```

### YAML
<a name="aws-properties-ec2-ec2fleet-networkbandwidthgbpsrequest-syntax.yaml"></a>

```
  [Max](#cfn-ec2-ec2fleet-networkbandwidthgbpsrequest-max): {{Number}}
  [Min](#cfn-ec2-ec2fleet-networkbandwidthgbpsrequest-min): {{Number}}
```

## Properties
<a name="aws-properties-ec2-ec2fleet-networkbandwidthgbpsrequest-properties"></a>

`Max`  <a name="cfn-ec2-ec2fleet-networkbandwidthgbpsrequest-max"></a>
The maximum amount of network bandwidth, in Gbps. To specify no maximum limit, omit this parameter.
*Required*: No
*Type*: Number
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Min`  <a name="cfn-ec2-ec2fleet-networkbandwidthgbpsrequest-min"></a>
The minimum amount of network bandwidth, in Gbps. To specify no minimum limit, omit this parameter.
*Required*: No
*Type*: Number
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
