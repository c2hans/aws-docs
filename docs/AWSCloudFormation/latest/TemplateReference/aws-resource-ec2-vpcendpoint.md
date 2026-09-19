---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-ec2-vpcendpoint.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::EC2::VPCEndpoint
<a name="aws-resource-ec2-vpcendpoint"></a>

Specifies a VPC endpoint. A VPC endpoint provides a private connection between your VPC and an endpoint service. You can use an endpoint service provided by AWS, an AWS Marketplace Partner, or another AWS accounts in your organization. For more information, see the [AWS PrivateLink User Guide](https://docs.aws.amazon.com/vpc/latest/privatelink/).

An endpoint of type `Interface` establishes connections between the subnets in your VPC and an AWS service, your own service, or a service hosted by another AWS account. With an interface VPC endpoint, you specify the subnets in which to create the endpoint and the security groups to associate with the endpoint network interfaces.

An endpoint of type `gateway` serves as a target for a route in your route table for traffic destined for Amazon S3 or DynamoDB. You can specify an endpoint policy for the endpoint, which controls access to the service from your VPC. You can also specify the VPC route tables that use the endpoint. For more information about connectivity to Amazon S3, see [Why can't I connect to an S3 bucket using a gateway VPC endpoint?](https://aws.amazon.com/premiumsupport/knowledge-center/connect-s3-vpc-endpoint)

An endpoint of type `GatewayLoadBalancer` provides private connectivity between your VPC and virtual appliances from a service provider.

## Syntax
<a name="aws-resource-ec2-vpcendpoint-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-ec2-vpcendpoint-syntax.json"></a>

```
{
  "Type" : "AWS::EC2::VPCEndpoint",
  "Properties" : {
      "[DnsOptions](#cfn-ec2-vpcendpoint-dnsoptions)" : {{DnsOptionsSpecification}},
      "[IpAddressType](#cfn-ec2-vpcendpoint-ipaddresstype)" : {{String}},
      "[PolicyDocument](#cfn-ec2-vpcendpoint-policydocument)" : {{Json}},
      "[PrivateDnsEnabled](#cfn-ec2-vpcendpoint-privatednsenabled)" : {{Boolean}},
      "[ResourceConfigurationArn](#cfn-ec2-vpcendpoint-resourceconfigurationarn)" : {{String}},
      "[RouteTableIds](#cfn-ec2-vpcendpoint-routetableids)" : {{[ String, ... ]}},
      "[SecurityGroupIds](#cfn-ec2-vpcendpoint-securitygroupids)" : {{[ String, ... ]}},
      "[ServiceName](#cfn-ec2-vpcendpoint-servicename)" : {{String}},
      "[ServiceNetworkArn](#cfn-ec2-vpcendpoint-servicenetworkarn)" : {{String}},
      "[ServiceRegion](#cfn-ec2-vpcendpoint-serviceregion)" : {{String}},
      "[SubnetIds](#cfn-ec2-vpcendpoint-subnetids)" : {{[ String, ... ]}},
      "[Tags](#cfn-ec2-vpcendpoint-tags)" : {{[ Tag, ... ]}},
      "[VpcEndpointType](#cfn-ec2-vpcendpoint-vpcendpointtype)" : {{String}},
      "[VpcId](#cfn-ec2-vpcendpoint-vpcid)" : {{String}}
    }
}
```

### YAML
<a name="aws-resource-ec2-vpcendpoint-syntax.yaml"></a>

```
Type: AWS::EC2::VPCEndpoint
Properties:
  [DnsOptions](#cfn-ec2-vpcendpoint-dnsoptions): {{
    DnsOptionsSpecification}}
  [IpAddressType](#cfn-ec2-vpcendpoint-ipaddresstype): {{String}}
  [PolicyDocument](#cfn-ec2-vpcendpoint-policydocument): {{Json}}
  [PrivateDnsEnabled](#cfn-ec2-vpcendpoint-privatednsenabled): {{Boolean}}
  [ResourceConfigurationArn](#cfn-ec2-vpcendpoint-resourceconfigurationarn): {{String}}
  [RouteTableIds](#cfn-ec2-vpcendpoint-routetableids): {{
    - String}}
  [SecurityGroupIds](#cfn-ec2-vpcendpoint-securitygroupids): {{
    - String}}
  [ServiceName](#cfn-ec2-vpcendpoint-servicename): {{String}}
  [ServiceNetworkArn](#cfn-ec2-vpcendpoint-servicenetworkarn): {{String}}
  [ServiceRegion](#cfn-ec2-vpcendpoint-serviceregion): {{String}}
  [SubnetIds](#cfn-ec2-vpcendpoint-subnetids): {{
    - String}}
  [Tags](#cfn-ec2-vpcendpoint-tags): {{
    - Tag}}
  [VpcEndpointType](#cfn-ec2-vpcendpoint-vpcendpointtype): {{String}}
  [VpcId](#cfn-ec2-vpcendpoint-vpcid): {{String}}
```

## Properties
<a name="aws-resource-ec2-vpcendpoint-properties"></a>

`DnsOptions`  <a name="cfn-ec2-vpcendpoint-dnsoptions"></a>
Describes the DNS options for an endpoint.
*Required*: No
*Type*: [DnsOptionsSpecification](aws-properties-ec2-vpcendpoint-dnsoptionsspecification.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`IpAddressType`  <a name="cfn-ec2-vpcendpoint-ipaddresstype"></a>
The supported IP address types.
*Required*: No
*Type*: String
*Allowed values*: `ipv4 | ipv6 | dualstack | not-specified`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`PolicyDocument`  <a name="cfn-ec2-vpcendpoint-policydocument"></a>
An endpoint policy, which controls access to the service from the VPC. The default endpoint policy allows full access to the service. Endpoint policies are supported only for gateway and interface endpoints.
For CloudFormation templates in YAML, you can provide the policy in JSON or YAML format. For example, if you have a JSON policy, you can convert it to YAML before including it in the YAML template, and AWS CloudFormation converts the policy to JSON format before calling the API actions for AWS PrivateLink. Alternatively, you can include the JSON directly in the YAML, as shown in the following `Properties` section:

```
Properties:
  VpcEndpointType: 'Interface'
  ServiceName: !Sub 'com.amazonaws.${AWS::Region}.logs'
  PolicyDocument: '{
    "Version":"2012-10-17",
    "Statement": [{
      "Effect":"Allow",
      "Principal":"*",
      "Action":["logs:Describe*","logs:Get*","logs:List*","logs:FilterLogEvents"],
      "Resource":"*"
    }]
  }'
```
*Required*: No
*Type*: Json
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`PrivateDnsEnabled`  <a name="cfn-ec2-vpcendpoint-privatednsenabled"></a>
Indicate whether to associate a private hosted zone with the specified VPC. The private hosted zone contains a record set for the default public DNS name for the service for the Region (for example, `kinesis.us-east-1.amazonaws.com`), which resolves to the private IP addresses of the endpoint network interfaces in the VPC. This enables you to make requests to the default public DNS name for the service instead of the public DNS names that are automatically generated by the VPC endpoint service.
To use a private hosted zone, you must set the following VPC attributes to `true`: `enableDnsHostnames` and `enableDnsSupport`.
This property is supported only for interface endpoints.
Default: `false`
*Required*: No
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ResourceConfigurationArn`  <a name="cfn-ec2-vpcendpoint-resourceconfigurationarn"></a>
The Amazon Resource Name (ARN) of the resource configuration.
*Required*: No
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`RouteTableIds`  <a name="cfn-ec2-vpcendpoint-routetableids"></a>
The IDs of the route tables. Routing is supported only for gateway endpoints.
*Required*: No
*Type*: Array of String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SecurityGroupIds`  <a name="cfn-ec2-vpcendpoint-securitygroupids"></a>
The IDs of the security groups to associate with the endpoint network interfaces. If this parameter is not specified, we use the default security group for the VPC. Security groups are supported only for interface endpoints.
*Required*: No
*Type*: Array of String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ServiceName`  <a name="cfn-ec2-vpcendpoint-servicename"></a>
The name of the endpoint service.
*Required*: No
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`ServiceNetworkArn`  <a name="cfn-ec2-vpcendpoint-servicenetworkarn"></a>
The Amazon Resource Name (ARN) of the service network.
*Required*: No
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`ServiceRegion`  <a name="cfn-ec2-vpcendpoint-serviceregion"></a>
Describes a Region.
*Required*: No
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`SubnetIds`  <a name="cfn-ec2-vpcendpoint-subnetids"></a>
The IDs of the subnets in which to create endpoint network interfaces. You must specify this property for an interface endpoint or a Gateway Load Balancer endpoint. You can't specify this property for a gateway endpoint. For a Gateway Load Balancer endpoint, you can specify only one subnet.
*Required*: Conditional
*Type*: Array of String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Tags`  <a name="cfn-ec2-vpcendpoint-tags"></a>
The tags to associate with the endpoint.
*Required*: No
*Type*: Array of [Tag](aws-properties-ec2-vpcendpoint-tag.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`VpcEndpointType`  <a name="cfn-ec2-vpcendpoint-vpcendpointtype"></a>
The type of endpoint.
Default: Gateway
*Required*: No
*Type*: String
*Allowed values*: `Interface | Gateway | GatewayLoadBalancer | ServiceNetwork | Resource | Tunnel`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`VpcId`  <a name="cfn-ec2-vpcendpoint-vpcid"></a>
The ID of the VPC.
*Required*: Yes
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## Return values
<a name="aws-resource-ec2-vpcendpoint-return-values"></a>

### Ref
<a name="aws-resource-ec2-vpcendpoint-return-values-ref"></a>

When you pass the logical ID of this resource to the intrinsic `Ref` function, `Ref` returns the ID of the VPC endpoint.

For more information about using the `Ref` function, see [`Ref`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-ref.html).

### Fn::GetAtt
<a name="aws-resource-ec2-vpcendpoint-return-values-fn--getatt"></a>

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [`Fn::GetAtt`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-getatt.html).

####
<a name="aws-resource-ec2-vpcendpoint-return-values-fn--getatt-fn--getatt"></a>

`CreationTimestamp`  <a name="CreationTimestamp-fn::getatt"></a>
The date and time the VPC endpoint was created. For example: `Fri Sep 28 23:34:36 UTC 2018.`

`DnsEntries`  <a name="DnsEntries-fn::getatt"></a>
(Interface endpoints) The DNS entries for the endpoint. Each entry is a combination of the hosted zone ID and the DNS name. The entries are ordered as follows: regional public DNS, zonal public DNS, private DNS, and wildcard DNS. This order is not enforced for AWS Marketplace services.
The following is an example. In the first entry, the hosted zone ID is Z1HUB23UULQXV and the DNS name is vpce-01abc23456de78f9g-12abccd3.ec2.us-east-1.vpce.amazonaws.com.
["Z1HUB23UULQXV:vpce-01abc23456de78f9g-12abccd3.ec2.us-east-1.vpce.amazonaws.com", "Z1HUB23UULQXV:vpce-01abc23456de78f9g-12abccd3-us-east-1a.ec2.us-east-1.vpce.amazonaws.com", "Z1C12344VYDITB0:ec2.us-east-1.amazonaws.com"]
If you update the `PrivateDnsEnabled` or `SubnetIds` properties, the DNS entries in the list will change.

`Id`  <a name="Id-fn::getatt"></a>
The ID of the VPC endpoint.

`NetworkInterfaceIds`  <a name="NetworkInterfaceIds-fn::getatt"></a>
(Interface endpoints) The network interface IDs. If you update the `PrivateDnsEnabled` or `SubnetIds` properties, the items in this list might change.

## Examples
<a name="aws-resource-ec2-vpcendpoint--examples"></a>

**Topics**
+ [Create an interface endpoint](#aws-resource-ec2-vpcendpoint--examples--Create_an_interface_endpoint)
+ [Create a gateway endpoint](#aws-resource-ec2-vpcendpoint--examples--Create_a_gateway_endpoint)
+ [Create a Gateway Load Balancer endpoint](#aws-resource-ec2-vpcendpoint--examples--Create_a_Gateway_Load_Balancer_endpoint)
+ [Create a resource endpoint](#aws-resource-ec2-vpcendpoint--examples--Create_a_resource_endpoint)
+ [Create a service network endpoint](#aws-resource-ec2-vpcendpoint--examples--Create_a_service_network_endpoint)

### Create an interface endpoint
<a name="aws-resource-ec2-vpcendpoint--examples--Create_an_interface_endpoint"></a>

The following example creates an interface endpoint for Amazon CloudWatch Logs in the current Region. Traffic to CloudWatch Logs from any subnet in the Availability Zones that contain `subnetA` and `subnetB` automatically traverses the interface endpoint.

You can customize the properties of `myVPC`, `subnetA`, `subnetB`, and `mySecurityGroup` as needed. Alternatively, specify the IDs of existing resources in `VpcId`, `SubnetIds`, and `SecurityGroupIds`.

#### YAML
<a name="aws-resource-ec2-vpcendpoint--examples--Create_an_interface_endpoint--yaml"></a>

```
Resources:
  CWLInterfaceEndpoint:
    Type: 'AWS::EC2::VPCEndpoint'
    Properties:
      VpcEndpointType: 'Interface'
      ServiceName: !Sub 'com.amazonaws.${AWS::Region}.logs'
      VpcId: !Ref myVPC
      PrivateDnsEnabled: true
      SubnetIds:
        - !Ref subnetA
        - !Ref subnetB
      SecurityGroupIds:
        - !Ref mySecurityGroup
  myVPC:
    Type: 'AWS::EC2::VPC'
    Properties:
      CidrBlock: 10.0.0.0/16
      EnableDnsSupport: true
      EnableDnsHostnames: true
      Tags:
        - Key: 'Name'
          Value: 'myVPC'
  subnetA:
    Type: 'AWS::EC2::Subnet'
    Properties:
      VpcId: !Ref myVPC
      CidrBlock: '10.0.1.0/24'
      AvailabilityZone: !Select [ 0, !GetAZs ]
  subnetB:
    Type: 'AWS::EC2::Subnet'
    Properties:
      VpcId: !Ref myVPC
      CidrBlock: '10.0.2.0/24'
      AvailabilityZone: !Select [ 1, !GetAZs ]
  mySecurityGroup:
    Type: 'AWS::EC2::SecurityGroup'
    Properties:
      GroupDescription: 'Allow HTTPS traffic from the VPC'
      VpcId: !Ref myVPC
      SecurityGroupIngress:
        - IpProtocol: tcp
          FromPort: 443
          ToPort: 443
          CidrIp: !GetAtt myVPC.CidrBlock
```

#### JSON
<a name="aws-resource-ec2-vpcendpoint--examples--Create_an_interface_endpoint--json"></a>

```
{
    "Resources": {
        "CWLInterfaceEndpoint": {
            "Type": "AWS::EC2::VPCEndpoint",
            "Properties": {
                "VpcEndpointType": "Interface",
                "ServiceName": {
                    "Fn::Sub": "com.amazonaws.${AWS::Region}.logs"
                },
                "VpcId": {
                    "Ref": "myVPC"
                },
                "PrivateDnsEnabled": true,
                "SubnetIds": [
                    {
                        "Ref": "subnetA"
                    },
                    {
                        "Ref": "subnetB"
                    }
                ],
                "SecurityGroupIds": [
                    {
                        "Ref": "mySecurityGroup"
                    }
                ]
            }
        },
        "myVPC": {
            "Type": "AWS::EC2::VPC",
            "Properties": {
                "CidrBlock": "10.0.0.0/16",
                "EnableDnsSupport": true,
                "EnableDnsHostnames": true,
                "Tags": [
                    {
                        "Key": "Name",
                        "Value": "myVPC"
                    }
                ]
            }
        },
        "subnetA": {
            "Type": "AWS::EC2::Subnet",
            "Properties": {
                "VpcId": {
                    "Ref": "myVPC"
                },
                "CidrBlock": "10.0.1.0/24",
                "AvailabilityZone": {
                    "Fn::Select": [
                        0,
                        {
                            "Fn::GetAZs": ""
                        }
                    ]
                }
            }
        },
        "subnetB": {
            "Type": "AWS::EC2::Subnet",
            "Properties": {
                "VpcId": {
                    "Ref": "myVPC"
                },
                "CidrBlock": "10.0.2.0/24",
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
        "mySecurityGroup": {
            "Type": "AWS::EC2::SecurityGroup",
            "Properties": {
                "GroupDescription": "Allow HTTPS traffic from the VPC",
                "VpcId": {
                    "Ref": "myVPC"
                },
                "SecurityGroupIngress": [
                    {
                        "IpProtocol": "tcp",
                        "FromPort": 443,
                        "ToPort": 443,
                        "CidrIp": {
                            "Fn::GetAtt": [
                                "myVPC",
                                "CidrBlock"
                            ]
                        }
                    }
                ]
            }
        }
    }
}
```

### Create a gateway endpoint
<a name="aws-resource-ec2-vpcendpoint--examples--Create_a_gateway_endpoint"></a>

The following example creates a gateway endpoint that connects the VPC defined by `myVPC` with Amazon S3 in the current Region. The endpoint policy allows only the `s3:GetObject` action on the specified bucket. Traffic to Amazon S3 from the subnets that are associated with the route table specified in `RouteTableIds` is automatically routed through the gateway endpoint.

You can customize the properties of `myVPC`, `mySubnet`, `myRouteTable`, and `mySubnetRouteTableAssociation` as needed. Alternatively, specify the IDs of existing resources in `VpcId` and `RouteTableIds`.

#### YAML
<a name="aws-resource-ec2-vpcendpoint--examples--Create_a_gateway_endpoint--yaml"></a>

```
Resources:
  S3GatewayEndpoint:
    Type: 'AWS::EC2::VPCEndpoint'
    Properties:
      VpcEndpointType: 'Gateway'
      VpcId: !Ref myVPC
      ServiceName: !Sub 'com.amazonaws.${AWS::Region}.s3'
      PolicyDocument:
        Version: 2012-10-17
        Statement:
          - Effect: Allow
            Principal: '*'
            Action:
              - 's3:GetObject'
            Resource:
              - 'arn:aws:s3:::amzn-s3-demo-bucket/*'
      RouteTableIds:
        - !Ref myRouteTable
  myVPC:
    Type: 'AWS::EC2::VPC'
    Properties:
      CidrBlock: '10.0.0.0/16'
      EnableDnsSupport: true
      EnableDnsHostnames: true
      Tags:
        - Key: 'Name'
          Value: 'myVPC'
  mySubnet:
    Type: 'AWS::EC2::Subnet'
    Properties:
      VpcId: !Ref myVPC
      CidrBlock: 10.0.0.0/24
      AvailabilityZone: !Select [ 0, !GetAZs ]
  myRouteTable:
    Type: 'AWS::EC2::RouteTable'
    Properties:
      VpcId: !Ref myVPC
  mySubnetRouteTableAssociation:
    Type: 'AWS::EC2::SubnetRouteTableAssociation'
    Properties:
      SubnetId: !Ref mySubnet
      RouteTableId: !Ref myRouteTable
```

#### JSON
<a name="aws-resource-ec2-vpcendpoint--examples--Create_a_gateway_endpoint--json"></a>

```
{
    "Resources": {
        "S3GatewayEndpoint": {
            "Type": "AWS::EC2::VPCEndpoint",
            "Properties": {
                "VpcEndpointType": "Gateway",
                "VpcId": {
                    "Ref": "myVPC"
                },
                "ServiceName": {
                    "Fn::Sub": "com.amazonaws.${AWS::Region}.s3"
                },
                "PolicyDocument": {
                    "Version": "2012-10-17",
                    "Statement": [
                        {
                            "Effect": "Allow",
                            "Principal": "*",
                            "Action": [
                                "s3:GetObject"
                            ],
                            "Resource": [
                                "arn:aws:s3:::amzn-s3-demo-bucket/*"
                            ]
                        }
                    ]
                },
                "RouteTableIds": [
                    {
                        "Ref": "myRouteTable"
                    }
                ]
            }
        },
        "myVPC": {
            "Type": "AWS::EC2::VPC",
            "Properties": {
                "CidrBlock": "10.0.0.0/16",
                "EnableDnsSupport": true,
                "EnableDnsHostnames": true,
                "Tags": [
                    {
                        "Key": "Name",
                        "Value": "myVPC"
                    }
                ]
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
                            "Fn::GetAZs": null
                        }
                    ]
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
        "mySubnetRouteTableAssociation": {
            "Type": "AWS::EC2::SubnetRouteTableAssociation",
            "Properties": {
                "SubnetId": {
                    "Ref": "mySubnet"
                },
                "RouteTableId": {
                    "Ref": "myRouteTable"
                }
            }
        }
    }
}
```

### Create a Gateway Load Balancer endpoint
<a name="aws-resource-ec2-vpcendpoint--examples--Create_a_Gateway_Load_Balancer_endpoint"></a>

The following example creates a Gateway Load Balancer endpoint that connects `myVPC` with the specified endpoint service in the current Region.

You can customize the properties of `myVPC` and `mySubnet` as needed. Alternatively, specify the IDs of existing resources in `VpcId` and `SubnetIds`.

#### YAML
<a name="aws-resource-ec2-vpcendpoint--examples--Create_a_Gateway_Load_Balancer_endpoint--yaml"></a>

```
Resources:
  GWLBEndpoint:
    Type: 'AWS::EC2::VPCEndpoint'
    Properties:
      VpcEndpointType: 'GatewayLoadBalancer'
      ServiceName: 'com.amazonaws.vpce.${AWS::Region}.vpce-svc-123123a1c43abc123'
      VpcId: !Ref myVPC
      SubnetIds:
        - !Ref mySubnet
  myVPC:
    Type: 'AWS::EC2::VPC'
    Properties:
      CidrBlock: '10.0.0.0/16'
      EnableDnsSupport: true
      EnableDnsHostnames: true
      Tags:
        - Key: 'Name'
          Value: 'myVPC'
  mySubnet:
    Type: 'AWS::EC2::Subnet'
    Properties:
      VpcId: !Ref myVPC
      CidrBlock: '10.0.0.0/24'
      AvailabilityZone: !Select [ 1, !GetAZs ]
```

#### JSON
<a name="aws-resource-ec2-vpcendpoint--examples--Create_a_Gateway_Load_Balancer_endpoint--json"></a>

```
{
    "Resources": {
        "GWLBEndpoint": {
            "Type": "AWS::EC2::VPCEndpoint",
            "Properties": {
                "VpcEndpointType": "GatewayLoadBalancer",
                "ServiceName": "com.amazonaws.vpce.${AWS::Region}.vpce-svc-123123a1c43abc123",
                "VpcId": {
                    "Ref": "myVPC"
                },
                "SubnetIds": [
                    {
                        "Ref": "mySubnet"
                    }
                ]
            }
        },
        "myVPC": {
            "Type": "AWS::EC2::VPC",
            "Properties": {
                "CidrBlock": "10.0.0.0/16",
                "EnableDnsSupport": true,
                "EnableDnsHostnames": true,
                "Tags": [
                    {
                        "Key": "Name",
                        "Value": "myVPC"
                    }
                ]
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
        }
    }
}
```

### Create a resource endpoint
<a name="aws-resource-ec2-vpcendpoint--examples--Create_a_resource_endpoint"></a>

The following example creates a resource endpoint that you can use to access a single IPv4 address. It also creates a resource gateway and a resource configuration. It assumes that you defined a VPC, a subnet, and a security group, which are referenced here as `myVPC`, `mySubnet`, and `mySecurityGroup`.

#### YAML
<a name="aws-resource-ec2-vpcendpoint--examples--Create_a_resource_endpoint--yaml"></a>

```
Resources:
  myResourceEndpoint:
    Type: 'AWS::EC2::VPCEndpoint'
    Properties:
      VpcEndpointType: 'Resource'
      VpcId: !Ref myVPC
      SubnetIds:
       - !Ref mySubnet
      ResourceConfigurationArn: !Ref myResourceConfiguration
  myResourceConfiguration:
    Type: 'AWS::VpcLattice::ResourceConfiguration'
    Properties:
      Name: test-resource-config
      ResourceConfigurationType: SINGLE
      ResourceGatewayId: !Ref myResourceGateway
      ResourceConfigurationDefinition:
       IpResource: 10.0.14.85
  myResourceGateway:
    Type: 'AWS::VpcLattice::ResourceGateway'
    Properties:
      Name: test-resource-gateway
      VpcIdentifier: !Ref myVPC
      SubnetIds:
       - !Ref mySubnet
      SecurityGroupIds:
       - !Ref mySecurityGroup
```

#### JSON
<a name="aws-resource-ec2-vpcendpoint--examples--Create_a_resource_endpoint--json"></a>

```
{
    "Resources": {
        "myResourceEndpoint": {
            "Type": "AWS::EC2::VPCEndpoint",
            "Properties": {
                "VpcEndpointType": "Resource",
                "VpcId": {
                    "Ref": "myVPC"
                },
                "SubnetIds": [
                    {
                        "Ref": "mySubnet"
                    }
                ],
                "ResourceConfigurationArn": {
                    "Ref": "myResourceConfiguration"
                }
            }
        },
        "myResourceConfiguration": {
            "Type": "AWS::VpcLattice::ResourceConfiguration",
            "Properties": {
                "Name": "test-resource-config",
                "ResourceConfigurationType": "SINGLE",
                "ResourceGatewayId": {
                    "Ref": "myResourceGateway"
                },
                "ResourceConfigurationDefinition": {
                    "IpResource": "10.0.14.85"
                }
            }
        },
        "myResourceGateway": {
            "Type": "AWS::VpcLattice::ResourceGateway",
            "Properties": {
                "Name": "test-resource-gateway",
                "VpcIdentifier": {
                    "Ref": "myVPC"
                },
                "SubnetIds": [
                    {
                        "Ref": "mySubnet"
                    }
                ],
                "SecurityGroupIds": [
                    {
                        "Ref": "mySecurityGroup"
                    }
                ]
            }
        }
    }
}
```

### Create a service network endpoint
<a name="aws-resource-ec2-vpcendpoint--examples--Create_a_service_network_endpoint"></a>

The following example creates a service network endpoint that you can use to access your service network. It also creates a service network. It assumes that you defined a VPC, a subnet, and a security group, which are referenced here as `myVPC`, `mySubnet`, and `mySecurityGroup`.

#### YAML
<a name="aws-resource-ec2-vpcendpoint--examples--Create_a_service_network_endpoint--yaml"></a>

```
Resources:
  myServiceNetworkEndpoint:
    Type: 'AWS::EC2::VPCEndpoint'
    Properties:
      VpcEndpointType: 'ServiceNetwork'
      VpcId: !Ref myVPC
      ServiceNetworkArn: !Ref myServiceNetwork
      SubnetIds:
        - !Ref mySubnet
      SecurityGroupIds:
        - !Ref mySecurityGroup
  myServiceNetwork:
    Type: 'AWS::VpcLattice::ServiceNetwork'
    Properties:
      Name: test-service-network
```

#### JSON
<a name="aws-resource-ec2-vpcendpoint--examples--Create_a_service_network_endpoint--json"></a>

```
{
    "Resources": {
        "myServiceNetworkEndpoint": {
            "Type": "AWS::EC2::VPCEndpoint",
            "Properties": {
                "VpcEndpointType": "ServiceNetwork",
                "VpcId": {
                    "Ref": "myVPC"
                },
                "ServiceNetworkArn": {
                    "Ref": "myServiceNetwork"
                },
                "SubnetIds": [
                    {
                        "Ref": "mySubnet"
                    }
                ],
                "SecurityGroupIds": [
                    {
                        "Ref": "mySecurityGroup"
                    }
                ]
            }
        },
        "myServiceNetwork": {
            "Type": "AWS::VpcLattice::ServiceNetwork",
            "Properties": {
                "Name": "test-service-network"
            }
        }
    }
}
```
