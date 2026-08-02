---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-dms-migrationproject-dataproviderdescriptor.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::DMS::MigrationProject DataProviderDescriptor
<a name="aws-properties-dms-migrationproject-dataproviderdescriptor"></a>

Information about a data provider.

## Syntax
<a name="aws-properties-dms-migrationproject-dataproviderdescriptor-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-dms-migrationproject-dataproviderdescriptor-syntax.json"></a>

```
{
  "[DataProviderArn](#cfn-dms-migrationproject-dataproviderdescriptor-dataproviderarn)" : {{String}},
  "[DataProviderIdentifier](#cfn-dms-migrationproject-dataproviderdescriptor-dataprovideridentifier)" : {{String}},
  "[DataProviderName](#cfn-dms-migrationproject-dataproviderdescriptor-dataprovidername)" : {{String}},
  "[SecretsManagerAccessRoleArn](#cfn-dms-migrationproject-dataproviderdescriptor-secretsmanageraccessrolearn)" : {{String}},
  "[SecretsManagerSecretId](#cfn-dms-migrationproject-dataproviderdescriptor-secretsmanagersecretid)" : {{String}}
}
```

### YAML
<a name="aws-properties-dms-migrationproject-dataproviderdescriptor-syntax.yaml"></a>

```
  [DataProviderArn](#cfn-dms-migrationproject-dataproviderdescriptor-dataproviderarn): {{String}}
  [DataProviderIdentifier](#cfn-dms-migrationproject-dataproviderdescriptor-dataprovideridentifier): {{String}}
  [DataProviderName](#cfn-dms-migrationproject-dataproviderdescriptor-dataprovidername): {{String}}
  [SecretsManagerAccessRoleArn](#cfn-dms-migrationproject-dataproviderdescriptor-secretsmanageraccessrolearn): {{String}}
  [SecretsManagerSecretId](#cfn-dms-migrationproject-dataproviderdescriptor-secretsmanagersecretid): {{String}}
```

## Properties
<a name="aws-properties-dms-migrationproject-dataproviderdescriptor-properties"></a>

`DataProviderArn`  <a name="cfn-dms-migrationproject-dataproviderdescriptor-dataproviderarn"></a>
The Amazon Resource Name (ARN) of the data provider.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`DataProviderIdentifier`  <a name="cfn-dms-migrationproject-dataproviderdescriptor-dataprovideridentifier"></a>
Property description not available.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`DataProviderName`  <a name="cfn-dms-migrationproject-dataproviderdescriptor-dataprovidername"></a>
The user-friendly name of the data provider.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SecretsManagerAccessRoleArn`  <a name="cfn-dms-migrationproject-dataproviderdescriptor-secretsmanageraccessrolearn"></a>
The ARN of the role used to access AWS Secrets Manager.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SecretsManagerSecretId`  <a name="cfn-dms-migrationproject-dataproviderdescriptor-secretsmanagersecretid"></a>
The identifier of the AWS Secrets Manager Secret used to store access credentials for the data provider.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
