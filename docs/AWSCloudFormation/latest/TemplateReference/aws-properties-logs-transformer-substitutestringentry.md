---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-logs-transformer-substitutestringentry.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Logs::Transformer SubstituteStringEntry
<a name="aws-properties-logs-transformer-substitutestringentry"></a>

This object defines one log field key that will be replaced using the [ substituteString](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/CloudWatch-Logs-Transformation-Processors.html#CloudWatch-Logs-Transformation-substituteString) processor.

## Syntax
<a name="aws-properties-logs-transformer-substitutestringentry-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-logs-transformer-substitutestringentry-syntax.json"></a>

```
{
  "[From](#cfn-logs-transformer-substitutestringentry-from)" : {{String}},
  "[Source](#cfn-logs-transformer-substitutestringentry-source)" : {{String}},
  "[To](#cfn-logs-transformer-substitutestringentry-to)" : {{String}}
}
```

### YAML
<a name="aws-properties-logs-transformer-substitutestringentry-syntax.yaml"></a>

```
  [From](#cfn-logs-transformer-substitutestringentry-from): {{String}}
  [Source](#cfn-logs-transformer-substitutestringentry-source): {{String}}
  [To](#cfn-logs-transformer-substitutestringentry-to): {{String}}
```

## Properties
<a name="aws-properties-logs-transformer-substitutestringentry-properties"></a>

`From`  <a name="cfn-logs-transformer-substitutestringentry-from"></a>
The regular expression string to be replaced. Special regex characters such as [ and ] must be escaped using \\\\ when using double quotes and with \\ when using single quotes. For more information, see [ Class Pattern](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/regex/Pattern.html) on the Oracle web site.
*Required*: Yes
*Type*: String
*Maximum*: `128`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Source`  <a name="cfn-logs-transformer-substitutestringentry-source"></a>
The key to modify
*Required*: Yes
*Type*: String
*Pattern*: `^.*[a-zA-Z0-9]+.*$`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`To`  <a name="cfn-logs-transformer-substitutestringentry-to"></a>
The string to be substituted for each match of `from`
*Required*: Yes
*Type*: String
*Maximum*: `128`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
