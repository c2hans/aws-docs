---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-cognito-logdeliveryconfiguration-s3configuration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Cognito::LogDeliveryConfiguration S3Configuration
<a name="aws-properties-cognito-logdeliveryconfiguration-s3configuration"></a>

Configuration for the Amazon S3 bucket destination of user activity log export with threat protection.

## Syntax
<a name="aws-properties-cognito-logdeliveryconfiguration-s3configuration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-cognito-logdeliveryconfiguration-s3configuration-syntax.json"></a>

```
{
  "[BucketArn](#cfn-cognito-logdeliveryconfiguration-s3configuration-bucketarn)" : {{String}}
}
```

### YAML
<a name="aws-properties-cognito-logdeliveryconfiguration-s3configuration-syntax.yaml"></a>

```
  [BucketArn](#cfn-cognito-logdeliveryconfiguration-s3configuration-bucketarn): {{String}}
```

## Properties
<a name="aws-properties-cognito-logdeliveryconfiguration-s3configuration-properties"></a>

`BucketArn`  <a name="cfn-cognito-logdeliveryconfiguration-s3configuration-bucketarn"></a>
The ARN of an Amazon S3 bucket that's the destination for threat protection log export.
*Required*: No
*Type*: String
*Pattern*: `arn:[\w+=/,.@-]+:[\w+=/,.@-]+:::[\w+=/,.@-]+(:[\w+=/,.@-]+)?(:[\w+=/,.@-]+)?`
*Minimum*: `3`
*Maximum*: `1024`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
