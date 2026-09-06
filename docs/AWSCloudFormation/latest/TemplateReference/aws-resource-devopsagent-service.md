---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-devopsagent-service.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::DevOpsAgent::Service
<a name="aws-resource-devopsagent-service"></a>

The `AWS::DevOpsAgent::Service` resource registers an external service for integration with the AWS DevOps Agent service.

Most service types require replacement when you modify their configuration. `MCPServerSigV4` supports in-place updates, and `GitLab`, `MCPServer`, `MCPServerNewRelic`, and `MCPServerGrafana` support in-place credential rotation.

**Note**
Services that use OAuth authorization flows (for example, Datadog, GitHub, and Slack) require interactive browser-based registration through the AWS DevOps Agent console. You cannot register these service types using this resource.

## Syntax
<a name="aws-resource-devopsagent-service-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-devopsagent-service-syntax.json"></a>

```
{
  "Type" : "AWS::DevOpsAgent::Service",
  "Properties" : {
      "[ExchangeUrlPrivateConnectionName](#cfn-devopsagent-service-exchangeurlprivateconnectionname)" : {{String}},
      "[KmsKeyArn](#cfn-devopsagent-service-kmskeyarn)" : {{String}},
      "[PrivateConnectionName](#cfn-devopsagent-service-privateconnectionname)" : {{String}},
      "[ServiceDetails](#cfn-devopsagent-service-servicedetails)" : {{ServiceDetails}},
      "[ServiceType](#cfn-devopsagent-service-servicetype)" : {{String}},
      "[Tags](#cfn-devopsagent-service-tags)" : {{[ Tag, ... ]}},
      "[TargetUrlPrivateConnectionName](#cfn-devopsagent-service-targeturlprivateconnectionname)" : {{String}}
    }
}
```

### YAML
<a name="aws-resource-devopsagent-service-syntax.yaml"></a>

```
Type: AWS::DevOpsAgent::Service
Properties:
  [ExchangeUrlPrivateConnectionName](#cfn-devopsagent-service-exchangeurlprivateconnectionname): {{String}}
  [KmsKeyArn](#cfn-devopsagent-service-kmskeyarn): {{String}}
  [PrivateConnectionName](#cfn-devopsagent-service-privateconnectionname): {{String}}
  [ServiceDetails](#cfn-devopsagent-service-servicedetails): {{
    ServiceDetails}}
  [ServiceType](#cfn-devopsagent-service-servicetype): {{String}}
  [Tags](#cfn-devopsagent-service-tags): {{
    - Tag}}
  [TargetUrlPrivateConnectionName](#cfn-devopsagent-service-targeturlprivateconnectionname): {{String}}
```

## Properties
<a name="aws-resource-devopsagent-service-properties"></a>

`ExchangeUrlPrivateConnectionName`  <a name="cfn-devopsagent-service-exchangeurlprivateconnectionname"></a>
The name of the private connection used to reach the OAuth token exchange endpoint only. You cannot specify this property together with `PrivateConnectionName`.
*Required*: No
*Type*: String
*Pattern*: `^[a-z0-9]([a-z0-9-]*[a-z0-9])?$`
*Minimum*: `3`
*Maximum*: `30`
*Update requires*: Updates are not supported.

`KmsKeyArn`  <a name="cfn-devopsagent-service-kmskeyarn"></a>
The ARN of the customer managed key used to encrypt the data of the registered service at rest.
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `2048`
*Update requires*: Updates are not supported.

`PrivateConnectionName`  <a name="cfn-devopsagent-service-privateconnectionname"></a>
The name of the private connection used to reach the service over a private network path, which applies to both the service endpoint and the OAuth token exchange endpoint.
*Required*: No
*Type*: String
*Pattern*: `^[a-z0-9]([a-z0-9-]*[a-z0-9])?$`
*Minimum*: `3`
*Maximum*: `30`
*Update requires*: Updates are not supported.

`ServiceDetails`  <a name="cfn-devopsagent-service-servicedetails"></a>
Service-specific configuration details provided during registration. The structure of this property depends on the value of `ServiceType`.
*Required*: No
*Type*: [ServiceDetails](aws-properties-devopsagent-service-servicedetails.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ServiceType`  <a name="cfn-devopsagent-service-servicetype"></a>
The type of external service to register.
*Required*: Yes
*Type*: String
*Allowed values*: `dynatrace | mcpserver | mcpserversplunk | mcpservernewrelic | gitlab | servicenow | pagerduty | azureidentity | mcpserversigv4 | mcpservergrafana`
*Update requires*: Updates are not supported.

`Tags`  <a name="cfn-devopsagent-service-tags"></a>
An array of key-value pairs to apply to this resource.
*Required*: No
*Type*: Array of [Tag](aws-properties-devopsagent-service-tag.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`TargetUrlPrivateConnectionName`  <a name="cfn-devopsagent-service-targeturlprivateconnectionname"></a>
The name of the private connection used to reach the service endpoint only. You cannot specify this property together with `PrivateConnectionName`.
*Required*: No
*Type*: String
*Pattern*: `^[a-z0-9]([a-z0-9-]*[a-z0-9])?$`
*Minimum*: `3`
*Maximum*: `30`
*Update requires*: Updates are not supported.

## Return values
<a name="aws-resource-devopsagent-service-return-values"></a>

### Ref
<a name="aws-resource-devopsagent-service-return-values-ref"></a>

When you pass the logical ID of this resource to the intrinsic `Ref` function, `Ref` returns the ServiceId.

For more information about using the `Ref` function, see [`Ref`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-ref.html).

### Fn::GetAtt
<a name="aws-resource-devopsagent-service-return-values-fn--getatt"></a>

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [`Fn::GetAtt`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-getatt.html).

####
<a name="aws-resource-devopsagent-service-return-values-fn--getatt-fn--getatt"></a>

`AccessibleResources`  <a name="AccessibleResources-fn::getatt"></a>
List of accessible resources for this service.

`Arn`  <a name="Arn-fn::getatt"></a>
The Amazon Resource Name (ARN) of the service.

`ServiceId`  <a name="ServiceId-fn::getatt"></a>
The unique identifier of the service.
