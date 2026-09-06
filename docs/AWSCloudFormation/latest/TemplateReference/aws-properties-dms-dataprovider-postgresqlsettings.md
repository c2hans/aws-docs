---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-dms-dataprovider-postgresqlsettings.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::DMS::DataProvider PostgreSqlSettings
<a name="aws-properties-dms-dataprovider-postgresqlsettings"></a>

Provides information that defines a PostgreSQL endpoint.

## Syntax
<a name="aws-properties-dms-dataprovider-postgresqlsettings-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-dms-dataprovider-postgresqlsettings-syntax.json"></a>

```
{
  "[CertificateArn](#cfn-dms-dataprovider-postgresqlsettings-certificatearn)" : {{String}},
  "[DatabaseName](#cfn-dms-dataprovider-postgresqlsettings-databasename)" : {{String}},
  "[Port](#cfn-dms-dataprovider-postgresqlsettings-port)" : {{Integer}},
  "[ServerName](#cfn-dms-dataprovider-postgresqlsettings-servername)" : {{String}},
  "[SslMode](#cfn-dms-dataprovider-postgresqlsettings-sslmode)" : {{String}}
}
```

### YAML
<a name="aws-properties-dms-dataprovider-postgresqlsettings-syntax.yaml"></a>

```
  [CertificateArn](#cfn-dms-dataprovider-postgresqlsettings-certificatearn): {{String}}
  [DatabaseName](#cfn-dms-dataprovider-postgresqlsettings-databasename): {{String}}
  [Port](#cfn-dms-dataprovider-postgresqlsettings-port): {{Integer}}
  [ServerName](#cfn-dms-dataprovider-postgresqlsettings-servername): {{String}}
  [SslMode](#cfn-dms-dataprovider-postgresqlsettings-sslmode): {{String}}
```

## Properties
<a name="aws-properties-dms-dataprovider-postgresqlsettings-properties"></a>

`CertificateArn`  <a name="cfn-dms-dataprovider-postgresqlsettings-certificatearn"></a>
Property description not available.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`DatabaseName`  <a name="cfn-dms-dataprovider-postgresqlsettings-databasename"></a>
Database name for the endpoint.
*Required*: Yes
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Port`  <a name="cfn-dms-dataprovider-postgresqlsettings-port"></a>
Endpoint TCP port. The default is 5432.
*Required*: Yes
*Type*: Integer
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ServerName`  <a name="cfn-dms-dataprovider-postgresqlsettings-servername"></a>
The host name of the endpoint database.
For an Amazon RDS PostgreSQL instance, this is the output of [DescribeDBInstances](https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_DescribeDBInstances.html), in the `[Endpoint](https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_Endpoint.html).Address` field.
For an Aurora PostgreSQL instance, this is the output of [DescribeDBClusters](https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_DescribeDBClusters.html), in the `Endpoint` field.
*Required*: Yes
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SslMode`  <a name="cfn-dms-dataprovider-postgresqlsettings-sslmode"></a>
Property description not available.
*Required*: Yes
*Type*: String
*Allowed values*: `none | require | verify-ca | verify-full`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
