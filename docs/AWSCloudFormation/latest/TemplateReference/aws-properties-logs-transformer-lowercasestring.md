---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-logs-transformer-lowercasestring.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Logs::Transformer LowerCaseString
<a name="aws-properties-logs-transformer-lowercasestring"></a>

This processor converts a string to lowercase.

For more information about this processor including examples, see [ lowerCaseString](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/CloudWatch-Logs-Transformation-Processors.html#CloudWatch-Logs-Transformation-lowerCaseString) in the *CloudWatch Logs User Guide*.

## Syntax
<a name="aws-properties-logs-transformer-lowercasestring-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-logs-transformer-lowercasestring-syntax.json"></a>

```
{
  "[WithKeys](#cfn-logs-transformer-lowercasestring-withkeys)" : {{[ String, ... ]}}
}
```

### YAML
<a name="aws-properties-logs-transformer-lowercasestring-syntax.yaml"></a>

```
  [WithKeys](#cfn-logs-transformer-lowercasestring-withkeys): {{
    - String}}
```

## Properties
<a name="aws-properties-logs-transformer-lowercasestring-properties"></a>

`WithKeys`  <a name="cfn-logs-transformer-lowercasestring-withkeys"></a>
The array caontaining the keys of the fields to convert to lowercase.
*Required*: Yes
*Type*: Array of String
*Minimum*: `1`
*Maximum*: `10`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
