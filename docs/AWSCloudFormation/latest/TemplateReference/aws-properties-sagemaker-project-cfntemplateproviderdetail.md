---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-sagemaker-project-cfntemplateproviderdetail.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::SageMaker::Project CfnTemplateProviderDetail
<a name="aws-properties-sagemaker-project-cfntemplateproviderdetail"></a>

 Details about a CloudFormation template provider configuration and associated provisioning information.

## Syntax
<a name="aws-properties-sagemaker-project-cfntemplateproviderdetail-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-sagemaker-project-cfntemplateproviderdetail-syntax.json"></a>

```
{
  "[Parameters](#cfn-sagemaker-project-cfntemplateproviderdetail-parameters)" : {{[ CfnStackParameter, ... ]}},
  "[RoleARN](#cfn-sagemaker-project-cfntemplateproviderdetail-rolearn)" : {{String}},
  "[TemplateName](#cfn-sagemaker-project-cfntemplateproviderdetail-templatename)" : {{String}},
  "[TemplateURL](#cfn-sagemaker-project-cfntemplateproviderdetail-templateurl)" : {{String}}
}
```

### YAML
<a name="aws-properties-sagemaker-project-cfntemplateproviderdetail-syntax.yaml"></a>

```
  [Parameters](#cfn-sagemaker-project-cfntemplateproviderdetail-parameters): {{
    - CfnStackParameter}}
  [RoleARN](#cfn-sagemaker-project-cfntemplateproviderdetail-rolearn): {{String}}
  [TemplateName](#cfn-sagemaker-project-cfntemplateproviderdetail-templatename): {{String}}
  [TemplateURL](#cfn-sagemaker-project-cfntemplateproviderdetail-templateurl): {{String}}
```

## Properties
<a name="aws-properties-sagemaker-project-cfntemplateproviderdetail-properties"></a>

`Parameters`  <a name="cfn-sagemaker-project-cfntemplateproviderdetail-parameters"></a>
 An array of CloudFormation stack parameters.
*Required*: No
*Type*: Array of [CfnStackParameter](aws-properties-sagemaker-project-cfnstackparameter.md)
*Minimum*: `0`
*Maximum*: `180`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`RoleARN`  <a name="cfn-sagemaker-project-cfntemplateproviderdetail-rolearn"></a>
 The IAM role used by CloudFormation to create the stack.
*Required*: No
*Type*: String
*Pattern*: `arn:aws[a-z\-]*:iam::\d{12}:role/?[a-zA-Z_0-9+=,.@\-_/]+`
*Minimum*: `20`
*Maximum*: `2048`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`TemplateName`  <a name="cfn-sagemaker-project-cfntemplateproviderdetail-templatename"></a>
 The unique identifier of the template within the project.
*Required*: Yes
*Type*: String
*Pattern*: `(?=.{1,32}$)[a-zA-Z0-9](-*[a-zA-Z0-9])*`
*Minimum*: `1`
*Maximum*: `32`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`TemplateURL`  <a name="cfn-sagemaker-project-cfntemplateproviderdetail-templateurl"></a>
 The Amazon S3 URL of the CloudFormation template.
*Required*: Yes
*Type*: String
*Pattern*: `(?=.{1,1024}$)(https)://([^/]+)/(.+)`
*Minimum*: `1`
*Maximum*: `1024`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
