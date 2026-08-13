---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-ec2-exportinstancetask-exporttos3task.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::EC2::ExportInstanceTask ExportToS3Task
<a name="aws-properties-ec2-exportinstancetask-exporttos3task"></a>

Describes the format and location for the export task.

## Syntax
<a name="aws-properties-ec2-exportinstancetask-exporttos3task-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-ec2-exportinstancetask-exporttos3task-syntax.json"></a>

```
{
  "[ContainerFormat](#cfn-ec2-exportinstancetask-exporttos3task-containerformat)" : {{String}},
  "[DiskImageFormat](#cfn-ec2-exportinstancetask-exporttos3task-diskimageformat)" : {{String}},
  "[S3Bucket](#cfn-ec2-exportinstancetask-exporttos3task-s3bucket)" : {{String}},
  "[S3Key](#cfn-ec2-exportinstancetask-exporttos3task-s3key)" : {{String}}
}
```

### YAML
<a name="aws-properties-ec2-exportinstancetask-exporttos3task-syntax.yaml"></a>

```
  [ContainerFormat](#cfn-ec2-exportinstancetask-exporttos3task-containerformat): {{String}}
  [DiskImageFormat](#cfn-ec2-exportinstancetask-exporttos3task-diskimageformat): {{String}}
  [S3Bucket](#cfn-ec2-exportinstancetask-exporttos3task-s3bucket): {{String}}
  [S3Key](#cfn-ec2-exportinstancetask-exporttos3task-s3key): {{String}}
```

## Properties
<a name="aws-properties-ec2-exportinstancetask-exporttos3task-properties"></a>

`ContainerFormat`  <a name="cfn-ec2-exportinstancetask-exporttos3task-containerformat"></a>
The container format used to combine disk images with metadata (such as OVF). If absent, only the disk image is exported.
*Required*: No
*Type*: String
*Allowed values*: `ova`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`DiskImageFormat`  <a name="cfn-ec2-exportinstancetask-exporttos3task-diskimageformat"></a>
The format for the exported image.
*Required*: No
*Type*: String
*Allowed values*: `VMDK | RAW | VHD`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`S3Bucket`  <a name="cfn-ec2-exportinstancetask-exporttos3task-s3bucket"></a>
The Amazon S3 bucket for the destination image. The destination bucket must exist and have an access control list (ACL) attached that specifies the Region-specific canonical account ID for the `Grantee`. For more information about the ACL to your S3 bucket, see [Prerequisites](https://docs.aws.amazon.com/vm-import/latest/userguide/vmexport.html#vmexport-prerequisites) in the VM Import/Export User Guide.
*Required*: No
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`S3Key`  <a name="cfn-ec2-exportinstancetask-exporttos3task-s3key"></a>
The encryption key for your S3 bucket.
*Required*: No
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)
