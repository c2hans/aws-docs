---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-events-endpoint-failoverconfig.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Events::Endpoint FailoverConfig
<a name="aws-properties-events-endpoint-failoverconfig"></a>

The failover configuration for an endpoint. This includes what triggers failover and what happens when it's triggered.

## Syntax
<a name="aws-properties-events-endpoint-failoverconfig-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-events-endpoint-failoverconfig-syntax.json"></a>

```
{
  "[Primary](#cfn-events-endpoint-failoverconfig-primary)" : {{Primary}},
  "[Secondary](#cfn-events-endpoint-failoverconfig-secondary)" : {{Secondary}}
}
```

### YAML
<a name="aws-properties-events-endpoint-failoverconfig-syntax.yaml"></a>

```
  [Primary](#cfn-events-endpoint-failoverconfig-primary): {{
    Primary}}
  [Secondary](#cfn-events-endpoint-failoverconfig-secondary): {{
    Secondary}}
```

## Properties
<a name="aws-properties-events-endpoint-failoverconfig-properties"></a>

`Primary`  <a name="cfn-events-endpoint-failoverconfig-primary"></a>
The main Region of the endpoint.
*Required*: Yes
*Type*: [Primary](aws-properties-events-endpoint-primary.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Secondary`  <a name="cfn-events-endpoint-failoverconfig-secondary"></a>
The Region that events are routed to when failover is triggered or event replication is enabled.
*Required*: Yes
*Type*: [Secondary](aws-properties-events-endpoint-secondary.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
