---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-elasticloadbalancingv2-loadbalancer.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::ElasticLoadBalancingV2::LoadBalancer
<a name="aws-resource-elasticloadbalancingv2-loadbalancer"></a>

Specifies an Application Load Balancer, a Network Load Balancer, or a Gateway Load Balancer.

## Syntax
<a name="aws-resource-elasticloadbalancingv2-loadbalancer-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-elasticloadbalancingv2-loadbalancer-syntax.json"></a>

```
{
  "Type" : "AWS::ElasticLoadBalancingV2::LoadBalancer",
  "Properties" : {
      "[EnableCapacityReservationProvisionStabilize](#cfn-elasticloadbalancingv2-loadbalancer-enablecapacityreservationprovisionstabilize)" : {{Boolean}},
      "[EnablePrefixForIpv6SourceNat](#cfn-elasticloadbalancingv2-loadbalancer-enableprefixforipv6sourcenat)" : {{String}},
      "[EnforceSecurityGroupInboundRulesOnPrivateLinkTraffic](#cfn-elasticloadbalancingv2-loadbalancer-enforcesecuritygroupinboundrulesonprivatelinktraffic)" : {{String}},
      "[IpAddressType](#cfn-elasticloadbalancingv2-loadbalancer-ipaddresstype)" : {{String}},
      "[Ipv4IpamPoolId](#cfn-elasticloadbalancingv2-loadbalancer-ipv4ipampoolid)" : {{String}},
      "[LoadBalancerAttributes](#cfn-elasticloadbalancingv2-loadbalancer-loadbalancerattributes)" : {{[ LoadBalancerAttribute, ... ]}},
      "[MinimumLoadBalancerCapacity](#cfn-elasticloadbalancingv2-loadbalancer-minimumloadbalancercapacity)" : {{MinimumLoadBalancerCapacity}},
      "[Name](#cfn-elasticloadbalancingv2-loadbalancer-name)" : {{String}},
      "[Scheme](#cfn-elasticloadbalancingv2-loadbalancer-scheme)" : {{String}},
      "[SecurityGroups](#cfn-elasticloadbalancingv2-loadbalancer-securitygroups)" : {{[ String, ... ]}},
      "[SubnetMappings](#cfn-elasticloadbalancingv2-loadbalancer-subnetmappings)" : {{[ SubnetMapping, ... ]}},
      "[Subnets](#cfn-elasticloadbalancingv2-loadbalancer-subnets)" : {{[ String, ... ]}},
      "[Tags](#cfn-elasticloadbalancingv2-loadbalancer-tags)" : {{[ Tag, ... ]}},
      "[Type](#cfn-elasticloadbalancingv2-loadbalancer-type)" : {{String}}
    }
}
```

### YAML
<a name="aws-resource-elasticloadbalancingv2-loadbalancer-syntax.yaml"></a>

```
Type: AWS::ElasticLoadBalancingV2::LoadBalancer
Properties:
  [EnableCapacityReservationProvisionStabilize](#cfn-elasticloadbalancingv2-loadbalancer-enablecapacityreservationprovisionstabilize): {{Boolean}}
  [EnablePrefixForIpv6SourceNat](#cfn-elasticloadbalancingv2-loadbalancer-enableprefixforipv6sourcenat): {{String}}
  [EnforceSecurityGroupInboundRulesOnPrivateLinkTraffic](#cfn-elasticloadbalancingv2-loadbalancer-enforcesecuritygroupinboundrulesonprivatelinktraffic): {{String}}
  [IpAddressType](#cfn-elasticloadbalancingv2-loadbalancer-ipaddresstype): {{String}}
  [Ipv4IpamPoolId](#cfn-elasticloadbalancingv2-loadbalancer-ipv4ipampoolid): {{String}}
  [LoadBalancerAttributes](#cfn-elasticloadbalancingv2-loadbalancer-loadbalancerattributes): {{
    - LoadBalancerAttribute}}
  [MinimumLoadBalancerCapacity](#cfn-elasticloadbalancingv2-loadbalancer-minimumloadbalancercapacity): {{
    MinimumLoadBalancerCapacity}}
  [Name](#cfn-elasticloadbalancingv2-loadbalancer-name): {{String}}
  [Scheme](#cfn-elasticloadbalancingv2-loadbalancer-scheme): {{String}}
  [SecurityGroups](#cfn-elasticloadbalancingv2-loadbalancer-securitygroups): {{
    - String}}
  [SubnetMappings](#cfn-elasticloadbalancingv2-loadbalancer-subnetmappings): {{
    - SubnetMapping}}
  [Subnets](#cfn-elasticloadbalancingv2-loadbalancer-subnets): {{
    - String}}
  [Tags](#cfn-elasticloadbalancingv2-loadbalancer-tags): {{
    - Tag}}
  [Type](#cfn-elasticloadbalancingv2-loadbalancer-type): {{String}}
```

