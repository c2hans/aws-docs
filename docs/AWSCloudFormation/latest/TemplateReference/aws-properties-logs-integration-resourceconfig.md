---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-logs-integration-resourceconfig.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Logs::Integration ResourceConfig
<a name="aws-properties-logs-integration-resourceconfig"></a>

This structure contains configuration details about an integration between CloudWatch Logs and another entity.

## Syntax
<a name="aws-properties-logs-integration-resourceconfig-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-logs-integration-resourceconfig-syntax.json"></a>

```
{
  "[OpenSearchResourceConfig](#cfn-logs-integration-resourceconfig-opensearchresourceconfig)" : {{OpenSearchResourceConfig}}
}
```

### YAML
<a name="aws-properties-logs-integration-resourceconfig-syntax.yaml"></a>

```
  [OpenSearchResourceConfig](#cfn-logs-integration-resourceconfig-opensearchresourceconfig): {{
    OpenSearchResourceConfig}}
```

## Properties
<a name="aws-properties-logs-integration-resourceconfig-properties"></a>

`OpenSearchResourceConfig`  <a name="cfn-logs-integration-resourceconfig-opensearchresourceconfig"></a>
This structure contains configuration details about an integration between CloudWatch Logs and OpenSearch Service.
*Required*: No
*Type*: [OpenSearchResourceConfig](aws-properties-logs-integration-opensearchresourceconfig.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
