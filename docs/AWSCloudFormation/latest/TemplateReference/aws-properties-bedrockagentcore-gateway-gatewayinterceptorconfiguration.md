---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-bedrockagentcore-gateway-gatewayinterceptorconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::BedrockAgentCore::Gateway GatewayInterceptorConfiguration
<a name="aws-properties-bedrockagentcore-gateway-gatewayinterceptorconfiguration"></a>

The configuration for an interceptor on a gateway. This structure defines settings for an interceptor that will be invoked during the invocation of the gateway.

## Syntax
<a name="aws-properties-bedrockagentcore-gateway-gatewayinterceptorconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-bedrockagentcore-gateway-gatewayinterceptorconfiguration-syntax.json"></a>

```
{
  "[InputConfiguration](#cfn-bedrockagentcore-gateway-gatewayinterceptorconfiguration-inputconfiguration)" : {{InterceptorInputConfiguration}},
  "[InterceptionPoints](#cfn-bedrockagentcore-gateway-gatewayinterceptorconfiguration-interceptionpoints)" : {{[ String, ... ]}},
  "[Interceptor](#cfn-bedrockagentcore-gateway-gatewayinterceptorconfiguration-interceptor)" : {{InterceptorConfiguration}}
}
```

### YAML
<a name="aws-properties-bedrockagentcore-gateway-gatewayinterceptorconfiguration-syntax.yaml"></a>

```
  [InputConfiguration](#cfn-bedrockagentcore-gateway-gatewayinterceptorconfiguration-inputconfiguration): {{
    InterceptorInputConfiguration}}
  [InterceptionPoints](#cfn-bedrockagentcore-gateway-gatewayinterceptorconfiguration-interceptionpoints): {{
    - String}}
  [Interceptor](#cfn-bedrockagentcore-gateway-gatewayinterceptorconfiguration-interceptor): {{
    InterceptorConfiguration}}
```

## Properties
<a name="aws-properties-bedrockagentcore-gateway-gatewayinterceptorconfiguration-properties"></a>

`InputConfiguration`  <a name="cfn-bedrockagentcore-gateway-gatewayinterceptorconfiguration-inputconfiguration"></a>
The configuration for the input of the interceptor. This field specifies how the input to the interceptor is constructed
*Required*: No
*Type*: [InterceptorInputConfiguration](aws-properties-bedrockagentcore-gateway-interceptorinputconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`InterceptionPoints`  <a name="cfn-bedrockagentcore-gateway-gatewayinterceptorconfiguration-interceptionpoints"></a>
The supported points of interception. This field specifies which points during the gateway invocation to invoke the interceptor
*Required*: Yes
*Type*: Array of String
*Minimum*: `1`
*Maximum*: `2`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Interceptor`  <a name="cfn-bedrockagentcore-gateway-gatewayinterceptorconfiguration-interceptor"></a>
The infrastructure settings of an interceptor configuration. This structure defines how the interceptor can be invoked.
*Required*: Yes
*Type*: [InterceptorConfiguration](aws-properties-bedrockagentcore-gateway-interceptorconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
