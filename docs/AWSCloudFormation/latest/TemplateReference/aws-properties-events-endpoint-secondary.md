---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-events-endpoint-secondary.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Events::Endpoint Secondary

The secondary Region that processes events when failover is triggered or replication is enabled.

## Syntax
<a name="aws-properties-events-endpoint-secondary-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-events-endpoint-secondary-syntax.json"></a>

```json
{
  "[Route](#cfn-events-endpoint-secondary-route)" : {{String}}
}
```

### YAML
<a name="aws-properties-events-endpoint-secondary-syntax.yaml"></a>

```yaml
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
