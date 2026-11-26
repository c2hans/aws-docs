---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-bedrockagentcore-runtime-s3bucketmountconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::BedrockAgentCore::Runtime S3BucketMountConfiguration

<a name="aws-properties-bedrockagentcore-runtime-s3bucketmountconfiguration-description"></a>The `S3BucketMountConfiguration` property type specifies Property description not available. for an [AWS::BedrockAgentCore::Runtime](aws-resource-bedrockagentcore-runtime.md).

## Syntax
<a name="aws-properties-bedrockagentcore-runtime-s3bucketmountconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-bedrockagentcore-runtime-s3bucketmountconfiguration-syntax.json"></a>

```json
{
  "[Bucket](#cfn-bedrockagentcore-runtime-s3bucketmountconfiguration-bucket)" : {{String}},
  "[MountPath](#cfn-bedrockagentcore-runtime-s3bucketmountconfiguration-mountpath)" : {{String}},
  "[Prefix](#cfn-bedrockagentcore-runtime-s3bucketmountconfiguration-prefix)" : {{String}},
  "[S3BucketOwner](#cfn-bedrockagentcore-runtime-s3bucketmountconfiguration-s3bucketowner)" : {{String}},
  "[S3BucketRegion](#cfn-bedrockagentcore-runtime-s3bucketmountconfiguration-s3bucketregion)" : {{String}}
}
```

### YAML
<a name="aws-properties-bedrockagentcore-runtime-s3bucketmountconfiguration-syntax.yaml"></a>

```yaml
  [Bucket](#cfn-bedrockagentcore-runtime-s3bucketmountconfiguration-bucket): {{String}}
  [MountPath](#cfn-bedrockagentcore-runtime-s3bucketmountconfiguration-mountpath): {{String}}
  [Prefix](#cfn-bedrockagentcore-runtime-s3bucketmountconfiguration-prefix): {{String}}
  [S3BucketOwner](#cfn-bedrockagentcore-runtime-s3bucketmountconfiguration-s3bucketowner): {{String}}
  [S3BucketRegion](#cfn-bedrockagentcore-runtime-s3bucketmountconfiguration-s3bucketregion): {{String}}
```

## Properties
<a name="aws-properties-bedrockagentcore-runtime-s3bucketmountconfiguration-properties"></a>

`Bucket`  <a name="cfn-bedrockagentcore-runtime-s3bucketmountconfiguration-bucket"></a>
Property description not available.
*Required*: Yes
*Type*: String
*Minimum*: `3`
*Maximum*: `63`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`MountPath`  <a name="cfn-bedrockagentcore-runtime-s3bucketmountconfiguration-mountpath"></a>
Property description not available.
*Required*: Yes
*Type*: String
*Pattern*: `^/mnt/[a-zA-Z0-9._-]+/?$`
*Minimum*: `6`
*Maximum*: `200`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Prefix`  <a name="cfn-bedrockagentcore-runtime-s3bucketmountconfiguration-prefix"></a>
Property description not available.
*Required*: No
*Type*: String
*Pattern*: `^[a-zA-Z0-9{][a-zA-Z0-9!_.*'()/{}-]*$`
*Minimum*: `1`
*Maximum*: `1024`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`S3BucketOwner`  <a name="cfn-bedrockagentcore-runtime-s3bucketmountconfiguration-s3bucketowner"></a>
Property description not available.
*Required*: No
*Type*: String
*Pattern*: `^[0-9]{12}$`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`S3BucketRegion`  <a name="cfn-bedrockagentcore-runtime-s3bucketmountconfiguration-s3bucketregion"></a>
Property description not available.
*Required*: No
*Type*: String
*Pattern*: `^([a-z]+-){2,3}\d+$`
*Minimum*: `1`
*Maximum*: `32`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
