---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-fsx-s3accesspointattachment-ontapfilesystemidentity.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::FSx::S3AccessPointAttachment OntapFileSystemIdentity
<a name="aws-properties-fsx-s3accesspointattachment-ontapfilesystemidentity"></a>

Specifies the file system user identity that will be used for authorizing all file access requests that are made using the S3 access point. The identity can be either a UNIX user or a Windows user.

## Syntax
<a name="aws-properties-fsx-s3accesspointattachment-ontapfilesystemidentity-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-fsx-s3accesspointattachment-ontapfilesystemidentity-syntax.json"></a>

```
{
  "[Type](#cfn-fsx-s3accesspointattachment-ontapfilesystemidentity-type)" : {{String}},
  "[UnixUser](#cfn-fsx-s3accesspointattachment-ontapfilesystemidentity-unixuser)" : {{OntapUnixFileSystemUser}},
  "[WindowsUser](#cfn-fsx-s3accesspointattachment-ontapfilesystemidentity-windowsuser)" : {{OntapWindowsFileSystemUser}}
}
```

### YAML
<a name="aws-properties-fsx-s3accesspointattachment-ontapfilesystemidentity-syntax.yaml"></a>

```
  [Type](#cfn-fsx-s3accesspointattachment-ontapfilesystemidentity-type): {{String}}
  [UnixUser](#cfn-fsx-s3accesspointattachment-ontapfilesystemidentity-unixuser): {{
    OntapUnixFileSystemUser}}
  [WindowsUser](#cfn-fsx-s3accesspointattachment-ontapfilesystemidentity-windowsuser): {{
    OntapWindowsFileSystemUser}}
```

## Properties
<a name="aws-properties-fsx-s3accesspointattachment-ontapfilesystemidentity-properties"></a>

`Type`  <a name="cfn-fsx-s3accesspointattachment-ontapfilesystemidentity-type"></a>
Specifies the FSx for ONTAP user identity type. Valid values are `UNIX` and `WINDOWS`.
*Required*: Yes
*Type*: String
*Allowed values*: `UNIX | WINDOWS`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`UnixUser`  <a name="cfn-fsx-s3accesspointattachment-ontapfilesystemidentity-unixuser"></a>
Specifies the UNIX user identity for file system operations.
*Required*: No
*Type*: [OntapUnixFileSystemUser](aws-properties-fsx-s3accesspointattachment-ontapunixfilesystemuser.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`WindowsUser`  <a name="cfn-fsx-s3accesspointattachment-ontapfilesystemidentity-windowsuser"></a>
Specifies the Windows user identity for file system operations.
*Required*: No
*Type*: [OntapWindowsFileSystemUser](aws-properties-fsx-s3accesspointattachment-ontapwindowsfilesystemuser.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
