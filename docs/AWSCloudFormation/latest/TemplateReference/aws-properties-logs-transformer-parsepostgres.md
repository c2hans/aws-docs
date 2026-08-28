---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-logs-transformer-parsepostgres.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Logs::Transformer ParsePostgres
<a name="aws-properties-logs-transformer-parsepostgres"></a>

Use this processor to parse RDS for PostgreSQL vended logs, extract fields, and and convert them into a JSON format. This processor always processes the entire log event message. For more information about this processor including examples, see [ parsePostGres](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/CloudWatch-Logs-Transformation-Processors.html#CloudWatch-Logs-Transformation-parsePostGres).

For more information about RDS for PostgreSQL log format, see [ RDS for PostgreSQL database log filesTCP flag sequence](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_LogAccess.Concepts.PostgreSQL.html#USER_LogAccess.Concepts.PostgreSQL.Log_Format.log-line-prefix).

**Important**
If you use this processor, it must be the first processor in your transformer.

## Syntax
<a name="aws-properties-logs-transformer-parsepostgres-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-logs-transformer-parsepostgres-syntax.json"></a>

```
{
  "[Source](#cfn-logs-transformer-parsepostgres-source)" : {{String}}
}
```

### YAML
<a name="aws-properties-logs-transformer-parsepostgres-syntax.yaml"></a>

```
  [Source](#cfn-logs-transformer-parsepostgres-source): {{String}}
```

## Properties
<a name="aws-properties-logs-transformer-parsepostgres-properties"></a>

`Source`  <a name="cfn-logs-transformer-parsepostgres-source"></a>
Omit this parameter and the whole log message will be processed by this processor. No other value than `@message` is allowed for `source`.
*Required*: No
*Type*: String
*Pattern*: `^.*[a-zA-Z0-9]+.*$`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
