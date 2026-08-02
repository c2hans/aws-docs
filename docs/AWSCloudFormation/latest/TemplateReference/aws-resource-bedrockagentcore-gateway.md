---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-bedrockagentcore-gateway.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::BedrockAgentCore::Gateway
<a name="aws-resource-bedrockagentcore-gateway"></a>

Amazon Bedrock AgentCore Gateway provides a unified connectivity layer between agents and the tools and resources they need to interact with.

For more information about creating a gateway, see [Set up an Amazon Bedrock AgentCore gateway](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/gateway-building.html).

See the **Properties** section below for descriptions of both the required and optional properties.

## Syntax
<a name="aws-resource-bedrockagentcore-gateway-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-bedrockagentcore-gateway-syntax.json"></a>

```
{
  "Type" : "AWS::BedrockAgentCore::Gateway",
  "Properties" : {
      "[AuthorizerConfiguration](#cfn-bedrockagentcore-gateway-authorizerconfiguration)" : {{AuthorizerConfiguration}},
      "[AuthorizerType](#cfn-bedrockagentcore-gateway-authorizertype)" : {{String}},
      "[Description](#cfn-bedrockagentcore-gateway-description)" : {{String}},
      "[ExceptionLevel](#cfn-bedrockagentcore-gateway-exceptionlevel)" : {{String}},
      "[InterceptorConfigurations](#cfn-bedrockagentcore-gateway-interceptorconfigurations)" : {{[ GatewayInterceptorConfiguration, ... ]}},
      "[KmsKeyArn](#cfn-bedrockagentcore-gateway-kmskeyarn)" : {{String}},
      "[Name](#cfn-bedrockagentcore-gateway-name)" : {{String}},
      "[PolicyEngineConfiguration](#cfn-bedrockagentcore-gateway-policyengineconfiguration)" : {{GatewayPolicyEngineConfiguration}},
      "[ProtocolConfiguration](#cfn-bedrockagentcore-gateway-protocolconfiguration)" : {{GatewayProtocolConfiguration}},
      "[ProtocolType](#cfn-bedrockagentcore-gateway-protocoltype)" : {{}},
      "[RoleArn](#cfn-bedrockagentcore-gateway-rolearn)" : {{String}},
      "[Tags](#cfn-bedrockagentcore-gateway-tags)" : {{{{{Key}}: {{Value}}, ...}}}
    }
}
```

### YAML
<a name="aws-resource-bedrockagentcore-gateway-syntax.yaml"></a>

```
Type: AWS::BedrockAgentCore::Gateway
Properties:
  [AuthorizerConfiguration](#cfn-bedrockagentcore-gateway-authorizerconfiguration): {{
    AuthorizerConfiguration}}
  [AuthorizerType](#cfn-bedrockagentcore-gateway-authorizertype): {{String}}
  [Description](#cfn-bedrockagentcore-gateway-description): {{String}}
  [ExceptionLevel](#cfn-bedrockagentcore-gateway-exceptionlevel): {{String}}
  [InterceptorConfigurations](#cfn-bedrockagentcore-gateway-interceptorconfigurations): {{
    - GatewayInterceptorConfiguration}}
  [KmsKeyArn](#cfn-bedrockagentcore-gateway-kmskeyarn): {{String}}
  [Name](#cfn-bedrockagentcore-gateway-name): {{String}}
  [PolicyEngineConfiguration](#cfn-bedrockagentcore-gateway-policyengineconfiguration): {{
    GatewayPolicyEngineConfiguration}}
  [ProtocolConfiguration](#cfn-bedrockagentcore-gateway-protocolconfiguration): {{
    GatewayProtocolConfiguration}}
  [ProtocolType](#cfn-bedrockagentcore-gateway-protocoltype): {{
    }}
  [RoleArn](#cfn-bedrockagentcore-gateway-rolearn): {{String}}
  [Tags](#cfn-bedrockagentcore-gateway-tags): {{
    {{Key}}: {{Value}}}}
```

## Properties
<a name="aws-resource-bedrockagentcore-gateway-properties"></a>

