---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-lambda-function-filesystemconfig.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Lambda::Function FileSystemConfig
<a name="aws-properties-lambda-function-filesystemconfig"></a>

Details about the connection between a Lambda function and an [Amazon EFS file system](https://docs.aws.amazon.com/lambda/latest/dg/configuration-filesystem.html) or an [Amazon S3 file system](https://docs.aws.amazon.com/lambda/latest/dg/configuration-filesystem.html).

## Syntax
<a name="aws-properties-lambda-function-filesystemconfig-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-lambda-function-filesystemconfig-syntax.json"></a>

```
{
  "[Arn](#cfn-lambda-function-filesystemconfig-arn)" : {{String}},
  "[LocalMountPath](#cfn-lambda-function-filesystemconfig-localmountpath)" : {{String}},
  "[S3FilesConfig](#cfn-lambda-function-filesystemconfig-s3filesconfig)" : {{S3FilesConfig}}
}
```

### YAML
<a name="aws-properties-lambda-function-filesystemconfig-syntax.yaml"></a>

```
  [Arn](#cfn-lambda-function-filesystemconfig-arn): {{String}}
  [LocalMountPath](#cfn-lambda-function-filesystemconfig-localmountpath): {{String}}
  [S3FilesConfig](#cfn-lambda-function-filesystemconfig-s3filesconfig): {{
    S3FilesConfig}}
```

## Properties
<a name="aws-properties-lambda-function-filesystemconfig-properties"></a>

`Arn`  <a name="cfn-lambda-function-filesystemconfig-arn"></a>
The Amazon Resource Name (ARN) of the Amazon EFS or Amazon S3 Files access point that provides access to the file system.
*Required*: Yes
*Type*: String
*Pattern*: `^arn:aws[a-zA-Z-]*:elasticfilesystem:(eusc-)?[a-z]{2}((-gov)|(-iso([a-z]?)))?-[a-z]+-\d{1}:\d{12}:access-point/fsap-[a-f0-9]{17}$|^arn:aws[-a-z]*:s3files:[0-9a-z-:]+:file-system/fs-[0-9a-f]{17,40}/access-point/fsap-[0-9a-f]{17,40}$`
*Maximum*: `200`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`LocalMountPath`  <a name="cfn-lambda-function-filesystemconfig-localmountpath"></a>
The path where the function can access the file system, starting with `/mnt/`.
*Required*: Yes
*Type*: String
*Pattern*: `^/mnt/[a-zA-Z0-9-_.]+$`
*Maximum*: `160`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`S3FilesConfig`  <a name="cfn-lambda-function-filesystemconfig-s3filesconfig"></a>
The configuration for how your function accesses data on an Amazon S3 file system. Valid only when the file system access point ARN is an Amazon S3 Files access point. If you specify a different access point type (for example, Amazon Elastic File System), the operation returns an `InvalidParameterException`.
*Required*: No
*Type*: [S3FilesConfig](aws-properties-lambda-function-s3filesconfig.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
