---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-dms-dataprovider-docdbsettings.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::DMS::DataProvider DocDbSettings
<a name="aws-properties-dms-dataprovider-docdbsettings"></a>

Provides information that defines a DocumentDB endpoint.

## Syntax
<a name="aws-properties-dms-dataprovider-docdbsettings-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-dms-dataprovider-docdbsettings-syntax.json"></a>

```
{
  "[CertificateArn](#cfn-dms-dataprovider-docdbsettings-certificatearn)" : {{String}},
  "[DatabaseName](#cfn-dms-dataprovider-docdbsettings-databasename)" : {{String}},
  "[Port](#cfn-dms-dataprovider-docdbsettings-port)" : {{Integer}},
  "[ServerName](#cfn-dms-dataprovider-docdbsettings-servername)" : {{String}},
  "[SslMode](#cfn-dms-dataprovider-docdbsettings-sslmode)" : {{String}}
}
```

### YAML
<a name="aws-properties-dms-dataprovider-docdbsettings-syntax.yaml"></a>

```
  [CertificateArn](#cfn-dms-dataprovider-docdbsettings-certificatearn): {{String}}
  [DatabaseName](#cfn-dms-dataprovider-docdbsettings-databasename): {{String}}
  [Port](#cfn-dms-dataprovider-docdbsettings-port): {{Integer}}
  [ServerName](#cfn-dms-dataprovider-docdbsettings-servername): {{String}}
  [SslMode](#cfn-dms-dataprovider-docdbsettings-sslmode): {{String}}
```

## Properties
<a name="aws-properties-dms-dataprovider-docdbsettings-properties"></a>

`CertificateArn`  <a name="cfn-dms-dataprovider-docdbsettings-certificatearn"></a>
Property description not available.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`DatabaseName`  <a name="cfn-dms-dataprovider-docdbsettings-databasename"></a>
 The database name on the DocumentDB source endpoint.
*Required*: Yes
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Port`  <a name="cfn-dms-dataprovider-docdbsettings-port"></a>
 The port value for the DocumentDB source endpoint.
*Required*: Yes
*Type*: Integer
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ServerName`  <a name="cfn-dms-dataprovider-docdbsettings-servername"></a>
 The name of the server on the DocumentDB source endpoint.
*Required*: Yes
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SslMode`  <a name="cfn-dms-dataprovider-docdbsettings-sslmode"></a>
Property description not available.
*Required*: No
*Type*: String
*Allowed values*: `none | require | verify-full`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
