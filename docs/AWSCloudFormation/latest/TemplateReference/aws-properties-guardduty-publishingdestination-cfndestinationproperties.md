---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-guardduty-publishingdestination-cfndestinationproperties.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::GuardDuty::PublishingDestination CFNDestinationProperties
<a name="aws-properties-guardduty-publishingdestination-cfndestinationproperties"></a>

Contains the Amazon Resource Name (ARN) of the resource that receives the published findings, such as an S3 bucket, and the ARN of the KMS key that is used to encrypt these published findings.

## Syntax
<a name="aws-properties-guardduty-publishingdestination-cfndestinationproperties-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-guardduty-publishingdestination-cfndestinationproperties-syntax.json"></a>

```
{
  "[DestinationArn](#cfn-guardduty-publishingdestination-cfndestinationproperties-destinationarn)" : {{String}},
  "[KmsKeyArn](#cfn-guardduty-publishingdestination-cfndestinationproperties-kmskeyarn)" : {{String}}
}
```

### YAML
<a name="aws-properties-guardduty-publishingdestination-cfndestinationproperties-syntax.yaml"></a>

```
  [DestinationArn](#cfn-guardduty-publishingdestination-cfndestinationproperties-destinationarn): {{String}}
  [KmsKeyArn](#cfn-guardduty-publishingdestination-cfndestinationproperties-kmskeyarn): {{String}}
```

## Properties
<a name="aws-properties-guardduty-publishingdestination-cfndestinationproperties-properties"></a>

`DestinationArn`  <a name="cfn-guardduty-publishingdestination-cfndestinationproperties-destinationarn"></a>
The ARN of the resource where the findings are published.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`KmsKeyArn`  <a name="cfn-guardduty-publishingdestination-cfndestinationproperties-kmskeyarn"></a>
The ARN of the KMS key to use for encryption.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
