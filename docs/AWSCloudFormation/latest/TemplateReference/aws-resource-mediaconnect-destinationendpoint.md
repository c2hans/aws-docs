---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-mediaconnect-destinationendpoint.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::MediaConnect::DestinationEndpoint
<a name="aws-resource-mediaconnect-destinationendpoint"></a>

<a name="aws-resource-mediaconnect-destinationendpoint-description"></a>The `AWS::MediaConnect::DestinationEndpoint` resource Property description not available. for MediaConnect.

## Syntax
<a name="aws-resource-mediaconnect-destinationendpoint-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-mediaconnect-destinationendpoint-syntax.json"></a>

```
{
  "Type" : "AWS::MediaConnect::DestinationEndpoint",
  "Properties" : {
      "[Configuration](#cfn-mediaconnect-destinationendpoint-configuration)" : {{DestinationEndpointConfiguration}},
      "[Description](#cfn-mediaconnect-destinationendpoint-description)" : {{String}},
      "[RegionName](#cfn-mediaconnect-destinationendpoint-regionname)" : {{String}},
      "[Tags](#cfn-mediaconnect-destinationendpoint-tags)" : {{[ Tag, ... ]}}
    }
}
```

### YAML
<a name="aws-resource-mediaconnect-destinationendpoint-syntax.yaml"></a>

```
Type: AWS::MediaConnect::DestinationEndpoint
Properties:
  [Configuration](#cfn-mediaconnect-destinationendpoint-configuration): {{
    DestinationEndpointConfiguration}}
  [Description](#cfn-mediaconnect-destinationendpoint-description): {{String}}
  [RegionName](#cfn-mediaconnect-destinationendpoint-regionname): {{String}}
  [Tags](#cfn-mediaconnect-destinationendpoint-tags): {{
    - Tag}}
```

## Properties
<a name="aws-resource-mediaconnect-destinationendpoint-properties"></a>

`Configuration`  <a name="cfn-mediaconnect-destinationendpoint-configuration"></a>
The configuration settings for the destination endpoint.
*Required*: Yes
*Type*: [DestinationEndpointConfiguration](aws-properties-mediaconnect-destinationendpoint-destinationendpointconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Description`  <a name="cfn-mediaconnect-destinationendpoint-description"></a>
The description of the destination endpoint.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`RegionName`  <a name="cfn-mediaconnect-destinationendpoint-regionname"></a>
The name of the AWS Region in which the destination endpoint is located.
*Required*: No
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Tags`  <a name="cfn-mediaconnect-destinationendpoint-tags"></a>
The tags associated with the destination endpoint. Each tag is a key-value pair.
*Required*: No
*Type*: Array of [Tag](aws-properties-mediaconnect-destinationendpoint-tag.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-mediaconnect-destinationendpoint-return-values"></a>

### Ref
<a name="aws-resource-mediaconnect-destinationendpoint-return-values-ref"></a>

### Fn::GetAtt
<a name="aws-resource-mediaconnect-destinationendpoint-return-values-fn--getatt"></a>

####
<a name="aws-resource-mediaconnect-destinationendpoint-return-values-fn--getatt-fn--getatt"></a>

`Arn`  <a name="Arn-fn::getatt"></a>
The Amazon Resource Name (ARN) of the destination endpoint.

`AvailabilityZone`  <a name="AvailabilityZone-fn::getatt"></a>
The Availability Zone in which the destination endpoint is located.

`AvailabilityZoneId`  <a name="AvailabilityZoneId-fn::getatt"></a>
The ID of the Availability Zone in which the destination endpoint is located.

`ConnectionState`  <a name="ConnectionState-fn::getatt"></a>
The connection state of the destination endpoint. Valid values include the following:
+ `CONNECTED` – The destination endpoint is connected to a source endpoint.
+ `DISCONNECTED` – The destination endpoint isn't connected to a source endpoint.
+ `CONNECTING` – The destination endpoint is connecting to a source endpoint.
+ `DISCONNECTING` – The destination endpoint is disconnecting from a source endpoint.

`CreatedAt`  <a name="CreatedAt-fn::getatt"></a>
The date and time when the destination endpoint was created.

`DestinationType`  <a name="DestinationType-fn::getatt"></a>
The type of the destination endpoint. Valid values include the following:
+ `STANDARD` – A destination endpoint that represents an external destination over a standard protocol, such as RTP, RIST, or SRT.
+ `ROUTER_INPUT` – A destination endpoint that represents a router input.

`Id`  <a name="Id-fn::getatt"></a>
The unique identifier of the destination endpoint.

`LifecycleManagement`  <a name="LifecycleManagement-fn::getatt"></a>
The entity that manages the lifecycle of the destination endpoint.

`Name`  <a name="Name-fn::getatt"></a>
The name of the destination endpoint.

`RegistrationState`  <a name="RegistrationState-fn::getatt"></a>
The registration state of the destination endpoint. Valid values include the following:
+ `REGISTERED` – The destination endpoint is registered and ready to use.
+ `REGISTERING` – MediaConnect is registering the destination endpoint.
+ `DEREGISTERING` – MediaConnect is deregistering the destination endpoint.
+ `REGISTRATION_FAILED` – MediaConnect couldn't register the destination endpoint.

`UpdatedAt`  <a name="UpdatedAt-fn::getatt"></a>
The date and time when the destination endpoint was last updated.
