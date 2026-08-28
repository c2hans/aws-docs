---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-apptest-testcase-outputfile.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::AppTest::TestCase OutputFile
<a name="aws-properties-apptest-testcase-outputfile"></a>

Specifies an output file.

## Syntax
<a name="aws-properties-apptest-testcase-outputfile-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-apptest-testcase-outputfile-syntax.json"></a>

```
{
  "[FileLocation](#cfn-apptest-testcase-outputfile-filelocation)" : {{String}}
}
```

### YAML
<a name="aws-properties-apptest-testcase-outputfile-syntax.yaml"></a>

```
  [FileLocation](#cfn-apptest-testcase-outputfile-filelocation): {{String}}
```

## Properties
<a name="aws-properties-apptest-testcase-outputfile-properties"></a>

`FileLocation`  <a name="cfn-apptest-testcase-outputfile-filelocation"></a>
The file location of the output file.
*Required*: No
*Type*: String
*Minimum*: `0`
*Maximum*: `1024`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
