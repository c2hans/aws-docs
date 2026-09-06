---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-ec2-launchtemplate-networkbandwidthgbps.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::EC2::LaunchTemplate NetworkBandwidthGbps
<a name="aws-properties-ec2-launchtemplate-networkbandwidthgbps"></a>

The minimum and maximum amount of network bandwidth, in gigabits per second (Gbps).

**Note**
Setting the minimum bandwidth does not guarantee that your instance will achieve the minimum bandwidth. Amazon EC2 will identify instance types that support the specified minimum bandwidth, but the actual bandwidth of your instance might go below the specified minimum at times. For more information, see [Available instance bandwidth](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-instance-network-bandwidth.html#available-instance-bandwidth) in the *Amazon EC2 User Guide*.

## Syntax
<a name="aws-properties-ec2-launchtemplate-networkbandwidthgbps-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-ec2-launchtemplate-networkbandwidthgbps-syntax.json"></a>

```
{
  "[Max](#cfn-ec2-launchtemplate-networkbandwidthgbps-max)" : {{Number}},
  "[Min](#cfn-ec2-launchtemplate-networkbandwidthgbps-min)" : {{Number}}
}
```

### YAML
<a name="aws-properties-ec2-launchtemplate-networkbandwidthgbps-syntax.yaml"></a>

```
  [Max](#cfn-ec2-launchtemplate-networkbandwidthgbps-max): {{Number}}
  [Min](#cfn-ec2-launchtemplate-networkbandwidthgbps-min): {{Number}}
```

## Properties
<a name="aws-properties-ec2-launchtemplate-networkbandwidthgbps-properties"></a>

`Max`  <a name="cfn-ec2-launchtemplate-networkbandwidthgbps-max"></a>
The maximum amount of network bandwidth, in Gbps. To specify no maximum limit, omit this parameter.
*Required*: No
*Type*: Number
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Min`  <a name="cfn-ec2-launchtemplate-networkbandwidthgbps-min"></a>
The minimum amount of network bandwidth, in Gbps. If this parameter is not specified, there is no minimum limit.
*Required*: No
*Type*: Number
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
