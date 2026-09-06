---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-glue-catalog-datalakeaccessproperties.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Glue::Catalog DataLakeAccessProperties
<a name="aws-properties-glue-catalog-datalakeaccessproperties"></a>

Input properties to configure data lake access for your catalog resource in the AWS Glue Data Catalog.

## Syntax
<a name="aws-properties-glue-catalog-datalakeaccessproperties-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-glue-catalog-datalakeaccessproperties-syntax.json"></a>

```
{
  "[AllowFullTableExternalDataAccess](#cfn-glue-catalog-datalakeaccessproperties-allowfulltableexternaldataaccess)" : {{String}},
  "[CatalogType](#cfn-glue-catalog-datalakeaccessproperties-catalogtype)" : {{String}},
  "[DataLakeAccess](#cfn-glue-catalog-datalakeaccessproperties-datalakeaccess)" : {{Boolean}},
  "[DataTransferRole](#cfn-glue-catalog-datalakeaccessproperties-datatransferrole)" : {{String}},
  "[KmsKey](#cfn-glue-catalog-datalakeaccessproperties-kmskey)" : {{String}},
  "[ManagedWorkgroupName](#cfn-glue-catalog-datalakeaccessproperties-managedworkgroupname)" : {{String}},
  "[ManagedWorkgroupStatus](#cfn-glue-catalog-datalakeaccessproperties-managedworkgroupstatus)" : {{String}},
  "[RedshiftDatabaseName](#cfn-glue-catalog-datalakeaccessproperties-redshiftdatabasename)" : {{String}}
}
```

### YAML
<a name="aws-properties-glue-catalog-datalakeaccessproperties-syntax.yaml"></a>

```
  [AllowFullTableExternalDataAccess](#cfn-glue-catalog-datalakeaccessproperties-allowfulltableexternaldataaccess): {{String}}
  [CatalogType](#cfn-glue-catalog-datalakeaccessproperties-catalogtype): {{String}}
  [DataLakeAccess](#cfn-glue-catalog-datalakeaccessproperties-datalakeaccess): {{Boolean}}
  [DataTransferRole](#cfn-glue-catalog-datalakeaccessproperties-datatransferrole): {{String}}
  [KmsKey](#cfn-glue-catalog-datalakeaccessproperties-kmskey): {{String}}
  [ManagedWorkgroupName](#cfn-glue-catalog-datalakeaccessproperties-managedworkgroupname): {{String}}
  [ManagedWorkgroupStatus](#cfn-glue-catalog-datalakeaccessproperties-managedworkgroupstatus): {{String}}
  [RedshiftDatabaseName](#cfn-glue-catalog-datalakeaccessproperties-redshiftdatabasename): {{String}}
```

## Properties
<a name="aws-properties-glue-catalog-datalakeaccessproperties-properties"></a>

`AllowFullTableExternalDataAccess`  <a name="cfn-glue-catalog-datalakeaccessproperties-allowfulltableexternaldataaccess"></a>
Allows third-party engines to access data in Amazon S3 locations that are registered with AWS Lake Formation.
*Required*: No
*Type*: String
*Allowed values*: `True | False`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`CatalogType`  <a name="cfn-glue-catalog-datalakeaccessproperties-catalogtype"></a>
Specifies a federated catalog type for the native catalog resource. The currently supported type is `aws:redshift`.
*Required*: No
*Type*: String
*Pattern*: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\t]*`
*Minimum*: `1`
*Maximum*: `255`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`DataLakeAccess`  <a name="cfn-glue-catalog-datalakeaccessproperties-datalakeaccess"></a>
Turns on or off data lake access for Apache Spark applications that access Amazon Redshift databases in the Data Catalog from any non-Redshift engine, such as Amazon Athena, Amazon EMR, or AWS Glue ETL.
*Required*: No
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`DataTransferRole`  <a name="cfn-glue-catalog-datalakeaccessproperties-datatransferrole"></a>
A role that will be assumed by AWS Glue for transferring data into/out of the staging bucket during a query.
*Required*: No
*Type*: String
*Pattern*: `^arn:aws(-(cn|us-gov|iso(-[bef])?))?:iam::[0-9]{12}:role/.+`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`KmsKey`  <a name="cfn-glue-catalog-datalakeaccessproperties-kmskey"></a>
An encryption key that will be used for the staging bucket that will be created along with the catalog.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ManagedWorkgroupName`  <a name="cfn-glue-catalog-datalakeaccessproperties-managedworkgroupname"></a>
The name of the managed workgroup associated with the catalog.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ManagedWorkgroupStatus`  <a name="cfn-glue-catalog-datalakeaccessproperties-managedworkgroupstatus"></a>
The status of the managed workgroup.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`RedshiftDatabaseName`  <a name="cfn-glue-catalog-datalakeaccessproperties-redshiftdatabasename"></a>
The name of the Redshift database.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
