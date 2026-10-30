---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-bedrockagentcore-gatewayrule-circuitbreakerconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::BedrockAgentCore::GatewayRule CircuitBreakerConfiguration
<a name="aws-properties-bedrockagentcore-gatewayrule-circuitbreakerconfiguration"></a>

Specifies whether the circuit breaker monitors failures for the targets in a fallback chain.

## Syntax
<a name="aws-properties-bedrockagentcore-gatewayrule-circuitbreakerconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-bedrockagentcore-gatewayrule-circuitbreakerconfiguration-syntax.json"></a>

```
{
  "[Mode](#cfn-bedrockagentcore-gatewayrule-circuitbreakerconfiguration-mode)" : {{}}
}
```

### YAML
<a name="aws-properties-bedrockagentcore-gatewayrule-circuitbreakerconfiguration-syntax.yaml"></a>

```
  [Mode](#cfn-bedrockagentcore-gatewayrule-circuitbreakerconfiguration-mode): {{
    }}
```

## Properties
<a name="aws-properties-bedrockagentcore-gatewayrule-circuitbreakerconfiguration-properties"></a>

`Mode`  <a name="cfn-bedrockagentcore-gatewayrule-circuitbreakerconfiguration-mode"></a>
Specifies whether you want the circuit breaker turned on. To turn it off, set this value to `DISABLED`. The default is `ENABLED`.
*Required*: No
*Type*:
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
