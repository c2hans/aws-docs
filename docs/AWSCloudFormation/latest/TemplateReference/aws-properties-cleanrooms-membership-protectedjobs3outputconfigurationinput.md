---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-cleanrooms-membership-protectedjobs3outputconfigurationinput.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::CleanRooms::Membership ProtectedJobS3OutputConfigurationInput
<a name="aws-properties-cleanrooms-membership-protectedjobs3outputconfigurationinput"></a>

Contains input information for protected jobs with an S3 output type.

## Syntax
<a name="aws-properties-cleanrooms-membership-protectedjobs3outputconfigurationinput-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-cleanrooms-membership-protectedjobs3outputconfigurationinput-syntax.json"></a>

```
{
  "[Bucket](#cfn-cleanrooms-membership-protectedjobs3outputconfigurationinput-bucket)" : {{String}},
  "[KeyPrefix](#cfn-cleanrooms-membership-protectedjobs3outputconfigurationinput-keyprefix)" : {{String}}
}
```

### YAML
<a name="aws-properties-cleanrooms-membership-protectedjobs3outputconfigurationinput-syntax.yaml"></a>

```
  [Bucket](#cfn-cleanrooms-membership-protectedjobs3outputconfigurationinput-bucket): {{String}}
  [KeyPrefix](#cfn-cleanrooms-membership-protectedjobs3outputconfigurationinput-keyprefix): {{String}}
```

## Properties
<a name="aws-properties-cleanrooms-membership-protectedjobs3outputconfigurationinput-properties"></a>

`Bucket`  <a name="cfn-cleanrooms-membership-protectedjobs3outputconfigurationinput-bucket"></a>
 The S3 bucket for job output.
*Required*: Yes
*Type*: String
*Minimum*: `3`
*Maximum*: `63`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`KeyPrefix`  <a name="cfn-cleanrooms-membership-protectedjobs3outputconfigurationinput-keyprefix"></a>
The S3 prefix to unload the protected job results.
*Required*: No
*Type*: String
*Pattern*: `[\w!.=*/-]*`
*Minimum*: `0`
*Maximum*: `512`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
