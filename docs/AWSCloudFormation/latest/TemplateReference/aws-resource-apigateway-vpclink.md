---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-apigateway-vpclink.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::ApiGateway::VpcLink
<a name="aws-resource-apigateway-vpclink"></a>

The `AWS::ApiGateway::VpcLink` resource creates an API Gateway VPC link for a REST API to access resources in an Amazon Virtual Private Cloud (VPC). For more information, see [vpclink:create](https://docs.aws.amazon.com/apigateway/latest/api/API_CreateVpcLink.html) in the `Amazon API Gateway REST API Reference`.

## Syntax
<a name="aws-resource-apigateway-vpclink-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-apigateway-vpclink-syntax.json"></a>

```
{
  "Type" : "AWS::ApiGateway::VpcLink",
  "Properties" : {
      "[Description](#cfn-apigateway-vpclink-description)" : {{String}},
      "[Name](#cfn-apigateway-vpclink-name)" : {{String}},
      "[Tags](#cfn-apigateway-vpclink-tags)" : {{[ Tag, ... ]}},
      "[TargetArns](#cfn-apigateway-vpclink-targetarns)" : {{[ String, ... ]}}
    }
}
```

### YAML
<a name="aws-resource-apigateway-vpclink-syntax.yaml"></a>

```
Type: AWS::ApiGateway::VpcLink
Properties:
  [Description](#cfn-apigateway-vpclink-description): {{String}}
  [Name](#cfn-apigateway-vpclink-name): {{String}}
  [Tags](#cfn-apigateway-vpclink-tags): {{
    - Tag}}
  [TargetArns](#cfn-apigateway-vpclink-targetarns): {{
    - String}}
```

## Properties
<a name="aws-resource-apigateway-vpclink-properties"></a>

`Description`  <a name="cfn-apigateway-vpclink-description"></a>
The description of the VPC link.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Name`  <a name="cfn-apigateway-vpclink-name"></a>
The name used to label and identify the VPC link.
*Required*: Yes
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Tags`  <a name="cfn-apigateway-vpclink-tags"></a>
An array of arbitrary tags (key-value pairs) to associate with the VPC link.
*Required*: No
*Type*: Array of [Tag](aws-properties-apigateway-vpclink-tag.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`TargetArns`  <a name="cfn-apigateway-vpclink-targetarns"></a>
The ARN of the network load balancer of the VPC targeted by the VPC link. The network load balancer must be owned by the same AWS account of the API owner.
*Required*: Yes
*Type*: Array of String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## Return values
<a name="aws-resource-apigateway-vpclink-return-values"></a>

### Ref
<a name="aws-resource-apigateway-vpclink-return-values-ref"></a>

When you pass the logical ID of this resource to the intrinsic `Ref` function, `Ref` returns the ID of the `VpcLink`.

For more information about using the `Ref` function, see [`Ref`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-ref.html).

### Fn::GetAtt
<a name="aws-resource-apigateway-vpclink-return-values-fn--getatt"></a>

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [`Fn::GetAtt`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-getatt.html).

####
<a name="aws-resource-apigateway-vpclink-return-values-fn--getatt-fn--getatt"></a>

`VpcLinkId`  <a name="VpcLinkId-fn::getatt"></a>
The ID for the VPC link. For example: `abc123`.

## Examples
<a name="aws-resource-apigateway-vpclink--examples"></a>

### Create VPC link
<a name="aws-resource-apigateway-vpclink--examples--Create_VPC_link"></a>

#### JSON
<a name="aws-resource-apigateway-vpclink--examples--Create_VPC_link--json"></a>

```
{
    "Parameters": {
        "description": {
            "Type": "String"
        },
        "name": {
            "Type": "String"
        }
    },
    "Resources": {
        "MyVpcLink": {
            "Type": "AWS::ApiGateway::VpcLink",
            "Properties": {
                "Description": {
                    "Ref": "description"
                },
                "Name": {
                    "Ref": "name"
                },
                "TargetArns": [
                    {
                        "Ref": "MyLoadBalancer"
                    }
                ]
            }
        },
        "MyLoadBalancer": {
            "Type": "AWS::ElasticLoadBalancingV2::LoadBalancer",
            "Properties": {
                "Type": "network",
                "Subnets": [
                    {
                        "Ref": "MySubnet"
                    }
                ]
            }
        },
        "MySubnet": {
            "Type": "AWS::EC2::Subnet",
            "Properties": {
                "VpcId": {
                    "Ref": "MyVPC"
                },
                "CidrBlock": "10.0.0.0/24"
            }
        },
        "MyVPC": {
            "Type": "AWS::EC2::VPC",
            "Properties": {
                "CidrBlock": "10.0.0.0/16"
            }
        },
        "MyInternetGateway": {
            "Type": "AWS::EC2::InternetGateway"
        },
        "MyInternetGatewayAttachment": {
            "Type": "AWS::EC2::VPCGatewayAttachment",
            "Properties": {
                "VpcId": {
                    "Ref": "MyVPC"
                },
                "InternetGatewayId": {
                    "Ref": "MyInternetGateway"
                }
            }
        }
    }
}
```

#### YAML
<a name="aws-resource-apigateway-vpclink--examples--Create_VPC_link--yaml"></a>

```
Parameters:
    description:
        Type: String
    name:
        Type: String
Resources:
    MyVpcLink:
        Type: AWS::ApiGateway::VpcLink
        Properties:
            Description: !Ref description
            Name: !Ref name
            TargetArns:
               - !Ref MyLoadBalancer
    MyLoadBalancer:
            Type: AWS::ElasticLoadBalancingV2::LoadBalancer
            Properties:
                Type: network
                Subnets:
                   - !Ref MySubnet
    MySubnet:
        Type: AWS::EC2::Subnet
        Properties:
            VpcId: !Ref MyVPC
            CidrBlock: 10.0.0.0/24
    MyVPC:
        Type: AWS::EC2::VPC
        Properties:
            CidrBlock: 10.0.0.0/16
    MyInternetGateway:
        Type: AWS::EC2::InternetGateway
    MyInternetGatewayAttachment:
        Type: AWS::EC2::VPCGatewayAttachment
        Properties:
            VpcId: !Ref MyVPC
            InternetGatewayId: !Ref MyInternetGateway
```

## See also
<a name="aws-resource-apigateway-vpclink--seealso"></a>
+ [vpclink:create](https://docs.aws.amazon.com/apigateway/latest/api/API_CreateVpcLink.html) in the *Amazon API Gateway REST API Reference*

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
