---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-apptest-testcase-compareaction.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::AppTest::TestCase CompareAction
<a name="aws-properties-apptest-testcase-compareaction"></a>

Compares the action.

## Syntax
<a name="aws-properties-apptest-testcase-compareaction-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-apptest-testcase-compareaction-syntax.json"></a>

```
{
  "[Input](#cfn-apptest-testcase-compareaction-input)" : {{Input}},
  "[Output](#cfn-apptest-testcase-compareaction-output)" : {{Output}}
}
```

### YAML
<a name="aws-properties-apptest-testcase-compareaction-syntax.yaml"></a>

```
  [Input](#cfn-apptest-testcase-compareaction-input): {{
    Input}}
  [Output](#cfn-apptest-testcase-compareaction-output): {{
    Output}}
```

## Properties
<a name="aws-properties-apptest-testcase-compareaction-properties"></a>

`Input`  <a name="cfn-apptest-testcase-compareaction-input"></a>
The input of the compare action.
*Required*: Yes
*Type*: [Input](aws-properties-apptest-testcase-input.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Output`  <a name="cfn-apptest-testcase-compareaction-output"></a>
The output of the compare action.
*Required*: No
*Type*: [Output](aws-properties-apptest-testcase-output.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
