---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-route53globalresolver-accesssource.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Route53GlobalResolver::AccessSource
<a name="aws-resource-route53globalresolver-accesssource"></a>

Creates an access source for a DNS view. Access sources define IP addresses or CIDR ranges that are allowed to send DNS queries to the Route 53 Global Resolver, along with the permitted DNS protocols.

**Important**
Route 53 Global Resolver is a global service that supports resolvers in multiple AWS Regions but you must specify the US East (Ohio) Region to create, update, or otherwise work with Route 53 Global Resolver resources. That is, for example, specify `--region us-east-2` on AWS CLI commands.

## Syntax
<a name="aws-resource-route53globalresolver-accesssource-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-route53globalresolver-accesssource-syntax.json"></a>

```
{
  "Type" : "AWS::Route53GlobalResolver::AccessSource",
  "Properties" : {
      "[Cidr](#cfn-route53globalresolver-accesssource-cidr)" : {{String}},
      "[ClientToken](#cfn-route53globalresolver-accesssource-clienttoken)" : {{String}},
      "[DnsViewId](#cfn-route53globalresolver-accesssource-dnsviewid)" : {{String}},
      "[IpAddressType](#cfn-route53globalresolver-accesssource-ipaddresstype)" : {{String}},
      "[Name](#cfn-route53globalresolver-accesssource-name)" : {{String}},
      "[Protocol](#cfn-route53globalresolver-accesssource-protocol)" : {{String}},
      "[Tags](#cfn-route53globalresolver-accesssource-tags)" : {{[ Tag, ... ]}}
    }
}
```

### YAML
<a name="aws-resource-route53globalresolver-accesssource-syntax.yaml"></a>

```
Type: AWS::Route53GlobalResolver::AccessSource
Properties:
  [Cidr](#cfn-route53globalresolver-accesssource-cidr): {{String}}
  [ClientToken](#cfn-route53globalresolver-accesssource-clienttoken): {{String}}
  [DnsViewId](#cfn-route53globalresolver-accesssource-dnsviewid): {{String}}
  [IpAddressType](#cfn-route53globalresolver-accesssource-ipaddresstype): {{String}}
  [Name](#cfn-route53globalresolver-accesssource-name): {{String}}
  [Protocol](#cfn-route53globalresolver-accesssource-protocol): {{String}}
  [Tags](#cfn-route53globalresolver-accesssource-tags): {{
    - Tag}}
```

## Properties
<a name="aws-resource-route53globalresolver-accesssource-properties"></a>

`Cidr`  <a name="cfn-route53globalresolver-accesssource-cidr"></a>
The CIDR block that defines the IP address range for the access source.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `42`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ClientToken`  <a name="cfn-route53globalresolver-accesssource-clienttoken"></a>
A unique string that identifies the request and ensures idempotency.
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `256`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`DnsViewId`  <a name="cfn-route53globalresolver-accesssource-dnsviewid"></a>
The ID of the DNS view that the access source is associated with.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `64`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`IpAddressType`  <a name="cfn-route53globalresolver-accesssource-ipaddresstype"></a>
The IP address type of the access source.
*Required*: No
*Type*: String
*Allowed values*: `IPV4 | IPV6`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Name`  <a name="cfn-route53globalresolver-accesssource-name"></a>
The name of the access source.
*Required*: No
*Type*: String
*Pattern*: `(?!^[0-9]+$)([a-zA-Z0-9-_' ']+)`
*Minimum*: `1`
*Maximum*: `64`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Protocol`  <a name="cfn-route53globalresolver-accesssource-protocol"></a>
The protocol used by the access source.
*Required*: Yes
*Type*: String
*Allowed values*: `DO53 | DOH | DOT`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Tags`  <a name="cfn-route53globalresolver-accesssource-tags"></a>
Tags to associate with the access source.
*Required*: No
*Type*: Array of [Tag](aws-properties-route53globalresolver-accesssource-tag.md)
*Maximum*: `50`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-route53globalresolver-accesssource-return-values"></a>

### Ref
<a name="aws-resource-route53globalresolver-accesssource-return-values-ref"></a>

### Fn::GetAtt
<a name="aws-resource-route53globalresolver-accesssource-return-values-fn--getatt"></a>

####
<a name="aws-resource-route53globalresolver-accesssource-return-values-fn--getatt-fn--getatt"></a>

`AccessSourceId`  <a name="AccessSourceId-fn::getatt"></a>
The unique identifier for the access source.

`Arn`  <a name="Arn-fn::getatt"></a>
The Amazon Resource Name (ARN) of the access source.

`CreatedAt`  <a name="CreatedAt-fn::getatt"></a>
The date and time when the access source was created.

`Status`  <a name="Status-fn::getatt"></a>
The current status of the access source.

`UpdatedAt`  <a name="UpdatedAt-fn::getatt"></a>
The date and time when the access source was last updated.
