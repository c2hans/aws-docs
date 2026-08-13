---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-rds-dbproxy.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::RDS::DBProxy
<a name="aws-resource-rds-dbproxy"></a>

The `AWS::RDS::DBProxy` resource creates or updates a DB proxy.

For information about RDS Proxy for Amazon RDS, see [ Managing Connections with Amazon RDS Proxy](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/rds-proxy.html) in the *Amazon RDS User Guide*.

For information about RDS Proxy for Amazon Aurora, see [ Managing Connections with Amazon RDS Proxy](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/rds-proxy.html) in the *Amazon Aurora User Guide*.

**Note**
Limitations apply to RDS Proxy, including DB engine version limitations and AWS Region limitations.
For information about limitations that apply to RDS Proxy for Amazon RDS, see [ Limitations for RDS Proxy](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/rds-proxy.html#rds-proxy.limitations) in the *Amazon RDS User Guide*.
For information about that apply to RDS Proxy for Amazon Aurora, see [ Limitations for RDS Proxy](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/rds-proxy.html#rds-proxy.limitations) in the *Amazon Aurora User Guide*.

## Syntax
<a name="aws-resource-rds-dbproxy-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-rds-dbproxy-syntax.json"></a>

```
{
  "Type" : "AWS::RDS::DBProxy",
  "Properties" : {
      "[Auth](#cfn-rds-dbproxy-auth)" : {{[ AuthFormat, ... ]}},
      "[DBProxyName](#cfn-rds-dbproxy-dbproxyname)" : {{String}},
      "[DebugLogging](#cfn-rds-dbproxy-debuglogging)" : {{Boolean}},
      "[DefaultAuthScheme](#cfn-rds-dbproxy-defaultauthscheme)" : {{String}},
      "[EndpointNetworkType](#cfn-rds-dbproxy-endpointnetworktype)" : {{String}},
      "[EngineFamily](#cfn-rds-dbproxy-enginefamily)" : {{String}},
      "[IdleClientTimeout](#cfn-rds-dbproxy-idleclienttimeout)" : {{Integer}},
      "[RequireTLS](#cfn-rds-dbproxy-requiretls)" : {{Boolean}},
      "[RoleArn](#cfn-rds-dbproxy-rolearn)" : {{String}},
      "[Tags](#cfn-rds-dbproxy-tags)" : {{[ TagFormat, ... ]}},
      "[TargetConnectionNetworkType](#cfn-rds-dbproxy-targetconnectionnetworktype)" : {{String}},
      "[VpcSecurityGroupIds](#cfn-rds-dbproxy-vpcsecuritygroupids)" : {{[ String, ... ]}},
      "[VpcSubnetIds](#cfn-rds-dbproxy-vpcsubnetids)" : {{[ String, ... ]}}
    }
}
```

### YAML
<a name="aws-resource-rds-dbproxy-syntax.yaml"></a>

```
Type: AWS::RDS::DBProxy
Properties:
  [Auth](#cfn-rds-dbproxy-auth): {{
    - AuthFormat}}
  [DBProxyName](#cfn-rds-dbproxy-dbproxyname): {{String}}
  [DebugLogging](#cfn-rds-dbproxy-debuglogging): {{Boolean}}
  [DefaultAuthScheme](#cfn-rds-dbproxy-defaultauthscheme): {{String}}
  [EndpointNetworkType](#cfn-rds-dbproxy-endpointnetworktype): {{String}}
  [EngineFamily](#cfn-rds-dbproxy-enginefamily): {{String}}
  [IdleClientTimeout](#cfn-rds-dbproxy-idleclienttimeout): {{Integer}}
  [RequireTLS](#cfn-rds-dbproxy-requiretls): {{Boolean}}
  [RoleArn](#cfn-rds-dbproxy-rolearn): {{String}}
  [Tags](#cfn-rds-dbproxy-tags): {{
    - TagFormat}}
  [TargetConnectionNetworkType](#cfn-rds-dbproxy-targetconnectionnetworktype): {{String}}
  [VpcSecurityGroupIds](#cfn-rds-dbproxy-vpcsecuritygroupids): {{
    - String}}
  [VpcSubnetIds](#cfn-rds-dbproxy-vpcsubnetids): {{
    - String}}
```

## Properties
<a name="aws-resource-rds-dbproxy-properties"></a>

`Auth`  <a name="cfn-rds-dbproxy-auth"></a>
The authorization mechanism that the proxy uses.
*Required*: No
*Type*: Array of [AuthFormat](aws-properties-rds-dbproxy-authformat.md)
*Minimum*: `1`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`DBProxyName`  <a name="cfn-rds-dbproxy-dbproxyname"></a>
The identifier for the proxy. This name must be unique for all proxies owned by your AWS account in the specified AWS Region. An identifier must begin with a letter and must contain only ASCII letters, digits, and hyphens; it can't end with a hyphen or contain two consecutive hyphens.
*Required*: Yes
*Type*: String
*Pattern*: `[0-z]*`
*Maximum*: `64`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`DebugLogging`  <a name="cfn-rds-dbproxy-debuglogging"></a>
Specifies whether the proxy logs detailed connection and query information. When you enable `DebugLogging`, the proxy captures connection details and connection pool behavior from your queries. Debug logging increases CloudWatch costs and can impact proxy performance. Enable this option only when you need to troubleshoot connection or performance issues.
*Required*: No
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`DefaultAuthScheme`  <a name="cfn-rds-dbproxy-defaultauthscheme"></a>
The default authentication scheme that the proxy uses for client connections to the proxy and connections from the proxy to the underlying database. Valid values are `NONE` and `IAM_AUTH`. When set to `IAM_AUTH`, the proxy uses end-to-end IAM authentication to connect to the database.
*Required*: No
*Type*: String
*Allowed values*: `IAM_AUTH | NONE`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`EndpointNetworkType`  <a name="cfn-rds-dbproxy-endpointnetworktype"></a>
The network type of the DB proxy endpoint. The network type determines the IP version that the proxy endpoint supports.
Valid values:
+ `IPV4` - The proxy endpoint supports IPv4 only.
+ `IPV6` - The proxy endpoint supports IPv6 only.
+ `DUAL` - The proxy endpoint supports both IPv4 and IPv6.
*Required*: No
*Type*: String
*Allowed values*: `IPV4 | IPV6 | DUAL`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`EngineFamily`  <a name="cfn-rds-dbproxy-enginefamily"></a>
The kinds of databases that the proxy can connect to. This value determines which database network protocol the proxy recognizes when it interprets network traffic to and from the database. For Aurora MySQL, RDS for MariaDB, and RDS for MySQL databases, specify `MYSQL`. For Aurora PostgreSQL and RDS for PostgreSQL databases, specify `POSTGRESQL`. For RDS for Microsoft SQL Server, specify `SQLSERVER`.
*Required*: Yes
*Type*: String
*Allowed values*: `MYSQL | POSTGRESQL | SQLSERVER`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`IdleClientTimeout`  <a name="cfn-rds-dbproxy-idleclienttimeout"></a>
The number of seconds that a connection to the proxy can be inactive before the proxy disconnects it. You can set this value higher or lower than the connection timeout limit for the associated database.
*Required*: No
*Type*: Integer
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`RequireTLS`  <a name="cfn-rds-dbproxy-requiretls"></a>
Specifies whether Transport Layer Security (TLS) encryption is required for connections to the proxy. By enabling this setting, you can enforce encrypted TLS connections to the proxy.
*Required*: No
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`RoleArn`  <a name="cfn-rds-dbproxy-rolearn"></a>
The Amazon Resource Name (ARN) of the IAM role that the proxy uses to access secrets in AWS Secrets Manager.
*Required*: Yes
*Type*: String
*Minimum*: `20`
*Maximum*: `2048`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Tags`  <a name="cfn-rds-dbproxy-tags"></a>
An optional set of key-value pairs to associate arbitrary data of your choosing with the proxy.
*Required*: No
*Type*: Array of [TagFormat](aws-properties-rds-dbproxy-tagformat.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`TargetConnectionNetworkType`  <a name="cfn-rds-dbproxy-targetconnectionnetworktype"></a>
The network type that the proxy uses to connect to the target database. The network type determines the IP version that the proxy uses for connections to the database.
Valid values:
+ `IPV4` - The proxy connects to the database using IPv4 only.
+ `IPV6` - The proxy connects to the database using IPv6 only.
*Required*: No
*Type*: String
*Allowed values*: `IPV4 | IPV6`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`VpcSecurityGroupIds`  <a name="cfn-rds-dbproxy-vpcsecuritygroupids"></a>
One or more VPC security group IDs to associate with the new proxy.
If you plan to update the resource, don't specify VPC security groups in a shared VPC.
*Required*: No
*Type*: Array of String
*Minimum*: `1`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`VpcSubnetIds`  <a name="cfn-rds-dbproxy-vpcsubnetids"></a>
One or more VPC subnet IDs to associate with the new proxy.
*Required*: Yes
*Type*: Array of String
*Minimum*: `2`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## Return values
<a name="aws-resource-rds-dbproxy-return-values"></a>

### Ref
<a name="aws-resource-rds-dbproxy-return-values-ref"></a>

When you pass the logical ID of this resource to the intrinsic `Ref` function, `Ref` returns the name of the DB proxy.

For more information about using the `Ref` function, see [`Ref`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-ref.html).

### Fn::GetAtt
<a name="aws-resource-rds-dbproxy-return-values-fn--getatt"></a>

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [`Fn::GetAtt`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-getatt.html).

####
<a name="aws-resource-rds-dbproxy-return-values-fn--getatt-fn--getatt"></a>

`DBProxyArn`  <a name="DBProxyArn-fn::getatt"></a>
The Amazon Resource Name (ARN) for the proxy.

`Endpoint`  <a name="Endpoint-fn::getatt"></a>
The endpoint that you can use to connect to the DB proxy. You include the endpoint value in the connection string for a database client application.

`VpcId`  <a name="VpcId-fn::getatt"></a>
The VPC ID to associate with the DB proxy.

## Examples
<a name="aws-resource-rds-dbproxy--examples"></a>

### Creating a DB proxy and registering a DB instance
<a name="aws-resource-rds-dbproxy--examples--Creating_a_DB_proxy_and_registering_a_DB_instance"></a>

The following example creates a DB proxy and registers a DB instance.

#### JSON
<a name="aws-resource-rds-dbproxy--examples--Creating_a_DB_proxy_and_registering_a_DB_instance--json"></a>

```
{
    "AWSTemplateFormatVersion": "2010-09-09",
    "Parameters": {
        "ProxyName": {
            "Type": "String",
            "Default": "exampleProxy"
        },
        "InstanceName": {
            "Type": "String",
            "Default": "database-1"
        },
        "BootstrapSecretReaderRoleArn": {
            "Type": "String",
            "Default": "arn:aws:iam::123456789012:role/RDSSecretReaderRoleForDBProxy"
        },
        "BootstrapProxySecretArn": {
            "Type": "String",
            "Default": "arn:aws:secretsmanager:us-west-2:123456789012:secret:MySecretForDBProxy"
        },
        "SubnetIds": {
            "Type": "String",
            "Default": "subnet-01b761b31fb498f20,subnet-012b9a958ef0f9949,subnet-05e8e263052025378"
        }
    },
    "Resources": {
        "TestDBProxy": {
            "Type": "AWS::RDS::DBProxy",
            "Properties": {
                "DebugLogging": true,
                "DBProxyName": {
                    "Ref": "ProxyName"
                },
                "EngineFamily": "MYSQL",
                "IdleClientTimeout": 120,
                "RequireTLS": true,
                "RoleArn": {
                    "Ref": "BootstrapSecretReaderRoleArn"
                },
                "Auth": [
                    {
                        "AuthScheme": "SECRETS",
                        "SecretArn": {
                            "Ref": "BootstrapProxySecretArn"
                        },
                        "IAMAuth": "DISABLED"
                    }
                ],
                "VpcSubnetIds": {
                    "Fn::Split": [
                        ",",
                        {
                            "Ref": "SubnetIds"
                        }
                    ]
                }
            }
        },
        "ProxyTargetGroup": {
            "Type": "AWS::RDS::DBProxyTargetGroup",
            "Properties": {
                "DBProxyName": {
                    "Ref": "TestDBProxy"
                },
                "DBInstanceIdentifiers": [
                    {
                        "Ref": "InstanceName"
                    }
                ],
                "TargetGroupName": "default",
                "ConnectionPoolConfigurationInfo": {
                    "MaxConnectionsPercent": 100,
                    "MaxIdleConnectionsPercent": 50,
                    "ConnectionBorrowTimeout": 120
                }
            }
        }
    }
}
```

#### YAML
<a name="aws-resource-rds-dbproxy--examples--Creating_a_DB_proxy_and_registering_a_DB_instance--yaml"></a>

```
AWSTemplateFormatVersion: 2010-09-09
Parameters:
  ProxyName:
    Type: String
    Default: exampleProxy
  InstanceName:
    Type: String
    Default: database-1
  BootstrapSecretReaderRoleArn:
    Type: String
    Default: arn:aws:iam::123456789012:role/RDSSecretReaderRoleForDBProxy
  BootstrapProxySecretArn:
    Type: String
    Default: arn:aws:secretsmanager:us-west-2:123456789012:secret:MySecretForDBProxy
  SubnetIds:
    Type: String
    Default: subnet-01b761b31fb498f20,subnet-012b9a958ef0f9949,subnet-05e8e263052025378
Resources:
  TestDBProxy:
    Type: AWS::RDS::DBProxy
    Properties:
      DebugLogging: true
      DBProxyName: !Ref ProxyName
      EngineFamily: MYSQL
      IdleClientTimeout: 120
      RequireTLS: true
      RoleArn:
        !Ref BootstrapSecretReaderRoleArn
      Auth:
        - {AuthScheme: SECRETS, SecretArn: !Ref BootstrapProxySecretArn, IAMAuth: DISABLED}
      VpcSubnetIds:
        Fn::Split: [",", !Ref SubnetIds]
  ProxyTargetGroup:
    Type: AWS::RDS::DBProxyTargetGroup
    Properties:
      DBProxyName: !Ref TestDBProxy
      DBInstanceIdentifiers: [!Ref InstanceName]
      TargetGroupName: default
      ConnectionPoolConfigurationInfo:
          MaxConnectionsPercent: 100
          MaxIdleConnectionsPercent: 50
          ConnectionBorrowTimeout: 120
```
