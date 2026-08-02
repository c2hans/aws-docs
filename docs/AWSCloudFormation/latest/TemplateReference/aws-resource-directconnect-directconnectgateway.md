---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-directconnect-directconnectgateway.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::DirectConnect::DirectConnectGateway
<a name="aws-resource-directconnect-directconnectgateway"></a>

Creates a Direct Connect gateway, which is an intermediate object that enables you to connect a set of virtual interfaces and virtual private gateways. A Direct Connect gateway is global and visible in any AWS Region after it is created. The virtual interfaces and virtual private gateways that are connected through a Direct Connect gateway can be in different AWS Regions. This enables you to connect to a VPC in any Region, regardless of the Region in which the virtual interfaces are located, and pass traffic between them.

For more information, see [Direct Connect gateways](https://docs.aws.amazon.com/directconnect/latest/UserGuide/direct-connect-gateways-intro.html) in the * Direct Connect User Guide *.

## Syntax
<a name="aws-resource-directconnect-directconnectgateway-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-directconnect-directconnectgateway-syntax.json"></a>

```
{
  "Type" : "AWS::DirectConnect::DirectConnectGateway",
  "Properties" : {
      "[AmazonSideAsn](#cfn-directconnect-directconnectgateway-amazonsideasn)" : {{String}},
      "[DirectConnectGatewayName](#cfn-directconnect-directconnectgateway-directconnectgatewayname)" : {{String}},
      "[Tags](#cfn-directconnect-directconnectgateway-tags)" : {{[ Tag, ... ]}}
    }
}
```

### YAML
<a name="aws-resource-directconnect-directconnectgateway-syntax.yaml"></a>

```
Type: AWS::DirectConnect::DirectConnectGateway
Properties:
  [AmazonSideAsn](#cfn-directconnect-directconnectgateway-amazonsideasn): {{String}}
  [DirectConnectGatewayName](#cfn-directconnect-directconnectgateway-directconnectgatewayname): {{String}}
  [Tags](#cfn-directconnect-directconnectgateway-tags): {{
    - Tag}}
```

## Properties
<a name="aws-resource-directconnect-directconnectgateway-properties"></a>

`AmazonSideAsn`  <a name="cfn-directconnect-directconnectgateway-amazonsideasn"></a>
The autonomous system number (ASN) for Border Gateway Protocol (BGP) to be configured on the Amazon side of the connection. The ASN must be in the private range of 64,512 to 65,534 or 4,200,000,000 to 4,294,967,294. The default is 64512.
*Required*: No
*Type*: String
*Pattern*: `^[1-9][0-9]*$`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`DirectConnectGatewayName`  <a name="cfn-directconnect-directconnectgateway-directconnectgatewayname"></a>
The name of the Direct Connect gateway.
*Required*: Yes
*Type*: String
*Pattern*: `^[\w \-_,\/]{1,100}$`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Tags`  <a name="cfn-directconnect-directconnectgateway-tags"></a>
Information about a tag.
*Required*: No
*Type*: Array of [Tag](aws-properties-directconnect-directconnectgateway-tag.md)
*Minimum*: `1`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-directconnect-directconnectgateway-return-values"></a>

### Ref
<a name="aws-resource-directconnect-directconnectgateway-return-values-ref"></a>

When you pass the logical ID of this resource to the intrinsic `Ref` function, `Ref` returns the Amazon Resource Name (ARN) of the Direct Connect gateway.

For more information about using the `Ref` function, see [https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-ref.html](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-ref.html).

### Fn::GetAtt
<a name="aws-resource-directconnect-directconnectgateway-return-values-fn--getatt"></a>

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-getatt.html](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-getatt.html).

####
<a name="aws-resource-directconnect-directconnectgateway-return-values-fn--getatt-fn--getatt"></a>

`DirectConnectGatewayArn`  <a name="DirectConnectGatewayArn-fn::getatt"></a>
The Amazon Resource Name (ARN) of the Direct Connect gateway.

`DirectConnectGatewayId`  <a name="DirectConnectGatewayId-fn::getatt"></a>
The ID of the Direct Connect gateway.

## Examples
<a name="aws-resource-directconnect-directconnectgateway--examples"></a>

### Basic Direct Connect gateway
<a name="aws-resource-directconnect-directconnectgateway--examples--Basic_Direct_Connect_gateway"></a>

This example shows a basic Direct Connect gateway.

#### JSON
<a name="aws-resource-directconnect-directconnectgateway--examples--Basic_Direct_Connect_gateway--json"></a>

```
{
  "Resources": {
    "myDirectConnectGateway": {
      "Type": "AWS::DirectConnect::DirectConnectGateway",
      "Properties": {
        "DirectConnectGatewayName": "cfn-directconnectgateway-example",
        "AmazonSideAsn": "65412",
        "Tags": [
          {
            "Key": "example-key",
            "Value": "example-value"
          }
        ]
      }
    }
  }
}
```

#### YAML
<a name="aws-resource-directconnect-directconnectgateway--examples--Basic_Direct_Connect_gateway--yaml"></a>

```
Resources:
  myDirectConnectGateway:
    Type: AWS::DirectConnect::DirectConnectGateway
    Properties:
      DirectConnectGatewayName: cfn-directconnectgateway-example
      AmazonSideAsn: '65412'
      Tags:
      - Key: example-key
        Value: example-value
```
