---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-cognito-userpool-userpooladdons.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Cognito::UserPool UserPoolAddOns
<a name="aws-properties-cognito-userpool-userpooladdons"></a>

User pool add-ons. Contains settings for activation of threat protection. To log user security information but take no action, set to `AUDIT`. To configure automatic security responses to risky traffic to your user pool, set to `ENFORCED`.

For more information, see [Adding advanced security to a user pool](https://docs.aws.amazon.com/cognito/latest/developerguide/cognito-user-pool-settings-advanced-security.html). To activate this setting, your user pool must be on the [ Plus tier](https://docs.aws.amazon.com/cognito/latest/developerguide/feature-plans-features-plus.html).

## Syntax
<a name="aws-properties-cognito-userpool-userpooladdons-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-cognito-userpool-userpooladdons-syntax.json"></a>

```
{
  "[AdvancedSecurityAdditionalFlows](#cfn-cognito-userpool-userpooladdons-advancedsecurityadditionalflows)" : {{AdvancedSecurityAdditionalFlows}},
  "[AdvancedSecurityMode](#cfn-cognito-userpool-userpooladdons-advancedsecuritymode)" : {{String}}
}
```

### YAML
<a name="aws-properties-cognito-userpool-userpooladdons-syntax.yaml"></a>

```
  [AdvancedSecurityAdditionalFlows](#cfn-cognito-userpool-userpooladdons-advancedsecurityadditionalflows): {{
    AdvancedSecurityAdditionalFlows}}
  [AdvancedSecurityMode](#cfn-cognito-userpool-userpooladdons-advancedsecuritymode): {{String}}
```

## Properties
<a name="aws-properties-cognito-userpool-userpooladdons-properties"></a>

`AdvancedSecurityAdditionalFlows`  <a name="cfn-cognito-userpool-userpooladdons-advancedsecurityadditionalflows"></a>
Threat protection configuration options for additional authentication types in your user pool, including custom authentication.
*Required*: No
*Type*: [AdvancedSecurityAdditionalFlows](aws-properties-cognito-userpool-advancedsecurityadditionalflows.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`AdvancedSecurityMode`  <a name="cfn-cognito-userpool-userpooladdons-advancedsecuritymode"></a>
The operating mode of threat protection for standard authentication types in your user pool, including username-password and secure remote password (SRP) authentication.
*Required*: No
*Type*: String
*Allowed values*: `OFF | AUDIT | ENFORCED`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
