---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-msk-replicator-s3.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::MSK::Replicator S3
<a name="aws-properties-msk-replicator-s3"></a>

S3 details for ReplicatorLogDelivery.

## Syntax
<a name="aws-properties-msk-replicator-s3-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-msk-replicator-s3-syntax.json"></a>

```
{
  "[Bucket](#cfn-msk-replicator-s3-bucket)" : {{String}},
  "[Enabled](#cfn-msk-replicator-s3-enabled)" : {{Boolean}},
  "[Prefix](#cfn-msk-replicator-s3-prefix)" : {{String}}
}
```

### YAML
<a name="aws-properties-msk-replicator-s3-syntax.yaml"></a>

```
  [Bucket](#cfn-msk-replicator-s3-bucket): {{String}}
  [Enabled](#cfn-msk-replicator-s3-enabled): {{Boolean}}
  [Prefix](#cfn-msk-replicator-s3-prefix): {{String}}
```

## Properties
<a name="aws-properties-msk-replicator-s3-properties"></a>

`Bucket`  <a name="cfn-msk-replicator-s3-bucket"></a>
The S3 bucket that is the destination for log delivery.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Enabled`  <a name="cfn-msk-replicator-s3-enabled"></a>
Whether log delivery to S3 is enabled.
*Required*: Yes
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Prefix`  <a name="cfn-msk-replicator-s3-prefix"></a>
The S3 prefix that is the destination for log delivery.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
