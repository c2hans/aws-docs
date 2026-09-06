---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-athena-workgroup-s3loggingconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Athena::WorkGroup S3LoggingConfiguration
<a name="aws-properties-athena-workgroup-s3loggingconfiguration"></a>

Configuration settings for delivering logs to Amazon S3 buckets.

## Syntax
<a name="aws-properties-athena-workgroup-s3loggingconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-athena-workgroup-s3loggingconfiguration-syntax.json"></a>

```
{
  "[Enabled](#cfn-athena-workgroup-s3loggingconfiguration-enabled)" : {{Boolean}},
  "[KmsKey](#cfn-athena-workgroup-s3loggingconfiguration-kmskey)" : {{String}},
  "[LogLocation](#cfn-athena-workgroup-s3loggingconfiguration-loglocation)" : {{String}}
}
```

### YAML
<a name="aws-properties-athena-workgroup-s3loggingconfiguration-syntax.yaml"></a>

```
  [Enabled](#cfn-athena-workgroup-s3loggingconfiguration-enabled): {{Boolean}}
  [KmsKey](#cfn-athena-workgroup-s3loggingconfiguration-kmskey): {{String}}
  [LogLocation](#cfn-athena-workgroup-s3loggingconfiguration-loglocation): {{String}}
```

## Properties
<a name="aws-properties-athena-workgroup-s3loggingconfiguration-properties"></a>

`Enabled`  <a name="cfn-athena-workgroup-s3loggingconfiguration-enabled"></a>
Enables S3 log delivery.
*Required*: No
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`KmsKey`  <a name="cfn-athena-workgroup-s3loggingconfiguration-kmskey"></a>
The KMS key ARN to encrypt the logs published to the given Amazon S3 destination.
*Required*: No
*Type*: String
*Pattern*: `^arn:aws[a-z\-]*:kms:([a-z0-9\-]+):\d{12}:key/?[a-zA-Z_0-9+=,.@\-_/]+$|^arn:aws[a-z\-]*:kms:([a-z0-9\-]+):\d{12}:alias/?[a-zA-Z_0-9+=,.@\-_/]+$|^alias/[a-zA-Z0-9/_-]+$|[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}`
*Minimum*: `1`
*Maximum*: `2048`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`LogLocation`  <a name="cfn-athena-workgroup-s3loggingconfiguration-loglocation"></a>
The Amazon S3 destination URI for log publishing.
*Required*: No
*Type*: String
*Pattern*: `^s3://[a-z0-9][a-z0-9\-]*[a-z0-9](/.*)?$`
*Maximum*: `1024`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
