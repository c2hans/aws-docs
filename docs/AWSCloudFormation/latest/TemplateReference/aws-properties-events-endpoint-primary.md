---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-events-endpoint-primary.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Events::Endpoint Primary
<a name="aws-properties-events-endpoint-primary"></a>

The primary Region of the endpoint.

## Syntax
<a name="aws-properties-events-endpoint-primary-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-events-endpoint-primary-syntax.json"></a>

```
{
  "[HealthCheck](#cfn-events-endpoint-primary-healthcheck)" : {{String}}
}
```

### YAML
<a name="aws-properties-events-endpoint-primary-syntax.yaml"></a>

```
  [HealthCheck](#cfn-events-endpoint-primary-healthcheck): {{String}}
```

## Properties
<a name="aws-properties-events-endpoint-primary-properties"></a>

`HealthCheck`  <a name="cfn-events-endpoint-primary-healthcheck"></a>
The ARN of the health check used by the endpoint to determine whether failover is triggered.
*Required*: Yes
*Type*: String
*Pattern*: `^arn:aws([a-z]|\-)*:route53:::healthcheck/[\-a-z0-9]+$`
*Minimum*: `1`
*Maximum*: `1600`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
