---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-fsx-s3accesspointattachment-openzfsfilesystemidentity.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::FSx::S3AccessPointAttachment OpenZFSFileSystemIdentity
<a name="aws-properties-fsx-s3accesspointattachment-openzfsfilesystemidentity"></a>

Specifies the file system user identity that will be used for authorizing all file access requests that are made using the S3 access point.

## Syntax
<a name="aws-properties-fsx-s3accesspointattachment-openzfsfilesystemidentity-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-fsx-s3accesspointattachment-openzfsfilesystemidentity-syntax.json"></a>

```
{
  "[PosixUser](#cfn-fsx-s3accesspointattachment-openzfsfilesystemidentity-posixuser)" : {{OpenZFSPosixFileSystemUser}},
  "[Type](#cfn-fsx-s3accesspointattachment-openzfsfilesystemidentity-type)" : {{String}}
}
```

### YAML
<a name="aws-properties-fsx-s3accesspointattachment-openzfsfilesystemidentity-syntax.yaml"></a>

```
  [PosixUser](#cfn-fsx-s3accesspointattachment-openzfsfilesystemidentity-posixuser): {{
    OpenZFSPosixFileSystemUser}}
  [Type](#cfn-fsx-s3accesspointattachment-openzfsfilesystemidentity-type): {{String}}
```

## Properties
<a name="aws-properties-fsx-s3accesspointattachment-openzfsfilesystemidentity-properties"></a>

`PosixUser`  <a name="cfn-fsx-s3accesspointattachment-openzfsfilesystemidentity-posixuser"></a>
Specifies the UID and GIDs of the file system POSIX user.
*Required*: Yes
*Type*: [OpenZFSPosixFileSystemUser](aws-properties-fsx-s3accesspointattachment-openzfsposixfilesystemuser.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Type`  <a name="cfn-fsx-s3accesspointattachment-openzfsfilesystemidentity-type"></a>
Specifies the FSx for OpenZFS user identity type, accepts only `POSIX`.
*Required*: Yes
*Type*: String
*Allowed values*: `POSIX`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)
