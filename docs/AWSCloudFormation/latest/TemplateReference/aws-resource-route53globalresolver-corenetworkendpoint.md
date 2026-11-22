---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-route53globalresolver-corenetworkendpoint.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Route53GlobalResolver::CoreNetworkEndpoint

Creates a core network endpoint, which enables DNS resolution for AWS Cloud WAN core network segments. The endpoint connects a Route 53 Global Resolver to an AWS Cloud WAN core network so that resources attached to the core network can send DNS queries to the resolver.

**Important**
Route 53 Global Resolver is a global service that supports resolvers in multiple AWS Regions, but you must specify the US East (Ohio) Region to create, update, or otherwise work with Route 53 Global Resolver resources. That is, for example, specify `--region us-east-2` on AWS CLI commands.

## Syntax
<a name="aws-resource-route53globalresolver-corenetworkendpoint-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-route53globalresolver-corenetworkendpoint-syntax.json"></a>

```json
{
  "Type" : "AWS::Route53GlobalResolver::CoreNetworkEndpoint",
  "Properties" : {
      "[ClientToken](#cfn-route53globalresolver-corenetworkendpoint-clienttoken)" : {{String}},
      "[CoreNetworkArn](#cfn-route53globalresolver-corenetworkendpoint-corenetworkarn)" : {{String}},
      "[GlobalResolverId](#cfn-route53globalresolver-corenetworkendpoint-globalresolverid)" : {{String}},
      "[IpAddresses](#cfn-route53globalresolver-corenetworkendpoint-ipaddresses)" : {{[ IpAddress, ... ]}},
      "[Name](#cfn-route53globalresolver-corenetworkendpoint-name)" : {{String}},
      "[Tags](#cfn-route53globalresolver-corenetworkendpoint-tags)" : {{[ Tag, ... ]}}
    }
}
```

### YAML
<a name="aws-resource-route53globalresolver-corenetworkendpoint-syntax.yaml"></a>

```yaml
Type: AWS::Route53GlobalResolver::CoreNetworkEndpoint
Properties:
  [ClientToken](#cfn-route53globalresolver-corenetworkendpoint-clienttoken): {{String}}
  [CoreNetworkArn](#cfn-route53globalresolver-corenetworkendpoint-corenetworkarn): {{String}}
  [GlobalResolverId](#cfn-route53globalresolver-corenetworkendpoint-globalresolverid): {{String}}
  [IpAddresses](#cfn-route53globalresolver-corenetworkendpoint-ipaddresses): {{
    - IpAddress}}
  [Name](#cfn-route53globalresolver-corenetworkendpoint-name): {{String}}
  [Tags](#cfn-route53globalresolver-corenetworkendpoint-tags): {{
    - Tag}}
```

## Properties
<a name="aws-resource-route53globalresolver-corenetworkendpoint-properties"></a>

`ClientToken`  <a name="cfn-route53globalresolver-corenetworkendpoint-clienttoken"></a>
A unique, case-sensitive identifier that ensures the request is idempotent. Making the same request multiple times with the same `clientToken` produces the same result every time.
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `256`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`CoreNetworkArn`  <a name="cfn-route53globalresolver-corenetworkendpoint-corenetworkarn"></a>
The Amazon Resource Name (ARN) of the AWS Cloud WAN core network to connect to this endpoint.
*Required*: Yes
*Type*: String
*Pattern*: `^arn:[-.a-z0-9]{1,63}:[-.a-z0-9]{1,63}:[-.a-z0-9]{0,63}:[-.a-z0-9]{0,63}:[^/].{0,1023}$`
*Minimum*: `1`
*Maximum*: `2048`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`GlobalResolverId`  <a name="cfn-route53globalresolver-corenetworkendpoint-globalresolverid"></a>
The ID of the Route 53 Global Resolver to associate with this core network endpoint.
*Required*: Yes
*Type*: String
*Pattern*: `^[-.a-zA-Z0-9]+$`
*Minimum*: `1`
*Maximum*: `64`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`IpAddresses`  <a name="cfn-route53globalresolver-corenetworkendpoint-ipaddresses"></a>
The IP addresses that the core network endpoint uses to resolve DNS queries within the AWS Cloud WAN core network.
*Required*: Yes
*Type*: Array of [IpAddress](aws-properties-route53globalresolver-corenetworkendpoint-ipaddress.md)
*Minimum*: `1`
*Maximum*: `5`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Name`  <a name="cfn-route53globalresolver-corenetworkendpoint-name"></a>
A descriptive name for the core network endpoint.
*Required*: No
*Type*: String
*Pattern*: `^(?!^[0-9]+$)([a-zA-Z0-9-_/' ']+)$`
*Minimum*: `1`
*Maximum*: `64`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Tags`  <a name="cfn-route53globalresolver-corenetworkendpoint-tags"></a>
An array of user-defined keys and optional values that you can use to categorize and organize the core network endpoint.
*Required*: No
*Type*: Array of [Tag](aws-properties-route53globalresolver-corenetworkendpoint-tag.md)
*Maximum*: `50`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-route53globalresolver-corenetworkendpoint-return-values"></a>

### Ref
<a name="aws-resource-route53globalresolver-corenetworkendpoint-return-values-ref"></a>

When you pass the logical ID of this resource to the intrinsic `Ref` function, `Ref` returns the ID of the core network endpoint. For example:

 `{ "Ref": "myCoreNetworkEndpoint" }`

For the core network endpoint `myCoreNetworkEndpoint`, `Ref` returns the core network endpoint ID, such as `cne-1234567890abcdef0`.

For more information about using the `Ref` function, see [`Ref`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-ref.html).

### Fn::GetAtt
<a name="aws-resource-route53globalresolver-corenetworkendpoint-return-values-fn--getatt"></a>

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [`Fn::GetAtt`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-getatt.html).

####
<a name="aws-resource-route53globalresolver-corenetworkendpoint-return-values-fn--getatt-fn--getatt"></a>

`Arn`  <a name="Arn-fn::getatt"></a>
The Amazon Resource Name (ARN) of the core network endpoint.

`AvailableRegions`  <a name="AvailableRegions-fn::getatt"></a>
The AWS Regions in which the core network endpoint is available.

`CoreNetworkEndpointId`  <a name="CoreNetworkEndpointId-fn::getatt"></a>
The unique identifier of the core network endpoint.

`CreatedAt`  <a name="CreatedAt-fn::getatt"></a>
The date and time when the core network endpoint was created.

`Status`  <a name="Status-fn::getatt"></a>
The current status of the core network endpoint.

`UpdatedAt`  <a name="UpdatedAt-fn::getatt"></a>
The date and time when the core network endpoint was last updated.
