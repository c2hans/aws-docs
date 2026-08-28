---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-route53resolver-resolverrule-targetaddress.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Route53Resolver::ResolverRule TargetAddress
<a name="aws-properties-route53resolver-resolverrule-targetaddress"></a>

In a [CreateResolverRule](https://docs.aws.amazon.com/Route53/latest/APIReference/API_route53resolver_CreateResolverRule.html) request, an array of the IPs that you want to forward DNS queries to.

## Syntax
<a name="aws-properties-route53resolver-resolverrule-targetaddress-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-route53resolver-resolverrule-targetaddress-syntax.json"></a>

```
{
  "[Ip](#cfn-route53resolver-resolverrule-targetaddress-ip)" : {{String}},
  "[Ipv6](#cfn-route53resolver-resolverrule-targetaddress-ipv6)" : {{String}},
  "[Port](#cfn-route53resolver-resolverrule-targetaddress-port)" : {{String}},
  "[Protocol](#cfn-route53resolver-resolverrule-targetaddress-protocol)" : {{String}},
  "[ServerNameIndication](#cfn-route53resolver-resolverrule-targetaddress-servernameindication)" : {{String}}
}
```

### YAML
<a name="aws-properties-route53resolver-resolverrule-targetaddress-syntax.yaml"></a>

```
  [Ip](#cfn-route53resolver-resolverrule-targetaddress-ip): {{String}}
  [Ipv6](#cfn-route53resolver-resolverrule-targetaddress-ipv6): {{String}}
  [Port](#cfn-route53resolver-resolverrule-targetaddress-port): {{String}}
  [Protocol](#cfn-route53resolver-resolverrule-targetaddress-protocol): {{String}}
  [ServerNameIndication](#cfn-route53resolver-resolverrule-targetaddress-servernameindication): {{String}}
```

## Properties
<a name="aws-properties-route53resolver-resolverrule-targetaddress-properties"></a>

`Ip`  <a name="cfn-route53resolver-resolverrule-targetaddress-ip"></a>
One IPv4 address that you want to forward DNS queries to.
*Required*: No
*Type*: String
*Minimum*: `7`
*Maximum*: `36`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Ipv6`  <a name="cfn-route53resolver-resolverrule-targetaddress-ipv6"></a>
 One IPv6 address that you want to forward DNS queries to.
*Required*: No
*Type*: String
*Minimum*: `7`
*Maximum*: `39`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Port`  <a name="cfn-route53resolver-resolverrule-targetaddress-port"></a>
The port at `Ip` that you want to forward DNS queries to.
*Required*: No
*Type*: String
*Minimum*: `0`
*Maximum*: `65535`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Protocol`  <a name="cfn-route53resolver-resolverrule-targetaddress-protocol"></a>
 The protocols for the target address. The protocol you choose needs to be supported by the outbound endpoint of the Resolver rule.
*Required*: No
*Type*: String
*Allowed values*: `Do53 | DoH`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ServerNameIndication`  <a name="cfn-route53resolver-resolverrule-targetaddress-servernameindication"></a>
 The Server Name Indication of the DoH server that you want to forward queries to. This is only used if the Protocol of the `TargetAddress` is `DoH`.
*Required*: No
*Type*: String
*Minimum*: `0`
*Maximum*: `255`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also
<a name="aws-properties-route53resolver-resolverrule-targetaddress--seealso"></a>
+ [Return values](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53resolver-resolverrule.html#aws-resource-route53resolver-resolverrule-return-values) in the topic [AWS::Route53Resolver::ResolverRule](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53resolver-resolverrule.html)
+ [TargetAddress](https://docs.aws.amazon.com/Route53/latest/APIReference/API_route53resolver_TargetAddress.html) in the *Amazon Route 53 API Reference*

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
