---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-amplify-app-environmentvariable.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Amplify::App EnvironmentVariable
<a name="aws-properties-amplify-app-environmentvariable"></a>

Environment variables are key-value pairs that are available at build time. Set environment variables for all branches in your app.

## Syntax
<a name="aws-properties-amplify-app-environmentvariable-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-amplify-app-environmentvariable-syntax.json"></a>

```
{
  "[Name](#cfn-amplify-app-environmentvariable-name)" : {{String}},
  "[Value](#cfn-amplify-app-environmentvariable-value)" : {{String}}
}
```

### YAML
<a name="aws-properties-amplify-app-environmentvariable-syntax.yaml"></a>

```
  [Name](#cfn-amplify-app-environmentvariable-name): {{String}}
  [Value](#cfn-amplify-app-environmentvariable-value): {{String}}
```

## Properties
<a name="aws-properties-amplify-app-environmentvariable-properties"></a>

`Name`  <a name="cfn-amplify-app-environmentvariable-name"></a>
The environment variable name.
*Required*: Yes
*Type*: String
*Pattern*: `(?s).*`
*Maximum*: `255`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Value`  <a name="cfn-amplify-app-environmentvariable-value"></a>
The environment variable value.
*Required*: Yes
*Type*: String
*Pattern*: `(?s).*`
*Maximum*: `5500`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
