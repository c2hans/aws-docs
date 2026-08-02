---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-ses-receiptrule-connectaction.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::SES::ReceiptRule ConnectAction
<a name="aws-properties-ses-receiptrule-connectaction"></a>

When included in a receipt rule, this action parses the received message and starts an email contact in Amazon Connect on your behalf.

**Note**
When you receive emails, the maximum email size (including headers) is 40 MB. Additionally, emails may only have up to 10 attachments. Emails larger than 40 MB or with more than 10 attachments will be bounced.

We recommend that you configure this action via Amazon Connect.

## Syntax
<a name="aws-properties-ses-receiptrule-connectaction-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-ses-receiptrule-connectaction-syntax.json"></a>

```
{
  "[IAMRoleARN](#cfn-ses-receiptrule-connectaction-iamrolearn)" : {{String}},
  "[InstanceARN](#cfn-ses-receiptrule-connectaction-instancearn)" : {{String}}
}
```

### YAML
<a name="aws-properties-ses-receiptrule-connectaction-syntax.yaml"></a>

```
  [IAMRoleARN](#cfn-ses-receiptrule-connectaction-iamrolearn): {{String}}
  [InstanceARN](#cfn-ses-receiptrule-connectaction-instancearn): {{String}}
```

## Properties
<a name="aws-properties-ses-receiptrule-connectaction-properties"></a>

`IAMRoleARN`  <a name="cfn-ses-receiptrule-connectaction-iamrolearn"></a>
 The Amazon Resource Name (ARN) of the IAM role to be used by Amazon Simple Email Service while starting email contacts to the Amazon Connect instance. This role should have permission to invoke `connect:StartEmailContact` for the given Amazon Connect instance.
*Required*: Yes
*Type*: String
*Pattern*: `arn:[\w-]+:iam::[0-9]+:role/[\w-]+`
*Minimum*: `20`
*Maximum*: `2048`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`InstanceARN`  <a name="cfn-ses-receiptrule-connectaction-instancearn"></a>
The Amazon Resource Name (ARN) for the Amazon Connect instance that Amazon SES integrates with for starting email contacts.
For more information about Amazon Connect instances, see the [Amazon Connect Administrator Guide](https://docs.aws.amazon.com/connect/latest/adminguide/amazon-connect-instances.html)
*Required*: Yes
*Type*: String
*Pattern*: `arn:(aws|aws-us-gov):connect:[a-z]{2}-[a-z]+-[0-9-]{1}:[0-9]{1,20}:instance/[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
