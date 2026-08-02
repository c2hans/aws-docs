---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-s3files-filesystem.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::S3Files::FileSystem
<a name="aws-resource-s3files-filesystem"></a>

The `AWS::S3Files::FileSystem` resource specifies an Amazon S3 Files file system scoped to a bucket or prefix within a bucket, enabling file system access to S3 data.

## Syntax
<a name="aws-resource-s3files-filesystem-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-s3files-filesystem-syntax.json"></a>

```
{
  "Type" : "AWS::S3Files::FileSystem",
  "Properties" : {
      "[AcceptBucketWarning](#cfn-s3files-filesystem-acceptbucketwarning)" : {{Boolean}},
      "[Bucket](#cfn-s3files-filesystem-bucket)" : {{String}},
      "[ClientToken](#cfn-s3files-filesystem-clienttoken)" : {{String}},
      "[KmsKeyId](#cfn-s3files-filesystem-kmskeyid)" : {{String}},
      "[Prefix](#cfn-s3files-filesystem-prefix)" : {{String}},
      "[RoleArn](#cfn-s3files-filesystem-rolearn)" : {{String}},
      "[SynchronizationConfiguration](#cfn-s3files-filesystem-synchronizationconfiguration)" : {{SynchronizationConfiguration}},
      "[Tags](#cfn-s3files-filesystem-tags)" : {{[ Tag, ... ]}}
    }
}
```

### YAML
<a name="aws-resource-s3files-filesystem-syntax.yaml"></a>

```
Type: AWS::S3Files::FileSystem
Properties:
  [AcceptBucketWarning](#cfn-s3files-filesystem-acceptbucketwarning): {{Boolean}}
  [Bucket](#cfn-s3files-filesystem-bucket): {{String}}
  [ClientToken](#cfn-s3files-filesystem-clienttoken): {{String}}
  [KmsKeyId](#cfn-s3files-filesystem-kmskeyid): {{String}}
  [Prefix](#cfn-s3files-filesystem-prefix): {{String}}
  [RoleArn](#cfn-s3files-filesystem-rolearn): {{String}}
  [SynchronizationConfiguration](#cfn-s3files-filesystem-synchronizationconfiguration): {{
    SynchronizationConfiguration}}
  [Tags](#cfn-s3files-filesystem-tags): {{
    - Tag}}
```

## Properties
<a name="aws-resource-s3files-filesystem-properties"></a>

`AcceptBucketWarning`  <a name="cfn-s3files-filesystem-acceptbucketwarning"></a>
A boolean that indicates you have read and accept the warning about the S3 bucket being used for the file system. Set this to `true` to acknowledge the warning.
*Required*: No
*Type*: Boolean
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Bucket`  <a name="cfn-s3files-filesystem-bucket"></a>
The Amazon Resource Name (ARN) of the S3 bucket.
*Required*: Yes
*Type*: String
*Pattern*: `^(arn:aws[a-zA-Z0-9-]*:s3:::.+)$`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`ClientToken`  <a name="cfn-s3files-filesystem-clienttoken"></a>
A string of up to 64 ASCII characters that Amazon S3 Files uses to ensure idempotent creation.
*Required*: No
*Type*: String
*Pattern*: `^(.+)$`
*Minimum*: `1`
*Maximum*: `64`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`KmsKeyId`  <a name="cfn-s3files-filesystem-kmskeyid"></a>
The ID of the AWS KMS key used to encrypt the file system.
*Required*: No
*Type*: String
*Pattern*: `^([0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}|mrk-[0-9a-f]{32}|alias/[a-zA-Z0-9/_-]+|(arn:aws[-a-z]*:kms:[a-z0-9-]+:\d{12}:((key/[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12})|(key/mrk-[0-9a-f]{32})|(alias/[a-zA-Z0-9/_-]+))))$`
*Maximum*: `2048`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Prefix`  <a name="cfn-s3files-filesystem-prefix"></a>
The S3 key prefix that scopes the file system. When specified, the file system provides access only to objects under this prefix in the bucket.
*Required*: No
*Type*: String
*Pattern*: `^(|.*/)$`
*Maximum*: `1024`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`RoleArn`  <a name="cfn-s3files-filesystem-rolearn"></a>
The Amazon Resource Name (ARN) of the IAM role used for S3 access.
*Required*: Yes
*Type*: String
*Pattern*: `^arn:(aws[a-zA-Z-]*)?:iam::\d{12}:role/?[a-zA-Z_0-9+=,.@\-_/]+$`
*Maximum*: `2048`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`SynchronizationConfiguration`  <a name="cfn-s3files-filesystem-synchronizationconfiguration"></a>
The synchronization configuration for the file system, including import data rules and expiration data rules that control how data is synchronized between S3 and the file system.
*Required*: No
*Type*: [SynchronizationConfiguration](aws-properties-s3files-filesystem-synchronizationconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Tags`  <a name="cfn-s3files-filesystem-tags"></a>
An array of key-value pairs to apply to this resource.
For more information, see [Tag](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-resource-tags.html).
*Required*: No
*Type*: Array of [Tag](aws-properties-s3files-filesystem-tag.md)
*Maximum*: `50`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-s3files-filesystem-return-values"></a>

### Ref
<a name="aws-resource-s3files-filesystem-return-values-ref"></a>

When you pass the logical ID of this resource to the intrinsic `Ref` function, `Ref` returns the Amazon Resource Name (ARN) of the file system.

For more information about using the `Ref` function, see [https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-ref.html](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-ref.html).

### Fn::GetAtt
<a name="aws-resource-s3files-filesystem-return-values-fn--getatt"></a>

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-getatt.html](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-getatt.html).

####
<a name="aws-resource-s3files-filesystem-return-values-fn--getatt-fn--getatt"></a>

`CreationTime`  <a name="CreationTime-fn::getatt"></a>
The time when the file system was created.

`FileSystemArn`  <a name="FileSystemArn-fn::getatt"></a>
The Amazon Resource Name (ARN) of the file system.

`FileSystemId`  <a name="FileSystemId-fn::getatt"></a>
The ID of the file system.

`OwnerId`  <a name="OwnerId-fn::getatt"></a>
The AWS account ID of the file system owner.

`Status`  <a name="Status-fn::getatt"></a>
The current status of the file system.

`StatusMessage`  <a name="StatusMessage-fn::getatt"></a>
Additional information about the file system status.

`SynchronizationConfiguration.LatestVersionNumber`  <a name="SynchronizationConfiguration.LatestVersionNumber-fn::getatt"></a>
The latest version number of the synchronization configuration.
