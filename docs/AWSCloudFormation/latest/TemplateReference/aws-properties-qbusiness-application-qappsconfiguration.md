---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-qbusiness-application-qappsconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QBusiness::Application QAppsConfiguration
<a name="aws-properties-qbusiness-application-qappsconfiguration"></a>

Configuration information about Amazon Q Apps.

## Syntax
<a name="aws-properties-qbusiness-application-qappsconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-qbusiness-application-qappsconfiguration-syntax.json"></a>

```
{
  "[QAppsControlMode](#cfn-qbusiness-application-qappsconfiguration-qappscontrolmode)" : {{String}}
}
```

### YAML
<a name="aws-properties-qbusiness-application-qappsconfiguration-syntax.yaml"></a>

```
  [QAppsControlMode](#cfn-qbusiness-application-qappsconfiguration-qappscontrolmode): {{String}}
```

## Properties
<a name="aws-properties-qbusiness-application-qappsconfiguration-properties"></a>

`QAppsControlMode`  <a name="cfn-qbusiness-application-qappsconfiguration-qappscontrolmode"></a>
Status information about whether end users can create and use Amazon Q Apps in the web experience.
*Required*: Yes
*Type*: String
*Allowed values*: `ENABLED | DISABLED`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
