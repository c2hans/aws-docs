---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-interconnect-connection.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Interconnect::Connection
<a name="aws-resource-interconnect-connection"></a>

The `AWS::Interconnect::Connection` resource specifies a managed network connection between AWS and a partner cloud service provider. Amazon Web Services Interconnect connections enable hybrid and multicloud connectivity through partner-provided last-mile or cross-cloud connectivity.

## Syntax
<a name="aws-resource-interconnect-connection-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-interconnect-connection-syntax.json"></a>

```
{
  "Type" : "AWS::Interconnect::Connection",
  "Properties" : {
      "[ActivationKey](#cfn-interconnect-connection-activationkey)" : {{String}},
      "[AttachPoint](#cfn-interconnect-connection-attachpoint)" : {{AttachPoint}},
      "[Bandwidth](#cfn-interconnect-connection-bandwidth)" : {{String}},
      "[Description](#cfn-interconnect-connection-description)" : {{String}},
      "[EnvironmentId](#cfn-interconnect-connection-environmentid)" : {{String}},
      "[RemoteAccount](#cfn-interconnect-connection-remoteaccount)" : {{RemoteAccount}},
      "[Tags](#cfn-interconnect-connection-tags)" : {{[ Tag, ... ]}}
    }
}
```

### YAML
<a name="aws-resource-interconnect-connection-syntax.yaml"></a>

```
Type: AWS::Interconnect::Connection
Properties:
  [ActivationKey](#cfn-interconnect-connection-activationkey): {{String}}
  [AttachPoint](#cfn-interconnect-connection-attachpoint): {{
    AttachPoint}}
  [Bandwidth](#cfn-interconnect-connection-bandwidth): {{String}}
  [Description](#cfn-interconnect-connection-description): {{String}}
  [EnvironmentId](#cfn-interconnect-connection-environmentid): {{String}}
  [RemoteAccount](#cfn-interconnect-connection-remoteaccount): {{
    RemoteAccount}}
  [Tags](#cfn-interconnect-connection-tags): {{
    - Tag}}
```

## Properties
<a name="aws-resource-interconnect-connection-properties"></a>

`ActivationKey`  <a name="cfn-interconnect-connection-activationkey"></a>
The activation key for accepting a connection proposal from a partner cloud service provider. Mutually exclusive with `EnvironmentId`.
*Required*: No
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`AttachPoint`  <a name="cfn-interconnect-connection-attachpoint"></a>
The logical attachment point in your AWS network where the managed connection is connected. Currently, the only supported type of attach point is a AWS Direct Connect gateway.
*Required*: Yes
*Type*: [AttachPoint](aws-properties-interconnect-connection-attachpoint.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Bandwidth`  <a name="cfn-interconnect-connection-bandwidth"></a>
The bandwidth of the connection (for example, `50Mbps` or `1Gbps`). Required when creating a connection through AWS.
*Required*: No
*Type*: String
*Pattern*: `^\d+[MG]bps$`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Description`  <a name="cfn-interconnect-connection-description"></a>
A description of the connection.
*Required*: No
*Type*: String
*Pattern*: `^[-a-zA-Z0-9_ ]+$`
*Maximum*: `255`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`EnvironmentId`  <a name="cfn-interconnect-connection-environmentid"></a>
The ID of the environment for the connection. Required when creating a connection through AWS. Mutually exclusive with `ActivationKey`.
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `32`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`RemoteAccount`  <a name="cfn-interconnect-connection-remoteaccount"></a>
The remote account identifier for the connection. Required when creating a connection through AWS. Replaces `RemoteOwnerAccount`.
*Required*: No
*Type*: [RemoteAccount](aws-properties-interconnect-connection-remoteaccount.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Tags`  <a name="cfn-interconnect-connection-tags"></a>
An array of key-value pairs to apply to this resource.
For more information, see [Tag](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-resource-tags.html).
*Required*: No
*Type*: Array of [Tag](aws-properties-interconnect-connection-tag.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-interconnect-connection-return-values"></a>

### Ref
<a name="aws-resource-interconnect-connection-return-values-ref"></a>

When you pass the logical ID of this resource to the intrinsic `Ref` function, `Ref` returns the Amazon Resource Name (ARN) of the connection.

For more information about using the `Ref` function, see [`Ref`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-ref.html).

### Fn::GetAtt
<a name="aws-resource-interconnect-connection-return-values-fn--getatt"></a>

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [`Fn::GetAtt`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-getatt.html).

####
<a name="aws-resource-interconnect-connection-return-values-fn--getatt-fn--getatt"></a>

`Arn`  <a name="Arn-fn::getatt"></a>
The Amazon Resource Name (ARN) of the connection.

`BillingTier`  <a name="BillingTier-fn::getatt"></a>
The billing tier assigned to the connection.

`ConnectionId`  <a name="ConnectionId-fn::getatt"></a>
The unique identifier of the connection.

`OwnerAccount`  <a name="OwnerAccount-fn::getatt"></a>
The AWS account ID of the connection owner.

`SharedId`  <a name="SharedId-fn::getatt"></a>
An identifier used by both AWS and the remote partner to identify the connection.

`State`  <a name="State-fn::getatt"></a>
The current state of the connection. Valid values are:
+ `requested`: The initial state of the connection. The state remains here until the connection is accepted on the partner portal.
+ `pending`: The connection has been accepted and is being provisioned between AWS and the partner.
+ `available`: The connection has been fully provisioned between AWS and the partner.
+ `down`: The connection is provisioned but not currently passing traffic.
+ `deleting`: The connection is being deleted.
+ `deleted`: The connection has been deleted.
+ `failed`: The connection failed to be created.

`Type`  <a name="Type-fn::getatt"></a>
The type of managed connection.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
