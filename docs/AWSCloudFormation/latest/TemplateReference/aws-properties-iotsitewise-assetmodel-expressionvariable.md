---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-iotsitewise-assetmodel-expressionvariable.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::IoTSiteWise::AssetModel ExpressionVariable
<a name="aws-properties-iotsitewise-assetmodel-expressionvariable"></a>

Contains expression variable information.

## Syntax
<a name="aws-properties-iotsitewise-assetmodel-expressionvariable-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-iotsitewise-assetmodel-expressionvariable-syntax.json"></a>

```
{
  "[Name](#cfn-iotsitewise-assetmodel-expressionvariable-name)" : {{String}},
  "[Value](#cfn-iotsitewise-assetmodel-expressionvariable-value)" : {{VariableValue}}
}
```

### YAML
<a name="aws-properties-iotsitewise-assetmodel-expressionvariable-syntax.yaml"></a>

```
  [Name](#cfn-iotsitewise-assetmodel-expressionvariable-name): {{String}}
  [Value](#cfn-iotsitewise-assetmodel-expressionvariable-value): {{
    VariableValue}}
```

## Properties
<a name="aws-properties-iotsitewise-assetmodel-expressionvariable-properties"></a>

`Name`  <a name="cfn-iotsitewise-assetmodel-expressionvariable-name"></a>
The friendly name of the variable to be used in the expression.
*Required*: Yes
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Value`  <a name="cfn-iotsitewise-assetmodel-expressionvariable-value"></a>
The variable that identifies an asset property from which to use values.
*Required*: Yes
*Type*: [VariableValue](aws-properties-iotsitewise-assetmodel-variablevalue.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
