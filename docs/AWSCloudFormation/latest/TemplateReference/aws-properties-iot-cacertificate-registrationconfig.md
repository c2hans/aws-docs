---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-iot-cacertificate-registrationconfig.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::IoT::CACertificate RegistrationConfig
<a name="aws-properties-iot-cacertificate-registrationconfig"></a>

The registration configuration.

## Syntax
<a name="aws-properties-iot-cacertificate-registrationconfig-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-iot-cacertificate-registrationconfig-syntax.json"></a>

```
{
  "[RoleArn](#cfn-iot-cacertificate-registrationconfig-rolearn)" : {{String}},
  "[TemplateBody](#cfn-iot-cacertificate-registrationconfig-templatebody)" : {{String}},
  "[TemplateName](#cfn-iot-cacertificate-registrationconfig-templatename)" : {{String}}
}
```

### YAML
<a name="aws-properties-iot-cacertificate-registrationconfig-syntax.yaml"></a>

```
  [RoleArn](#cfn-iot-cacertificate-registrationconfig-rolearn): {{String}}
  [TemplateBody](#cfn-iot-cacertificate-registrationconfig-templatebody): {{String}}
  [TemplateName](#cfn-iot-cacertificate-registrationconfig-templatename): {{String}}
```

## Properties
<a name="aws-properties-iot-cacertificate-registrationconfig-properties"></a>

`RoleArn`  <a name="cfn-iot-cacertificate-registrationconfig-rolearn"></a>
The ARN of the role.
*Required*: No
*Type*: String
*Pattern*: `arn:(aws[a-zA-Z-]*)?:iam::\d{12}:role/?[a-zA-Z_0-9+=,.@\-_/]+`
*Minimum*: `20`
*Maximum*: `2048`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`TemplateBody`  <a name="cfn-iot-cacertificate-registrationconfig-templatebody"></a>
The template body.
*Required*: No
*Type*: String
*Pattern*: `[\s\S]*`
*Minimum*: `0`
*Maximum*: `10240`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`TemplateName`  <a name="cfn-iot-cacertificate-registrationconfig-templatename"></a>
The name of the provisioning template.
*Required*: No
*Type*: String
*Pattern*: `^[0-9A-Za-z_-]+$`
*Minimum*: `1`
*Maximum*: `36`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
