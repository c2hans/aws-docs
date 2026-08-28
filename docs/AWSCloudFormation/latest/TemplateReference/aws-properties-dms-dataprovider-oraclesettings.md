---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-dms-dataprovider-oraclesettings.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::DMS::DataProvider OracleSettings
<a name="aws-properties-dms-dataprovider-oraclesettings"></a>

Provides information that defines an Oracle endpoint.

## Syntax
<a name="aws-properties-dms-dataprovider-oraclesettings-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-dms-dataprovider-oraclesettings-syntax.json"></a>

```
{
  "[AsmServer](#cfn-dms-dataprovider-oraclesettings-asmserver)" : {{String}},
  "[CertificateArn](#cfn-dms-dataprovider-oraclesettings-certificatearn)" : {{String}},
  "[DatabaseName](#cfn-dms-dataprovider-oraclesettings-databasename)" : {{String}},
  "[Port](#cfn-dms-dataprovider-oraclesettings-port)" : {{Integer}},
  "[SecretsManagerOracleAsmAccessRoleArn](#cfn-dms-dataprovider-oraclesettings-secretsmanageroracleasmaccessrolearn)" : {{String}},
  "[SecretsManagerOracleAsmSecretId](#cfn-dms-dataprovider-oraclesettings-secretsmanageroracleasmsecretid)" : {{String}},
  "[SecretsManagerSecurityDbEncryptionAccessRoleArn](#cfn-dms-dataprovider-oraclesettings-secretsmanagersecuritydbencryptionaccessrolearn)" : {{String}},
  "[SecretsManagerSecurityDbEncryptionSecretId](#cfn-dms-dataprovider-oraclesettings-secretsmanagersecuritydbencryptionsecretid)" : {{String}},
  "[ServerName](#cfn-dms-dataprovider-oraclesettings-servername)" : {{String}},
  "[SslMode](#cfn-dms-dataprovider-oraclesettings-sslmode)" : {{String}}
}
```

### YAML
<a name="aws-properties-dms-dataprovider-oraclesettings-syntax.yaml"></a>

```
  [AsmServer](#cfn-dms-dataprovider-oraclesettings-asmserver): {{String}}
  [CertificateArn](#cfn-dms-dataprovider-oraclesettings-certificatearn): {{String}}
  [DatabaseName](#cfn-dms-dataprovider-oraclesettings-databasename): {{String}}
  [Port](#cfn-dms-dataprovider-oraclesettings-port): {{Integer}}
  [SecretsManagerOracleAsmAccessRoleArn](#cfn-dms-dataprovider-oraclesettings-secretsmanageroracleasmaccessrolearn): {{String}}
  [SecretsManagerOracleAsmSecretId](#cfn-dms-dataprovider-oraclesettings-secretsmanageroracleasmsecretid): {{String}}
  [SecretsManagerSecurityDbEncryptionAccessRoleArn](#cfn-dms-dataprovider-oraclesettings-secretsmanagersecuritydbencryptionaccessrolearn): {{String}}
  [SecretsManagerSecurityDbEncryptionSecretId](#cfn-dms-dataprovider-oraclesettings-secretsmanagersecuritydbencryptionsecretid): {{String}}
  [ServerName](#cfn-dms-dataprovider-oraclesettings-servername): {{String}}
  [SslMode](#cfn-dms-dataprovider-oraclesettings-sslmode): {{String}}
```

## Properties
<a name="aws-properties-dms-dataprovider-oraclesettings-properties"></a>

`AsmServer`  <a name="cfn-dms-dataprovider-oraclesettings-asmserver"></a>
For an Oracle source endpoint, your ASM server address. You can set this value from the `asm_server` value. You set `asm_server` as part of the extra connection attribute string to access an Oracle server with Binary Reader that uses ASM. For more information, see [Configuration for change data capture (CDC) on an Oracle source database](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Source.Oracle.html#dms/latest/userguide/CHAP_Source.Oracle.html#CHAP_Source.Oracle.CDC.Configuration).
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`CertificateArn`  <a name="cfn-dms-dataprovider-oraclesettings-certificatearn"></a>
Property description not available.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`DatabaseName`  <a name="cfn-dms-dataprovider-oraclesettings-databasename"></a>
Database name for the endpoint.
*Required*: Yes
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Port`  <a name="cfn-dms-dataprovider-oraclesettings-port"></a>
Endpoint TCP port.
*Required*: Yes
*Type*: Integer
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SecretsManagerOracleAsmAccessRoleArn`  <a name="cfn-dms-dataprovider-oraclesettings-secretsmanageroracleasmaccessrolearn"></a>
Required only if your Oracle endpoint uses Automatic Storage Management (ASM). The full ARN of the IAM role that specifies AWS DMS as the trusted entity and grants the required permissions to access the `SecretsManagerOracleAsmSecret`. This `SecretsManagerOracleAsmSecret` has the secret value that allows access to the Oracle ASM of the endpoint.
You can specify one of two sets of values for these permissions. You can specify the values for this setting and `SecretsManagerOracleAsmSecretId`. Or you can specify clear-text values for `AsmUser`, `AsmPassword`, and `AsmServerName`. You can't specify both. For more information on creating this `SecretsManagerOracleAsmSecret` and the `SecretsManagerOracleAsmAccessRoleArn` and `SecretsManagerOracleAsmSecretId` required to access it, see [Using secrets to access AWS Database Migration Service resources](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Security.html#security-iam-secretsmanager) in the *AWS Database Migration Service User Guide*.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SecretsManagerOracleAsmSecretId`  <a name="cfn-dms-dataprovider-oraclesettings-secretsmanageroracleasmsecretid"></a>
Required only if your Oracle endpoint uses Automatic Storage Management (ASM). The full ARN, partial ARN, or friendly name of the `SecretsManagerOracleAsmSecret` that contains the Oracle ASM connection details for the Oracle endpoint.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SecretsManagerSecurityDbEncryptionAccessRoleArn`  <a name="cfn-dms-dataprovider-oraclesettings-secretsmanagersecuritydbencryptionaccessrolearn"></a>
Property description not available.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SecretsManagerSecurityDbEncryptionSecretId`  <a name="cfn-dms-dataprovider-oraclesettings-secretsmanagersecuritydbencryptionsecretid"></a>
Property description not available.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ServerName`  <a name="cfn-dms-dataprovider-oraclesettings-servername"></a>
Fully qualified domain name of the endpoint.
For an Amazon RDS Oracle instance, this is the output of [DescribeDBInstances](https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_DescribeDBInstances.html), in the `[Endpoint](https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_Endpoint.html).Address` field.
*Required*: Yes
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SslMode`  <a name="cfn-dms-dataprovider-oraclesettings-sslmode"></a>
Property description not available.
*Required*: Yes
*Type*: String
*Allowed values*: `none | require | verify-ca | verify-full`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
