---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-sagemaker-userprofile-customposixuserconfig.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::SageMaker::UserProfile CustomPosixUserConfig
<a name="aws-properties-sagemaker-userprofile-customposixuserconfig"></a>

Details about the POSIX identity that is used for file system operations.

## Syntax
<a name="aws-properties-sagemaker-userprofile-customposixuserconfig-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-sagemaker-userprofile-customposixuserconfig-syntax.json"></a>

```
{
  "[Gid](#cfn-sagemaker-userprofile-customposixuserconfig-gid)" : {{Integer}},
  "[Uid](#cfn-sagemaker-userprofile-customposixuserconfig-uid)" : {{Integer}}
}
```

### YAML
<a name="aws-properties-sagemaker-userprofile-customposixuserconfig-syntax.yaml"></a>

```
  [Gid](#cfn-sagemaker-userprofile-customposixuserconfig-gid): {{Integer}}
  [Uid](#cfn-sagemaker-userprofile-customposixuserconfig-uid): {{Integer}}
```

## Properties
<a name="aws-properties-sagemaker-userprofile-customposixuserconfig-properties"></a>

`Gid`  <a name="cfn-sagemaker-userprofile-customposixuserconfig-gid"></a>
The POSIX group ID.
*Required*: Yes
*Type*: Integer
*Minimum*: `1001`
*Maximum*: `4000000`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Uid`  <a name="cfn-sagemaker-userprofile-customposixuserconfig-uid"></a>
The POSIX user ID.
*Required*: Yes
*Type*: Integer
*Minimum*: `10000`
*Maximum*: `4000000`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
