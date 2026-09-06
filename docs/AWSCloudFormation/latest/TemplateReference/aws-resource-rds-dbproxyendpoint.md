---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-rds-dbproxyendpoint.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::RDS::DBProxyEndpoint
<a name="aws-resource-rds-dbproxyendpoint"></a>

The `AWS::RDS::DBProxyEndpoint` resource creates or updates a DB proxy endpoint. You can use custom proxy endpoints to access a proxy through a different VPC than the proxy's default VPC.

For more information about RDS Proxy, see [ AWS::RDS::DBProxy](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-rds-dbproxy.html).

## Syntax
<a name="aws-resource-rds-dbproxyendpoint-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-rds-dbproxyendpoint-syntax.json"></a>

```
{
  "Type" : "AWS::RDS::DBProxyEndpoint",
  "Properties" : {
      "[DBProxyEndpointName](#cfn-rds-dbproxyendpoint-dbproxyendpointname)" : {{String}},
      "[DBProxyName](#cfn-rds-dbproxyendpoint-dbproxyname)" : {{String}},
      "[EndpointNetworkType](#cfn-rds-dbproxyendpoint-endpointnetworktype)" : {{String}},
      "[Tags](#cfn-rds-dbproxyendpoint-tags)" : {{[ TagFormat, ... ]}},
      "[TargetRole](#cfn-rds-dbproxyendpoint-targetrole)" : {{String}},
      "[VpcSecurityGroupIds](#cfn-rds-dbproxyendpoint-vpcsecuritygroupids)" : {{[ String, ... ]}},
      "[VpcSubnetIds](#cfn-rds-dbproxyendpoint-vpcsubnetids)" : {{[ String, ... ]}}
    }
}
```

### YAML
<a name="aws-resource-rds-dbproxyendpoint-syntax.yaml"></a>

```
Type: AWS::RDS::DBProxyEndpoint
Properties:
  [DBProxyEndpointName](#cfn-rds-dbproxyendpoint-dbproxyendpointname): {{String}}
  [DBProxyName](#cfn-rds-dbproxyendpoint-dbproxyname): {{String}}
  [EndpointNetworkType](#cfn-rds-dbproxyendpoint-endpointnetworktype): {{String}}
  [Tags](#cfn-rds-dbproxyendpoint-tags): {{
    - TagFormat}}
  [TargetRole](#cfn-rds-dbproxyendpoint-targetrole): {{String}}
  [VpcSecurityGroupIds](#cfn-rds-dbproxyendpoint-vpcsecuritygroupids): {{
    - String}}
  [VpcSubnetIds](#cfn-rds-dbproxyendpoint-vpcsubnetids): {{
    - String}}
```

## Properties
<a name="aws-resource-rds-dbproxyendpoint-properties"></a>

