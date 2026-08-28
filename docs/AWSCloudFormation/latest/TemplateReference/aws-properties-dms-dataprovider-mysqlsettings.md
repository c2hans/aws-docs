---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-dms-dataprovider-mysqlsettings.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::DMS::DataProvider MySqlSettings
<a name="aws-properties-dms-dataprovider-mysqlsettings"></a>

Provides information that defines a MySQL endpoint.

## Syntax
<a name="aws-properties-dms-dataprovider-mysqlsettings-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-dms-dataprovider-mysqlsettings-syntax.json"></a>

```
{
  "[CertificateArn](#cfn-dms-dataprovider-mysqlsettings-certificatearn)" : {{String}},
  "[Port](#cfn-dms-dataprovider-mysqlsettings-port)" : {{Integer}},
  "[ServerName](#cfn-dms-dataprovider-mysqlsettings-servername)" : {{String}},
  "[SslMode](#cfn-dms-dataprovider-mysqlsettings-sslmode)" : {{String}}
}
```

### YAML
<a name="aws-properties-dms-dataprovider-mysqlsettings-syntax.yaml"></a>

```
  [CertificateArn](#cfn-dms-dataprovider-mysqlsettings-certificatearn): {{String}}
  [Port](#cfn-dms-dataprovider-mysqlsettings-port): {{Integer}}
  [ServerName](#cfn-dms-dataprovider-mysqlsettings-servername): {{String}}
  [SslMode](#cfn-dms-dataprovider-mysqlsettings-sslmode): {{String}}
```

## Properties
<a name="aws-properties-dms-dataprovider-mysqlsettings-properties"></a>

`CertificateArn`  <a name="cfn-dms-dataprovider-mysqlsettings-certificatearn"></a>
Property description not available.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Port`  <a name="cfn-dms-dataprovider-mysqlsettings-port"></a>
Endpoint TCP port.
*Required*: Yes
*Type*: Integer
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ServerName`  <a name="cfn-dms-dataprovider-mysqlsettings-servername"></a>
The host name of the endpoint database.
For an Amazon RDS MySQL instance, this is the output of [DescribeDBInstances](https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_DescribeDBInstances.html), in the `[Endpoint](https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_Endpoint.html).Address` field.
For an Aurora MySQL instance, this is the output of [DescribeDBClusters](https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_DescribeDBClusters.html), in the `Endpoint` field.
*Required*: Yes
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SslMode`  <a name="cfn-dms-dataprovider-mysqlsettings-sslmode"></a>
Property description not available.
*Required*: Yes
*Type*: String
*Allowed values*: `none | require | verify-ca | verify-full`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
