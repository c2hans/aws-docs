---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-transfer-user-posixprofile.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Transfer::User PosixProfile
<a name="aws-properties-transfer-user-posixprofile"></a>

The full POSIX identity, including user ID (`Uid`), group ID (`Gid`), and any secondary groups IDs (`SecondaryGids`), that controls your users' access to your Amazon EFS file systems. The POSIX permissions that are set on files and directories in your file system determine the level of access your users get when transferring files into and out of your Amazon EFS file systems.

## Syntax
<a name="aws-properties-transfer-user-posixprofile-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-transfer-user-posixprofile-syntax.json"></a>

```
{
  "[Gid](#cfn-transfer-user-posixprofile-gid)" : {{Number}},
  "[SecondaryGids](#cfn-transfer-user-posixprofile-secondarygids)" : {{[ Number, ... ]}},
  "[Uid](#cfn-transfer-user-posixprofile-uid)" : {{Number}}
}
```

### YAML
<a name="aws-properties-transfer-user-posixprofile-syntax.yaml"></a>

```
  [Gid](#cfn-transfer-user-posixprofile-gid): {{Number}}
  [SecondaryGids](#cfn-transfer-user-posixprofile-secondarygids): {{
    - Number}}
  [Uid](#cfn-transfer-user-posixprofile-uid): {{Number}}
```

## Properties
<a name="aws-properties-transfer-user-posixprofile-properties"></a>

`Gid`  <a name="cfn-transfer-user-posixprofile-gid"></a>
The POSIX group ID used for all EFS operations by this user.
*Required*: Yes
*Type*: Number
*Minimum*: `0`
*Maximum*: `4294967295`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SecondaryGids`  <a name="cfn-transfer-user-posixprofile-secondarygids"></a>
The secondary POSIX group IDs used for all EFS operations by this user.
*Required*: No
*Type*: Array of Number
*Minimum*: `0 | 0`
*Maximum*: `16 | 4294967295`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Uid`  <a name="cfn-transfer-user-posixprofile-uid"></a>
The POSIX user ID used for all EFS operations by this user.
*Required*: Yes
*Type*: Number
*Minimum*: `0`
*Maximum*: `4294967295`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
