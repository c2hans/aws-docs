---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-sagemaker-userprofile-fsxlustrefilesystemconfig.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::SageMaker::UserProfile FSxLustreFileSystemConfig
<a name="aws-properties-sagemaker-userprofile-fsxlustrefilesystemconfig"></a>

The settings for assigning a custom Amazon FSx for Lustre file system to a user profile or space for an Amazon SageMaker Domain.

## Syntax
<a name="aws-properties-sagemaker-userprofile-fsxlustrefilesystemconfig-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-sagemaker-userprofile-fsxlustrefilesystemconfig-syntax.json"></a>

```
{
  "[FileSystemId](#cfn-sagemaker-userprofile-fsxlustrefilesystemconfig-filesystemid)" : {{String}},
  "[FileSystemPath](#cfn-sagemaker-userprofile-fsxlustrefilesystemconfig-filesystempath)" : {{String}}
}
```

### YAML
<a name="aws-properties-sagemaker-userprofile-fsxlustrefilesystemconfig-syntax.yaml"></a>

```
  [FileSystemId](#cfn-sagemaker-userprofile-fsxlustrefilesystemconfig-filesystemid): {{String}}
  [FileSystemPath](#cfn-sagemaker-userprofile-fsxlustrefilesystemconfig-filesystempath): {{String}}
```

## Properties
<a name="aws-properties-sagemaker-userprofile-fsxlustrefilesystemconfig-properties"></a>

`FileSystemId`  <a name="cfn-sagemaker-userprofile-fsxlustrefilesystemconfig-filesystemid"></a>
The globally unique, 17-digit, ID of the file system, assigned by Amazon FSx for Lustre.
*Required*: Yes
*Type*: String
*Pattern*: `^(fs-[0-9a-f]{8,})$`
*Minimum*: `11`
*Maximum*: `21`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`FileSystemPath`  <a name="cfn-sagemaker-userprofile-fsxlustrefilesystemconfig-filesystempath"></a>
The path to the file system directory that is accessible in Amazon SageMaker Studio. Permitted users can access only this directory and below.
*Required*: No
*Type*: String
*Pattern*: `^\/\S*$`
*Minimum*: `1`
*Maximum*: `256`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
