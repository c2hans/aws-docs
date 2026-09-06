---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-datazone-datasource-redshiftserverlessstorage.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::DataZone::DataSource RedshiftServerlessStorage
<a name="aws-properties-datazone-datasource-redshiftserverlessstorage"></a>

The details of the Amazon Redshift Serverless workgroup storage.

## Syntax
<a name="aws-properties-datazone-datasource-redshiftserverlessstorage-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-datazone-datasource-redshiftserverlessstorage-syntax.json"></a>

```
{
  "[WorkgroupName](#cfn-datazone-datasource-redshiftserverlessstorage-workgroupname)" : {{String}}
}
```

### YAML
<a name="aws-properties-datazone-datasource-redshiftserverlessstorage-syntax.yaml"></a>

```
  [WorkgroupName](#cfn-datazone-datasource-redshiftserverlessstorage-workgroupname): {{String}}
```

## Properties
<a name="aws-properties-datazone-datasource-redshiftserverlessstorage-properties"></a>

`WorkgroupName`  <a name="cfn-datazone-datasource-redshiftserverlessstorage-workgroupname"></a>
The name of the Amazon Redshift Serverless workgroup.
*Required*: Yes
*Type*: String
*Pattern*: `^[a-z0-9-]+$`
*Minimum*: `3`
*Maximum*: `64`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
