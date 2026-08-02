---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-ec2-vpnconnection-cloudwatchlogoptionsspecification.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::EC2::VPNConnection CloudwatchLogOptionsSpecification
<a name="aws-properties-ec2-vpnconnection-cloudwatchlogoptionsspecification"></a>

Options for sending VPN tunnel logs to CloudWatch.

## Syntax
<a name="aws-properties-ec2-vpnconnection-cloudwatchlogoptionsspecification-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-ec2-vpnconnection-cloudwatchlogoptionsspecification-syntax.json"></a>

```
{
  "[BgpLogEnabled](#cfn-ec2-vpnconnection-cloudwatchlogoptionsspecification-bgplogenabled)" : {{Boolean}},
  "[BgpLogGroupArn](#cfn-ec2-vpnconnection-cloudwatchlogoptionsspecification-bgploggrouparn)" : {{String}},
  "[BgpLogOutputFormat](#cfn-ec2-vpnconnection-cloudwatchlogoptionsspecification-bgplogoutputformat)" : {{String}},
  "[LogEnabled](#cfn-ec2-vpnconnection-cloudwatchlogoptionsspecification-logenabled)" : {{Boolean}},
  "[LogGroupArn](#cfn-ec2-vpnconnection-cloudwatchlogoptionsspecification-loggrouparn)" : {{String}},
  "[LogOutputFormat](#cfn-ec2-vpnconnection-cloudwatchlogoptionsspecification-logoutputformat)" : {{String}}
}
```

### YAML
<a name="aws-properties-ec2-vpnconnection-cloudwatchlogoptionsspecification-syntax.yaml"></a>

```
  [BgpLogEnabled](#cfn-ec2-vpnconnection-cloudwatchlogoptionsspecification-bgplogenabled): {{Boolean}}
  [BgpLogGroupArn](#cfn-ec2-vpnconnection-cloudwatchlogoptionsspecification-bgploggrouparn): {{String}}
  [BgpLogOutputFormat](#cfn-ec2-vpnconnection-cloudwatchlogoptionsspecification-bgplogoutputformat): {{String}}
  [LogEnabled](#cfn-ec2-vpnconnection-cloudwatchlogoptionsspecification-logenabled): {{Boolean}}
  [LogGroupArn](#cfn-ec2-vpnconnection-cloudwatchlogoptionsspecification-loggrouparn): {{String}}
  [LogOutputFormat](#cfn-ec2-vpnconnection-cloudwatchlogoptionsspecification-logoutputformat): {{String}}
```

## Properties
<a name="aws-properties-ec2-vpnconnection-cloudwatchlogoptionsspecification-properties"></a>

`BgpLogEnabled`  <a name="cfn-ec2-vpnconnection-cloudwatchlogoptionsspecification-bgplogenabled"></a>
Specifies whether to enable BGP logging for the VPN connection. Default value is `False`.
Valid values: `True` \| `False`
*Required*: No
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`BgpLogGroupArn`  <a name="cfn-ec2-vpnconnection-cloudwatchlogoptionsspecification-bgploggrouparn"></a>
The Amazon Resource Name (ARN) of the CloudWatch log group where BGP logs will be sent.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`BgpLogOutputFormat`  <a name="cfn-ec2-vpnconnection-cloudwatchlogoptionsspecification-bgplogoutputformat"></a>
The desired output format for BGP logs to be sent to CloudWatch. Default format is `json`.
Valid values: `json` \| `text`
*Required*: No
*Type*: String
*Allowed values*: `json | text`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`LogEnabled`  <a name="cfn-ec2-vpnconnection-cloudwatchlogoptionsspecification-logenabled"></a>
Enable or disable VPN tunnel logging feature. Default value is `False`.
Valid values: `True` \| `False`
*Required*: No
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`LogGroupArn`  <a name="cfn-ec2-vpnconnection-cloudwatchlogoptionsspecification-loggrouparn"></a>
The Amazon Resource Name (ARN) of the CloudWatch log group to send logs to.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`LogOutputFormat`  <a name="cfn-ec2-vpnconnection-cloudwatchlogoptionsspecification-logoutputformat"></a>
Set log format. Default format is `json`.
Valid values: `json` \| `text`
*Required*: No
*Type*: String
*Allowed values*: `json | text`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
