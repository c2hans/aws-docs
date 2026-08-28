---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-fsx-s3accesspointattachment-filesystemgid.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::FSx::S3AccessPointAttachment FileSystemGID
<a name="aws-properties-fsx-s3accesspointattachment-filesystemgid"></a>

The GID of the file system user.

## Syntax
<a name="aws-properties-fsx-s3accesspointattachment-filesystemgid-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-fsx-s3accesspointattachment-filesystemgid-syntax.json"></a>

```
{
  "[Gid](#cfn-fsx-s3accesspointattachment-filesystemgid-gid)" : {{Number}}
}
```

### YAML
<a name="aws-properties-fsx-s3accesspointattachment-filesystemgid-syntax.yaml"></a>

```
  [Gid](#cfn-fsx-s3accesspointattachment-filesystemgid-gid): {{Number}}
```

## Properties
<a name="aws-properties-fsx-s3accesspointattachment-filesystemgid-properties"></a>

`Gid`  <a name="cfn-fsx-s3accesspointattachment-filesystemgid-gid"></a>
The GID of the file system user.
*Required*: Yes
*Type*: Number
*Minimum*: `0`
*Maximum*: `4294967295`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
