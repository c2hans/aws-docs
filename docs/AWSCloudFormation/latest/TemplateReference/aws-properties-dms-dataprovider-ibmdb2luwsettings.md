---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-dms-dataprovider-ibmdb2luwsettings.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::DMS::DataProvider IbmDb2LuwSettings
<a name="aws-properties-dms-dataprovider-ibmdb2luwsettings"></a>

<a name="aws-properties-dms-dataprovider-ibmdb2luwsettings-description"></a>The `IbmDb2LuwSettings` property type specifies Property description not available. for an [AWS::DMS::DataProvider](aws-resource-dms-dataprovider.md).

## Syntax
<a name="aws-properties-dms-dataprovider-ibmdb2luwsettings-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-dms-dataprovider-ibmdb2luwsettings-syntax.json"></a>

```
{
  "[CertificateArn](#cfn-dms-dataprovider-ibmdb2luwsettings-certificatearn)" : {{String}},
  "[DatabaseName](#cfn-dms-dataprovider-ibmdb2luwsettings-databasename)" : {{String}},
  "[Port](#cfn-dms-dataprovider-ibmdb2luwsettings-port)" : {{Integer}},
  "[ServerName](#cfn-dms-dataprovider-ibmdb2luwsettings-servername)" : {{String}},
  "[SslMode](#cfn-dms-dataprovider-ibmdb2luwsettings-sslmode)" : {{String}}
}
```

### YAML
<a name="aws-properties-dms-dataprovider-ibmdb2luwsettings-syntax.yaml"></a>

```
  [CertificateArn](#cfn-dms-dataprovider-ibmdb2luwsettings-certificatearn): {{String}}
  [DatabaseName](#cfn-dms-dataprovider-ibmdb2luwsettings-databasename): {{String}}
  [Port](#cfn-dms-dataprovider-ibmdb2luwsettings-port): {{Integer}}
  [ServerName](#cfn-dms-dataprovider-ibmdb2luwsettings-servername): {{String}}
  [SslMode](#cfn-dms-dataprovider-ibmdb2luwsettings-sslmode): {{String}}
```

## Properties
<a name="aws-properties-dms-dataprovider-ibmdb2luwsettings-properties"></a>

`CertificateArn`  <a name="cfn-dms-dataprovider-ibmdb2luwsettings-certificatearn"></a>
Property description not available.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`DatabaseName`  <a name="cfn-dms-dataprovider-ibmdb2luwsettings-databasename"></a>
Property description not available.
*Required*: Yes
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Port`  <a name="cfn-dms-dataprovider-ibmdb2luwsettings-port"></a>
Property description not available.
*Required*: Yes
*Type*: Integer
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ServerName`  <a name="cfn-dms-dataprovider-ibmdb2luwsettings-servername"></a>
Property description not available.
*Required*: Yes
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SslMode`  <a name="cfn-dms-dataprovider-ibmdb2luwsettings-sslmode"></a>
Property description not available.
*Required*: Yes
*Type*: String
*Allowed values*: `none | verify-ca`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
