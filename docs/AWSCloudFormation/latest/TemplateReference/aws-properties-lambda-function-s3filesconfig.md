---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-lambda-function-s3filesconfig.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Lambda::Function S3FilesConfig
<a name="aws-properties-lambda-function-s3filesconfig"></a>

Setting controls how your function accesses data from an Amazon S3 file system.

## Syntax
<a name="aws-properties-lambda-function-s3filesconfig-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-lambda-function-s3filesconfig-syntax.json"></a>

```
{
  "[DirectS3Read](#cfn-lambda-function-s3filesconfig-directs3read)" : {{String}}
}
```

### YAML
<a name="aws-properties-lambda-function-s3filesconfig-syntax.yaml"></a>

```
  [DirectS3Read](#cfn-lambda-function-s3filesconfig-directs3read): {{String}}
```

## Properties
<a name="aws-properties-lambda-function-s3filesconfig-properties"></a>

`DirectS3Read`  <a name="cfn-lambda-function-s3filesconfig-directs3read"></a>
Specifies if a function reads from the file system for the lowest latency, or through Amazon S3 Files feature "direct Amazon S3 bucket reads" for the highest throughput. Valid values:
+ `AUTO` (default) – Direct reads are active for functions you configure with 512 MB or more of memory.
+ `ENABLED` – Enforces all reads are directly from the Amazon S3 bucket, regardless of available memory (less than 512 MB).
+ `DISABLED` – Routes all reads through the file system, regardless of memory configuration.
To use direct reads, you must grant the execution role the `s3:GetObject` and `s3:GetObjectVersion` permissions. If a direct read fails, Lambda automatically falls back to reading through the file system.
*Required*: No
*Type*: String
*Allowed values*: `ENABLED | DISABLED | AUTO`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
