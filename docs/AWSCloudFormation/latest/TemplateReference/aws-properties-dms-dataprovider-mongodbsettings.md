---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-dms-dataprovider-mongodbsettings.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::DMS::DataProvider MongoDbSettings
<a name="aws-properties-dms-dataprovider-mongodbsettings"></a>

Provides information that defines a MongoDB endpoint.

## Syntax
<a name="aws-properties-dms-dataprovider-mongodbsettings-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-dms-dataprovider-mongodbsettings-syntax.json"></a>

```
{
  "[AuthMechanism](#cfn-dms-dataprovider-mongodbsettings-authmechanism)" : {{String}},
  "[AuthSource](#cfn-dms-dataprovider-mongodbsettings-authsource)" : {{String}},
  "[AuthType](#cfn-dms-dataprovider-mongodbsettings-authtype)" : {{String}},
  "[CertificateArn](#cfn-dms-dataprovider-mongodbsettings-certificatearn)" : {{String}},
  "[DatabaseName](#cfn-dms-dataprovider-mongodbsettings-databasename)" : {{String}},
  "[Port](#cfn-dms-dataprovider-mongodbsettings-port)" : {{Integer}},
  "[ServerName](#cfn-dms-dataprovider-mongodbsettings-servername)" : {{String}},
  "[SslMode](#cfn-dms-dataprovider-mongodbsettings-sslmode)" : {{String}}
}
```

### YAML
<a name="aws-properties-dms-dataprovider-mongodbsettings-syntax.yaml"></a>

```
  [AuthMechanism](#cfn-dms-dataprovider-mongodbsettings-authmechanism): {{String}}
  [AuthSource](#cfn-dms-dataprovider-mongodbsettings-authsource): {{String}}
  [AuthType](#cfn-dms-dataprovider-mongodbsettings-authtype): {{String}}
  [CertificateArn](#cfn-dms-dataprovider-mongodbsettings-certificatearn): {{String}}
  [DatabaseName](#cfn-dms-dataprovider-mongodbsettings-databasename): {{String}}
  [Port](#cfn-dms-dataprovider-mongodbsettings-port): {{Integer}}
  [ServerName](#cfn-dms-dataprovider-mongodbsettings-servername): {{String}}
  [SslMode](#cfn-dms-dataprovider-mongodbsettings-sslmode): {{String}}
```

## Properties
<a name="aws-properties-dms-dataprovider-mongodbsettings-properties"></a>

`AuthMechanism`  <a name="cfn-dms-dataprovider-mongodbsettings-authmechanism"></a>
 The authentication mechanism you use to access the MongoDB source endpoint.
For the default value, in MongoDB version 2.x, `"default"` is `"mongodb_cr"`. For MongoDB version 3.x or later, `"default"` is `"scram_sha_1"`. This setting isn't used when `AuthType` is set to `"no"`.
*Required*: No
*Type*: String
*Allowed values*: `default | mongodb_cr | scram_sha_1`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`AuthSource`  <a name="cfn-dms-dataprovider-mongodbsettings-authsource"></a>
 The MongoDB database name. This setting isn't used when `AuthType` is set to `"no"`.
The default is `"admin"`.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`AuthType`  <a name="cfn-dms-dataprovider-mongodbsettings-authtype"></a>
 The authentication type you use to access the MongoDB source endpoint.
When when set to `"no"`, user name and password parameters are not used and can be empty.
*Required*: No
*Type*: String
*Allowed values*: `no | password`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`CertificateArn`  <a name="cfn-dms-dataprovider-mongodbsettings-certificatearn"></a>
Property description not available.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`DatabaseName`  <a name="cfn-dms-dataprovider-mongodbsettings-databasename"></a>
 The database name on the MongoDB source endpoint.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Port`  <a name="cfn-dms-dataprovider-mongodbsettings-port"></a>
 The port value for the MongoDB source endpoint.
*Required*: Yes
*Type*: Integer
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ServerName`  <a name="cfn-dms-dataprovider-mongodbsettings-servername"></a>
 The name of the server on the MongoDB source endpoint. For MongoDB Atlas, provide the server name for any of the servers in the replication set.
*Required*: Yes
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SslMode`  <a name="cfn-dms-dataprovider-mongodbsettings-sslmode"></a>
Property description not available.
*Required*: No
*Type*: String
*Allowed values*: `none | require | verify-full`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
