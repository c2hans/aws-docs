---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-fsx-s3accesspointattachment-ontapunixfilesystemuser.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::FSx::S3AccessPointAttachment OntapUnixFileSystemUser
<a name="aws-properties-fsx-s3accesspointattachment-ontapunixfilesystemuser"></a>

The FSx for ONTAP UNIX file system user that is used for authorizing all file access requests that are made using the S3 access point.

## Syntax
<a name="aws-properties-fsx-s3accesspointattachment-ontapunixfilesystemuser-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-fsx-s3accesspointattachment-ontapunixfilesystemuser-syntax.json"></a>

```
{
  "[Name](#cfn-fsx-s3accesspointattachment-ontapunixfilesystemuser-name)" : {{String}}
}
```

### YAML
<a name="aws-properties-fsx-s3accesspointattachment-ontapunixfilesystemuser-syntax.yaml"></a>

```
  [Name](#cfn-fsx-s3accesspointattachment-ontapunixfilesystemuser-name): {{String}}
```

## Properties
<a name="aws-properties-fsx-s3accesspointattachment-ontapunixfilesystemuser-properties"></a>

`Name`  <a name="cfn-fsx-s3accesspointattachment-ontapunixfilesystemuser-name"></a>
The name of the UNIX user. The name can be up to 256 characters long.
*Required*: Yes
*Type*: String
*Pattern*: `^[^\u0000\u0085\u2028\u2029\r\n]{1,256}$`
*Minimum*: `1`
*Maximum*: `256`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)
