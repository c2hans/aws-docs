---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-personalize-batchinferencejob-s3dataconfig.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Personalize::BatchInferenceJob S3DataConfig
<a name="aws-properties-personalize-batchinferencejob-s3dataconfig"></a>

The configuration details of an Amazon S3 input or output bucket.

## Syntax
<a name="aws-properties-personalize-batchinferencejob-s3dataconfig-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-personalize-batchinferencejob-s3dataconfig-syntax.json"></a>

```
{
  "[Path](#cfn-personalize-batchinferencejob-s3dataconfig-path)" : {{String}}
}
```

### YAML
<a name="aws-properties-personalize-batchinferencejob-s3dataconfig-syntax.yaml"></a>

```
  [Path](#cfn-personalize-batchinferencejob-s3dataconfig-path): {{String}}
```

## Properties
<a name="aws-properties-personalize-batchinferencejob-s3dataconfig-properties"></a>

`Path`  <a name="cfn-personalize-batchinferencejob-s3dataconfig-path"></a>
The file path of the Amazon S3 bucket.
*Required*: Yes
*Type*: String
*Pattern*: `^(s3|http|https)://.+$`
*Maximum*: `256`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)
