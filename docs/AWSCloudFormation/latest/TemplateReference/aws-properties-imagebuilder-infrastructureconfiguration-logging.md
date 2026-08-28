---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-imagebuilder-infrastructureconfiguration-logging.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::ImageBuilder::InfrastructureConfiguration Logging
<a name="aws-properties-imagebuilder-infrastructureconfiguration-logging"></a>

Logging configuration defines where Image Builder uploads your logs.

## Syntax
<a name="aws-properties-imagebuilder-infrastructureconfiguration-logging-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-imagebuilder-infrastructureconfiguration-logging-syntax.json"></a>

```
{
  "[S3Logs](#cfn-imagebuilder-infrastructureconfiguration-logging-s3logs)" : {{S3Logs}}
}
```

### YAML
<a name="aws-properties-imagebuilder-infrastructureconfiguration-logging-syntax.yaml"></a>

```
  [S3Logs](#cfn-imagebuilder-infrastructureconfiguration-logging-s3logs): {{
    S3Logs}}
```

## Properties
<a name="aws-properties-imagebuilder-infrastructureconfiguration-logging-properties"></a>

`S3Logs`  <a name="cfn-imagebuilder-infrastructureconfiguration-logging-s3logs"></a>
The Amazon S3 logging configuration.
*Required*: No
*Type*: [S3Logs](aws-properties-imagebuilder-infrastructureconfiguration-s3logs.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
