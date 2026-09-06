---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-directconnect-lag.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::DirectConnect::Lag
<a name="aws-resource-directconnect-lag"></a>

Creates a link aggregation group (LAG) in a specific Direct Connect location. A LAG is a logical interface that uses the Link Aggregation Control Protocol (LACP) to aggregate multiple interfaces, enabling you to treat them as a single interface.

All connections in a LAG must use the same bandwidth (either 1Gbps, 10Gbps, 100Gbps, or 400Gbps) and must terminate at the same Direct Connect endpoint.

You can have up to 10 dedicated connections per location. Regardless of this limit, if you request more connections for the LAG than Direct Connect can allocate on a single endpoint, no LAG is created.

If the AWS account used to create a LAG is a registered Direct Connect Partner, the LAG is automatically enabled to host sub-connections. For a LAG owned by a partner, any associated virtual interfaces cannot be directly configured.

**Note**
LAGs created using CloudFormation have no connections by default.

For more information, see [Direct Connect link aggregation groups (LAGs)](https://docs.aws.amazon.com/directconnect/latest/UserGuide/lags.html) in the * Direct Connect User Guide *.

## Syntax
<a name="aws-resource-directconnect-lag-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-directconnect-lag-syntax.json"></a>

```
{
  "Type" : "AWS::DirectConnect::Lag",
  "Properties" : {
      "[ConnectionsBandwidth](#cfn-directconnect-lag-connectionsbandwidth)" : {{String}},
      "[LagName](#cfn-directconnect-lag-lagname)" : {{String}},
      "[Location](#cfn-directconnect-lag-location)" : {{String}},
      "[MinimumLinks](#cfn-directconnect-lag-minimumlinks)" : {{Integer}},
      "[ProviderName](#cfn-directconnect-lag-providername)" : {{String}},
      "[RequestMACSec](#cfn-directconnect-lag-requestmacsec)" : {{Boolean}},
      "[Tags](#cfn-directconnect-lag-tags)" : {{[ Tag, ... ]}}
    }
}
```

### YAML
<a name="aws-resource-directconnect-lag-syntax.yaml"></a>

```
Type: AWS::DirectConnect::Lag
Properties:
  [ConnectionsBandwidth](#cfn-directconnect-lag-connectionsbandwidth): {{String}}
  [LagName](#cfn-directconnect-lag-lagname): {{String}}
  [Location](#cfn-directconnect-lag-location): {{String}}
  [MinimumLinks](#cfn-directconnect-lag-minimumlinks): {{Integer}}
  [ProviderName](#cfn-directconnect-lag-providername): {{String}}
  [RequestMACSec](#cfn-directconnect-lag-requestmacsec): {{Boolean}}
  [Tags](#cfn-directconnect-lag-tags): {{
    - Tag}}
```

## Properties
<a name="aws-resource-directconnect-lag-properties"></a>

`ConnectionsBandwidth`  <a name="cfn-directconnect-lag-connectionsbandwidth"></a>
The individual bandwidth of the physical connections bundled by the LAG. The possible values are 1Gbps, 10Gbps, 100Gbps, or 400 Gbps..
*Required*: Yes
*Type*: String
*Pattern*: `^[1-9][0-9]*(M|G)bps$`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`LagName`  <a name="cfn-directconnect-lag-lagname"></a>
The name of the LAG.
*Required*: Yes
*Type*: String
*Pattern*: `^[\w \-_,\/]{1,200}$`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Location`  <a name="cfn-directconnect-lag-location"></a>
The location of the LAG.
*Required*: Yes
*Type*: String
*Pattern*: `^[a-zA-Z0-9-]+$`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`MinimumLinks`  <a name="cfn-directconnect-lag-minimumlinks"></a>
The minimum number of physical dedicated connections that must be operational for the LAG itself to be operational.
This property cannot be used when the LAG is being created for the first time using the template.
*Required*: No
*Type*: Integer
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ProviderName`  <a name="cfn-directconnect-lag-providername"></a>
The name of the service provider associated with the LAG.
*Required*: No
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`RequestMACSec`  <a name="cfn-directconnect-lag-requestmacsec"></a>
Indicates whether the connection will support MAC Security (MACsec).
All connections in the LAG must be capable of supporting MAC Security (MACsec). For information about MAC Security (MACsec) prerequisties, see [MACsec prerequisties](https://docs.aws.amazon.com/directconnect/latest/UserGuide/direct-connect-mac-sec-getting-started.html#mac-sec-prerequisites) in the *Direct Connect User Guide*.
*Required*: No
*Type*: Boolean
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Tags`  <a name="cfn-directconnect-lag-tags"></a>
The tags associated with the LAG.
*Required*: No
*Type*: Array of [Tag](aws-properties-directconnect-lag-tag.md)
*Minimum*: `1`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-directconnect-lag-return-values"></a>

### Ref
<a name="aws-resource-directconnect-lag-return-values-ref"></a>

When you pass the logical ID of this resource to the intrinsic `Ref` function, `Ref` returns the Amazon Resource Name (ARN) of the LAG.

For more information about using the `Ref` function, see [`Ref`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-ref.html).

### Fn::GetAtt
<a name="aws-resource-directconnect-lag-return-values-fn--getatt"></a>

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [`Fn::GetAtt`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-getatt.html).

####
<a name="aws-resource-directconnect-lag-return-values-fn--getatt-fn--getatt"></a>

`LagArn`  <a name="LagArn-fn::getatt"></a>
The Amazon Resource Name (ARN) of the LAG.

`LagId`  <a name="LagId-fn::getatt"></a>
The ID of the LAG.

`LagState`  <a name="LagState-fn::getatt"></a>
The state of the LAG. The following are the possible values:
+ `requested`: The initial state of a LAG. The LAG stays in the requested state until the Letter of Authorization (LOA) is available.
+ `pending`: The LAG has been approved and is being initialized.
+ `available`: The network link is established and the LAG is ready for use.
+ `down`: The network link is down.
+ `deleting`: The LAG is being deleted.
+ `deleted`: The LAG is deleted.
+ `unknown`: The state of the LAG is not available.

## Examples
<a name="aws-resource-directconnect-lag--examples"></a>

### Create LAG with one connection
<a name="aws-resource-directconnect-lag--examples--Create_LAG_with_one_connection"></a>

This example shows a basic LAG which has one connection created on it. The bandwidth of the connections on the LAG is 10Gbps.

#### JSON
<a name="aws-resource-directconnect-lag--examples--Create_LAG_with_one_connection--json"></a>

```
{
  "Resources": {
    "myLag": {
      "Type": "AWS::DirectConnect::Lag",
      "Properties": {
        "LagName": "cfn-lag-example",
        "ConnectionsBandwidth": "10Gbps",
        "Location": "EqSY3",
        "Tags": [
          {
            "Key": "example-key",
            "Value": "example-value"
          }
        ]
      }
    },
    "myConnection": {
      "Type": "AWS::DirectConnect::Connection",
      "Properties": {
        "ConnectionName": "cfn-connection-example",
        "Bandwidth": "10Gbps",
        "Location": "EqSY3",
        "LagId": {
          "Ref": "myLag"
        }
      }
    }
  }
}
```

#### YAML
<a name="aws-resource-directconnect-lag--examples--Create_LAG_with_one_connection--yaml"></a>

```
Resources:
  myLag:
    Type: AWS::DirectConnect::Lag
    Properties:
      LagName: cfn-lag-example
      ConnectionsBandwidth: 10Gbps
      Location: EqSY3
      Tags:
      - Key: example-key
        Value: example-value
  myConnection:
    Type: AWS::DirectConnect::Connection
    Properties:
      ConnectionName: cfn-connection-example
      Bandwidth: 10Gbps
      Location: EqSY3
      LagId: !Ref myLag
```
