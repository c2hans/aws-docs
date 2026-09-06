---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-sagemaker-partnerapp-partnerappconfig.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::SageMaker::PartnerApp PartnerAppConfig
<a name="aws-properties-sagemaker-partnerapp-partnerappconfig"></a>

A collection of configuration settings for the PartnerApp.

## Syntax
<a name="aws-properties-sagemaker-partnerapp-partnerappconfig-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-sagemaker-partnerapp-partnerappconfig-syntax.json"></a>

```
{
  "[AdminUsers](#cfn-sagemaker-partnerapp-partnerappconfig-adminusers)" : {{[ String, ... ]}},
  "[Arguments](#cfn-sagemaker-partnerapp-partnerappconfig-arguments)" : {{{{{Key}}: {{Value}}, ...}}}
}
```

### YAML
<a name="aws-properties-sagemaker-partnerapp-partnerappconfig-syntax.yaml"></a>

```
  [AdminUsers](#cfn-sagemaker-partnerapp-partnerappconfig-adminusers): {{
    - String}}
  [Arguments](#cfn-sagemaker-partnerapp-partnerappconfig-arguments): {{
    {{Key}}: {{Value}}}}
```

## Properties
<a name="aws-properties-sagemaker-partnerapp-partnerappconfig-properties"></a>

`AdminUsers`  <a name="cfn-sagemaker-partnerapp-partnerappconfig-adminusers"></a>
A list of users that will have administrative access to the Partner AI App.
*Required*: No
*Type*: Array of String
*Minimum*: `0`
*Maximum*: `5`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Arguments`  <a name="cfn-sagemaker-partnerapp-partnerappconfig-arguments"></a>
Additional arguments passed to the Partner AI App during initialization or runtime.
*Required*: No
*Type*: Object of String
*Pattern*: `^(?!\s*$).{1,256}$`
*Maximum*: `1024`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
