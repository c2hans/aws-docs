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
