---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-route53resolver-resolverendpoint-ipaddressrequest.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Route53Resolver::ResolverEndpoint IpAddressRequest
<a name="aws-properties-route53resolver-resolverendpoint-ipaddressrequest"></a>

In a [CreateResolverEndpoint](https://docs.aws.amazon.com/Route53/latest/APIReference/API_route53resolver_CreateResolverEndpoint.html) request, the IP address that DNS queries originate from (for outbound endpoints) or that you forward DNS queries to (for inbound endpoints). `IpAddressRequest` also includes the ID of the subnet that contains the IP address.

## Syntax
<a name="aws-properties-route53resolver-resolverendpoint-ipaddressrequest-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-route53resolver-resolverendpoint-ipaddressrequest-syntax.json"></a>

```
{
  "[Ip](#cfn-route53resolver-resolverendpoint-ipaddressrequest-ip)" : {{String}},
  "[Ipv6](#cfn-route53resolver-resolverendpoint-ipaddressrequest-ipv6)" : {{String}},
  "[SubnetId](#cfn-route53resolver-resolverendpoint-ipaddressrequest-subnetid)" : {{String}}
}
```

### YAML
<a name="aws-properties-route53resolver-resolverendpoint-ipaddressrequest-syntax.yaml"></a>

```
  [Ip](#cfn-route53resolver-resolverendpoint-ipaddressrequest-ip): {{String}}
  [Ipv6](#cfn-route53resolver-resolverendpoint-ipaddressrequest-ipv6): {{String}}
  [SubnetId](#cfn-route53resolver-resolverendpoint-ipaddressrequest-subnetid): {{String}}
```

## Properties
<a name="aws-properties-route53resolver-resolverendpoint-ipaddressrequest-properties"></a>

`Ip`  <a name="cfn-route53resolver-resolverendpoint-ipaddressrequest-ip"></a>
The IPv4 address that you want to use for DNS queries.
*Required*: No
*Type*: String
*Minimum*: `7`
*Maximum*: `36`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Ipv6`  <a name="cfn-route53resolver-resolverendpoint-ipaddressrequest-ipv6"></a>
 The IPv6 address that you want to use for DNS queries.
*Required*: No
*Type*: String
*Minimum*: `7`
*Maximum*: `39`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SubnetId`  <a name="cfn-route53resolver-resolverendpoint-ipaddressrequest-subnetid"></a>
The ID of the subnet that contains the IP address.
We recommend using [VPC Resolver on AWS Outposts](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/outpost-resolver-getting-started.html) to create endpoints on AWS Outposts Racks.
Outposts subnets with [Local Network Interface (LNI)](https://docs.aws.amazon.com/outposts/latest/server-userguide/local-network-interface.html) enabled are not compatible with Route 53 Resolver endpoints. If you enable LNI on a subnet that contains Route 53 Resolver endpoint elastic network interfaces (ENIs), those ENIs will stop functioning. For more information, see [Subnet compatibility for Resolver endpoints](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/best-practices-resolver.html#best-practices-resolver-subnet-compatibility) in the *Amazon Route 53 Developer Guide*.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `32`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also
<a name="aws-properties-route53resolver-resolverendpoint-ipaddressrequest--seealso"></a>
+ [Return values](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53resolver-resolverendpoint.html#aws-resource-route53resolver-resolverendpoint-return-values) in the topic [AWS::Route53Resolver::ResolverEndpoint](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53resolver-resolverendpoint.html)
+ [IpAddressRequest](https://docs.aws.amazon.com/Route53/latest/APIReference/API_route53resolver_IpAddressRequest.html) in the *Amazon Route 53 API Reference*

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
