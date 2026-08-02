---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-route53resolver-resolverendpoint.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Route53Resolver::ResolverEndpoint
<a name="aws-resource-route53resolver-resolverendpoint"></a>

Creates a Resolver endpoint. There are two types of Resolver endpoints, inbound and outbound:
+ An *inbound Resolver endpoint* forwards DNS queries to the DNS service for a VPC from your network.
+ An *outbound Resolver endpoint* forwards DNS queries from the DNS service for a VPC to your network.

**Important**
You cannot update `ResolverEndpointType` and `IpAddresses` in the same request.
When you update a dual-stack IP address, you must update both IP addresses. You can’t update only an IPv4 or IPv6 and keep an existing IP address.

## Syntax
<a name="aws-resource-route53resolver-resolverendpoint-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-route53resolver-resolverendpoint-syntax.json"></a>

```
{
  "Type" : "AWS::Route53Resolver::ResolverEndpoint",
  "Properties" : {
      "[Direction](#cfn-route53resolver-resolverendpoint-direction)" : {{String}},
      "[Dns64Enabled](#cfn-route53resolver-resolverendpoint-dns64enabled)" : {{Boolean}},
      "[IpAddresses](#cfn-route53resolver-resolverendpoint-ipaddresses)" : {{[ IpAddressRequest, ... ]}},
      "[Ipv6InternetAccessEnabled](#cfn-route53resolver-resolverendpoint-ipv6internetaccessenabled)" : {{Boolean}},
      "[Name](#cfn-route53resolver-resolverendpoint-name)" : {{String}},
      "[OutpostArn](#cfn-route53resolver-resolverendpoint-outpostarn)" : {{String}},
      "[PreferredInstanceType](#cfn-route53resolver-resolverendpoint-preferredinstancetype)" : {{String}},
      "[Protocols](#cfn-route53resolver-resolverendpoint-protocols)" : {{[ String, ... ]}},
      "[ResolverEndpointType](#cfn-route53resolver-resolverendpoint-resolverendpointtype)" : {{String}},
      "[RniEnhancedMetricsEnabled](#cfn-route53resolver-resolverendpoint-rnienhancedmetricsenabled)" : {{Boolean}},
      "[SecurityGroupIds](#cfn-route53resolver-resolverendpoint-securitygroupids)" : {{[ String, ... ]}},
      "[Tags](#cfn-route53resolver-resolverendpoint-tags)" : {{[ Tag, ... ]}},
      "[TargetNameServerMetricsEnabled](#cfn-route53resolver-resolverendpoint-targetnameservermetricsenabled)" : {{Boolean}}
    }
}
```

### YAML
<a name="aws-resource-route53resolver-resolverendpoint-syntax.yaml"></a>

```
Type: AWS::Route53Resolver::ResolverEndpoint
Properties:
  [Direction](#cfn-route53resolver-resolverendpoint-direction): {{String}}
  [Dns64Enabled](#cfn-route53resolver-resolverendpoint-dns64enabled): {{Boolean}}
  [IpAddresses](#cfn-route53resolver-resolverendpoint-ipaddresses): {{
    - IpAddressRequest}}
  [Ipv6InternetAccessEnabled](#cfn-route53resolver-resolverendpoint-ipv6internetaccessenabled): {{Boolean}}
  [Name](#cfn-route53resolver-resolverendpoint-name): {{String}}
  [OutpostArn](#cfn-route53resolver-resolverendpoint-outpostarn): {{String}}
  [PreferredInstanceType](#cfn-route53resolver-resolverendpoint-preferredinstancetype): {{String}}
  [Protocols](#cfn-route53resolver-resolverendpoint-protocols): {{
    - String}}
  [ResolverEndpointType](#cfn-route53resolver-resolverendpoint-resolverendpointtype): {{String}}
  [RniEnhancedMetricsEnabled](#cfn-route53resolver-resolverendpoint-rnienhancedmetricsenabled): {{Boolean}}
  [SecurityGroupIds](#cfn-route53resolver-resolverendpoint-securitygroupids): {{
    - String}}
  [Tags](#cfn-route53resolver-resolverendpoint-tags): {{
    - Tag}}
  [TargetNameServerMetricsEnabled](#cfn-route53resolver-resolverendpoint-targetnameservermetricsenabled): {{Boolean}}
```

