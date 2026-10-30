---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-mediaconnect-sourceendpoint.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::MediaConnect::SourceEndpoint
<a name="aws-resource-mediaconnect-sourceendpoint"></a>

<a name="aws-resource-mediaconnect-sourceendpoint-description"></a>The `AWS::MediaConnect::SourceEndpoint` resource Property description not available. for MediaConnect.

## Syntax
<a name="aws-resource-mediaconnect-sourceendpoint-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-mediaconnect-sourceendpoint-syntax.json"></a>

```
{
  "Type" : "AWS::MediaConnect::SourceEndpoint",
  "Properties" : {
      "[Configuration](#cfn-mediaconnect-sourceendpoint-configuration)" : {{SourceEndpointConfiguration}},
      "[Description](#cfn-mediaconnect-sourceendpoint-description)" : {{String}},
      "[RegionName](#cfn-mediaconnect-sourceendpoint-regionname)" : {{String}},
      "[Tags](#cfn-mediaconnect-sourceendpoint-tags)" : {{[ Tag, ... ]}}
    }
}
```

### YAML
<a name="aws-resource-mediaconnect-sourceendpoint-syntax.yaml"></a>

```
Type: AWS::MediaConnect::SourceEndpoint
Properties:
  [Configuration](#cfn-mediaconnect-sourceendpoint-configuration): {{
    SourceEndpointConfiguration}}
  [Description](#cfn-mediaconnect-sourceendpoint-description): {{String}}
  [RegionName](#cfn-mediaconnect-sourceendpoint-regionname): {{String}}
  [Tags](#cfn-mediaconnect-sourceendpoint-tags): {{
    - Tag}}
```

## Properties
<a name="aws-resource-mediaconnect-sourceendpoint-properties"></a>

`Configuration`  <a name="cfn-mediaconnect-sourceendpoint-configuration"></a>
The configuration settings for the source endpoint.
*Required*: Yes
*Type*: [SourceEndpointConfiguration](aws-properties-mediaconnect-sourceendpoint-sourceendpointconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Description`  <a name="cfn-mediaconnect-sourceendpoint-description"></a>
The description of the source endpoint.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`RegionName`  <a name="cfn-mediaconnect-sourceendpoint-regionname"></a>
The name of the AWS Region in which the source endpoint is located.
*Required*: No
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Tags`  <a name="cfn-mediaconnect-sourceendpoint-tags"></a>
The tags associated with the source endpoint. Each tag is a key-value pair.
*Required*: No
*Type*: Array of [Tag](aws-properties-mediaconnect-sourceendpoint-tag.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-mediaconnect-sourceendpoint-return-values"></a>

### Ref
<a name="aws-resource-mediaconnect-sourceendpoint-return-values-ref"></a>

### Fn::GetAtt
<a name="aws-resource-mediaconnect-sourceendpoint-return-values-fn--getatt"></a>

####
<a name="aws-resource-mediaconnect-sourceendpoint-return-values-fn--getatt-fn--getatt"></a>

`Arn`  <a name="Arn-fn::getatt"></a>
The Amazon Resource Name (ARN) of the source endpoint.

`AvailabilityZone`  <a name="AvailabilityZone-fn::getatt"></a>
The Availability Zone in which the source endpoint is located.

`AvailabilityZoneId`  <a name="AvailabilityZoneId-fn::getatt"></a>
The ID of the Availability Zone in which the source endpoint is located.

`ConnectionState`  <a name="ConnectionState-fn::getatt"></a>
The connection state of the source endpoint. Valid values include the following:
+ `CONNECTED` – The source endpoint is connected to a destination endpoint.
+ `DISCONNECTED` – The source endpoint isn't connected to a destination endpoint.
+ `CONNECTING` – The source endpoint is connecting to a destination endpoint.
+ `DISCONNECTING` – The source endpoint is disconnecting from a destination endpoint.

`CreatedAt`  <a name="CreatedAt-fn::getatt"></a>
The date and time when the source endpoint was created.

`Id`  <a name="Id-fn::getatt"></a>
The unique identifier of the source endpoint.

`LifecycleManagement`  <a name="LifecycleManagement-fn::getatt"></a>
The entity that manages the lifecycle of the source endpoint.

`Name`  <a name="Name-fn::getatt"></a>
The name of the source endpoint.

`RegistrationState`  <a name="RegistrationState-fn::getatt"></a>
The registration state of the source endpoint. Valid values include the following:
+ `REGISTERED` – The source endpoint is registered and ready to use.
+ `REGISTERING` – MediaConnect is registering the source endpoint.
+ `DEREGISTERING` – MediaConnect is deregistering the source endpoint.
+ `REGISTRATION_FAILED` – MediaConnect couldn't register the source endpoint.

`SourceType`  <a name="SourceType-fn::getatt"></a>
The type of the source endpoint. Valid values include the following:
+ `STANDARD` – A source endpoint that represents an external source over a standard protocol, such as RTP, RIST, or SRT.
+ `ROUTER_OUTPUT` – A source endpoint that represents a router output.

`UpdatedAt`  <a name="UpdatedAt-fn::getatt"></a>
The date and time when the source endpoint was last updated.
