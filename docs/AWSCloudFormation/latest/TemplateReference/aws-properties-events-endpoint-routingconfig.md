---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-events-endpoint-routingconfig.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Events::Endpoint RoutingConfig
<a name="aws-properties-events-endpoint-routingconfig"></a>

The routing configuration of the endpoint.

## Syntax
<a name="aws-properties-events-endpoint-routingconfig-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-events-endpoint-routingconfig-syntax.json"></a>

```
{
  "[FailoverConfig](#cfn-events-endpoint-routingconfig-failoverconfig)" : {{FailoverConfig}}
}
```

### YAML
<a name="aws-properties-events-endpoint-routingconfig-syntax.yaml"></a>

```
  [FailoverConfig](#cfn-events-endpoint-routingconfig-failoverconfig): {{
    FailoverConfig}}
```

## Properties
<a name="aws-properties-events-endpoint-routingconfig-properties"></a>

`FailoverConfig`  <a name="cfn-events-endpoint-routingconfig-failoverconfig"></a>
The failover configuration for an endpoint. This includes what triggers failover and what happens when it's triggered.
*Required*: Yes
*Type*: [FailoverConfig](aws-properties-events-endpoint-failoverconfig.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
