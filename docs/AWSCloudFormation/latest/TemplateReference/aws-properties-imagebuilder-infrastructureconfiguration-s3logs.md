---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-imagebuilder-infrastructureconfiguration-s3logs.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::ImageBuilder::InfrastructureConfiguration S3Logs
<a name="aws-properties-imagebuilder-infrastructureconfiguration-s3logs"></a>

Amazon S3 logging configuration.

## Syntax
<a name="aws-properties-imagebuilder-infrastructureconfiguration-s3logs-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-imagebuilder-infrastructureconfiguration-s3logs-syntax.json"></a>

```
{
  "[S3BucketName](#cfn-imagebuilder-infrastructureconfiguration-s3logs-s3bucketname)" : {{String}},
  "[S3KeyPrefix](#cfn-imagebuilder-infrastructureconfiguration-s3logs-s3keyprefix)" : {{String}}
}
```

### YAML
<a name="aws-properties-imagebuilder-infrastructureconfiguration-s3logs-syntax.yaml"></a>

```
  [S3BucketName](#cfn-imagebuilder-infrastructureconfiguration-s3logs-s3bucketname): {{String}}
  [S3KeyPrefix](#cfn-imagebuilder-infrastructureconfiguration-s3logs-s3keyprefix): {{String}}
```

## Properties
<a name="aws-properties-imagebuilder-infrastructureconfiguration-s3logs-properties"></a>

`S3BucketName`  <a name="cfn-imagebuilder-infrastructureconfiguration-s3logs-s3bucketname"></a>
The name of an existing Amazon S3 bucket where Image Builder saves build logs. The bucket isn't validated when you create or update the configuration, and Image Builder doesn't create it. The instance profile associated with this infrastructure configuration must have permission to write to the bucket.
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `1024`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`S3KeyPrefix`  <a name="cfn-imagebuilder-infrastructureconfiguration-s3logs-s3keyprefix"></a>
The Amazon S3 key prefix under which Image Builder writes build and test logs in the bucket.
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `1024`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
