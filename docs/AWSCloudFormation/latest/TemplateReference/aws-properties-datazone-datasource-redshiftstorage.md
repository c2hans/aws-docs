---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-datazone-datasource-redshiftstorage.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::DataZone::DataSource RedshiftStorage
<a name="aws-properties-datazone-datasource-redshiftstorage"></a>

The details of the Amazon Redshift storage as part of the configuration of an Amazon Redshift data source run.

## Syntax
<a name="aws-properties-datazone-datasource-redshiftstorage-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-datazone-datasource-redshiftstorage-syntax.json"></a>

```
{
  "[RedshiftClusterSource](#cfn-datazone-datasource-redshiftstorage-redshiftclustersource)" : {{RedshiftClusterStorage}},
  "[RedshiftServerlessSource](#cfn-datazone-datasource-redshiftstorage-redshiftserverlesssource)" : {{RedshiftServerlessStorage}}
}
```

### YAML
<a name="aws-properties-datazone-datasource-redshiftstorage-syntax.yaml"></a>

```
  [RedshiftClusterSource](#cfn-datazone-datasource-redshiftstorage-redshiftclustersource): {{
    RedshiftClusterStorage}}
  [RedshiftServerlessSource](#cfn-datazone-datasource-redshiftstorage-redshiftserverlesssource): {{
    RedshiftServerlessStorage}}
```

## Properties
<a name="aws-properties-datazone-datasource-redshiftstorage-properties"></a>

`RedshiftClusterSource`  <a name="cfn-datazone-datasource-redshiftstorage-redshiftclustersource"></a>
The details of the Amazon Redshift cluster source.
*Required*: No
*Type*: [RedshiftClusterStorage](aws-properties-datazone-datasource-redshiftclusterstorage.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`RedshiftServerlessSource`  <a name="cfn-datazone-datasource-redshiftstorage-redshiftserverlesssource"></a>
The details of the Amazon Redshift Serverless workgroup source.
*Required*: No
*Type*: [RedshiftServerlessStorage](aws-properties-datazone-datasource-redshiftserverlessstorage.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
