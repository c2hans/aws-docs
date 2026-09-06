---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-elasticloadbalancing-loadbalancer.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::ElasticLoadBalancing::LoadBalancer
<a name="aws-resource-elasticloadbalancing-loadbalancer"></a>

Specifies a Classic Load Balancer.

If this resource has a public IP address and is also in a VPC that is defined in the same template, you must use the [DependsOn attribute](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-attribute-dependson.html) to declare a dependency on the VPC-gateway attachment.

## Syntax
<a name="aws-resource-elasticloadbalancing-loadbalancer-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-elasticloadbalancing-loadbalancer-syntax.json"></a>

```
{
  "Type" : "AWS::ElasticLoadBalancing::LoadBalancer",
  "Properties" : {
      "[AccessLoggingPolicy](#cfn-elasticloadbalancing-loadbalancer-accessloggingpolicy)" : {{AccessLoggingPolicy}},
      "[AppCookieStickinessPolicy](#cfn-elasticloadbalancing-loadbalancer-appcookiestickinesspolicy)" : {{[ AppCookieStickinessPolicy, ... ]}},
      "[AvailabilityZones](#cfn-elasticloadbalancing-loadbalancer-availabilityzones)" : {{[ String, ... ]}},
      "[ConnectionDrainingPolicy](#cfn-elasticloadbalancing-loadbalancer-connectiondrainingpolicy)" : {{ConnectionDrainingPolicy}},
      "[ConnectionSettings](#cfn-elasticloadbalancing-loadbalancer-connectionsettings)" : {{ConnectionSettings}},
      "[CrossZone](#cfn-elasticloadbalancing-loadbalancer-crosszone)" : {{Boolean}},
      "[HealthCheck](#cfn-elasticloadbalancing-loadbalancer-healthcheck)" : {{HealthCheck}},
      "[Instances](#cfn-elasticloadbalancing-loadbalancer-instances)" : {{[ String, ... ]}},
      "[LBCookieStickinessPolicy](#cfn-elasticloadbalancing-loadbalancer-lbcookiestickinesspolicy)" : {{[ LBCookieStickinessPolicy, ... ]}},
      "[Listeners](#cfn-elasticloadbalancing-loadbalancer-listeners)" : {{[ Listeners, ... ]}},
      "[LoadBalancerName](#cfn-elasticloadbalancing-loadbalancer-loadbalancername)" : {{String}},
      "[Policies](#cfn-elasticloadbalancing-loadbalancer-policies)" : {{[ Policies, ... ]}},
      "[Scheme](#cfn-elasticloadbalancing-loadbalancer-scheme)" : {{String}},
      "[SecurityGroups](#cfn-elasticloadbalancing-loadbalancer-securitygroups)" : {{[ String, ... ]}},
      "[Subnets](#cfn-elasticloadbalancing-loadbalancer-subnets)" : {{[ String, ... ]}},
      "[Tags](#cfn-elasticloadbalancing-loadbalancer-tags)" : {{[ Tag, ... ]}}
    }
}
```

### YAML
<a name="aws-resource-elasticloadbalancing-loadbalancer-syntax.yaml"></a>

```
Type: AWS::ElasticLoadBalancing::LoadBalancer
Properties:
  [AccessLoggingPolicy](#cfn-elasticloadbalancing-loadbalancer-accessloggingpolicy): {{
    AccessLoggingPolicy}}
  [AppCookieStickinessPolicy](#cfn-elasticloadbalancing-loadbalancer-appcookiestickinesspolicy): {{
    - AppCookieStickinessPolicy}}
  [AvailabilityZones](#cfn-elasticloadbalancing-loadbalancer-availabilityzones): {{
    - String}}
  [ConnectionDrainingPolicy](#cfn-elasticloadbalancing-loadbalancer-connectiondrainingpolicy): {{
    ConnectionDrainingPolicy}}
  [ConnectionSettings](#cfn-elasticloadbalancing-loadbalancer-connectionsettings): {{
    ConnectionSettings}}
  [CrossZone](#cfn-elasticloadbalancing-loadbalancer-crosszone): {{Boolean}}
  [HealthCheck](#cfn-elasticloadbalancing-loadbalancer-healthcheck): {{
    HealthCheck}}
  [Instances](#cfn-elasticloadbalancing-loadbalancer-instances): {{
    - String}}
  [LBCookieStickinessPolicy](#cfn-elasticloadbalancing-loadbalancer-lbcookiestickinesspolicy): {{
    - LBCookieStickinessPolicy}}
  [Listeners](#cfn-elasticloadbalancing-loadbalancer-listeners): {{
    - Listeners}}
  [LoadBalancerName](#cfn-elasticloadbalancing-loadbalancer-loadbalancername): {{String}}
  [Policies](#cfn-elasticloadbalancing-loadbalancer-policies): {{
    - Policies}}
  [Scheme](#cfn-elasticloadbalancing-loadbalancer-scheme): {{String}}
  [SecurityGroups](#cfn-elasticloadbalancing-loadbalancer-securitygroups): {{
    - String}}
  [Subnets](#cfn-elasticloadbalancing-loadbalancer-subnets): {{
    - String}}
  [Tags](#cfn-elasticloadbalancing-loadbalancer-tags): {{
    - Tag}}
```

