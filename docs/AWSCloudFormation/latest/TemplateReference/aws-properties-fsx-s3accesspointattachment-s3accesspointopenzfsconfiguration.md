---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-fsx-s3accesspointattachment-s3accesspointopenzfsconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::FSx::S3AccessPointAttachment S3AccessPointOpenZFSConfiguration
<a name="aws-properties-fsx-s3accesspointattachment-s3accesspointopenzfsconfiguration"></a>

Describes the FSx for OpenZFS attachment configuration of an S3 access point attachment.

## Syntax
<a name="aws-properties-fsx-s3accesspointattachment-s3accesspointopenzfsconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-fsx-s3accesspointattachment-s3accesspointopenzfsconfiguration-syntax.json"></a>

```
{
  "[FileSystemIdentity](#cfn-fsx-s3accesspointattachment-s3accesspointopenzfsconfiguration-filesystemidentity)" : {{OpenZFSFileSystemIdentity}},
  "[VolumeId](#cfn-fsx-s3accesspointattachment-s3accesspointopenzfsconfiguration-volumeid)" : {{String}}
}
```

### YAML
<a name="aws-properties-fsx-s3accesspointattachment-s3accesspointopenzfsconfiguration-syntax.yaml"></a>

```
  [FileSystemIdentity](#cfn-fsx-s3accesspointattachment-s3accesspointopenzfsconfiguration-filesystemidentity): {{
    OpenZFSFileSystemIdentity}}
  [VolumeId](#cfn-fsx-s3accesspointattachment-s3accesspointopenzfsconfiguration-volumeid): {{String}}
```

## Properties
<a name="aws-properties-fsx-s3accesspointattachment-s3accesspointopenzfsconfiguration-properties"></a>

`FileSystemIdentity`  <a name="cfn-fsx-s3accesspointattachment-s3accesspointopenzfsconfiguration-filesystemidentity"></a>
The file system identity used to authorize file access requests made using the S3 access point.
*Required*: Yes
*Type*: [OpenZFSFileSystemIdentity](aws-properties-fsx-s3accesspointattachment-openzfsfilesystemidentity.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`VolumeId`  <a name="cfn-fsx-s3accesspointattachment-s3accesspointopenzfsconfiguration-volumeid"></a>
The ID of the FSx for OpenZFS volume that the S3 access point is attached to.
*Required*: Yes
*Type*: String
*Pattern*: `^(fsvol-[0-9a-f]{17,})$`
*Minimum*: `23`
*Maximum*: `23`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)
