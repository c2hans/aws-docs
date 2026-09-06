---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-fis-targetaccountconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::FIS::TargetAccountConfiguration
<a name="aws-resource-fis-targetaccountconfiguration"></a>

Creates a target account configuration for the experiment template. A target account configuration is required when `accountTargeting` of `experimentOptions` is set to `multi-account`. For more information, see [experiment options](https://docs.aws.amazon.com/fis/latest/userguide/experiment-options.html) in the *AWS Fault Injection Service User Guide*.

## Syntax
<a name="aws-resource-fis-targetaccountconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-fis-targetaccountconfiguration-syntax.json"></a>

```
{
  "Type" : "AWS::FIS::TargetAccountConfiguration",
  "Properties" : {
      "[AccountId](#cfn-fis-targetaccountconfiguration-accountid)" : {{String}},
      "[Description](#cfn-fis-targetaccountconfiguration-description)" : {{String}},
      "[ExperimentTemplateId](#cfn-fis-targetaccountconfiguration-experimenttemplateid)" : {{String}},
      "[RoleArn](#cfn-fis-targetaccountconfiguration-rolearn)" : {{String}}
    }
}
```

### YAML
<a name="aws-resource-fis-targetaccountconfiguration-syntax.yaml"></a>

```
Type: AWS::FIS::TargetAccountConfiguration
Properties:
  [AccountId](#cfn-fis-targetaccountconfiguration-accountid): {{String}}
  [Description](#cfn-fis-targetaccountconfiguration-description): {{String}}
  [ExperimentTemplateId](#cfn-fis-targetaccountconfiguration-experimenttemplateid): {{String}}
  [RoleArn](#cfn-fis-targetaccountconfiguration-rolearn): {{String}}
```

## Properties
<a name="aws-resource-fis-targetaccountconfiguration-properties"></a>

`AccountId`  <a name="cfn-fis-targetaccountconfiguration-accountid"></a>
The AWS account ID of the target account.
*Required*: Yes
*Type*: String
*Maximum*: `512`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Description`  <a name="cfn-fis-targetaccountconfiguration-description"></a>
The description of the target account.
*Required*: No
*Type*: String
*Maximum*: `512`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ExperimentTemplateId`  <a name="cfn-fis-targetaccountconfiguration-experimenttemplateid"></a>
The ID of the experiment template.
*Required*: Yes
*Type*: String
*Pattern*: `[\S]+`
*Maximum*: `64`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`RoleArn`  <a name="cfn-fis-targetaccountconfiguration-rolearn"></a>
The Amazon Resource Name (ARN) of an IAM role for the target account.
*Required*: Yes
*Type*: String
*Maximum*: `1224`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-fis-targetaccountconfiguration-return-values"></a>

### Ref
<a name="aws-resource-fis-targetaccountconfiguration-return-values-ref"></a>
