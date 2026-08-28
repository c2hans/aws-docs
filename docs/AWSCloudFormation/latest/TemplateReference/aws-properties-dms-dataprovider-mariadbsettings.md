---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-dms-dataprovider-mariadbsettings.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::DMS::DataProvider MariaDbSettings
<a name="aws-properties-dms-dataprovider-mariadbsettings"></a>

<a name="aws-properties-dms-dataprovider-mariadbsettings-description"></a>The `MariaDbSettings` property type specifies Property description not available. for an [AWS::DMS::DataProvider](aws-resource-dms-dataprovider.md).

## Syntax
<a name="aws-properties-dms-dataprovider-mariadbsettings-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-dms-dataprovider-mariadbsettings-syntax.json"></a>

```
{
  "[CertificateArn](#cfn-dms-dataprovider-mariadbsettings-certificatearn)" : {{String}},
  "[Port](#cfn-dms-dataprovider-mariadbsettings-port)" : {{Integer}},
  "[ServerName](#cfn-dms-dataprovider-mariadbsettings-servername)" : {{String}},
  "[SslMode](#cfn-dms-dataprovider-mariadbsettings-sslmode)" : {{String}}
}
```

### YAML
<a name="aws-properties-dms-dataprovider-mariadbsettings-syntax.yaml"></a>

```
  [CertificateArn](#cfn-dms-dataprovider-mariadbsettings-certificatearn): {{String}}
  [Port](#cfn-dms-dataprovider-mariadbsettings-port): {{Integer}}
  [ServerName](#cfn-dms-dataprovider-mariadbsettings-servername): {{String}}
  [SslMode](#cfn-dms-dataprovider-mariadbsettings-sslmode): {{String}}
```

## Properties
<a name="aws-properties-dms-dataprovider-mariadbsettings-properties"></a>

`CertificateArn`  <a name="cfn-dms-dataprovider-mariadbsettings-certificatearn"></a>
Property description not available.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Port`  <a name="cfn-dms-dataprovider-mariadbsettings-port"></a>
Property description not available.
*Required*: Yes
*Type*: Integer
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ServerName`  <a name="cfn-dms-dataprovider-mariadbsettings-servername"></a>
Property description not available.
*Required*: Yes
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SslMode`  <a name="cfn-dms-dataprovider-mariadbsettings-sslmode"></a>
Property description not available.
*Required*: Yes
*Type*: String
*Allowed values*: `none | require | verify-ca | verify-full`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
