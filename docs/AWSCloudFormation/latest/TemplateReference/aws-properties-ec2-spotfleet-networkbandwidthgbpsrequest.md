---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-ec2-spotfleet-networkbandwidthgbpsrequest.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::EC2::SpotFleet NetworkBandwidthGbpsRequest
<a name="aws-properties-ec2-spotfleet-networkbandwidthgbpsrequest"></a>

The minimum and maximum amount of baseline network bandwidth, in gigabits per second (Gbps). For more information, see [Amazon EC2 instance network bandwidth](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-instance-network-bandwidth.html) in the *Amazon EC2 User Guide*.

Default: No minimum or maximum limits

## Syntax
<a name="aws-properties-ec2-spotfleet-networkbandwidthgbpsrequest-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-ec2-spotfleet-networkbandwidthgbpsrequest-syntax.json"></a>

```
{
  "[Max](#cfn-ec2-spotfleet-networkbandwidthgbpsrequest-max)" : {{Number}},
  "[Min](#cfn-ec2-spotfleet-networkbandwidthgbpsrequest-min)" : {{Number}}
}
```

### YAML
<a name="aws-properties-ec2-spotfleet-networkbandwidthgbpsrequest-syntax.yaml"></a>

```
  [Max](#cfn-ec2-spotfleet-networkbandwidthgbpsrequest-max): {{Number}}
  [Min](#cfn-ec2-spotfleet-networkbandwidthgbpsrequest-min): {{Number}}
```

## Properties
<a name="aws-properties-ec2-spotfleet-networkbandwidthgbpsrequest-properties"></a>

`Max`  <a name="cfn-ec2-spotfleet-networkbandwidthgbpsrequest-max"></a>
The maximum amount of network bandwidth, in Gbps. To specify no maximum limit, omit this parameter.
*Required*: No
*Type*: Number
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Min`  <a name="cfn-ec2-spotfleet-networkbandwidthgbpsrequest-min"></a>
The minimum amount of network bandwidth, in Gbps. To specify no minimum limit, omit this parameter.
*Required*: No
*Type*: Number
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
