---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-ec2-verifiedaccessinstance-cloudwatchlogs.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::EC2::VerifiedAccessInstance CloudWatchLogs
<a name="aws-properties-ec2-verifiedaccessinstance-cloudwatchlogs"></a>

Options for CloudWatch Logs as a logging destination.

## Syntax
<a name="aws-properties-ec2-verifiedaccessinstance-cloudwatchlogs-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-ec2-verifiedaccessinstance-cloudwatchlogs-syntax.json"></a>

```
{
  "[Enabled](#cfn-ec2-verifiedaccessinstance-cloudwatchlogs-enabled)" : {{Boolean}},
  "[LogGroup](#cfn-ec2-verifiedaccessinstance-cloudwatchlogs-loggroup)" : {{String}}
}
```

### YAML
<a name="aws-properties-ec2-verifiedaccessinstance-cloudwatchlogs-syntax.yaml"></a>

```
  [Enabled](#cfn-ec2-verifiedaccessinstance-cloudwatchlogs-enabled): {{Boolean}}
  [LogGroup](#cfn-ec2-verifiedaccessinstance-cloudwatchlogs-loggroup): {{String}}
```

## Properties
<a name="aws-properties-ec2-verifiedaccessinstance-cloudwatchlogs-properties"></a>

`Enabled`  <a name="cfn-ec2-verifiedaccessinstance-cloudwatchlogs-enabled"></a>
Indicates whether logging is enabled.
*Required*: No
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`LogGroup`  <a name="cfn-ec2-verifiedaccessinstance-cloudwatchlogs-loggroup"></a>
The ID of the CloudWatch Logs log group.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