## Properties
<a name="aws-resource-elasticloadbalancing-loadbalancer-properties"></a>

`AccessLoggingPolicy`  <a name="cfn-elasticloadbalancing-loadbalancer-accessloggingpolicy"></a>
Information about where and how access logs are stored for the load balancer.
*Required*: No
*Type*: [AccessLoggingPolicy](aws-properties-elasticloadbalancing-loadbalancer-accessloggingpolicy.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`AppCookieStickinessPolicy`  <a name="cfn-elasticloadbalancing-loadbalancer-appcookiestickinesspolicy"></a>
Information about a policy for application-controlled session stickiness.
*Required*: No
*Type*: [Array](aws-properties-elasticloadbalancing-loadbalancer-appcookiestickinesspolicy.md) of [AppCookieStickinessPolicy](aws-properties-elasticloadbalancing-loadbalancer-appcookiestickinesspolicy.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`AvailabilityZones`  <a name="cfn-elasticloadbalancing-loadbalancer-availabilityzones"></a>
The Availability Zones for a load balancer in a default VPC. For a load balancer in a nondefault VPC, specify `Subnets` instead.
Update requires replacement if you did not previously specify an Availability Zone or if you are removing all Availability Zones. Otherwise, update requires no interruption.
*Required*: No
*Type*: Array of String
*Update requires*: [Some interruptions](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-some-interrupt)

`ConnectionDrainingPolicy`  <a name="cfn-elasticloadbalancing-loadbalancer-connectiondrainingpolicy"></a>
If enabled, the load balancer allows existing requests to complete before the load balancer shifts traffic away from a deregistered or unhealthy instance.
For more information, see [Configure connection draining](https://docs.aws.amazon.com/elasticloadbalancing/latest/classic/config-conn-drain.html) in the *User Guide for Classic Load Balancers*.
*Required*: No
*Type*: [ConnectionDrainingPolicy](aws-properties-elasticloadbalancing-loadbalancer-connectiondrainingpolicy.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ConnectionSettings`  <a name="cfn-elasticloadbalancing-loadbalancer-connectionsettings"></a>
If enabled, the load balancer allows the connections to remain idle (no data is sent over the connection) for the specified duration.
By default, Elastic Load Balancing maintains a 60-second idle connection timeout for both front-end and back-end connections of your load balancer. For more information, see [Configure idle connection timeout](https://docs.aws.amazon.com/elasticloadbalancing/latest/classic/config-idle-timeout.html) in the *User Guide for Classic Load Balancers*.
*Required*: No
*Type*: [ConnectionSettings](aws-properties-elasticloadbalancing-loadbalancer-connectionsettings.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`CrossZone`  <a name="cfn-elasticloadbalancing-loadbalancer-crosszone"></a>
If enabled, the load balancer routes the request traffic evenly across all instances regardless of the Availability Zones.
For more information, see [Configure cross-zone load balancing](https://docs.aws.amazon.com/elasticloadbalancing/latest/classic/enable-disable-crosszone-lb.html) in the *User Guide for Classic Load Balancers*.
*Required*: No
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`HealthCheck`  <a name="cfn-elasticloadbalancing-loadbalancer-healthcheck"></a>
The health check settings to use when evaluating the health of your EC2 instances.
Update requires replacement if you did not previously specify health check settings or if you are removing the health check settings. Otherwise, update requires no interruption.
*Required*: No
*Type*: [HealthCheck](aws-properties-elasticloadbalancing-loadbalancer-healthcheck.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Instances`  <a name="cfn-elasticloadbalancing-loadbalancer-instances"></a>
The IDs of the instances for the load balancer.
*Required*: No
*Type*: Array of String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`LBCookieStickinessPolicy`  <a name="cfn-elasticloadbalancing-loadbalancer-lbcookiestickinesspolicy"></a>
Information about a policy for duration-based session stickiness.
*Required*: No
*Type*: [Array](aws-properties-elasticloadbalancing-loadbalancer-lbcookiestickinesspolicy.md) of [LBCookieStickinessPolicy](aws-properties-elasticloadbalancing-loadbalancer-lbcookiestickinesspolicy.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Listeners`  <a name="cfn-elasticloadbalancing-loadbalancer-listeners"></a>
The listeners for the load balancer. You can specify at most one listener per port.
If you update the properties for a listener, AWS CloudFormation deletes the existing listener and creates a new one with the specified properties. While the new listener is being created, clients cannot connect to the load balancer.
*Required*: Yes
*Type*: [Array](aws-properties-elasticloadbalancing-loadbalancer-listeners.md) of [Listeners](aws-properties-elasticloadbalancing-loadbalancer-listeners.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`LoadBalancerName`  <a name="cfn-elasticloadbalancing-loadbalancer-loadbalancername"></a>
The name of the load balancer. This name must be unique within your set of load balancers for the region.
If you don't specify a name, AWS CloudFormation generates a unique physical ID for the load balancer. For more information, see [Name Type](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-name.html). If you specify a name, you cannot perform updates that require replacement of this resource, but you can perform other updates. To replace the resource, specify a new name.
*Required*: No
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Policies`  <a name="cfn-elasticloadbalancing-loadbalancer-policies"></a>
The policies defined for your Classic Load Balancer. Specify only back-end server policies.
*Required*: No
*Type*: [Array](aws-properties-elasticloadbalancing-loadbalancer-policies.md) of [Policies](aws-properties-elasticloadbalancing-loadbalancer-policies.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Scheme`  <a name="cfn-elasticloadbalancing-loadbalancer-scheme"></a>
The type of load balancer. Valid only for load balancers in a VPC.
If `Scheme` is `internet-facing`, the load balancer has a public DNS name that resolves to a public IP address.
If `Scheme` is `internal`, the load balancer has a public DNS name that resolves to a private IP address.
*Required*: No
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`SecurityGroups`  <a name="cfn-elasticloadbalancing-loadbalancer-securitygroups"></a>
The security groups for the load balancer. Valid only for load balancers in a VPC.
*Required*: No
*Type*: Array of String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Subnets`  <a name="cfn-elasticloadbalancing-loadbalancer-subnets"></a>
The IDs of the subnets for the load balancer. You can specify at most one subnet per Availability Zone.
Update requires replacement if you did not previously specify a subnet or if you are removing all subnets. Otherwise, update requires no interruption. To update to a different subnet in the current Availability Zone, you must first update to a subnet in a different Availability Zone, then update to the new subnet in the original Availability Zone.
*Required*: No
*Type*: Array of String
*Update requires*: [Some interruptions](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-some-interrupt)

`Tags`  <a name="cfn-elasticloadbalancing-loadbalancer-tags"></a>
The tags associated with a load balancer.
*Required*: No
*Type*: Array of [Tag](aws-properties-elasticloadbalancing-loadbalancer-tag.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-elasticloadbalancing-loadbalancer-return-values"></a>

### Ref
<a name="aws-resource-elasticloadbalancing-loadbalancer-return-values-ref"></a>

When you pass the logical ID of this resource to the intrinsic `Ref` function, `Ref` returns the name of the load balancer.

For more information about using the `Ref` function, see [`Ref`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-ref.html).

### Fn::GetAtt
<a name="aws-resource-elasticloadbalancing-loadbalancer-return-values-fn--getatt"></a>

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [`Fn::GetAtt`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-getatt.html).

####
<a name="aws-resource-elasticloadbalancing-loadbalancer-return-values-fn--getatt-fn--getatt"></a>

`CanonicalHostedZoneName`  <a name="CanonicalHostedZoneName-fn::getatt"></a>
The name of the Route 53 hosted zone that is associated with the load balancer. Internal-facing load balancers don't use this value, use `DNSName` instead.

`CanonicalHostedZoneNameID`  <a name="CanonicalHostedZoneNameID-fn::getatt"></a>
The ID of the Route 53 hosted zone name that is associated with the load balancer.

`DNSName`  <a name="DNSName-fn::getatt"></a>
The DNS name for the load balancer.

`SourceSecurityGroup.GroupName`  <a name="SourceSecurityGroup.GroupName-fn::getatt"></a>
The name of the security group that you can use as part of your inbound rules for your load balancer's back-end instances.

`SourceSecurityGroup.OwnerAlias`  <a name="SourceSecurityGroup.OwnerAlias-fn::getatt"></a>
The owner of the source security group.

## Examples
<a name="aws-resource-elasticloadbalancing-loadbalancer--examples"></a>

**Topics**
+ [Classic Load Balancer in a default VPC](#aws-resource-elasticloadbalancing-loadbalancer--examples--Classic_Load_Balancer_in_a_default_VPC)
+ [Classic Load Balancer in a nondefault VPC](#aws-resource-elasticloadbalancing-loadbalancer--examples--Classic_Load_Balancer_in_a_nondefault_VPC)

### Classic Load Balancer in a default VPC
<a name="aws-resource-elasticloadbalancing-loadbalancer--examples--Classic_Load_Balancer_in_a_default_VPC"></a>

The following example specifies a Classic Load Balancer with a secure listener in a default VPC.

#### JSON
<a name="aws-resource-elasticloadbalancing-loadbalancer--examples--Classic_Load_Balancer_in_a_default_VPC--json"></a>

```
"MyLoadBalancer" : {
    "Type": "AWS::ElasticLoadBalancing::LoadBalancer",
    "Properties": {
        "AvailabilityZones": [ "us-east-2a" ],
        "CrossZone": "true",
        "Listeners": [{
            "InstancePort": "80",
            "InstanceProtocol": "HTTP",
            "LoadBalancerPort": "443",
            "Protocol": "HTTPS",
            "PolicyNames": [ "My-SSLNegotiation-Policy" ],
            "SSLCertificateId": "arn:aws:iam::123456789012:server-certificate/my-server-certificate"
        }],
        "HealthCheck": {
            "Target": "HTTP:80/",
            "HealthyThreshold": "2",
            "UnhealthyThreshold": "3",
            "Interval": "10",
            "Timeout": "5"
        },
        "Policies": [{
            "PolicyName": "My-SSLNegotiation-Policy",
            "PolicyType": "SSLNegotiationPolicyType",
            "Attributes": [{
                "Name": "Reference-Security-Policy",
                "Value": "ELBSecurityPolicy-TLS-1-2-2017-01"
            }]
        }]
    }
}
```

#### YAML
<a name="aws-resource-elasticloadbalancing-loadbalancer--examples--Classic_Load_Balancer_in_a_default_VPC--yaml"></a>

```
MyLoadBalancer:
    Type: AWS::ElasticLoadBalancing::LoadBalancer
    Properties:
      AvailabilityZones:
      - "us-east-2a"
      CrossZone: true
      Listeners:
      - InstancePort: '80'
        InstanceProtocol: HTTP
        LoadBalancerPort: '443'
        Protocol: HTTPS
        PolicyNames:
        - My-SSLNegotiation-Policy
        SSLCertificateId: arn:aws:iam::123456789012:server-certificate/my-server-certificate
      HealthCheck:
        Target: HTTP:80/
        HealthyThreshold: '2'
        UnhealthyThreshold: '3'
        Interval: '10'
        Timeout: '5'
      Policies:
      - PolicyName: My-SSLNegotiation-Policy
        PolicyType: SSLNegotiationPolicyType
        Attributes:
        - Name: Reference-Security-Policy
          Value: ELBSecurityPolicy-TLS-1-2-2017-01
```

### Classic Load Balancer in a nondefault VPC
<a name="aws-resource-elasticloadbalancing-loadbalancer--examples--Classic_Load_Balancer_in_a_nondefault_VPC"></a>

The following example specifies a Classic Load Balancer with an HTTP listener and a VPC with one subnet and an internet gateway.

#### JSON
<a name="aws-resource-elasticloadbalancing-loadbalancer--examples--Classic_Load_Balancer_in_a_nondefault_VPC--json"></a>

```
{
    "Resources": {
        "myLoadBalancer": {
            "Type": "AWS::ElasticLoadBalancing::LoadBalancer",
            "Properties": {
                "Subnets": [
                    {
                        "Ref": "mySubnet"
                    }
                ],
                "Listeners": [
                    {
                        "LoadBalancerPort": "80",
                        "InstancePort": "80",
                        "Protocol": "HTTP"
                    }
                ]
            }
        },
        "myVPC": {
            "Type": "AWS::EC2::VPC",
            "Properties": {
                "CidrBlock": "10.0.0.0/16",
                "EnableDnsSupport": true,
                "EnableDnsHostnames": true
            }
        },
        "mySubnet": {
            "Type": "AWS::EC2::Subnet",
            "Properties": {
                "VpcId": {
                    "Ref": "myVPC"
                },
                "CidrBlock": "10.0.0.0/24",
                "AvailabilityZone": {
                    "Fn::Select": [
                        1,
                        {
                            "Fn::GetAZs": ""
                        }
                    ]
                }
            }
        },
        "myInternetGateway": {
            "Type": "AWS::EC2::InternetGateway"
        },
        "myGatewayAttachment": {
            "Type": "AWS::EC2::VPCGatewayAttachment",
            "Properties": {
                "VpcId": {
                    "Ref": "myVPC"
                },
                "InternetGatewayId": {
                    "Ref": "myInternetGateway"
                }
            }
        },
        "myRouteTable": {
            "Type": "AWS::EC2::RouteTable",
            "Properties": {
                "VpcId": {
                    "Ref": "myVPC"
                }
            }
        },
        "myRoute": {
            "Type": "AWS::EC2::Route",
            "Properties": {
                "DestinationCidrBlock": "0.0.0.0/0",
                "GatewayId": {
                    "Ref": "myInternetGateway"
                },
                "RouteTableId": {
                    "Ref": "myRouteTable"
                }
            }
        },
        "myRouteTableAssociation": {
            "Type": "AWS::EC2::SubnetRouteTableAssociation",
            "Properties": {
                "RouteTableId": {
                    "Ref": "myRouteTable"
                },
                "SubnetId": {
                    "Ref": "mySubnet"
                }
            }
        }
    }
}
```

#### YAML
<a name="aws-resource-elasticloadbalancing-loadbalancer--examples--Classic_Load_Balancer_in_a_nondefault_VPC--yaml"></a>

```
Resources:
  myLoadBalancer:
    Type: AWS::ElasticLoadBalancing::LoadBalancer
    Properties:
      Subnets:
      - !Ref mySubnet
      Listeners:
      - LoadBalancerPort: '80'
        InstancePort: '80'
        Protocol: HTTP
  myVPC:
    Type: AWS::EC2::VPC
    Properties:
      CidrBlock: 10.0.0.0/16
      EnableDnsSupport: true
      EnableDnsHostnames: true
  mySubnet:
    Type: AWS::EC2::Subnet
    Properties:
      VpcId: !Ref myVPC
      CidrBlock: 10.0.0.0/24
      AvailabilityZone: !Select [ 1, !GetAZs ]
  myInternetGateway:
    Type: AWS::EC2::InternetGateway
  myGatewayAttachment:
    Type: AWS::EC2::VPCGatewayAttachment
    Properties:
      VpcId: !Ref myVPC
      InternetGatewayId: !Ref myInternetGateway
  myRouteTable:
    Type: AWS::EC2::RouteTable
    Properties:
      VpcId: !Ref myVPC
  myRoute:
    Type: AWS::EC2::Route
    Properties:
      DestinationCidrBlock: 0.0.0.0/0
      GatewayId: !Ref myInternetGateway
      RouteTableId: !Ref myRouteTable
  myRouteTableAssociation:
    Type: AWS::EC2::SubnetRouteTableAssociation
    Properties:
      RouteTableId: !Ref myRouteTable
      SubnetId: !Ref mySubnet
```

## See also
<a name="aws-resource-elasticloadbalancing-loadbalancer--seealso"></a>
+  [Elastic Load Balancing Template Snippets](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/quickref-elb.html)
+ [CreateLoadBalancer](https://docs.aws.amazon.com/elasticloadbalancing/2012-06-01/APIReference/API_CreateLoadBalancer.html) in the *Elastic Load Balancing API Reference (version 2012-06-01)*
+ [ModifyLoadBalancerAttributes](https://docs.aws.amazon.com/elasticloadbalancing/2012-06-01/APIReference/API_ModifyLoadBalancerAttributes.html) in the *Elastic Load Balancing API Reference (version 2012-06-01)*
+ [ConfigureHealthCheck](https://docs.aws.amazon.com/elasticloadbalancing/2012-06-01/APIReference/API_ConfigureHealthCheck.html) in the *Elastic Load Balancing API Reference (version 2012-06-01)*
+  [User Guide for Classic Load Balancers](https://docs.aws.amazon.com/elasticloadbalancing/latest/classic)
