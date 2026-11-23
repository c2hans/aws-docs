---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-mediaconnect-routeroutput-fabricconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::MediaConnect::RouterOutput FabricConfiguration

The fabric configuration settings for the router output.

## Syntax
<a name="aws-properties-mediaconnect-routeroutput-fabricconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-mediaconnect-routeroutput-fabricconfiguration-syntax.json"></a>

```json
{
  "[RecoveryLatencyMode](#cfn-mediaconnect-routeroutput-fabricconfiguration-recoverylatencymode)" : {{String}}
}
```

### YAML
<a name="aws-properties-mediaconnect-routeroutput-fabricconfiguration-syntax.yaml"></a>

```yaml
  [RecoveryLatencyMode](#cfn-mediaconnect-routeroutput-fabricconfiguration-recoverylatencymode): {{String}}
```

## Properties
<a name="aws-properties-mediaconnect-routeroutput-fabricconfiguration-properties"></a>

`RecoveryLatencyMode`  <a name="cfn-mediaconnect-routeroutput-fabricconfiguration-recoverylatencymode"></a>
The recovery latency mode for the router fabric connection. Valid values include the following:
+ `BALANCED` (default) – Optimizes for stream quality.
+ `LOW_LATENCY` – Reduces latency at the potential cost of stream quality under adverse network conditions.
*Required*: Yes
*Type*: String
*Allowed values*: `BALANCED | LOW_LATENCY`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
