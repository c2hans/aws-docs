---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-amplify-branch-environmentvariable.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Amplify::Branch EnvironmentVariable
<a name="aws-properties-amplify-branch-environmentvariable"></a>

The EnvironmentVariable property type sets environment variables for a specific branch. Environment variables are key-value pairs that are available at build time.

## Syntax
<a name="aws-properties-amplify-branch-environmentvariable-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-amplify-branch-environmentvariable-syntax.json"></a>

```
{
  "[Name](#cfn-amplify-branch-environmentvariable-name)" : {{String}},
  "[Value](#cfn-amplify-branch-environmentvariable-value)" : {{String}}
}
```

### YAML
<a name="aws-properties-amplify-branch-environmentvariable-syntax.yaml"></a>

```
  [Name](#cfn-amplify-branch-environmentvariable-name): {{String}}
  [Value](#cfn-amplify-branch-environmentvariable-value): {{String}}
```

## Properties
<a name="aws-properties-amplify-branch-environmentvariable-properties"></a>

`Name`  <a name="cfn-amplify-branch-environmentvariable-name"></a>
The environment variable name.
*Required*: Yes
*Type*: String
*Pattern*: `(?s).*`
*Maximum*: `255`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Value`  <a name="cfn-amplify-branch-environmentvariable-value"></a>
The environment variable value.
*Required*: Yes
*Type*: String
*Pattern*: `(?s).*`
*Maximum*: `5500`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
