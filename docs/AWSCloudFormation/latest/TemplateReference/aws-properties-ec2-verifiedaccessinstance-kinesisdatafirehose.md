---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-ec2-verifiedaccessinstance-kinesisdatafirehose.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::EC2::VerifiedAccessInstance KinesisDataFirehose
<a name="aws-properties-ec2-verifiedaccessinstance-kinesisdatafirehose"></a>

Options for Kinesis as a logging destination.

## Syntax
<a name="aws-properties-ec2-verifiedaccessinstance-kinesisdatafirehose-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-ec2-verifiedaccessinstance-kinesisdatafirehose-syntax.json"></a>

```
{
  "[DeliveryStream](#cfn-ec2-verifiedaccessinstance-kinesisdatafirehose-deliverystream)" : {{String}},
  "[Enabled](#cfn-ec2-verifiedaccessinstance-kinesisdatafirehose-enabled)" : {{Boolean}}
}
```

### YAML
<a name="aws-properties-ec2-verifiedaccessinstance-kinesisdatafirehose-syntax.yaml"></a>

```
  [DeliveryStream](#cfn-ec2-verifiedaccessinstance-kinesisdatafirehose-deliverystream): {{String}}
  [Enabled](#cfn-ec2-verifiedaccessinstance-kinesisdatafirehose-enabled): {{Boolean}}
```

## Properties
<a name="aws-properties-ec2-verifiedaccessinstance-kinesisdatafirehose-properties"></a>

`DeliveryStream`  <a name="cfn-ec2-verifiedaccessinstance-kinesisdatafirehose-deliverystream"></a>
The ID of the delivery stream.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Enabled`  <a name="cfn-ec2-verifiedaccessinstance-kinesisdatafirehose-enabled"></a>
Indicates whether logging is enabled.
*Required*: No
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
