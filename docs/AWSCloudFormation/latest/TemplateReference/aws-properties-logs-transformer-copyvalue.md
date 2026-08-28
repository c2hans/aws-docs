---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-logs-transformer-copyvalue.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Logs::Transformer CopyValue
<a name="aws-properties-logs-transformer-copyvalue"></a>

This processor copies values within a log event. You can also use this processor to add metadata to log events by copying the values of the following metadata keys into the log events: `@logGroupName`, `@logGroupStream`, `@accountId`, `@regionName`.

For more information about this processor including examples, see [ copyValue](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/CloudWatch-Logs-Transformation-Processors.html#CloudWatch-Logs-Transformation-copyValue) in the *CloudWatch Logs User Guide*.

## Syntax
<a name="aws-properties-logs-transformer-copyvalue-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-logs-transformer-copyvalue-syntax.json"></a>

```
{
  "[Entries](#cfn-logs-transformer-copyvalue-entries)" : {{[ CopyValueEntry, ... ]}}
}
```

### YAML
<a name="aws-properties-logs-transformer-copyvalue-syntax.yaml"></a>

```
  [Entries](#cfn-logs-transformer-copyvalue-entries): {{
    - CopyValueEntry}}
```

## Properties
<a name="aws-properties-logs-transformer-copyvalue-properties"></a>

`Entries`  <a name="cfn-logs-transformer-copyvalue-entries"></a>
An array of `CopyValueEntry` objects, where each object contains the information about one field value to copy.
*Required*: Yes
*Type*: Array of [CopyValueEntry](aws-properties-logs-transformer-copyvalueentry.md)
*Minimum*: `1`
*Maximum*: `5`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
