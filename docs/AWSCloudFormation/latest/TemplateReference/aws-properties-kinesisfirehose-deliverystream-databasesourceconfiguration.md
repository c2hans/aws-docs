---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-kinesisfirehose-deliverystream-databasesourceconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::KinesisFirehose::DeliveryStream DatabaseSourceConfiguration
<a name="aws-properties-kinesisfirehose-deliverystream-databasesourceconfiguration"></a>

 The top level object for configuring streams with database as a source.

Amazon Data Firehose is in preview release and is subject to change.

## Syntax
<a name="aws-properties-kinesisfirehose-deliverystream-databasesourceconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-kinesisfirehose-deliverystream-databasesourceconfiguration-syntax.json"></a>

```
{
  "[Columns](#cfn-kinesisfirehose-deliverystream-databasesourceconfiguration-columns)" : {{DatabaseColumns}},
  "[Databases](#cfn-kinesisfirehose-deliverystream-databasesourceconfiguration-databases)" : {{Databases}},
  "[DatabaseSourceAuthenticationConfiguration](#cfn-kinesisfirehose-deliverystream-databasesourceconfiguration-databasesourceauthenticationconfiguration)" : {{DatabaseSourceAuthenticationConfiguration}},
  "[DatabaseSourceVPCConfiguration](#cfn-kinesisfirehose-deliverystream-databasesourceconfiguration-databasesourcevpcconfiguration)" : {{DatabaseSourceVPCConfiguration}},
  "[Digest](#cfn-kinesisfirehose-deliverystream-databasesourceconfiguration-digest)" : {{String}},
  "[Endpoint](#cfn-kinesisfirehose-deliverystream-databasesourceconfiguration-endpoint)" : {{String}},
  "[Port](#cfn-kinesisfirehose-deliverystream-databasesourceconfiguration-port)" : {{Integer}},
  "[PublicCertificate](#cfn-kinesisfirehose-deliverystream-databasesourceconfiguration-publiccertificate)" : {{String}},
  "[SnapshotWatermarkTable](#cfn-kinesisfirehose-deliverystream-databasesourceconfiguration-snapshotwatermarktable)" : {{String}},
  "[SSLMode](#cfn-kinesisfirehose-deliverystream-databasesourceconfiguration-sslmode)" : {{String}},
  "[SurrogateKeys](#cfn-kinesisfirehose-deliverystream-databasesourceconfiguration-surrogatekeys)" : {{[ String, ... ]}},
  "[Tables](#cfn-kinesisfirehose-deliverystream-databasesourceconfiguration-tables)" : {{DatabaseTables}},
  "[Type](#cfn-kinesisfirehose-deliverystream-databasesourceconfiguration-type)" : {{String}}
}
```

### YAML
<a name="aws-properties-kinesisfirehose-deliverystream-databasesourceconfiguration-syntax.yaml"></a>

```
  [Columns](#cfn-kinesisfirehose-deliverystream-databasesourceconfiguration-columns): {{
    DatabaseColumns}}
  [Databases](#cfn-kinesisfirehose-deliverystream-databasesourceconfiguration-databases): {{
    Databases}}
  [DatabaseSourceAuthenticationConfiguration](#cfn-kinesisfirehose-deliverystream-databasesourceconfiguration-databasesourceauthenticationconfiguration): {{
    DatabaseSourceAuthenticationConfiguration}}
  [DatabaseSourceVPCConfiguration](#cfn-kinesisfirehose-deliverystream-databasesourceconfiguration-databasesourcevpcconfiguration): {{
    DatabaseSourceVPCConfiguration}}
  [Digest](#cfn-kinesisfirehose-deliverystream-databasesourceconfiguration-digest): {{String}}
  [Endpoint](#cfn-kinesisfirehose-deliverystream-databasesourceconfiguration-endpoint): {{String}}
  [Port](#cfn-kinesisfirehose-deliverystream-databasesourceconfiguration-port): {{Integer}}
  [PublicCertificate](#cfn-kinesisfirehose-deliverystream-databasesourceconfiguration-publiccertificate): {{String}}
  [SnapshotWatermarkTable](#cfn-kinesisfirehose-deliverystream-databasesourceconfiguration-snapshotwatermarktable): {{String}}
  [SSLMode](#cfn-kinesisfirehose-deliverystream-databasesourceconfiguration-sslmode): {{String}}
  [SurrogateKeys](#cfn-kinesisfirehose-deliverystream-databasesourceconfiguration-surrogatekeys): {{
    - String}}
  [Tables](#cfn-kinesisfirehose-deliverystream-databasesourceconfiguration-tables): {{
    DatabaseTables}}
  [Type](#cfn-kinesisfirehose-deliverystream-databasesourceconfiguration-type): {{String}}
```

## Properties
<a name="aws-properties-kinesisfirehose-deliverystream-databasesourceconfiguration-properties"></a>

