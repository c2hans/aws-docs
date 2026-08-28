---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-qbusiness-application-personalizationconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QBusiness::Application PersonalizationConfiguration
<a name="aws-properties-qbusiness-application-personalizationconfiguration"></a>

Configuration information about chat response personalization. For more information, see [Personalizing chat responses](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/personalizing-chat-responses.html).

## Syntax
<a name="aws-properties-qbusiness-application-personalizationconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-qbusiness-application-personalizationconfiguration-syntax.json"></a>

```
{
  "[PersonalizationControlMode](#cfn-qbusiness-application-personalizationconfiguration-personalizationcontrolmode)" : {{String}}
}
```

### YAML
<a name="aws-properties-qbusiness-application-personalizationconfiguration-syntax.yaml"></a>

```
  [PersonalizationControlMode](#cfn-qbusiness-application-personalizationconfiguration-personalizationcontrolmode): {{String}}
```

## Properties
<a name="aws-properties-qbusiness-application-personalizationconfiguration-properties"></a>

`PersonalizationControlMode`  <a name="cfn-qbusiness-application-personalizationconfiguration-personalizationcontrolmode"></a>
An option to allow Amazon Q Business to customize chat responses using user specific metadata—specifically, location and job information—in your IAM Identity Center instance.
*Required*: Yes
*Type*: String
*Allowed values*: `ENABLED | DISABLED`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