## Properties
<a name="aws-resource-elasticloadbalancingv2-loadbalancer-properties"></a>

`EnableCapacityReservationProvisionStabilize`  <a name="cfn-elasticloadbalancingv2-loadbalancer-enablecapacityreservationprovisionstabilize"></a>
Indicates whether to enable stabilization when creating or updating an LCU reservation. This ensures that the final stack status reflects the status of the LCU reservation. The default is `false`.
*Required*: No
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`EnablePrefixForIpv6SourceNat`  <a name="cfn-elasticloadbalancingv2-loadbalancer-enableprefixforipv6sourcenat"></a>
[Network Load Balancers with UDP listeners] Indicates whether to use an IPv6 prefix from each subnet for source NAT. The IP address type must be `dualstack`. The default value is `off`.
*Required*: No
*Type*: String
*Allowed values*: `on | off`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`EnforceSecurityGroupInboundRulesOnPrivateLinkTraffic`  <a name="cfn-elasticloadbalancingv2-loadbalancer-enforcesecuritygroupinboundrulesonprivatelinktraffic"></a>
Indicates whether to evaluate inbound security group rules for traffic sent to a Network Load Balancer through AWS PrivateLink. The default is `on`.
You can't configure this property on a Network Load Balancer unless you associated a security group with the load balancer when you created it.
*Required*: No
*Type*: String
*Allowed values*: `on | off`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`IpAddressType`  <a name="cfn-elasticloadbalancingv2-loadbalancer-ipaddresstype"></a>
The IP address type. Internal load balancers must use `ipv4`.
[Application Load Balancers] The possible values are `ipv4` (IPv4 addresses), `dualstack` (IPv4 and IPv6 addresses), and `dualstack-without-public-ipv4` (public IPv6 addresses and private IPv4 and IPv6 addresses).
Application Load Balancer authentication supports IPv4 addresses only when connecting to an Identity Provider (IdP) or Amazon Cognito endpoint. Without a public IPv4 address the load balancer can't complete the authentication process, resulting in HTTP 500 errors.
[Network Load Balancers and Gateway Load Balancers] The possible values are `ipv4` (IPv4 addresses) and `dualstack` (IPv4 and IPv6 addresses).
*Required*: No
*Type*: String
*Allowed values*: `ipv4 | dualstack | dualstack-without-public-ipv4`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Ipv4IpamPoolId`  <a name="cfn-elasticloadbalancingv2-loadbalancer-ipv4ipampoolid"></a>
The ID of the IPv4 IPAM pool.
*Required*: No
*Type*: String
*Pattern*: `^(ipam-pool-)[a-zA-Z0-9]+$`
*Maximum*: `1000`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`LoadBalancerAttributes`  <a name="cfn-elasticloadbalancingv2-loadbalancer-loadbalancerattributes"></a>
The load balancer attributes. Attributes that you do not modify retain their current values.
*Required*: No
*Type*: Array of [LoadBalancerAttribute](aws-properties-elasticloadbalancingv2-loadbalancer-loadbalancerattribute.md)
*Maximum*: `20`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`MinimumLoadBalancerCapacity`  <a name="cfn-elasticloadbalancingv2-loadbalancer-minimumloadbalancercapacity"></a>
The minimum capacity for a load balancer.
*Required*: No
*Type*: [MinimumLoadBalancerCapacity](aws-properties-elasticloadbalancingv2-loadbalancer-minimumloadbalancercapacity.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Name`  <a name="cfn-elasticloadbalancingv2-loadbalancer-name"></a>
The name of the load balancer. This name must be unique per region per account, can have a maximum of 32 characters, must contain only alphanumeric characters or hyphens, must not begin or end with a hyphen, and must not begin with "internal-".
If you don't specify a name, AWS CloudFormation generates a unique physical ID for the load balancer. If you specify a name, you cannot perform updates that require replacement of this resource, but you can perform other updates. To replace the resource, specify a new name.
*Required*: No
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Scheme`  <a name="cfn-elasticloadbalancingv2-loadbalancer-scheme"></a>
The nodes of an Internet-facing load balancer have public IP addresses. The DNS name of an Internet-facing load balancer is publicly resolvable to the public IP addresses of the nodes. Therefore, Internet-facing load balancers can route requests from clients over the internet.
The nodes of an internal load balancer have only private IP addresses. The DNS name of an internal load balancer is publicly resolvable to the private IP addresses of the nodes. Therefore, internal load balancers can route requests only from clients with access to the VPC for the load balancer.
The default is an Internet-facing load balancer.
You can't specify a scheme for a Gateway Load Balancer.
*Required*: No
*Type*: String
*Allowed values*: `internet-facing | internal`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`SecurityGroups`  <a name="cfn-elasticloadbalancingv2-loadbalancer-securitygroups"></a>
[Application Load Balancers and Network Load Balancers] The IDs of the security groups for the load balancer.
*Required*: No
*Type*: Array of String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SubnetMappings`  <a name="cfn-elasticloadbalancingv2-loadbalancer-subnetmappings"></a>
The IDs of the subnets. You can specify only one subnet per Availability Zone. You must specify either subnets or subnet mappings, but not both.
[Application Load Balancers] You must specify subnets from at least two Availability Zones. You can't specify Elastic IP addresses for your subnets.
[Application Load Balancers on Outposts] You must specify one Outpost subnet.
[Application Load Balancers on Local Zones] You can specify subnets from one or more Local Zones.
[Network Load Balancers] You can specify subnets from one or more Availability Zones. You can specify one Elastic IP address per subnet if you need static IP addresses for your internet-facing load balancer. For internal load balancers, you can specify one private IP address per subnet from the IPv4 range of the subnet. For internet-facing load balancer, you can specify one IPv6 address per subnet.
[Gateway Load Balancers] You can specify subnets from one or more Availability Zones. You can't specify Elastic IP addresses for your subnets.
*Required*: Conditional
*Type*: Array of [SubnetMapping](aws-properties-elasticloadbalancingv2-loadbalancer-subnetmapping.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Subnets`  <a name="cfn-elasticloadbalancingv2-loadbalancer-subnets"></a>
The IDs of the subnets. You can specify only one subnet per Availability Zone. You must specify either subnets or subnet mappings, but not both. To specify an Elastic IP address, specify subnet mappings instead of subnets.
[Application Load Balancers] You must specify subnets from at least two Availability Zones.
[Application Load Balancers on Outposts] You must specify one Outpost subnet.
[Application Load Balancers on Local Zones] You can specify subnets from one or more Local Zones.
[Network Load Balancers and Gateway Load Balancers] You can specify subnets from one or more Availability Zones.
*Required*: Conditional
*Type*: Array of String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Tags`  <a name="cfn-elasticloadbalancingv2-loadbalancer-tags"></a>
The tags to assign to the load balancer.
*Required*: No
*Type*: Array of [Tag](aws-properties-elasticloadbalancingv2-loadbalancer-tag.md)
*Minimum*: `1`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Type`  <a name="cfn-elasticloadbalancingv2-loadbalancer-type"></a>
The type of load balancer. The default is `application`.
*Required*: No
*Type*: String
*Allowed values*: `application | network | gateway`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## Return values
<a name="aws-resource-elasticloadbalancingv2-loadbalancer-return-values"></a>

### Ref
<a name="aws-resource-elasticloadbalancingv2-loadbalancer-return-values-ref"></a>

When you pass the logical ID of this resource to the intrinsic `Ref` function, `Ref` returns the Amazon Resource Name (ARN) of the load balancer.

For more information about using the `Ref` function, see [`Ref`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-ref.html).

### Fn::GetAtt
<a name="aws-resource-elasticloadbalancingv2-loadbalancer-return-values-fn--getatt"></a>

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [`Fn::GetAtt`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-getatt.html).

####
<a name="aws-resource-elasticloadbalancingv2-loadbalancer-return-values-fn--getatt-fn--getatt"></a>

`CanonicalHostedZoneID`  <a name="CanonicalHostedZoneID-fn::getatt"></a>
The ID of the Amazon Route 53 hosted zone associated with the load balancer. For example, `Z2P70J7EXAMPLE`.

`DNSName`  <a name="DNSName-fn::getatt"></a>
The DNS name for the load balancer. For example, `my-load-balancer-424835706.us-west-2.elb.amazonaws.com`.

`LoadBalancerArn`  <a name="LoadBalancerArn-fn::getatt"></a>
The Amazon Resource Name (ARN) of the load balancer.

`LoadBalancerFullName`  <a name="LoadBalancerFullName-fn::getatt"></a>
The full name of the load balancer. For example, `app/my-load-balancer/50dc6c495c0c9188`.

`LoadBalancerName`  <a name="LoadBalancerName-fn::getatt"></a>
The name of the load balancer. For example, `my-load-balancer`.

`SecurityGroups`  <a name="SecurityGroups-fn::getatt"></a>
The IDs of the security groups for the load balancer.

## Examples
<a name="aws-resource-elasticloadbalancingv2-loadbalancer--examples"></a>

To get started with Elastic Load Balancer create a load balancer. After you create your load balancer, add a listener using [AWS::ElasticLoadBalancingV2::Listener](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elasticloadbalancingv2-listener.html).

**Topics**
+ [Create an Application Load Balancer](#aws-resource-elasticloadbalancingv2-loadbalancer--examples--Create_an_Application_Load_Balancer)
+ [Create a Network Load Balancer](#aws-resource-elasticloadbalancingv2-loadbalancer--examples--Create_a_Network_Load_Balancer)

### Create an Application Load Balancer
<a name="aws-resource-elasticloadbalancingv2-loadbalancer--examples--Create_an_Application_Load_Balancer"></a>

The following example creates an internal Application Load Balancer with an associated security group and a load balancer attribute.

#### YAML
<a name="aws-resource-elasticloadbalancingv2-loadbalancer--examples--Create_an_Application_Load_Balancer--yaml"></a>

```
myLoadBalancer:
    Type: 'AWS::ElasticLoadBalancingV2::LoadBalancer'
    Properties:
      Name: my-alb
      Type: application
      Scheme: internal
      Subnets:
        - !Ref subnet-AZ1
        - !Ref subnet-AZ2
      SecurityGroups:
        - !Ref mySecurityGroup
      LoadBalancerAttributes:
        - Key: "deletion_protection.enabled"
          Value: "true"
```

#### JSON
<a name="aws-resource-elasticloadbalancingv2-loadbalancer--examples--Create_an_Application_Load_Balancer--json"></a>

```
{
    "myLoadBalancer": {
        "Type": "AWS::ElasticLoadBalancingV2::LoadBalancer",
        "Properties": {
            "Name": "my-alb",
            "Type": "application",
            "Scheme": "internal",
            "Subnets": [
                {
                    "Ref": "subnet-AZ1"
                },
                {
                    "Ref": "subnet-AZ2"
                }
            ],
            "SecurityGroups": [
                {
                    "Ref": "mySecurityGroup"
                }
            ],
            "LoadBalancerAttributes": [
                {
                    "Key": "deletion_protection.enabled",
                    "Value": true
                }
            ]
        }
    }
}
```

### Create a Network Load Balancer
<a name="aws-resource-elasticloadbalancingv2-loadbalancer--examples--Create_a_Network_Load_Balancer"></a>

The following example creates an internal Network Load Balancer with an associated security group and a load balancer attribute.

#### YAML
<a name="aws-resource-elasticloadbalancingv2-loadbalancer--examples--Create_a_Network_Load_Balancer--yaml"></a>

```
myLoadBalancer:
    Type: 'AWS::ElasticLoadBalancingV2::LoadBalancer'
    Properties:
      Name: my-nlb
      Type: network
      Scheme: internal
      Subnets:
        - !Ref subnet-AZ1
        - !Ref subnet-AZ2
      SecurityGroups:
        - !Ref mySecurityGroup
      LoadBalancerAttributes:
        - Key: "deletion_protection.enabled"
          Value: "true"
```

#### JSON
<a name="aws-resource-elasticloadbalancingv2-loadbalancer--examples--Create_a_Network_Load_Balancer--json"></a>

```
{
    "myLoadBalancer": {
        "Type": "AWS::ElasticLoadBalancingV2::LoadBalancer",
        "Properties": {
            "Name": "my-alb",
            "Type": "network",
            "Scheme": "internal",
            "Subnets": [
                {
                    "Ref": "subnet-AZ1"
                },
                {
                    "Ref": "subnet-AZ2"
                }
            ],
            "SecurityGroups": [
                {
                    "Ref": "mySecurityGroup"
                }
            ],
            "LoadBalancerAttributes": [
                {
                    "Key": "deletion_protection.enabled",
                    "Value": true
                }
            ]
        }
    }
}
```

## See also
<a name="aws-resource-elasticloadbalancingv2-loadbalancer--seealso"></a>
+ [CreateLoadBalancer](https://docs.aws.amazon.com/elasticloadbalancing/latest/APIReference/API_CreateLoadBalancer.html) in the *Elastic Load Balancing API Reference (version 2015-12-01)*
+  [User Guide for Application Load Balancers](https://docs.aws.amazon.com/elasticloadbalancing/latest/application)
+  [User Guide for Network Load Balancers](https://docs.aws.amazon.com/elasticloadbalancing/latest/network)
+  [User Guide for Gateway Load Balancers](https://docs.aws.amazon.com/elasticloadbalancing/latest/gateway)
