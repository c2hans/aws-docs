---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-dms-dataprovider-microsoftsqlserversettings.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::DMS::DataProvider MicrosoftSqlServerSettings
<a name="aws-properties-dms-dataprovider-microsoftsqlserversettings"></a>

Provides information that defines a Microsoft SQL Server endpoint.

## Syntax
<a name="aws-properties-dms-dataprovider-microsoftsqlserversettings-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-dms-dataprovider-microsoftsqlserversettings-syntax.json"></a>

```
{
  "[CertificateArn](#cfn-dms-dataprovider-microsoftsqlserversettings-certificatearn)" : {{String}},
  "[DatabaseName](#cfn-dms-dataprovider-microsoftsqlserversettings-databasename)" : {{String}},
  "[Port](#cfn-dms-dataprovider-microsoftsqlserversettings-port)" : {{Integer}},
  "[S3AccessRoleArn](#cfn-dms-dataprovider-microsoftsqlserversettings-s3accessrolearn)" : {{String}},
  "[S3Path](#cfn-dms-dataprovider-microsoftsqlserversettings-s3path)" : {{String}},
  "[ServerName](#cfn-dms-dataprovider-microsoftsqlserversettings-servername)" : {{String}},
  "[SslMode](#cfn-dms-dataprovider-microsoftsqlserversettings-sslmode)" : {{String}}
}
```

### YAML
<a name="aws-properties-dms-dataprovider-microsoftsqlserversettings-syntax.yaml"></a>

```
  [CertificateArn](#cfn-dms-dataprovider-microsoftsqlserversettings-certificatearn): {{String}}
  [DatabaseName](#cfn-dms-dataprovider-microsoftsqlserversettings-databasename): {{String}}
  [Port](#cfn-dms-dataprovider-microsoftsqlserversettings-port): {{Integer}}
  [S3AccessRoleArn](#cfn-dms-dataprovider-microsoftsqlserversettings-s3accessrolearn): {{String}}
  [S3Path](#cfn-dms-dataprovider-microsoftsqlserversettings-s3path): {{String}}
  [ServerName](#cfn-dms-dataprovider-microsoftsqlserversettings-servername): {{String}}
  [SslMode](#cfn-dms-dataprovider-microsoftsqlserversettings-sslmode): {{String}}
```

## Properties
<a name="aws-properties-dms-dataprovider-microsoftsqlserversettings-properties"></a>

`CertificateArn`  <a name="cfn-dms-dataprovider-microsoftsqlserversettings-certificatearn"></a>
Property description not available.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`DatabaseName`  <a name="cfn-dms-dataprovider-microsoftsqlserversettings-databasename"></a>
Database name for the endpoint.
*Required*: Yes
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Port`  <a name="cfn-dms-dataprovider-microsoftsqlserversettings-port"></a>
Endpoint TCP port.
*Required*: Yes
*Type*: Integer
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`S3AccessRoleArn`  <a name="cfn-dms-dataprovider-microsoftsqlserversettings-s3accessrolearn"></a>
Property description not available.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`S3Path`  <a name="cfn-dms-dataprovider-microsoftsqlserversettings-s3path"></a>
Property description not available.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ServerName`  <a name="cfn-dms-dataprovider-microsoftsqlserversettings-servername"></a>
Fully qualified domain name of the endpoint. For an Amazon RDS SQL Server instance, this is the output of [DescribeDBInstances](https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_DescribeDBInstances.html), in the `[Endpoint](https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_Endpoint.html).Address` field.
*Required*: Yes
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SslMode`  <a name="cfn-dms-dataprovider-microsoftsqlserversettings-sslmode"></a>
Property description not available.
*Required*: Yes
*Type*: String
*Allowed values*: `none | require | verify-ca | verify-full`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
