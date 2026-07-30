---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-apptest-testcase-output.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::AppTest::TestCase Output
<a name="aws-properties-apptest-testcase-output"></a>

Specifies an output.

## Syntax
<a name="aws-properties-apptest-testcase-output-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-apptest-testcase-output-syntax.json"></a>

```
{
  "[File](#cfn-apptest-testcase-output-file)" : {{OutputFile}}
}
```

### YAML
<a name="aws-properties-apptest-testcase-output-syntax.yaml"></a>

```
  [File](#cfn-apptest-testcase-output-file): {{
    OutputFile}}
```

## Properties
<a name="aws-properties-apptest-testcase-output-properties"></a>

`File`  <a name="cfn-apptest-testcase-output-file"></a>
The file of the output.
*Required*: Yes
*Type*: [OutputFile](aws-properties-apptest-testcase-outputfile.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
