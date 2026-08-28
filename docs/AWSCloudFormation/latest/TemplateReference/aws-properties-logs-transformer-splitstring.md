---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-logs-transformer-splitstring.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Logs::Transformer SplitString
<a name="aws-properties-logs-transformer-splitstring"></a>

Use this processor to split a field into an array of strings using a delimiting character.

For more information about this processor including examples, see [ splitString](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/CloudWatch-Logs-Transformation-Processors.html#CloudWatch-Logs-Transformation-splitString) in the *CloudWatch Logs User Guide*.

## Syntax
<a name="aws-properties-logs-transformer-splitstring-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-logs-transformer-splitstring-syntax.json"></a>

```
{
  "[Entries](#cfn-logs-transformer-splitstring-entries)" : {{[ SplitStringEntry, ... ]}}
}
```

### YAML
<a name="aws-properties-logs-transformer-splitstring-syntax.yaml"></a>

```
  [Entries](#cfn-logs-transformer-splitstring-entries): {{
    - SplitStringEntry}}
```

## Properties
<a name="aws-properties-logs-transformer-splitstring-properties"></a>

`Entries`  <a name="cfn-logs-transformer-splitstring-entries"></a>
An array of `SplitStringEntry` objects, where each object contains the information about one field to split.
*Required*: Yes
*Type*: Array of [SplitStringEntry](aws-properties-logs-transformer-splitstringentry.md)
*Minimum*: `1`
*Maximum*: `10`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
