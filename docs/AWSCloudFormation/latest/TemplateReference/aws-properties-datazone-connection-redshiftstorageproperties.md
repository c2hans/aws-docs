---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-datazone-connection-redshiftstorageproperties.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::DataZone::Connection RedshiftStorageProperties
<a name="aws-properties-datazone-connection-redshiftstorageproperties"></a>

The Amazon Redshift storage properties.

## Syntax
<a name="aws-properties-datazone-connection-redshiftstorageproperties-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-datazone-connection-redshiftstorageproperties-syntax.json"></a>

```
{
  "[ClusterName](#cfn-datazone-connection-redshiftstorageproperties-clustername)" : {{String}},
  "[WorkgroupName](#cfn-datazone-connection-redshiftstorageproperties-workgroupname)" : {{String}}
}
```

### YAML
<a name="aws-properties-datazone-connection-redshiftstorageproperties-syntax.yaml"></a>

```
  [ClusterName](#cfn-datazone-connection-redshiftstorageproperties-clustername): {{String}}
  [WorkgroupName](#cfn-datazone-connection-redshiftstorageproperties-workgroupname): {{String}}
```

## Properties
<a name="aws-properties-datazone-connection-redshiftstorageproperties-properties"></a>

`ClusterName`  <a name="cfn-datazone-connection-redshiftstorageproperties-clustername"></a>
The cluster name in the Amazon Redshift storage properties.
*Required*: No
*Type*: String
*Pattern*: `^[a-z0-9-]+$`
*Minimum*: `0`
*Maximum*: `63`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`WorkgroupName`  <a name="cfn-datazone-connection-redshiftstorageproperties-workgroupname"></a>
The workgroup name in the Amazon Redshift storage properties.
*Required*: No
*Type*: String
*Pattern*: `^[a-z0-9-]+$`
*Minimum*: `3`
*Maximum*: `64`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
