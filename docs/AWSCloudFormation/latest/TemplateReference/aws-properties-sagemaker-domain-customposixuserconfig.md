---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-sagemaker-domain-customposixuserconfig.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::SageMaker::Domain CustomPosixUserConfig
<a name="aws-properties-sagemaker-domain-customposixuserconfig"></a>

Details about the POSIX identity that is used for file system operations.

## Syntax
<a name="aws-properties-sagemaker-domain-customposixuserconfig-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-sagemaker-domain-customposixuserconfig-syntax.json"></a>

```
{
  "[Gid](#cfn-sagemaker-domain-customposixuserconfig-gid)" : {{Integer}},
  "[Uid](#cfn-sagemaker-domain-customposixuserconfig-uid)" : {{Integer}}
}
```

### YAML
<a name="aws-properties-sagemaker-domain-customposixuserconfig-syntax.yaml"></a>

```
  [Gid](#cfn-sagemaker-domain-customposixuserconfig-gid): {{Integer}}
  [Uid](#cfn-sagemaker-domain-customposixuserconfig-uid): {{Integer}}
```

## Properties
<a name="aws-properties-sagemaker-domain-customposixuserconfig-properties"></a>

`Gid`  <a name="cfn-sagemaker-domain-customposixuserconfig-gid"></a>
The POSIX group ID.
*Required*: Yes
*Type*: Integer
*Minimum*: `1001`
*Maximum*: `4000000`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Uid`  <a name="cfn-sagemaker-domain-customposixuserconfig-uid"></a>
The POSIX user ID.
*Required*: Yes
*Type*: Integer
*Minimum*: `10000`
*Maximum*: `4000000`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
