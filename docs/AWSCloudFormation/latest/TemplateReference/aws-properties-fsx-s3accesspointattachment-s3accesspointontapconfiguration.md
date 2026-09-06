---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-fsx-s3accesspointattachment-s3accesspointontapconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::FSx::S3AccessPointAttachment S3AccessPointOntapConfiguration
<a name="aws-properties-fsx-s3accesspointattachment-s3accesspointontapconfiguration"></a>

Describes the FSx for ONTAP attachment configuration of an S3 access point attachment.

## Syntax
<a name="aws-properties-fsx-s3accesspointattachment-s3accesspointontapconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-fsx-s3accesspointattachment-s3accesspointontapconfiguration-syntax.json"></a>

```
{
  "[FileSystemIdentity](#cfn-fsx-s3accesspointattachment-s3accesspointontapconfiguration-filesystemidentity)" : {{OntapFileSystemIdentity}},
  "[VolumeId](#cfn-fsx-s3accesspointattachment-s3accesspointontapconfiguration-volumeid)" : {{String}}
}
```

### YAML
<a name="aws-properties-fsx-s3accesspointattachment-s3accesspointontapconfiguration-syntax.yaml"></a>

```
  [FileSystemIdentity](#cfn-fsx-s3accesspointattachment-s3accesspointontapconfiguration-filesystemidentity): {{
    OntapFileSystemIdentity}}
  [VolumeId](#cfn-fsx-s3accesspointattachment-s3accesspointontapconfiguration-volumeid): {{String}}
```

## Properties
<a name="aws-properties-fsx-s3accesspointattachment-s3accesspointontapconfiguration-properties"></a>

`FileSystemIdentity`  <a name="cfn-fsx-s3accesspointattachment-s3accesspointontapconfiguration-filesystemidentity"></a>
The file system identity used to authorize file access requests made using the S3 access point.
*Required*: Yes
*Type*: [OntapFileSystemIdentity](aws-properties-fsx-s3accesspointattachment-ontapfilesystemidentity.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`VolumeId`  <a name="cfn-fsx-s3accesspointattachment-s3accesspointontapconfiguration-volumeid"></a>
The ID of the FSx for ONTAP volume that the S3 access point is attached to.
*Required*: Yes
*Type*: String
*Pattern*: `^(fsvol-[0-9a-f]{17,})$`
*Minimum*: `23`
*Maximum*: `23`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)
