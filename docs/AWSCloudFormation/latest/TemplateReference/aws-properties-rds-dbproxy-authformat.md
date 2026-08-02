---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-rds-dbproxy-authformat.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::RDS::DBProxy AuthFormat
<a name="aws-properties-rds-dbproxy-authformat"></a>

Specifies the details of authentication used by a proxy to log in as a specific database user.

## Syntax
<a name="aws-properties-rds-dbproxy-authformat-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-rds-dbproxy-authformat-syntax.json"></a>

```
{
  "[AuthScheme](#cfn-rds-dbproxy-authformat-authscheme)" : {{String}},
  "[ClientPasswordAuthType](#cfn-rds-dbproxy-authformat-clientpasswordauthtype)" : {{String}},
  "[Description](#cfn-rds-dbproxy-authformat-description)" : {{String}},
  "[IAMAuth](#cfn-rds-dbproxy-authformat-iamauth)" : {{String}},
  "[SecretArn](#cfn-rds-dbproxy-authformat-secretarn)" : {{String}}
}
```

### YAML
<a name="aws-properties-rds-dbproxy-authformat-syntax.yaml"></a>

```
  [AuthScheme](#cfn-rds-dbproxy-authformat-authscheme): {{String}}
  [ClientPasswordAuthType](#cfn-rds-dbproxy-authformat-clientpasswordauthtype): {{String}}
  [Description](#cfn-rds-dbproxy-authformat-description): {{String}}
  [IAMAuth](#cfn-rds-dbproxy-authformat-iamauth): {{String}}
  [SecretArn](#cfn-rds-dbproxy-authformat-secretarn): {{String}}
```

## Properties
<a name="aws-properties-rds-dbproxy-authformat-properties"></a>

`AuthScheme`  <a name="cfn-rds-dbproxy-authformat-authscheme"></a>
The type of authentication that the proxy uses for connections from the proxy to the underlying database.
*Required*: No
*Type*: String
*Allowed values*: `SECRETS`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ClientPasswordAuthType`  <a name="cfn-rds-dbproxy-authformat-clientpasswordauthtype"></a>
Specifies the details of authentication used by a proxy to log in as a specific database user.
*Required*: No
*Type*: String
*Allowed values*: `MYSQL_NATIVE_PASSWORD | MYSQL_CACHING_SHA2_PASSWORD | POSTGRES_SCRAM_SHA_256 | POSTGRES_MD5 | SQL_SERVER_AUTHENTICATION`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Description`  <a name="cfn-rds-dbproxy-authformat-description"></a>
A user-specified description about the authentication used by a proxy to log in as a specific database user.
*Required*: No
*Type*: String
*Pattern*: `.*`
*Minimum*: `1`
*Maximum*: `1000`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`IAMAuth`  <a name="cfn-rds-dbproxy-authformat-iamauth"></a>
A value that indicates whether to require or disallow AWS Identity and Access Management (IAM) authentication for connections to the proxy. The `ENABLED` value is valid only for proxies with RDS for Microsoft SQL Server.
*Required*: No
*Type*: String
*Allowed values*: `DISABLED | REQUIRED | ENABLED`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SecretArn`  <a name="cfn-rds-dbproxy-authformat-secretarn"></a>
The Amazon Resource Name (ARN) representing the secret that the proxy uses to authenticate to the RDS DB instance or Aurora DB cluster. These secrets are stored within Amazon Secrets Manager.
*Required*: No
*Type*: String
*Minimum*: `20`
*Maximum*: `2048`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Examples
<a name="aws-properties-rds-dbproxy-authformat--examples"></a>

The following example specifies authentication details for a proxy.

### Authentication details
<a name="aws-properties-rds-dbproxy-authformat--examples--Authentication_details"></a>

#### JSON
<a name="aws-properties-rds-dbproxy-authformat--examples--Authentication_details--json"></a>

```
"ProcessorFeatures":[
   {
      "AuthScheme": "SECRETS",
      "ClientPasswordAuthType": "MYSQL_NATIVE_PASSWORD",
      "Description": "Proxy authentication for MySQL",
      "IAMAuth": "DISABLED",
      "SecretArn": "arn:aws:secretsmanager:us-west-2:111122223333:secret:aes128-1a2b3c"
   }
]
```

#### YAML
<a name="aws-properties-rds-dbproxy-authformat--examples--Authentication_details--yaml"></a>

```
Auth:
  AuthScheme: SECRETS
  ClientPasswordAuthType: MYSQL_NATIVE_PASSWORD
  Description: Proxy authentication for MySQL
  IAMAuth: DISABLED
  SecretArn: arn:aws:secretsmanager:us-west-2:111122223333:secret:aes128-1a2b3c
```
