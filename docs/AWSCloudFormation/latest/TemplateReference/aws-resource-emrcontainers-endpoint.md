---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-emrcontainers-endpoint.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::EMRContainers::Endpoint
<a name="aws-resource-emrcontainers-endpoint"></a>

This entity represents the endpoint that is managed by Amazon EMR on EKS.

## Syntax
<a name="aws-resource-emrcontainers-endpoint-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-emrcontainers-endpoint-syntax.json"></a>

```
{
  "Type" : "AWS::EMRContainers::Endpoint",
  "Properties" : {
      "[ConfigurationOverrides](#cfn-emrcontainers-endpoint-configurationoverrides)" : {{ConfigurationOverrides}},
      "[ExecutionRoleArn](#cfn-emrcontainers-endpoint-executionrolearn)" : {{String}},
      "[Name](#cfn-emrcontainers-endpoint-name)" : {{String}},
      "[ReleaseLabel](#cfn-emrcontainers-endpoint-releaselabel)" : {{String}},
      "[SessionIdleTimeoutInMinutes](#cfn-emrcontainers-endpoint-sessionidletimeoutinminutes)" : {{Integer}},
      "[Tags](#cfn-emrcontainers-endpoint-tags)" : {{[ Tag, ... ]}},
      "[Type](#cfn-emrcontainers-endpoint-type)" : {{String}},
      "[VirtualClusterId](#cfn-emrcontainers-endpoint-virtualclusterid)" : {{String}}
    }
}
```

### YAML
<a name="aws-resource-emrcontainers-endpoint-syntax.yaml"></a>

```
Type: AWS::EMRContainers::Endpoint
Properties:
  [ConfigurationOverrides](#cfn-emrcontainers-endpoint-configurationoverrides): {{
    ConfigurationOverrides}}
  [ExecutionRoleArn](#cfn-emrcontainers-endpoint-executionrolearn): {{String}}
  [Name](#cfn-emrcontainers-endpoint-name): {{String}}
  [ReleaseLabel](#cfn-emrcontainers-endpoint-releaselabel): {{String}}
  [SessionIdleTimeoutInMinutes](#cfn-emrcontainers-endpoint-sessionidletimeoutinminutes): {{Integer}}
  [Tags](#cfn-emrcontainers-endpoint-tags): {{
    - Tag}}
  [Type](#cfn-emrcontainers-endpoint-type): {{String}}
  [VirtualClusterId](#cfn-emrcontainers-endpoint-virtualclusterid): {{String}}
```

## Properties
<a name="aws-resource-emrcontainers-endpoint-properties"></a>

`ConfigurationOverrides`  <a name="cfn-emrcontainers-endpoint-configurationoverrides"></a>
The configuration settings that are used to override existing configurations for endpoints.
*Required*: No
*Type*: [ConfigurationOverrides](aws-properties-emrcontainers-endpoint-configurationoverrides.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`ExecutionRoleArn`  <a name="cfn-emrcontainers-endpoint-executionrolearn"></a>
The execution role ARN of the endpoint.
*Required*: Yes
*Type*: String
*Pattern*: `^arn:(aws[a-zA-Z0-9-]*):iam::(\d{12})?:(role((\u002F)|(\u002F[\u0021-\u007F]+\u002F))[\w+=,.@-]+)$`
*Minimum*: `20`
*Maximum*: `2048`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Name`  <a name="cfn-emrcontainers-endpoint-name"></a>
The name of the endpoint.
*Required*: No
*Type*: String
*Pattern*: `[0-9A-Za-z][A-Za-z0-9\-_]*`
*Minimum*: `1`
*Maximum*: `64`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`ReleaseLabel`  <a name="cfn-emrcontainers-endpoint-releaselabel"></a>
The EMR release version to be used for the endpoint.
*Required*: Yes
*Type*: String
*Pattern*: `[A-Za-z0-9._/-]+`
*Minimum*: `1`
*Maximum*: `64`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`SessionIdleTimeoutInMinutes`  <a name="cfn-emrcontainers-endpoint-sessionidletimeoutinminutes"></a>
Property description not available.
*Required*: No
*Type*: Integer
*Minimum*: `1`
*Maximum*: `1440`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Tags`  <a name="cfn-emrcontainers-endpoint-tags"></a>
The tags of the endpoint.
*Required*: No
*Type*: Array of [Tag](aws-properties-emrcontainers-endpoint-tag.md)
*Maximum*: `50`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Type`  <a name="cfn-emrcontainers-endpoint-type"></a>
The type of the endpoint.
*Required*: Yes
*Type*: String
*Pattern*: `.*\S.*`
*Minimum*: `1`
*Maximum*: `64`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`VirtualClusterId`  <a name="cfn-emrcontainers-endpoint-virtualclusterid"></a>
The ID of the endpoint's virtual cluster.
*Required*: Yes
*Type*: String
*Pattern*: `[0-9a-z]+`
*Minimum*: `1`
*Maximum*: `64`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## Return values
<a name="aws-resource-emrcontainers-endpoint-return-values"></a>

### Ref
<a name="aws-resource-emrcontainers-endpoint-return-values-ref"></a>

### Fn::GetAtt
<a name="aws-resource-emrcontainers-endpoint-return-values-fn--getatt"></a>

####
<a name="aws-resource-emrcontainers-endpoint-return-values-fn--getatt-fn--getatt"></a>

`Arn`  <a name="Arn-fn::getatt"></a>
The ARN of the endpoint.

`AuthProxyUrl`  <a name="AuthProxyUrl-fn::getatt"></a>
Property description not available.

`CreatedAt`  <a name="CreatedAt-fn::getatt"></a>
The date and time when the endpoint was created.

`FailureReason`  <a name="FailureReason-fn::getatt"></a>
 The reasons why the endpoint has failed.

`Id`  <a name="Id-fn::getatt"></a>
The ID of the endpoint.

`SecurityGroup`  <a name="SecurityGroup-fn::getatt"></a>
The security group configuration of the endpoint.

`ServerUrl`  <a name="ServerUrl-fn::getatt"></a>
The server URL of the endpoint.

`State`  <a name="State-fn::getatt"></a>
The state of the endpoint.

`StateDetails`  <a name="StateDetails-fn::getatt"></a>
 Additional details of the endpoint state.