`Columns`  <a name="cfn-kinesisfirehose-deliverystream-databasesourceconfiguration-columns"></a>
 The list of column patterns in source database endpoint for Firehose to read from.
Amazon Data Firehose is in preview release and is subject to change.
*Required*: No
*Type*: [DatabaseColumns](aws-properties-kinesisfirehose-deliverystream-databasecolumns.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Databases`  <a name="cfn-kinesisfirehose-deliverystream-databasesourceconfiguration-databases"></a>
 The list of database patterns in source database endpoint for Firehose to read from.
Amazon Data Firehose is in preview release and is subject to change.
*Required*: Yes
*Type*: [Databases](aws-properties-kinesisfirehose-deliverystream-databases.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`DatabaseSourceAuthenticationConfiguration`  <a name="cfn-kinesisfirehose-deliverystream-databasesourceconfiguration-databasesourceauthenticationconfiguration"></a>
 The structure to configure the authentication methods for Firehose to connect to source database endpoint.
Amazon Data Firehose is in preview release and is subject to change.
*Required*: Yes
*Type*: [DatabaseSourceAuthenticationConfiguration](aws-properties-kinesisfirehose-deliverystream-databasesourceauthenticationconfiguration.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`DatabaseSourceVPCConfiguration`  <a name="cfn-kinesisfirehose-deliverystream-databasesourceconfiguration-databasesourcevpcconfiguration"></a>
 The details of the VPC Endpoint Service which Firehose uses to create a PrivateLink to the database.
Amazon Data Firehose is in preview release and is subject to change.
*Required*: Yes
*Type*: [DatabaseSourceVPCConfiguration](aws-properties-kinesisfirehose-deliverystream-databasesourcevpcconfiguration.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Digest`  <a name="cfn-kinesisfirehose-deliverystream-databasesourceconfiguration-digest"></a>
Property description not available.
*Required*: No
*Type*: String
*Pattern*: `.*`
*Minimum*: `1`
*Maximum*: `512`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Endpoint`  <a name="cfn-kinesisfirehose-deliverystream-databasesourceconfiguration-endpoint"></a>
 The endpoint of the database server.
Amazon Data Firehose is in preview release and is subject to change.
*Required*: Yes
*Type*: String
*Pattern*: `^(?!\s*$).+`
*Minimum*: `1`
*Maximum*: `255`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Port`  <a name="cfn-kinesisfirehose-deliverystream-databasesourceconfiguration-port"></a>
The port of the database. This can be one of the following values.
+ 3306 for MySQL database type
+ 5432 for PostgreSQL database type
Amazon Data Firehose is in preview release and is subject to change.
*Required*: Yes
*Type*: Integer
*Minimum*: `0`
*Maximum*: `65535`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`PublicCertificate`  <a name="cfn-kinesisfirehose-deliverystream-databasesourceconfiguration-publiccertificate"></a>
Property description not available.
*Required*: No
*Type*: String
*Pattern*: `.*`
*Minimum*: `1`
*Maximum*: `4096`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`SnapshotWatermarkTable`  <a name="cfn-kinesisfirehose-deliverystream-databasesourceconfiguration-snapshotwatermarktable"></a>
 The fully qualified name of the table in source database endpoint that Firehose uses to track snapshot progress.
Amazon Data Firehose is in preview release and is subject to change.
*Required*: Yes
*Type*: String
*Pattern*: `[\u0001-\uFFFF]*`
*Minimum*: `1`
*Maximum*: `129`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`SSLMode`  <a name="cfn-kinesisfirehose-deliverystream-databasesourceconfiguration-sslmode"></a>
 The mode to enable or disable SSL when Firehose connects to the database endpoint.
Amazon Data Firehose is in preview release and is subject to change.
*Required*: No
*Type*: String
*Allowed values*: `Disabled | Enabled`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`SurrogateKeys`  <a name="cfn-kinesisfirehose-deliverystream-databasesourceconfiguration-surrogatekeys"></a>
 The optional list of table and column names used as unique key columns when taking snapshot if the tables don’t have primary keys configured.
Amazon Data Firehose is in preview release and is subject to change.
*Required*: No
*Type*: Array of String
*Minimum*: `1`
*Maximum*: `1024`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Tables`  <a name="cfn-kinesisfirehose-deliverystream-databasesourceconfiguration-tables"></a>
 The list of table patterns in source database endpoint for Firehose to read from.
Amazon Data Firehose is in preview release and is subject to change.
*Required*: Yes
*Type*: [DatabaseTables](aws-properties-kinesisfirehose-deliverystream-databasetables.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Type`  <a name="cfn-kinesisfirehose-deliverystream-databasesourceconfiguration-type"></a>
The type of database engine. This can be one of the following values.
+ MySQL
+ PostgreSQL
Amazon Data Firehose is in preview release and is subject to change.
*Required*: Yes
*Type*: String
*Allowed values*: `MySQL | PostgreSQL`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)
