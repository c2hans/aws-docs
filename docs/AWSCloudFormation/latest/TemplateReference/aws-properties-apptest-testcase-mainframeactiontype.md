---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-apptest-testcase-mainframeactiontype.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::AppTest::TestCase MainframeActionType
<a name="aws-properties-apptest-testcase-mainframeactiontype"></a>

Specifies the mainframe action type.

## Syntax
<a name="aws-properties-apptest-testcase-mainframeactiontype-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-apptest-testcase-mainframeactiontype-syntax.json"></a>

```
{
  "[Batch](#cfn-apptest-testcase-mainframeactiontype-batch)" : {{Batch}},
  "[Tn3270](#cfn-apptest-testcase-mainframeactiontype-tn3270)" : {{TN3270}}
}
```

### YAML
<a name="aws-properties-apptest-testcase-mainframeactiontype-syntax.yaml"></a>

```
  [Batch](#cfn-apptest-testcase-mainframeactiontype-batch): {{
    Batch}}
  [Tn3270](#cfn-apptest-testcase-mainframeactiontype-tn3270): {{
    TN3270}}
```

## Properties
<a name="aws-properties-apptest-testcase-mainframeactiontype-properties"></a>

`Batch`  <a name="cfn-apptest-testcase-mainframeactiontype-batch"></a>
The batch of the mainframe action type.
*Required*: No
*Type*: [Batch](aws-properties-apptest-testcase-batch.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Tn3270`  <a name="cfn-apptest-testcase-mainframeactiontype-tn3270"></a>
The tn3270 port of the mainframe action type.
*Required*: No
*Type*: [TN3270](aws-properties-apptest-testcase-tn3270.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
