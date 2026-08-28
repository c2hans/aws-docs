---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-amplifyuibuilder-theme.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::AmplifyUIBuilder::Theme
<a name="aws-resource-amplifyuibuilder-theme"></a>

The AWS::AmplifyUIBuilder::Theme resource specifies a theme within an Amplify app. A theme is a collection of style settings that apply globally to the components associated with the app.

## Syntax
<a name="aws-resource-amplifyuibuilder-theme-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-amplifyuibuilder-theme-syntax.json"></a>

```
{
  "Type" : "AWS::AmplifyUIBuilder::Theme",
  "Properties" : {
      "[AppId](#cfn-amplifyuibuilder-theme-appid)" : {{String}},
      "[EnvironmentName](#cfn-amplifyuibuilder-theme-environmentname)" : {{String}},
      "[Name](#cfn-amplifyuibuilder-theme-name)" : {{String}},
      "[Overrides](#cfn-amplifyuibuilder-theme-overrides)" : {{[ ThemeValues, ... ]}},
      "[Tags](#cfn-amplifyuibuilder-theme-tags)" : {{{{{Key}}: {{Value}}, ...}}},
      "[Values](#cfn-amplifyuibuilder-theme-values)" : {{[ ThemeValues, ... ]}}
    }
}
```

### YAML
<a name="aws-resource-amplifyuibuilder-theme-syntax.yaml"></a>

```
Type: AWS::AmplifyUIBuilder::Theme
Properties:
  [AppId](#cfn-amplifyuibuilder-theme-appid): {{String}}
  [EnvironmentName](#cfn-amplifyuibuilder-theme-environmentname): {{String}}
  [Name](#cfn-amplifyuibuilder-theme-name): {{String}}
  [Overrides](#cfn-amplifyuibuilder-theme-overrides): {{
    - ThemeValues}}
  [Tags](#cfn-amplifyuibuilder-theme-tags): {{
    {{Key}}: {{Value}}}}
  [Values](#cfn-amplifyuibuilder-theme-values): {{
    - ThemeValues}}
```

## Properties
<a name="aws-resource-amplifyuibuilder-theme-properties"></a>

`AppId`  <a name="cfn-amplifyuibuilder-theme-appid"></a>
The unique ID for the Amplify app associated with the theme.
*Required*: No
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`EnvironmentName`  <a name="cfn-amplifyuibuilder-theme-environmentname"></a>
The name of the backend environment that is a part of the Amplify app.
*Required*: No
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Name`  <a name="cfn-amplifyuibuilder-theme-name"></a>
The name of the theme.
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `255`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Overrides`  <a name="cfn-amplifyuibuilder-theme-overrides"></a>
Describes the properties that can be overriden to customize a theme.
*Required*: No
*Type*: Array of [ThemeValues](aws-properties-amplifyuibuilder-theme-themevalues.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Tags`  <a name="cfn-amplifyuibuilder-theme-tags"></a>
One or more key-value pairs to use when tagging the theme.
*Required*: No
*Type*: Object of String
*Pattern*: `^(?!aws:)[a-zA-Z+-=._:/]+$`
*Minimum*: `1`
*Maximum*: `256`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Values`  <a name="cfn-amplifyuibuilder-theme-values"></a>
A list of key-value pairs that defines the properties of the theme.
*Required*: No
*Type*: Array of [ThemeValues](aws-properties-amplifyuibuilder-theme-themevalues.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-amplifyuibuilder-theme-return-values"></a>

### Fn::GetAtt
<a name="aws-resource-amplifyuibuilder-theme-return-values-fn--getatt"></a>

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [`Fn::GetAtt`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-getatt.html).

####
<a name="aws-resource-amplifyuibuilder-theme-return-values-fn--getatt-fn--getatt"></a>

`CreatedAt`  <a name="CreatedAt-fn::getatt"></a>
The time that the theme was created.

`Id`  <a name="Id-fn::getatt"></a>
The ID for the theme.

`ModifiedAt`  <a name="ModifiedAt-fn::getatt"></a>
The time that the theme was modified.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
