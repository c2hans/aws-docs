---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-lambda-function-snapstart.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Lambda::Function SnapStart
<a name="aws-properties-lambda-function-snapstart"></a>

The function's [AWS Lambda SnapStart](https://docs.aws.amazon.com/lambda/latest/dg/snapstart.html) setting.

## Syntax
<a name="aws-properties-lambda-function-snapstart-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-lambda-function-snapstart-syntax.json"></a>

```
{
  "[ApplyOn](#cfn-lambda-function-snapstart-applyon)" : {{String}}
}
```

### YAML
<a name="aws-properties-lambda-function-snapstart-syntax.yaml"></a>

```
  [ApplyOn](#cfn-lambda-function-snapstart-applyon): {{String}}
```

## Properties
<a name="aws-properties-lambda-function-snapstart-properties"></a>

`ApplyOn`  <a name="cfn-lambda-function-snapstart-applyon"></a>
Set `ApplyOn` to `PublishedVersions` to create a snapshot of the initialized execution environment when you publish a function version.
*Required*: Yes
*Type*: String
*Allowed values*: `PublishedVersions | None`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
