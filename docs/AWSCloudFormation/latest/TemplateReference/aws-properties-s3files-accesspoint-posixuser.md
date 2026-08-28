---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-s3files-accesspoint-posixuser.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::S3Files::AccessPoint PosixUser
<a name="aws-properties-s3files-accesspoint-posixuser"></a>

Specifies the POSIX identity with uid, gid, and secondary group IDs for user enforcement.

## Syntax
<a name="aws-properties-s3files-accesspoint-posixuser-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-s3files-accesspoint-posixuser-syntax.json"></a>

```
{
  "[Gid](#cfn-s3files-accesspoint-posixuser-gid)" : {{String}},
  "[SecondaryGids](#cfn-s3files-accesspoint-posixuser-secondarygids)" : {{[ String, ... ]}},
  "[Uid](#cfn-s3files-accesspoint-posixuser-uid)" : {{String}}
}
```

### YAML
<a name="aws-properties-s3files-accesspoint-posixuser-syntax.yaml"></a>

```
  [Gid](#cfn-s3files-accesspoint-posixuser-gid): {{String}}
  [SecondaryGids](#cfn-s3files-accesspoint-posixuser-secondarygids): {{
    - String}}
  [Uid](#cfn-s3files-accesspoint-posixuser-uid): {{String}}
```

## Properties
<a name="aws-properties-s3files-accesspoint-posixuser-properties"></a>

`Gid`  <a name="cfn-s3files-accesspoint-posixuser-gid"></a>
The POSIX group ID used for all file system operations using this access point.
*Required*: Yes
*Type*: String
*Pattern*: `^[0-9]+$`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`SecondaryGids`  <a name="cfn-s3files-accesspoint-posixuser-secondarygids"></a>
Secondary POSIX group IDs used for all file system operations using this access point.
*Required*: No
*Type*: Array of String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Uid`  <a name="cfn-s3files-accesspoint-posixuser-uid"></a>
The POSIX user ID used for all file system operations using this access point.
*Required*: Yes
*Type*: String
*Pattern*: `^[0-9]+$`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
