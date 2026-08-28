---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-apptest-testcase-mainframeactionproperties.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::AppTest::TestCase MainframeActionProperties
<a name="aws-properties-apptest-testcase-mainframeactionproperties"></a>

Specifies the mainframe action properties.

## Syntax
<a name="aws-properties-apptest-testcase-mainframeactionproperties-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-apptest-testcase-mainframeactionproperties-syntax.json"></a>

```
{
  "[DmsTaskArn](#cfn-apptest-testcase-mainframeactionproperties-dmstaskarn)" : {{String}}
}
```

### YAML
<a name="aws-properties-apptest-testcase-mainframeactionproperties-syntax.yaml"></a>

```
  [DmsTaskArn](#cfn-apptest-testcase-mainframeactionproperties-dmstaskarn): {{String}}
```

## Properties
<a name="aws-properties-apptest-testcase-mainframeactionproperties-properties"></a>

`DmsTaskArn`  <a name="cfn-apptest-testcase-mainframeactionproperties-dmstaskarn"></a>
The DMS task ARN of the mainframe action properties.
*Required*: No
*Type*: String
*Pattern*: `^\S{1,1000}$`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
