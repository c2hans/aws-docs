---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-apptest-testcase-input.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::AppTest::TestCase Input
<a name="aws-properties-apptest-testcase-input"></a>

Specifies the input.

## Syntax
<a name="aws-properties-apptest-testcase-input-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-apptest-testcase-input-syntax.json"></a>

```
{
  "[File](#cfn-apptest-testcase-input-file)" : {{InputFile}}
}
```

### YAML
<a name="aws-properties-apptest-testcase-input-syntax.yaml"></a>

```
  [File](#cfn-apptest-testcase-input-file): {{
    InputFile}}
```

## Properties
<a name="aws-properties-apptest-testcase-input-properties"></a>

`File`  <a name="cfn-apptest-testcase-input-file"></a>
The file in the input.
*Required*: Yes
*Type*: [InputFile](aws-properties-apptest-testcase-inputfile.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
