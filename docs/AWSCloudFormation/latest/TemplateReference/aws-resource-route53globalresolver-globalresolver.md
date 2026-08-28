---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-route53globalresolver-globalresolver.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Route53GlobalResolver::GlobalResolver
<a name="aws-resource-route53globalresolver-globalresolver"></a>

Creates a new Route 53 Global Resolver instance. A Route 53 Global Resolver is a global, internet-accessible DNS resolver that provides secure DNS resolution for both public and private domains through global anycast IP addresses.

**Important**
Route 53 Global Resolver is a global service that supports resolvers in multiple AWS Regions but you must specify the US East (Ohio) Region to create, update, or otherwise work with Route 53 Global Resolver resources. That is, for example, specify `--region us-east-2` on AWS CLI commands.

## Syntax
<a name="aws-resource-route53globalresolver-globalresolver-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-route53globalresolver-globalresolver-syntax.json"></a>

```
{
  "Type" : "AWS::Route53GlobalResolver::GlobalResolver",
  "Properties" : {
      "[ClientToken](#cfn-route53globalresolver-globalresolver-clienttoken)" : {{String}},
      "[Description](#cfn-route53globalresolver-globalresolver-description)" : {{String}},
      "[IpAddressType](#cfn-route53globalresolver-globalresolver-ipaddresstype)" : {{String}},
      "[Name](#cfn-route53globalresolver-globalresolver-name)" : {{String}},
      "[ObservabilityRegion](#cfn-route53globalresolver-globalresolver-observabilityregion)" : {{String}},
      "[Regions](#cfn-route53globalresolver-globalresolver-regions)" : {{[ String, ... ]}},
      "[Tags](#cfn-route53globalresolver-globalresolver-tags)" : {{[ Tag, ... ]}}
    }
}
```

### YAML
<a name="aws-resource-route53globalresolver-globalresolver-syntax.yaml"></a>

```
Type: AWS::Route53GlobalResolver::GlobalResolver
Properties:
  [ClientToken](#cfn-route53globalresolver-globalresolver-clienttoken): {{String}}
  [Description](#cfn-route53globalresolver-globalresolver-description): {{String}}
  [IpAddressType](#cfn-route53globalresolver-globalresolver-ipaddresstype): {{String}}
  [Name](#cfn-route53globalresolver-globalresolver-name): {{String}}
  [ObservabilityRegion](#cfn-route53globalresolver-globalresolver-observabilityregion): {{String}}
  [Regions](#cfn-route53globalresolver-globalresolver-regions): {{
    - String}}
  [Tags](#cfn-route53globalresolver-globalresolver-tags): {{
    - Tag}}
```

## Properties
<a name="aws-resource-route53globalresolver-globalresolver-properties"></a>

`ClientToken`  <a name="cfn-route53globalresolver-globalresolver-clienttoken"></a>
The unique string that identifies the request and ensures idempotency.
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `256`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Description`  <a name="cfn-route53globalresolver-globalresolver-description"></a>
A description of the global resolver.
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `256`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`IpAddressType`  <a name="cfn-route53globalresolver-globalresolver-ipaddresstype"></a>
The IP address type for the Route 53 Global Resolver. Valid values are IPV4 (default) or DUAL\_STACK for both IPv4 and IPv6 support.
*Required*: No
*Type*: String
*Allowed values*: `IPV4 | DUAL_STACK`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Name`  <a name="cfn-route53globalresolver-globalresolver-name"></a>
The name of the global resolver.
*Required*: Yes
*Type*: String
*Pattern*: `(?!^[0-9]+$)([a-zA-Z0-9-_' ']+)`
*Minimum*: `1`
*Maximum*: `64`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ObservabilityRegion`  <a name="cfn-route53globalresolver-globalresolver-observabilityregion"></a>
The AWS Region where observability data is collected for the global resolver.
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `32`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Regions`  <a name="cfn-route53globalresolver-globalresolver-regions"></a>
The AWS Regions where the global resolver is deployed.
*Required*: Yes
*Type*: Array of String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Tags`  <a name="cfn-route53globalresolver-globalresolver-tags"></a>
Tags to associate with the Route 53 Global Resolver. Tags are key-value pairs that help you organize and identify your resources.
*Required*: No
*Type*: Array of [Tag](aws-properties-route53globalresolver-globalresolver-tag.md)
*Maximum*: `50`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-route53globalresolver-globalresolver-return-values"></a>

### Ref
<a name="aws-resource-route53globalresolver-globalresolver-return-values-ref"></a>

### Fn::GetAtt
<a name="aws-resource-route53globalresolver-globalresolver-return-values-fn--getatt"></a>

####
<a name="aws-resource-route53globalresolver-globalresolver-return-values-fn--getatt-fn--getatt"></a>

`Arn`  <a name="Arn-fn::getatt"></a>
The Amazon Resource Name (ARN) of the global resolver.

`CreatedAt`  <a name="CreatedAt-fn::getatt"></a>
The date and time when the global resolver was created.

`DnsName`  <a name="DnsName-fn::getatt"></a>
The DNS name of the global resolver.

`GlobalResolverId`  <a name="GlobalResolverId-fn::getatt"></a>
The unique identifier for the Route 53 Global Resolver.

`IPv4Addresses`  <a name="IPv4Addresses-fn::getatt"></a>
The IPv4 addresses assigned to the global resolver.

`IPv6Addresses`  <a name="IPv6Addresses-fn::getatt"></a>
The global anycast IPv6 addresses associated with the Route 53 Global Resolver. This field is only populated when ipAddressType is DUAL\_STACK. DNS clients can send queries to these addresses from anywhere on the internet.

`Status`  <a name="Status-fn::getatt"></a>
The current status of the global resolver.

`UpdatedAt`  <a name="UpdatedAt-fn::getatt"></a>
The date and time when the global resolver was last updated.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
