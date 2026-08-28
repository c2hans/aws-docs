---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-apptest-testcase-script.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::AppTest::TestCase Script
<a name="aws-properties-apptest-testcase-script"></a>

Specifies the script.

## Syntax
<a name="aws-properties-apptest-testcase-script-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-apptest-testcase-script-syntax.json"></a>

```
{
  "[ScriptLocation](#cfn-apptest-testcase-script-scriptlocation)" : {{String}},
  "[Type](#cfn-apptest-testcase-script-type)" : {{String}}
}
```

### YAML
<a name="aws-properties-apptest-testcase-script-syntax.yaml"></a>

```
  [ScriptLocation](#cfn-apptest-testcase-script-scriptlocation): {{String}}
  [Type](#cfn-apptest-testcase-script-type): {{String}}
```

## Properties
<a name="aws-properties-apptest-testcase-script-properties"></a>

`ScriptLocation`  <a name="cfn-apptest-testcase-script-scriptlocation"></a>
The script location of the scripts.
*Required*: Yes
*Type*: String
*Minimum*: `0`
*Maximum*: `1024`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Type`  <a name="cfn-apptest-testcase-script-type"></a>
The type of the scripts.
*Required*: Yes
*Type*: String
*Allowed values*: `Selenium`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
