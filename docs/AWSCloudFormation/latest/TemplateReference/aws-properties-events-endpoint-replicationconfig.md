---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-events-endpoint-replicationconfig.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Events::Endpoint ReplicationConfig
<a name="aws-properties-events-endpoint-replicationconfig"></a>

Endpoints can replicate all events to the secondary Region.

## Syntax
<a name="aws-properties-events-endpoint-replicationconfig-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-events-endpoint-replicationconfig-syntax.json"></a>

```
{
  "[State](#cfn-events-endpoint-replicationconfig-state)" : {{String}}
}
```

### YAML
<a name="aws-properties-events-endpoint-replicationconfig-syntax.yaml"></a>

```
  [State](#cfn-events-endpoint-replicationconfig-state): {{String}}
```

## Properties
<a name="aws-properties-events-endpoint-replicationconfig-properties"></a>

`State`  <a name="cfn-events-endpoint-replicationconfig-state"></a>
The state of event replication.
*Required*: Yes
*Type*: String
*Allowed values*: `ENABLED | DISABLED`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
