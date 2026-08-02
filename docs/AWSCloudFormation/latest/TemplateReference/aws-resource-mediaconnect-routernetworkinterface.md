---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-mediaconnect-routernetworkinterface.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::MediaConnect::RouterNetworkInterface
<a name="aws-resource-mediaconnect-routernetworkinterface"></a>

 The `AWS::MediaConnect::RouterNetworkInterface` resource defines how the router communicates with the outside world. Each router I/O needs a network interface, which determines how the router I/O connects to other resources and what security measures protect the connection.

You can work with two types of router network interface:
+ **Public network interfaces** - allow communication over the public internet.
+ **VPC network interfaces** - allow communication within your Amazon Virtual Private Cloud (VPC).

## Syntax
<a name="aws-resource-mediaconnect-routernetworkinterface-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-mediaconnect-routernetworkinterface-syntax.json"></a>

```
{
  "Type" : "AWS::MediaConnect::RouterNetworkInterface",
  "Properties" : {
      "[Configuration](#cfn-mediaconnect-routernetworkinterface-configuration)" : {{RouterNetworkInterfaceConfiguration}},
      "[Name](#cfn-mediaconnect-routernetworkinterface-name)" : {{String}},
      "[RegionName](#cfn-mediaconnect-routernetworkinterface-regionname)" : {{String}},
      "[Tags](#cfn-mediaconnect-routernetworkinterface-tags)" : {{[ Tag, ... ]}}
    }
}
```

### YAML
<a name="aws-resource-mediaconnect-routernetworkinterface-syntax.yaml"></a>

```
Type: AWS::MediaConnect::RouterNetworkInterface
Properties:
  [Configuration](#cfn-mediaconnect-routernetworkinterface-configuration): {{
    RouterNetworkInterfaceConfiguration}}
  [Name](#cfn-mediaconnect-routernetworkinterface-name): {{String}}
  [RegionName](#cfn-mediaconnect-routernetworkinterface-regionname): {{String}}
  [Tags](#cfn-mediaconnect-routernetworkinterface-tags): {{
    - Tag}}
```

## Properties
<a name="aws-resource-mediaconnect-routernetworkinterface-properties"></a>

`Configuration`  <a name="cfn-mediaconnect-routernetworkinterface-configuration"></a>
The configuration settings for a router network interface.
*Required*: Yes
*Type*: [RouterNetworkInterfaceConfiguration](aws-properties-mediaconnect-routernetworkinterface-routernetworkinterfaceconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Name`  <a name="cfn-mediaconnect-routernetworkinterface-name"></a>
The name of the router network interface.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `128`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`RegionName`  <a name="cfn-mediaconnect-routernetworkinterface-regionname"></a>
The AWS Region where the router network interface is located.
*Required*: No
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Tags`  <a name="cfn-mediaconnect-routernetworkinterface-tags"></a>
An array of key-value pairs to apply to this resource.
For more information, see [Resource tags](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-resource-tags.html).
*Required*: No
*Type*: Array of [Tag](aws-properties-mediaconnect-routernetworkinterface-tag.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-mediaconnect-routernetworkinterface-return-values"></a>

### Ref
<a name="aws-resource-mediaconnect-routernetworkinterface-return-values-ref"></a>

When you pass the logical ID of this resource to the intrinsic `Ref` function, `Ref` returns the router network interface ARN. For example:

 `{ "Ref": "arn:aws:mediaconnect:us-west-2:111122223333:routerNetworkInterface:00e8efe67aa3" }`

For more information about using the `Ref` function, see [https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-ref.html](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-ref.html).

### Fn::GetAtt
<a name="aws-resource-mediaconnect-routernetworkinterface-return-values-fn--getatt"></a>

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-getatt.html](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-getatt.html).

####
<a name="aws-resource-mediaconnect-routernetworkinterface-return-values-fn--getatt-fn--getatt"></a>

`Arn`  <a name="Arn-fn::getatt"></a>
The Amazon Resource Name (ARN) of the router network interface.

`AssociatedInputCount`  <a name="AssociatedInputCount-fn::getatt"></a>
The number of router inputs associated with the network interface.

`AssociatedOutputCount`  <a name="AssociatedOutputCount-fn::getatt"></a>
The number of router outputs associated with the network interface.

`CreatedAt`  <a name="CreatedAt-fn::getatt"></a>
The timestamp when the router network interface was created.

`Id`  <a name="Id-fn::getatt"></a>
The unique identifier of the router network interface.

`NetworkInterfaceType`  <a name="NetworkInterfaceType-fn::getatt"></a>
The type of the router network interface.

`State`  <a name="State-fn::getatt"></a>
The current state of the router network interface.

`UpdatedAt`  <a name="UpdatedAt-fn::getatt"></a>
The timestamp when the router network interface was last updated.