## Properties
<a name="aws-resource-route53resolver-resolverendpoint-properties"></a>

`Direction`  <a name="cfn-route53resolver-resolverendpoint-direction"></a>
Indicates whether the Resolver endpoint allows inbound or outbound DNS queries:
+ `INBOUND`: allows DNS queries to your VPC from your network
+ `OUTBOUND`: allows DNS queries from your VPC to your network
+ `INBOUND_DELEGATION`: Resolver delegates queries to Route 53 private hosted zones from your network.
*Required*: Yes
*Type*: String
*Allowed values*: `INBOUND | OUTBOUND | INBOUND_DELEGATION`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Dns64Enabled`  <a name="cfn-route53resolver-resolverendpoint-dns64enabled"></a>
Indicates whether DNS64 is enabled for the inbound Resolver endpoint. When `true`, Route 53 Resolver synthesizes AAAA (IPv6) records for IPv4-only services by prepending the `64:ff9b::/96` prefix to the IPv4 address.
*Required*: No
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`IpAddresses`  <a name="cfn-route53resolver-resolverendpoint-ipaddresses"></a>
The subnets and IP addresses in your VPC that DNS queries originate from (for outbound endpoints) or that you forward DNS queries to (for inbound endpoints). The subnet ID uniquely identifies a VPC.
Even though the minimum is 1, Route 53 requires that you create at least two.
We recommend using [VPC Resolver on AWS Outposts](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/outpost-resolver-getting-started.html) to create endpoints on AWS Outposts Racks.
Outposts subnets with [Local Network Interface (LNI)](https://docs.aws.amazon.com/outposts/latest/server-userguide/local-network-interface.html) enabled are not compatible with Route 53 Resolver endpoints. If you enable LNI on a subnet that contains Route 53 Resolver endpoint elastic network interfaces (ENIs), those ENIs will stop functioning. For more information, see [Subnet compatibility for Resolver endpoints](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/best-practices-resolver.html#best-practices-resolver-subnet-compatibility) in the *Amazon Route 53 Developer Guide*.
*Required*: Yes
*Type*: Array of [IpAddressRequest](aws-properties-route53resolver-resolverendpoint-ipaddressrequest.md)
*Minimum*: `2`
*Maximum*: `20`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Ipv6InternetAccessEnabled`  <a name="cfn-route53resolver-resolverendpoint-ipv6internetaccessenabled"></a>
Indicates whether IPv6 internet access is enabled for the outbound Resolver endpoint. When `true`, the endpoint elastic network interfaces (ENIs) can forward DNS queries to public IPv6 targets through an internet gateway.
*Required*: No
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Name`  <a name="cfn-route53resolver-resolverendpoint-name"></a>
A friendly name that lets you easily find a configuration in the Resolver dashboard in the Route 53 console.
*Required*: No
*Type*: String
*Pattern*: `(?!^[0-9]+$)([a-zA-Z0-9\-_' ']+)`
*Maximum*: `64`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`OutpostArn`  <a name="cfn-route53resolver-resolverendpoint-outpostarn"></a>
The ARN (Amazon Resource Name) for the Outpost.
*Required*: No
*Type*: String
*Pattern*: `^arn:aws([a-z-]+)?:outposts:[a-z\d-]+:\d{12}:outpost/op-[a-f0-9]{17}$`
*Minimum*: `1`
*Maximum*: `255`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`PreferredInstanceType`  <a name="cfn-route53resolver-resolverendpoint-preferredinstancetype"></a>
 The Amazon EC2 instance type.
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `255`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Protocols`  <a name="cfn-route53resolver-resolverendpoint-protocols"></a>
 Protocols used for the endpoint. DoH-FIPS is applicable for a default inbound endpoints only.
