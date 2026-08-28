---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-medialive-network.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::MediaLive::Network
<a name="aws-resource-medialive-network"></a>

Creates a network. A network is used to connect MediaLive clusters to your on-premises equipment.

## Syntax
<a name="aws-resource-medialive-network-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-medialive-network-syntax.json"></a>

```
{
  "Type" : "AWS::MediaLive::Network",
  "Properties" : {
      "[IpPools](#cfn-medialive-network-ippools)" : {{[ IpPool, ... ]}},
      "[Name](#cfn-medialive-network-name)" : {{String}},
      "[Routes](#cfn-medialive-network-routes)" : {{[ Route, ... ]}},
      "[Tags](#cfn-medialive-network-tags)" : {{[ Tags, ... ]}}
    }
}
```

### YAML
<a name="aws-resource-medialive-network-syntax.yaml"></a>

```
Type: AWS::MediaLive::Network
Properties:
  [IpPools](#cfn-medialive-network-ippools): {{
    - IpPool}}
  [Name](#cfn-medialive-network-name): {{String}}
  [Routes](#cfn-medialive-network-routes): {{
    - Route}}
  [Tags](#cfn-medialive-network-tags): {{
    - Tags}}
```

## Properties
<a name="aws-resource-medialive-network-properties"></a>

`IpPools`  <a name="cfn-medialive-network-ippools"></a>
The list of IP address CIDR pools for the network.
*Required*: Yes
*Type*: Array of [IpPool](aws-properties-medialive-network-ippool.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Name`  <a name="cfn-medialive-network-name"></a>
The user-specified name of the network.
*Required*: Yes
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Routes`  <a name="cfn-medialive-network-routes"></a>
The routes for the network.
*Required*: No
*Type*: Array of [Route](aws-properties-medialive-network-route.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Tags`  <a name="cfn-medialive-network-tags"></a>
Property description not available.
*Required*: No
*Type*: [Array](aws-properties-medialive-network-tags.md) of [Tags](aws-properties-medialive-network-tags.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-medialive-network-return-values"></a>

### Ref
<a name="aws-resource-medialive-network-return-values-ref"></a>

### Fn::GetAtt
<a name="aws-resource-medialive-network-return-values-fn--getatt"></a>

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [`Fn::GetAtt`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-getatt.html).

####
<a name="aws-resource-medialive-network-return-values-fn--getatt-fn--getatt"></a>

`Arn`  <a name="Arn-fn::getatt"></a>
The ARN of the network.

`AssociatedClusterIds`  <a name="AssociatedClusterIds-fn::getatt"></a>
The IDs of the clusters associated with this network.

`Id`  <a name="Id-fn::getatt"></a>
The unique ID of the network.

`State`  <a name="State-fn::getatt"></a>
The current state of the network.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
