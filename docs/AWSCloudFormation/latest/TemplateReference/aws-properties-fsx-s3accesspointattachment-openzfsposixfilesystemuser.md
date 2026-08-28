---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-fsx-s3accesspointattachment-openzfsposixfilesystemuser.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::FSx::S3AccessPointAttachment OpenZFSPosixFileSystemUser
<a name="aws-properties-fsx-s3accesspointattachment-openzfsposixfilesystemuser"></a>

The FSx for OpenZFS file system user that is used for authorizing all file access requests that are made using the S3 access point.

## Syntax
<a name="aws-properties-fsx-s3accesspointattachment-openzfsposixfilesystemuser-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-fsx-s3accesspointattachment-openzfsposixfilesystemuser-syntax.json"></a>

```
{
  "[Gid](#cfn-fsx-s3accesspointattachment-openzfsposixfilesystemuser-gid)" : {{Number}},
  "[SecondaryGids](#cfn-fsx-s3accesspointattachment-openzfsposixfilesystemuser-secondarygids)" : {{[ FileSystemGID, ... ]}},
  "[Uid](#cfn-fsx-s3accesspointattachment-openzfsposixfilesystemuser-uid)" : {{Number}}
}
```

### YAML
<a name="aws-properties-fsx-s3accesspointattachment-openzfsposixfilesystemuser-syntax.yaml"></a>

```
  [Gid](#cfn-fsx-s3accesspointattachment-openzfsposixfilesystemuser-gid): {{Number}}
  [SecondaryGids](#cfn-fsx-s3accesspointattachment-openzfsposixfilesystemuser-secondarygids): {{
    - FileSystemGID}}
  [Uid](#cfn-fsx-s3accesspointattachment-openzfsposixfilesystemuser-uid): {{Number}}
```

## Properties
<a name="aws-properties-fsx-s3accesspointattachment-openzfsposixfilesystemuser-properties"></a>

`Gid`  <a name="cfn-fsx-s3accesspointattachment-openzfsposixfilesystemuser-gid"></a>
The GID of the file system user.
*Required*: Yes
*Type*: Number
*Minimum*: `0`
*Maximum*: `4294967295`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`SecondaryGids`  <a name="cfn-fsx-s3accesspointattachment-openzfsposixfilesystemuser-secondarygids"></a>
The list of secondary GIDs for the file system user.
*Required*: No
*Type*: Array of [FileSystemGID](aws-properties-fsx-s3accesspointattachment-filesystemgid.md)
*Maximum*: `15`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Uid`  <a name="cfn-fsx-s3accesspointattachment-openzfsposixfilesystemuser-uid"></a>
The UID of the file system user.
*Required*: Yes
*Type*: Number
*Minimum*: `0`
*Maximum*: `4294967295`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