For an inbound endpoint you can apply the protocols as follows:
+  Do53 and DoH in combination.
+ Do53 and DoH-FIPS in combination.
+ Do53 alone.
+ DoH alone.
+ DoH-FIPS alone.
+ None, which is treated as Do53.
For a delegation inbound endpoint you can use Do53 only.
For an outbound endpoint you can apply the protocols as follows:
+  Do53 and DoH in combination.
+ Do53 alone.
+ DoH alone.
+ None, which is treated as Do53.
*Required*: No
*Type*: Array of String
*Minimum*: `1`
*Maximum*: `2`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ResolverEndpointType`  <a name="cfn-route53resolver-resolverendpoint-resolverendpointtype"></a>
 The Resolver endpoint IP address type.
*Required*: No
*Type*: String
*Allowed values*: `IPV6 | IPV4 | DUALSTACK`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`RniEnhancedMetricsEnabled`  <a name="cfn-route53resolver-resolverendpoint-rnienhancedmetricsenabled"></a>
Indicates whether RNI enhanced metrics are enabled for the Resolver endpoint. When enabled, one-minute granular metrics are published in CloudWatch for each RNI associated with this endpoint. When disabled, these metrics are not published.
*Required*: No
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SecurityGroupIds`  <a name="cfn-route53resolver-resolverendpoint-securitygroupids"></a>
The ID of one or more security groups that control access to this VPC. The security group must include one or more inbound rules (for inbound endpoints) or outbound rules (for outbound endpoints). Inbound and outbound rules must allow TCP and UDP access. For inbound access, open port 53. For outbound access, open the port that you're using for DNS queries on your network.
*Required*: Yes
*Type*: Array of String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Tags`  <a name="cfn-route53resolver-resolverendpoint-tags"></a>
Route 53 Resolver doesn't support updating tags through CloudFormation.
*Required*: No
*Type*: Array of [Tag](aws-properties-route53resolver-resolverendpoint-tag.md)
*Maximum*: `200`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`TargetNameServerMetricsEnabled`  <a name="cfn-route53resolver-resolverendpoint-targetnameservermetricsenabled"></a>
Indicates whether target name server metrics are enabled for the outbound Resolver endpoint. When enabled, one-minute granular metrics are published in CloudWatch for each target name server associated with this endpoint. When disabled, these metrics are not published. This feature is not supported for inbound Resolver endpoint.
*Required*: No
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-route53resolver-resolverendpoint-return-values"></a>

### Ref
<a name="aws-resource-route53resolver-resolverendpoint-return-values-ref"></a>

When you pass the logical ID of this resource to the intrinsic `Ref` function, `Ref` returns the `ResolverEndpoint` object.

For more information about using the `Ref` function, see [https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-ref.html](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-ref.html).

### Fn::GetAtt
<a name="aws-resource-route53resolver-resolverendpoint-return-values-fn--getatt"></a>

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-getatt.html](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-getatt.html).

####
<a name="aws-resource-route53resolver-resolverendpoint-return-values-fn--getatt-fn--getatt"></a>

`Arn`  <a name="Arn-fn::getatt"></a>
The Amazon Resource Name (ARN) of the resolver endpoint, such as `arn:aws:route53resolver:us-east-1:123456789012:resolver-endpoint/resolver-endpoint-a1bzhi`.

`Direction`  <a name="Direction-fn::getatt"></a>
Indicates whether the resolver endpoint allows inbound or outbound DNS queries.

`HostVPCId`  <a name="HostVPCId-fn::getatt"></a>
The ID of the VPC that you want to create the resolver endpoint in.

`IpAddressCount`  <a name="IpAddressCount-fn::getatt"></a>
The number of IP addresses that the resolver endpoint can use for DNS queries.

`Name`  <a name="Name-fn::getatt"></a>
The name that you assigned to the resolver endpoint when you created the endpoint.

`ResolverEndpointId`  <a name="ResolverEndpointId-fn::getatt"></a>
The ID of the resolver endpoint.

## Examples
<a name="aws-resource-route53resolver-resolverendpoint--examples"></a>

**Topics**
+ [Create Resolver endpoint](#aws-resource-route53resolver-resolverendpoint--examples--Create_Resolver_endpoint)
+ [Associate a Resolver rule with a VPC](#aws-resource-route53resolver-resolverendpoint--examples--Associate_a_Resolver_rule_with_a_VPC)

### Create Resolver endpoint
<a name="aws-resource-route53resolver-resolverendpoint--examples--Create_Resolver_endpoint"></a>

The following example creates an Amazon Route 53 outbound resolver endpoint. The `IpAddresses` object includes values for `SubnetId` but not for `Ip`. This causes Route 53 Resolver to automatically choose an IP address from among the available IP addresses in the specified subnet.

#### JSON
<a name="aws-resource-route53resolver-resolverendpoint--examples--Create_Resolver_endpoint--json"></a>

```
{
  "Type" : "AWS::Route53Resolver::ResolverEndpoint",
  "Properties" : {
    "Direction" : "Outbound",
    "IpAddresses" : [
      {
        "SubnetId": "subnet-0bca4d363dexample"
      },
      {
        "SubnetId": "subnet-0cdb5e474dexample"
      }
    ],
    "Name" : "MyOutboundEndpoint",
    "SecurityGroupIds" : [
      "sg-071b99f42example"
    ],
    "Tags" : [
      "Key": "LineOfBusiness",
      "Value": "Engineering"
    ]
  }
}
```

#### YAML
<a name="aws-resource-route53resolver-resolverendpoint--examples--Create_Resolver_endpoint--yaml"></a>

```
Type : AWS::Route53Resolver::ResolverEndpoint
Properties :
  Direction : Outbound
  IpAddresses :
    - SubnetId: subnet-0bca4d363dexample
    - SubnetId: subnet-0cdb5e474dexample
  Name : MyOutboundEndpoint
  SecurityGroupIds :
    - sg-071b99f42example
  Tags :
    -
      Key: LineOfBusiness
      Value: Engineering
