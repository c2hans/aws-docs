---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-events-endpoint-secondary.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Events::Endpoint Secondary
<a name="aws-properties-events-endpoint-secondary"></a>

The secondary Region that processes events when failover is triggered or replication is enabled.

## Syntax
<a name="aws-properties-events-endpoint-secondary-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-events-endpoint-secondary-syntax.json"></a>

```
{
  "[Route](#cfn-events-endpoint-secondary-route)" : {{String}}
}
```

### YAML
<a name="aws-properties-events-endpoint-secondary-syntax.yaml"></a>

```
  [Route](#cfn-events-endpoint-secondary-route): {{String}}
```

## Properties
<a name="aws-properties-events-endpoint-secondary-properties"></a>

`Route`  <a name="cfn-events-endpoint-secondary-route"></a>
Defines the secondary Region.
*Required*: Yes
*Type*: String
*Pattern*: `^[\-a-z0-9]+$`
*Minimum*: `9`
*Maximum*: `20`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
