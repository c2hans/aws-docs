---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-cognito-userpool-advancedsecurityadditionalflows.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Cognito::UserPool AdvancedSecurityAdditionalFlows
<a name="aws-properties-cognito-userpool-advancedsecurityadditionalflows"></a>

Threat protection configuration options for additional authentication types in your user pool, including custom authentication.

## Syntax
<a name="aws-properties-cognito-userpool-advancedsecurityadditionalflows-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-cognito-userpool-advancedsecurityadditionalflows-syntax.json"></a>

```
{
  "[CustomAuthMode](#cfn-cognito-userpool-advancedsecurityadditionalflows-customauthmode)" : {{String}}
}
```

### YAML
<a name="aws-properties-cognito-userpool-advancedsecurityadditionalflows-syntax.yaml"></a>

```
  [CustomAuthMode](#cfn-cognito-userpool-advancedsecurityadditionalflows-customauthmode): {{String}}
```

## Properties
<a name="aws-properties-cognito-userpool-advancedsecurityadditionalflows-properties"></a>

`CustomAuthMode`  <a name="cfn-cognito-userpool-advancedsecurityadditionalflows-customauthmode"></a>
The operating mode of threat protection in custom authentication with [ Custom authentication challenge Lambda triggers](https://docs.aws.amazon.com/cognito/latest/developerguide/user-pool-lambda-challenge.html).
*Required*: No
*Type*: String
*Allowed values*: `AUDIT | ENFORCED`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