```

### Associate a Resolver rule with a VPC
<a name="aws-resource-route53resolver-resolverendpoint--examples--Associate_a_Resolver_rule_with_a_VPC"></a>

The following example associates a resolver rule with a VPC. When you associate a rule with a VPC, Resolver forwards all DNS queries for the domain name that is specified in the rule and that originate in the VPC. The queries are forwarded to the IP addresses for the DNS resolvers that are specified in the rule.

#### JSON
<a name="aws-resource-route53resolver-resolverendpoint--examples--Associate_a_Resolver_rule_with_a_VPC--json"></a>

```
{
 "Type" : "AWS::Route53Resolver::ResolverRuleAssociation",
 "Properties" : {
	 "Name" : "MyResolverRuleAssociation",
	 "ResolverRuleId" : "rslvr-rr-5328a0899aexample",
	 "VPCId" : "vpc-03cf94c75cexample"
	 }
 }
```

#### YAML
<a name="aws-resource-route53resolver-resolverendpoint--examples--Associate_a_Resolver_rule_with_a_VPC--yaml"></a>

```
Type: "AWS::Route53Resolver::ResolverRuleAssociation"
	Properties:
	  Name: MyResolverRuleAssociation
	  ResolverRuleId: rslvr-rr-5328a0899aexample
	  VPCId: vpc-03cf94c75cexample
```

## See also
<a name="aws-resource-route53resolver-resolverendpoint--seealso"></a>
+ [ResolverEndpoint](https://docs.aws.amazon.com/Route53/latest/APIReference/API_route53resolver_ResolverEndpoint.html) in the *Amazon Route 53 API Reference*
