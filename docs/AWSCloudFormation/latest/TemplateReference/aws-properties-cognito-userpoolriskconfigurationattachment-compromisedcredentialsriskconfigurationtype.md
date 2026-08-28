---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-cognito-userpoolriskconfigurationattachment-compromisedcredentialsriskconfigurationtype.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Cognito::UserPoolRiskConfigurationAttachment CompromisedCredentialsRiskConfigurationType
<a name="aws-properties-cognito-userpoolriskconfigurationattachment-compromisedcredentialsriskconfigurationtype"></a>

Settings for compromised-credentials actions and authentication-event sources with advanced security features in full-function `ENFORCED` mode.

## Syntax
<a name="aws-properties-cognito-userpoolriskconfigurationattachment-compromisedcredentialsriskconfigurationtype-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-cognito-userpoolriskconfigurationattachment-compromisedcredentialsriskconfigurationtype-syntax.json"></a>

```
{
  "[Actions](#cfn-cognito-userpoolriskconfigurationattachment-compromisedcredentialsriskconfigurationtype-actions)" : {{CompromisedCredentialsActionsType}},
  "[EventFilter](#cfn-cognito-userpoolriskconfigurationattachment-compromisedcredentialsriskconfigurationtype-eventfilter)" : {{[ String, ... ]}}
}
```

### YAML
<a name="aws-properties-cognito-userpoolriskconfigurationattachment-compromisedcredentialsriskconfigurationtype-syntax.yaml"></a>

```
  [Actions](#cfn-cognito-userpoolriskconfigurationattachment-compromisedcredentialsriskconfigurationtype-actions): {{
    CompromisedCredentialsActionsType}}
  [EventFilter](#cfn-cognito-userpoolriskconfigurationattachment-compromisedcredentialsriskconfigurationtype-eventfilter): {{
    - String}}
```

## Properties
<a name="aws-properties-cognito-userpoolriskconfigurationattachment-compromisedcredentialsriskconfigurationtype-properties"></a>

`Actions`  <a name="cfn-cognito-userpoolriskconfigurationattachment-compromisedcredentialsriskconfigurationtype-actions"></a>
Settings for the actions that you want your user pool to take when Amazon Cognito detects compromised credentials.
*Required*: Yes
*Type*: [CompromisedCredentialsActionsType](aws-properties-cognito-userpoolriskconfigurationattachment-compromisedcredentialsactionstype.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`EventFilter`  <a name="cfn-cognito-userpoolriskconfigurationattachment-compromisedcredentialsriskconfigurationtype-eventfilter"></a>
Settings for the sign-in activity where you want to configure compromised-credentials actions. Defaults to all events.
*Required*: No
*Type*: Array of String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
