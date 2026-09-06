---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-route53globalresolver-dnsview.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Route53GlobalResolver::DnsView
<a name="aws-resource-route53globalresolver-dnsview"></a>

Creates a DNS view within a Route 53 Global Resolver. A DNS view models end users, user groups, networks, and devices, and serves as a parent resource that holds configurations controlling access, authorization, DNS firewall rules, and forwarding rules.

**Important**
Route 53 Global Resolver is a global service that supports resolvers in multiple AWS Regions but you must specify the US East (Ohio) Region to create, update, or otherwise work with Route 53 Global Resolver resources. That is, for example, specify `--region us-east-2` on AWS CLI commands.

## Syntax
<a name="aws-resource-route53globalresolver-dnsview-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-route53globalresolver-dnsview-syntax.json"></a>

```
{
  "Type" : "AWS::Route53GlobalResolver::DnsView",
  "Properties" : {
      "[ClientToken](#cfn-route53globalresolver-dnsview-clienttoken)" : {{String}},
      "[Description](#cfn-route53globalresolver-dnsview-description)" : {{String}},
      "[DnssecValidation](#cfn-route53globalresolver-dnsview-dnssecvalidation)" : {{String}},
      "[EdnsClientSubnet](#cfn-route53globalresolver-dnsview-ednsclientsubnet)" : {{String}},
      "[FirewallRulesFailOpen](#cfn-route53globalresolver-dnsview-firewallrulesfailopen)" : {{String}},
      "[GlobalResolverId](#cfn-route53globalresolver-dnsview-globalresolverid)" : {{String}},
      "[Name](#cfn-route53globalresolver-dnsview-name)" : {{String}},
      "[Tags](#cfn-route53globalresolver-dnsview-tags)" : {{[ Tag, ... ]}}
    }
}
```

### YAML
<a name="aws-resource-route53globalresolver-dnsview-syntax.yaml"></a>

```
Type: AWS::Route53GlobalResolver::DnsView
Properties:
  [ClientToken](#cfn-route53globalresolver-dnsview-clienttoken): {{String}}
  [Description](#cfn-route53globalresolver-dnsview-description): {{String}}
  [DnssecValidation](#cfn-route53globalresolver-dnsview-dnssecvalidation): {{String}}
  [EdnsClientSubnet](#cfn-route53globalresolver-dnsview-ednsclientsubnet): {{String}}
  [FirewallRulesFailOpen](#cfn-route53globalresolver-dnsview-firewallrulesfailopen): {{String}}
  [GlobalResolverId](#cfn-route53globalresolver-dnsview-globalresolverid): {{String}}
  [Name](#cfn-route53globalresolver-dnsview-name): {{String}}
  [Tags](#cfn-route53globalresolver-dnsview-tags): {{
    - Tag}}
```

## Properties
<a name="aws-resource-route53globalresolver-dnsview-properties"></a>

`ClientToken`  <a name="cfn-route53globalresolver-dnsview-clienttoken"></a>
A unique string that identifies the request and ensures idempotency.
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `256`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Description`  <a name="cfn-route53globalresolver-dnsview-description"></a>
An optional description for the DNS view.
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `256`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`DnssecValidation`  <a name="cfn-route53globalresolver-dnsview-dnssecvalidation"></a>
Whether to enable DNSSEC validation for DNS queries in this DNS view. When enabled, the resolver verifies the authenticity and integrity of DNS responses from public name servers for DNSSEC-signed domains.
*Required*: No
*Type*: String
*Allowed values*: `ENABLED | DISABLED`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`EdnsClientSubnet`  <a name="cfn-route53globalresolver-dnsview-ednsclientsubnet"></a>
Whether to enable EDNS Client Subnet injection for DNS queries in this DNS view. When enabled, client subnet information is forwarded to provide more accurate geographic-based DNS responses.
*Required*: No
*Type*: String
*Allowed values*: `ENABLED | DISABLED`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`FirewallRulesFailOpen`  <a name="cfn-route53globalresolver-dnsview-firewallrulesfailopen"></a>
Determines the behavior when Route 53 Global Resolver cannot apply DNS firewall rules due to service impairment. When enabled, DNS queries are allowed through; when disabled, queries are blocked.
*Required*: No
*Type*: String
*Allowed values*: `ENABLED | DISABLED`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`GlobalResolverId`  <a name="cfn-route53globalresolver-dnsview-globalresolverid"></a>
The ID of the Route 53 Global Resolver to associate with this DNS view.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `64`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Name`  <a name="cfn-route53globalresolver-dnsview-name"></a>
A descriptive name for the DNS view.
*Required*: Yes
*Type*: String
*Pattern*: `(?!^[0-9]+$)([a-zA-Z0-9-_' ']+)`
*Minimum*: `1`
*Maximum*: `64`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Tags`  <a name="cfn-route53globalresolver-dnsview-tags"></a>
Tags to associate with the DNS view.
*Required*: No
*Type*: Array of [Tag](aws-properties-route53globalresolver-dnsview-tag.md)
*Maximum*: `50`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-route53globalresolver-dnsview-return-values"></a>

### Ref
<a name="aws-resource-route53globalresolver-dnsview-return-values-ref"></a>

### Fn::GetAtt
<a name="aws-resource-route53globalresolver-dnsview-return-values-fn--getatt"></a>

####
<a name="aws-resource-route53globalresolver-dnsview-return-values-fn--getatt-fn--getatt"></a>

`Arn`  <a name="Arn-fn::getatt"></a>
The Amazon Resource Name (ARN) of the DNS view.

`CreatedAt`  <a name="CreatedAt-fn::getatt"></a>
The date and time when the DNS view was created.

`DnsViewId`  <a name="DnsViewId-fn::getatt"></a>
The unique identifier for the DNS view.

`Status`  <a name="Status-fn::getatt"></a>
The operational status of the DNS view.

`UpdatedAt`  <a name="UpdatedAt-fn::getatt"></a>
The date and time when the DNS view was last updated.
