---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-apptest-testcase-tn3270.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::AppTest::TestCase TN3270
<a name="aws-properties-apptest-testcase-tn3270"></a>

Specifies the TN3270 protocol.

## Syntax
<a name="aws-properties-apptest-testcase-tn3270-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-apptest-testcase-tn3270-syntax.json"></a>

```
{
  "[ExportDataSetNames](#cfn-apptest-testcase-tn3270-exportdatasetnames)" : {{[ String, ... ]}},
  "[Script](#cfn-apptest-testcase-tn3270-script)" : {{Script}}
}
```

### YAML
<a name="aws-properties-apptest-testcase-tn3270-syntax.yaml"></a>

```
  [ExportDataSetNames](#cfn-apptest-testcase-tn3270-exportdatasetnames): {{
    - String}}
  [Script](#cfn-apptest-testcase-tn3270-script): {{
    Script}}
```

## Properties
<a name="aws-properties-apptest-testcase-tn3270-properties"></a>

`ExportDataSetNames`  <a name="cfn-apptest-testcase-tn3270-exportdatasetnames"></a>
The data set names of the TN3270 protocol.
*Required*: No
*Type*: Array of String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Script`  <a name="cfn-apptest-testcase-tn3270-script"></a>
The script of the TN3270 protocol.
*Required*: Yes
*Type*: [Script](aws-properties-apptest-testcase-script.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
