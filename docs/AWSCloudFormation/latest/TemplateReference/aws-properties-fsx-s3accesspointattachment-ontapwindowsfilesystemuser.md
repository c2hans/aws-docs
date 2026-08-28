---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-fsx-s3accesspointattachment-ontapwindowsfilesystemuser.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::FSx::S3AccessPointAttachment OntapWindowsFileSystemUser
<a name="aws-properties-fsx-s3accesspointattachment-ontapwindowsfilesystemuser"></a>

The FSx for ONTAP Windows file system user that is used for authorizing all file access requests that are made using the S3 access point.

## Syntax
<a name="aws-properties-fsx-s3accesspointattachment-ontapwindowsfilesystemuser-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-fsx-s3accesspointattachment-ontapwindowsfilesystemuser-syntax.json"></a>

```
{
  "[Name](#cfn-fsx-s3accesspointattachment-ontapwindowsfilesystemuser-name)" : {{String}}
}
```

### YAML
<a name="aws-properties-fsx-s3accesspointattachment-ontapwindowsfilesystemuser-syntax.yaml"></a>

```
  [Name](#cfn-fsx-s3accesspointattachment-ontapwindowsfilesystemuser-name): {{String}}
```

## Properties
<a name="aws-properties-fsx-s3accesspointattachment-ontapwindowsfilesystemuser-properties"></a>

`Name`  <a name="cfn-fsx-s3accesspointattachment-ontapwindowsfilesystemuser-name"></a>
The name of the Windows user. The name can be up to 256 characters long and supports Active Directory users.
*Required*: Yes
*Type*: String
*Pattern*: `^[^\u0000\u0085\u2028\u2029\r\n]{1,256}$`
*Minimum*: `1`
*Maximum*: `256`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
