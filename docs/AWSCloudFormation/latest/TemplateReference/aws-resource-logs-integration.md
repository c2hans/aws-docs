---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-logs-integration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Logs::Integration
<a name="aws-resource-logs-integration"></a>

Creates an integration between CloudWatch Logs and another service in this account. Currently, only integrations with OpenSearch Service are supported, and currently you can have only one integration in your account.

Integrating with OpenSearch Service makes it possible for you to create curated vended logs dashboards, powered by OpenSearch Service analytics. For more information, see [Vended log dashboards powered by Amazon OpenSearch Service](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/CloudWatchLogs-OpenSearch-Dashboards.html).

You can use this operation only to create a new integration. You can't modify an existing integration.

## Syntax
<a name="aws-resource-logs-integration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-logs-integration-syntax.json"></a>

```
{
  "Type" : "AWS::Logs::Integration",
  "Properties" : {
      "[IntegrationName](#cfn-logs-integration-integrationname)" : {{String}},
      "[IntegrationType](#cfn-logs-integration-integrationtype)" : {{String}},
      "[ResourceConfig](#cfn-logs-integration-resourceconfig)" : {{ResourceConfig}}
    }
}
```

### YAML
<a name="aws-resource-logs-integration-syntax.yaml"></a>

```
Type: AWS::Logs::Integration
Properties:
  [IntegrationName](#cfn-logs-integration-integrationname): {{String}}
  [IntegrationType](#cfn-logs-integration-integrationtype): {{String}}
  [ResourceConfig](#cfn-logs-integration-resourceconfig): {{
    ResourceConfig}}
```

## Properties
<a name="aws-resource-logs-integration-properties"></a>

`IntegrationName`  <a name="cfn-logs-integration-integrationname"></a>
The name of this integration.
*Required*: Yes
*Type*: String
*Pattern*: `[\.\-_/#A-Za-z0-9]+`
*Minimum*: `1`
*Maximum*: `50`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`IntegrationType`  <a name="cfn-logs-integration-integrationtype"></a>
The type of integration. Integrations with OpenSearch Service have the type `OPENSEARCH`.
*Required*: Yes
*Type*: String
*Allowed values*: `OPENSEARCH`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`ResourceConfig`  <a name="cfn-logs-integration-resourceconfig"></a>
This structure contains configuration details about an integration between CloudWatch Logs and another entity.
*Required*: Yes
*Type*: [ResourceConfig](aws-properties-logs-integration-resourceconfig.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## Return values
<a name="aws-resource-logs-integration-return-values"></a>

### Ref
<a name="aws-resource-logs-integration-return-values-ref"></a>

### Fn::GetAtt
<a name="aws-resource-logs-integration-return-values-fn--getatt"></a>

####
<a name="aws-resource-logs-integration-return-values-fn--getatt-fn--getatt"></a>

`IntegrationStatus`  <a name="IntegrationStatus-fn::getatt"></a>
The current status of this integration.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