`DBProxyEndpointName`  <a name="cfn-rds-dbproxyendpoint-dbproxyendpointname"></a>
The name of the DB proxy endpoint to create.
*Required*: Yes
*Type*: String
*Pattern*: `[0-z]*`
*Maximum*: `64`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`DBProxyName`  <a name="cfn-rds-dbproxyendpoint-dbproxyname"></a>
The name of the DB proxy associated with the DB proxy endpoint that you create.
*Required*: Yes
*Type*: String
*Pattern*: `[0-z]*`
*Maximum*: `64`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`EndpointNetworkType`  <a name="cfn-rds-dbproxyendpoint-endpointnetworktype"></a>
The network type of the DB proxy endpoint. The network type determines the IP version that the proxy endpoint supports.
Valid values:
+ `IPV4` - The proxy endpoint supports IPv4 only.
+ `IPV6` - The proxy endpoint supports IPv6 only.
+ `DUAL` - The proxy endpoint supports both IPv4 and IPv6.
*Required*: No
*Type*: String
*Allowed values*: `IPV4 | IPV6 | DUAL`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Tags`  <a name="cfn-rds-dbproxyendpoint-tags"></a>
An optional set of key-value pairs to associate arbitrary data of your choosing with the proxy.
*Required*: No
*Type*: Array of [TagFormat](aws-properties-rds-dbproxyendpoint-tagformat.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`TargetRole`  <a name="cfn-rds-dbproxyendpoint-targetrole"></a>
A value that indicates whether the DB proxy endpoint can be used for read/write or read-only operations.
*Required*: No
*Type*: String
*Allowed values*: `READ_WRITE | READ_ONLY`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`VpcSecurityGroupIds`  <a name="cfn-rds-dbproxyendpoint-vpcsecuritygroupids"></a>
The VPC security group IDs for the DB proxy endpoint that you create. You can specify a different set of security group IDs than for the original DB proxy. The default is the default security group for the VPC.
*Required*: No
*Type*: Array of String
*Minimum*: `1`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`VpcSubnetIds`  <a name="cfn-rds-dbproxyendpoint-vpcsubnetids"></a>
The VPC subnet IDs for the DB proxy endpoint that you create. You can specify a different set of subnet IDs than for the original DB proxy.
*Required*: Yes
*Type*: Array of String
*Minimum*: `2`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## Return values
<a name="aws-resource-rds-dbproxyendpoint-return-values"></a>

### Ref
<a name="aws-resource-rds-dbproxyendpoint-return-values-ref"></a>

When you pass the logical ID of this resource to the intrinsic `Ref` function, `Ref` returns the name of the DB proxy endpoint.

For more information about using the `Ref` function, see [`Ref`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-ref.html).

### Fn::GetAtt
<a name="aws-resource-rds-dbproxyendpoint-return-values-fn--getatt"></a>

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [`Fn::GetAtt`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-getatt.html).

####
<a name="aws-resource-rds-dbproxyendpoint-return-values-fn--getatt-fn--getatt"></a>

`DBProxyEndpointArn`  <a name="DBProxyEndpointArn-fn::getatt"></a>
The Amazon Resource Name (ARN) for the DB proxy endpoint.

`Endpoint`  <a name="Endpoint-fn::getatt"></a>
The endpoint that you can use to connect to the DB proxy. You include the endpoint value in the connection string for a database client application.

`IsDefault`  <a name="IsDefault-fn::getatt"></a>
Indicates whether this endpoint is the default endpoint for the associated DB proxy. Default DB proxy endpoints always have read/write capability. Other endpoints that you associate with the DB proxy can be either read/write or read-only.

`VpcId`  <a name="VpcId-fn::getatt"></a>
Provides the VPC ID of the DB proxy endpoint.

## Examples
<a name="aws-resource-rds-dbproxyendpoint--examples"></a>

### Creating a custom DB proxy endpoint
<a name="aws-resource-rds-dbproxyendpoint--examples--Creating_a_custom_DB_proxy_endpoint"></a>

The following example creates a custom DB proxy endpoint.

#### JSON
<a name="aws-resource-rds-dbproxyendpoint--examples--Creating_a_custom_DB_proxy_endpoint--json"></a>

```
{
  "AWSTemplateFormatVersion": "2010-09-09",
  "Parameters": {
    "ProxyEndpointName": {
      "Type": "String",
      "Default": "exampleProxyEndpoint"
    },
    "ProxyName": {
      "Type": "String",
      "Default": "exampleProxy"
    },
    "SecurityGroupIds": {
      "Type": "String",
      "Default": "sg-12345678"
    },
    "SubnetIds": {
      "Type": "String",
      "Default": "subnet-12345677,subnet-12345678,subnet-12345679"
    }
  },
  "Resources": {
    "TestDBProxy": {
      "Type": "AWS::RDS::DBProxyEndpoint",
      "Properties": {
        "DBProxyEndpointName": {
          "Ref": "ProxyEndpointName"
        },
        "DBProxyName": {
          "Ref": "ProxyName"
        },
        "VpcSecurityGroupIds": {
          "Fn::Split": [
            ",",
            {
              "Ref": "SecurityGroupIds"
            }
          ]
        },
        "VpcSubnetIds": {
          "Fn::Split": [
            ",",
            {
              "Ref": "SubnetIds"
            }
          ]
        },
        "TargetRole": "READ_ONLY"
      }
    }
  }
}
```

#### YAML
<a name="aws-resource-rds-dbproxyendpoint--examples--Creating_a_custom_DB_proxy_endpoint--yaml"></a>

```
AWSTemplateFormatVersion: 2010-09-09
Parameters:
  ProxyEndpointName:
    Type: String
    Default: exampleProxyEndpoint
  ProxyName:
    Type: String
    Default: exampleProxy
  SubnetIds:
    Type: String
    Default: subnet-12345677,subnet-12345678,subnet-12345679
  SecurityGroupIds:
    Type: String
    Default: sg-12345678
Resources:
  TestDBProxyEndpoint:
    Type: AWS::RDS::DBProxyEndpoint
    Properties:
      DBProxyEndpointName: !Ref ProxyEndpointName
      DBProxyName: !Ref ProxyName
      VpcSubnetIds:
        Fn::Split: [",", !Ref SubnetIds]
      VpcSecurityGroupIds:
        Fn::Split: [",", !Ref SecurityGroupIds]
      TargetRole: READ_ONLY
```
