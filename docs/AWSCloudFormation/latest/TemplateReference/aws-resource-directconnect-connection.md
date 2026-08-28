---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-directconnect-connection.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::DirectConnect::Connection
<a name="aws-resource-directconnect-connection"></a>

Creates a connection between a customer network and a specific Direct Connect location.

A connection links your internal network to an Direct Connect location over a standard Ethernet fiber-optic cable. One end of the cable is connected to your router, the other to an Direct Connect router.

To find the locations for your Region, use [DescribeLocations](https://docs.aws.amazon.com/directconnect/latest/APIReference/API_DescribeLocations.html).

You can automatically add the new connection to a link aggregation group (LAG) by specifying a LAG ID in the request. This ensures that the new connection is allocated on the same Direct Connect endpoint that hosts the specified LAG. If there are no available ports on the endpoint, the request fails and no connection is created.

**Important**
Upon creation, a connection will enter the `requested` state. The connection cannot be used with other resources until it is approved and advances to `available` or `down`.
In order to create a virtual interface using a connection defined in the same CloudFormation template, it is recommended to create a LAG and create the virtual interface using the LAG. Member connections can be added to the LAG in the CloudFormation template.

For more information, see [Dedicated Direct Connect connections](https://docs.aws.amazon.com/directconnect/latest/UserGuide/dedicated_connection.html) in the * Direct Connect User Guide *.

## Syntax
<a name="aws-resource-directconnect-connection-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-directconnect-connection-syntax.json"></a>

```
{
  "Type" : "AWS::DirectConnect::Connection",
  "Properties" : {
      "[Bandwidth](#cfn-directconnect-connection-bandwidth)" : {{String}},
      "[ConnectionName](#cfn-directconnect-connection-connectionname)" : {{String}},
      "[LagId](#cfn-directconnect-connection-lagid)" : {{String}},
      "[Location](#cfn-directconnect-connection-location)" : {{String}},
      "[ProviderName](#cfn-directconnect-connection-providername)" : {{String}},
      "[RequestMACSec](#cfn-directconnect-connection-requestmacsec)" : {{Boolean}},
      "[Tags](#cfn-directconnect-connection-tags)" : {{[ Tag, ... ]}}
    }
}
```

### YAML
<a name="aws-resource-directconnect-connection-syntax.yaml"></a>

```
Type: AWS::DirectConnect::Connection
Properties:
  [Bandwidth](#cfn-directconnect-connection-bandwidth): {{String}}
  [ConnectionName](#cfn-directconnect-connection-connectionname): {{String}}
  [LagId](#cfn-directconnect-connection-lagid): {{String}}
  [Location](#cfn-directconnect-connection-location): {{String}}
  [ProviderName](#cfn-directconnect-connection-providername): {{String}}
  [RequestMACSec](#cfn-directconnect-connection-requestmacsec): {{Boolean}}
  [Tags](#cfn-directconnect-connection-tags): {{
    - Tag}}
```

## Properties
<a name="aws-resource-directconnect-connection-properties"></a>

`Bandwidth`  <a name="cfn-directconnect-connection-bandwidth"></a>
The bandwidth of the connection.
*Required*: Yes
*Type*: String
*Pattern*: `^[1-9][0-9]*(M|G)bps$`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`ConnectionName`  <a name="cfn-directconnect-connection-connectionname"></a>
The name of the connection.
*Required*: Yes
*Type*: String
*Pattern*: `^[\w \-_,\/]{1,200}$`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`LagId`  <a name="cfn-directconnect-connection-lagid"></a>
The ID or ARN of the LAG to associate the connection with.
Connectivity will be interrupted when associating or disassociating a connection with a LAG.
*Required*: No
*Type*: String
*Pattern*: `^(arn:aws[a-z-]*:directconnect:[a-z0-9-]+:[0-9]{12}:dxlag/)?dxlag-[a-zA-Z0-9]{8,21}$`
*Update requires*: [Some interruptions](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-some-interrupt)

`Location`  <a name="cfn-directconnect-connection-location"></a>
The location of the connection.
*Required*: Yes
*Type*: String
*Pattern*: `^[a-zA-Z0-9-]+$`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`ProviderName`  <a name="cfn-directconnect-connection-providername"></a>
The name of the service provider associated with the connection.
*Required*: No
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`RequestMACSec`  <a name="cfn-directconnect-connection-requestmacsec"></a>
Indicates whether you want the connection to support MAC Security (MACsec).
MAC Security (MACsec) is unavailable on hosted connections. For information about MAC Security (MACsec) prerequisites, see [MAC Security in Direct Connect](https://docs.aws.amazon.com/directconnect/latest/UserGuide/MACSec.html) in the *Direct Connect User Guide*.
*Required*: No
*Type*: Boolean
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Tags`  <a name="cfn-directconnect-connection-tags"></a>
The tags associated with the connection.
*Required*: No
*Type*: Array of [Tag](aws-properties-directconnect-connection-tag.md)
*Minimum*: `1`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-directconnect-connection-return-values"></a>

### Ref
<a name="aws-resource-directconnect-connection-return-values-ref"></a>

When you pass the logical ID of this resource to the intrinsic `Ref` function, `Ref` returns the Amazon Resource Name (ARN) of the connection.

For more information about using the `Ref` function, see [`Ref`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-ref.html).

### Fn::GetAtt
<a name="aws-resource-directconnect-connection-return-values-fn--getatt"></a>

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [`Fn::GetAtt`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-getatt.html).

####
<a name="aws-resource-directconnect-connection-return-values-fn--getatt-fn--getatt"></a>

`ConnectionArn`  <a name="ConnectionArn-fn::getatt"></a>
The Amazon Resource Name (ARN) of the connection.

`ConnectionId`  <a name="ConnectionId-fn::getatt"></a>
The ID of the connection.

`ConnectionState`  <a name="ConnectionState-fn::getatt"></a>
The state of the connection. The following are the possible values:
+ `ordering`: The initial state of a hosted connection provisioned on an interconnect. The connection stays in the ordering state until the owner of the hosted connection confirms or declines the connection order.
+ `requested`: The initial state of a standard connection. The connection stays in the requested state until the Letter of Authorization (LOA) is sent to the customer.
+ `pending`: The connection has been approved and is being initialized.
+ `available`: The network link is up and the connection is ready for use.
+ `down`: The network link is down.
+ `deleting`: The connection is being deleted.
+ `deleted`: The connection has been deleted.
+ `rejected`: A hosted connection in the `ordering` state enters the `rejected` state if it is deleted by the customer.
+ `unknown`: The state of the connection is not available.

## Examples
<a name="aws-resource-directconnect-connection--examples"></a>

### Basic connection
<a name="aws-resource-directconnect-connection--examples--Basic_connection"></a>

This example shows a basic connection. The bandwidth of the connection is 10Gbps.

#### JSON
<a name="aws-resource-directconnect-connection--examples--Basic_connection--json"></a>

```
{
  "Resources": {
    "myConnection": {
      "Type": "AWS::DirectConnect::Connection",
      "Properties": {
        "ConnectionName": "cfn-connection-example",
        "Bandwidth": "10Gbps",
        "Location": "EqSY3",
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
<a name="aws-resource-directconnect-connection--examples--Basic_connection--yaml"></a>

```
Resources:
  myConnection:
    Type: AWS::DirectConnect::Connection
    Properties:
      ConnectionName: cfn-connection-example
      Bandwidth: 10Gbps
      Location: EqSY3
      Tags:
      - Key: example-key
        Value: example-value
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
