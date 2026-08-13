---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-ec2-customergateway.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::EC2::CustomerGateway
<a name="aws-resource-ec2-customergateway"></a>

Specifies a customer gateway.

## Syntax
<a name="aws-resource-ec2-customergateway-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-ec2-customergateway-syntax.json"></a>

```
{
  "Type" : "AWS::EC2::CustomerGateway",
  "Properties" : {
      "[BgpAsn](#cfn-ec2-customergateway-bgpasn)" : {{Integer}},
      "[BgpAsnExtended](#cfn-ec2-customergateway-bgpasnextended)" : {{Number}},
      "[CertificateArn](#cfn-ec2-customergateway-certificatearn)" : {{String}},
      "[DeviceName](#cfn-ec2-customergateway-devicename)" : {{String}},
      "[IpAddress](#cfn-ec2-customergateway-ipaddress)" : {{String}},
      "[Tags](#cfn-ec2-customergateway-tags)" : {{[ Tag, ... ]}},
      "[Type](#cfn-ec2-customergateway-type)" : {{String}}
    }
}
```

### YAML
<a name="aws-resource-ec2-customergateway-syntax.yaml"></a>

```
Type: AWS::EC2::CustomerGateway
Properties:
  [BgpAsn](#cfn-ec2-customergateway-bgpasn): {{Integer}}
  [BgpAsnExtended](#cfn-ec2-customergateway-bgpasnextended): {{Number}}
  [CertificateArn](#cfn-ec2-customergateway-certificatearn): {{String}}
  [DeviceName](#cfn-ec2-customergateway-devicename): {{String}}
  [IpAddress](#cfn-ec2-customergateway-ipaddress): {{String}}
  [Tags](#cfn-ec2-customergateway-tags): {{
    - Tag}}
  [Type](#cfn-ec2-customergateway-type): {{String}}
```

## Properties
<a name="aws-resource-ec2-customergateway-properties"></a>

`BgpAsn`  <a name="cfn-ec2-customergateway-bgpasn"></a>
For customer gateway devices that support BGP, specify the device's ASN. You must specify either `BgpAsn` or `BgpAsnExtended` when creating the customer gateway. If the ASN is larger than `2,147,483,647`, you must use `BgpAsnExtended`.
Default: 65000
Valid values: `1` to `2,147,483,647`
*Required*: No
*Type*: Integer
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`BgpAsnExtended`  <a name="cfn-ec2-customergateway-bgpasnextended"></a>
For customer gateway devices that support BGP, specify the device's ASN. You must specify either `BgpAsn` or `BgpAsnExtended` when creating the customer gateway. If the ASN is larger than `2,147,483,647`, you must use `BgpAsnExtended`.
Valid values: `2,147,483,648` to `4,294,967,295`
*Required*: No
*Type*: Number
*Minimum*: `2147483648`
*Maximum*: `4294967294`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`CertificateArn`  <a name="cfn-ec2-customergateway-certificatearn"></a>
The Amazon Resource Name (ARN) for the customer gateway certificate.
*Required*: No
*Type*: String
*Pattern*: `^arn:(aws[a-zA-Z-]*)?:acm:[a-z]{2}((-gov)|(-iso([a-z]{1})?))?-[a-z]+-\d{1}:\d{12}:certificate\/[a-zA-Z0-9-_]+$`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`DeviceName`  <a name="cfn-ec2-customergateway-devicename"></a>
The name of customer gateway device.
*Required*: No
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`IpAddress`  <a name="cfn-ec2-customergateway-ipaddress"></a>
The IP address for the customer gateway device's outside interface. The address must be static. If `OutsideIpAddressType` in your VPN connection options is set to `PrivateIpv4`, you can use an RFC6598 or RFC1918 private IPv4 address. If `OutsideIpAddressType` is set to `Ipv6`, you can use an IPv6 address.
*Required*: Yes
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Tags`  <a name="cfn-ec2-customergateway-tags"></a>
One or more tags for the customer gateway.
*Required*: No
*Type*: Array of [Tag](aws-properties-ec2-customergateway-tag.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Type`  <a name="cfn-ec2-customergateway-type"></a>
The type of VPN connection that this customer gateway supports (`ipsec.1`).
*Required*: Yes
*Type*: String
*Allowed values*: `ipsec.1`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## Return values
<a name="aws-resource-ec2-customergateway-return-values"></a>

### Ref
<a name="aws-resource-ec2-customergateway-return-values-ref"></a>

When you pass the logical ID of this resource to the intrinsic `Ref` function, `Ref` returns the ID of the customer gateway.

For more information about using the `Ref` function, see [`Ref`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-ref.html).

### Fn::GetAtt
<a name="aws-resource-ec2-customergateway-return-values-fn--getatt"></a>

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [`Fn::GetAtt`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-getatt.html).

####
<a name="aws-resource-ec2-customergateway-return-values-fn--getatt-fn--getatt"></a>

`CustomerGatewayId`  <a name="CustomerGatewayId-fn::getatt"></a>
The ID of the customer gateway.

## Examples
<a name="aws-resource-ec2-customergateway--examples"></a>

### Create a customer gateway
<a name="aws-resource-ec2-customergateway--examples--Create_a_customer_gateway"></a>

The following example creates a customer gateway.

#### YAML
<a name="aws-resource-ec2-customergateway--examples--Create_a_customer_gateway--yaml"></a>

```
myCustomerGateway:
    Type: AWS::EC2::CustomerGateway
    Properties:
        Type: ipsec.1
        BgpAsn: 65534
        IpAddress: 12.1.2.3
```

#### JSON
<a name="aws-resource-ec2-customergateway--examples--Create_a_customer_gateway--json"></a>

```
{
    "myCustomerGateway" : {
        "Type" : "AWS::EC2::CustomerGateway",
        "Properties" : {
            "Type" : "ipsec.1",
            "BgpAsn" : "65534",
            "IpAddress" : "12.1.2.3"
        }
    }
}
```

## See also
<a name="aws-resource-ec2-customergateway--seealso"></a>
+ [CreateCustomerGateway](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/ApiReference-query-CreateCustomerGateway.html) in the *Amazon EC2 API Reference*