`AuthorizerConfiguration`  <a name="cfn-bedrockagentcore-gateway-authorizerconfiguration"></a>
Represents inbound authorization configuration options used to authenticate incoming requests.
*Required*: No
*Type*: [AuthorizerConfiguration](aws-properties-bedrockagentcore-gateway-authorizerconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`AuthorizerType`  <a name="cfn-bedrockagentcore-gateway-authorizertype"></a>
The type of authorizer used by the gateway.
*Required*: Yes
*Type*: String
*Allowed values*: `CUSTOM_JWT | AWS_IAM | NONE | AUTHENTICATE_ONLY`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Description`  <a name="cfn-bedrockagentcore-gateway-description"></a>
The description of the gateway.
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `200`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ExceptionLevel`  <a name="cfn-bedrockagentcore-gateway-exceptionlevel"></a>
The exception level for the gateway.
*Required*: No
*Type*: String
*Allowed values*: `DEBUG`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`InterceptorConfigurations`  <a name="cfn-bedrockagentcore-gateway-interceptorconfigurations"></a>
A list of configuration settings for a gateway interceptor. Gateway interceptors allow custom code to be invoked during gateway invocations.
*Required*: No
*Type*: Array of [GatewayInterceptorConfiguration](aws-properties-bedrockagentcore-gateway-gatewayinterceptorconfiguration.md)
*Minimum*: `1`
*Maximum*: `2`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`KmsKeyArn`  <a name="cfn-bedrockagentcore-gateway-kmskeyarn"></a>
The KMS key ARN for the gateway.
*Required*: No
*Type*: String
*Pattern*: `^arn:[a-z0-9-]{1,20}:kms:[a-zA-Z0-9-]*:[0-9]{12}:key/[a-zA-Z0-9-]{36}$`
*Minimum*: `1`
*Maximum*: `2048`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Name`  <a name="cfn-bedrockagentcore-gateway-name"></a>
The name of the gateway.
*Required*: Yes
*Type*: String
*Pattern*: `^([0-9a-zA-Z][-]?){1,100}$`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`PolicyEngineConfiguration`  <a name="cfn-bedrockagentcore-gateway-policyengineconfiguration"></a>
The policy engine configuration for the gateway. A policy engine is a collection of policies that evaluates and authorizes agent tool calls. When associated with a gateway, the policy engine intercepts all agent requests and determines whether to allow or deny each action based on the defined policies.
*Required*: No
*Type*: [GatewayPolicyEngineConfiguration](aws-properties-bedrockagentcore-gateway-gatewaypolicyengineconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ProtocolConfiguration`  <a name="cfn-bedrockagentcore-gateway-protocolconfiguration"></a>
The protocol configuration for the gateway target.
*Required*: No
*Type*: [GatewayProtocolConfiguration](aws-properties-bedrockagentcore-gateway-gatewayprotocolconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ProtocolType`  <a name="cfn-bedrockagentcore-gateway-protocoltype"></a>
The protocol type used by the gateway.
*Required*: No
*Type*:
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`RoleArn`  <a name="cfn-bedrockagentcore-gateway-rolearn"></a>
The ARN of the IAM role that provides permissions for the gateway to access AWS services.
*Required*: Yes
*Type*: String
*Pattern*: `^arn:[a-z0-9-]{1,20}:iam::([0-9]{12})?:role/.+$`
*Minimum*: `1`
*Maximum*: `2048`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Tags`  <a name="cfn-bedrockagentcore-gateway-tags"></a>
The tags for the gateway.
*Required*: No
*Type*: Object of String
*Pattern*: `^[a-zA-Z0-9\s._:/=+@-]*$`
*Minimum*: `0`
*Maximum*: `256`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-bedrockagentcore-gateway-return-values"></a>

### Ref
<a name="aws-resource-bedrockagentcore-gateway-return-values-ref"></a>

When you pass the logical ID of this resource to the intrinsic `Ref` function, `Ref` returns the gateway identifier. For example:

 `my-gateway-a1b2c3d4e5`

For more information about using the `Ref` function, see [https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-ref.html](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-ref.html).

### Fn::GetAtt
<a name="aws-resource-bedrockagentcore-gateway-return-values-fn--getatt"></a>

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-getatt.html](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-getatt.html).

####
<a name="aws-resource-bedrockagentcore-gateway-return-values-fn--getatt-fn--getatt"></a>

`CreatedAt`  <a name="CreatedAt-fn::getatt"></a>
The date and time at which the target was created.

`GatewayArn`  <a name="GatewayArn-fn::getatt"></a>
The Amazon Resource Name (ARN) of the gateway target.

`GatewayIdentifier`  <a name="GatewayIdentifier-fn::getatt"></a>
The unique identifier of the gateway.

`GatewayUrl`  <a name="GatewayUrl-fn::getatt"></a>
The URL endpoint for the gateway.

`Status`  <a name="Status-fn::getatt"></a>
The status for the gateway.

`StatusReasons`  <a name="StatusReasons-fn::getatt"></a>
The status reasons for the target status.

`UpdatedAt`  <a name="UpdatedAt-fn::getatt"></a>
The date and time at which the target was updated.
