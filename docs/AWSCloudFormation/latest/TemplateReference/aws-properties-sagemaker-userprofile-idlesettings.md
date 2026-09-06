---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-sagemaker-userprofile-idlesettings.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::SageMaker::UserProfile IdleSettings
<a name="aws-properties-sagemaker-userprofile-idlesettings"></a>

Settings related to idle shutdown of Studio applications.

## Syntax
<a name="aws-properties-sagemaker-userprofile-idlesettings-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-sagemaker-userprofile-idlesettings-syntax.json"></a>

```
{
  "[IdleTimeoutInMinutes](#cfn-sagemaker-userprofile-idlesettings-idletimeoutinminutes)" : {{Integer}},
  "[LifecycleManagement](#cfn-sagemaker-userprofile-idlesettings-lifecyclemanagement)" : {{String}},
  "[MaxIdleTimeoutInMinutes](#cfn-sagemaker-userprofile-idlesettings-maxidletimeoutinminutes)" : {{Integer}},
  "[MinIdleTimeoutInMinutes](#cfn-sagemaker-userprofile-idlesettings-minidletimeoutinminutes)" : {{Integer}}
}
```

### YAML
<a name="aws-properties-sagemaker-userprofile-idlesettings-syntax.yaml"></a>

```
  [IdleTimeoutInMinutes](#cfn-sagemaker-userprofile-idlesettings-idletimeoutinminutes): {{Integer}}
  [LifecycleManagement](#cfn-sagemaker-userprofile-idlesettings-lifecyclemanagement): {{String}}
  [MaxIdleTimeoutInMinutes](#cfn-sagemaker-userprofile-idlesettings-maxidletimeoutinminutes): {{Integer}}
  [MinIdleTimeoutInMinutes](#cfn-sagemaker-userprofile-idlesettings-minidletimeoutinminutes): {{Integer}}
```

## Properties
<a name="aws-properties-sagemaker-userprofile-idlesettings-properties"></a>

`IdleTimeoutInMinutes`  <a name="cfn-sagemaker-userprofile-idlesettings-idletimeoutinminutes"></a>
The time that SageMaker waits after the application becomes idle before shutting it down.
*Required*: No
*Type*: Integer
*Minimum*: `60`
*Maximum*: `525600`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`LifecycleManagement`  <a name="cfn-sagemaker-userprofile-idlesettings-lifecyclemanagement"></a>
Indicates whether idle shutdown is activated for the application type.
*Required*: No
*Type*: String
*Allowed values*: `ENABLED | DISABLED`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`MaxIdleTimeoutInMinutes`  <a name="cfn-sagemaker-userprofile-idlesettings-maxidletimeoutinminutes"></a>
The maximum value in minutes that custom idle shutdown can be set to by the user.
*Required*: No
*Type*: Integer
*Minimum*: `60`
*Maximum*: `525600`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`MinIdleTimeoutInMinutes`  <a name="cfn-sagemaker-userprofile-idlesettings-minidletimeoutinminutes"></a>
The minimum value in minutes that custom idle shutdown can be set to by the user.
*Required*: No
*Type*: Integer
*Minimum*: `60`
*Maximum*: `525600`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
