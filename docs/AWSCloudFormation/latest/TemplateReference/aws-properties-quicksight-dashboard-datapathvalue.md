---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-quicksight-dashboard-datapathvalue.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::Dashboard DataPathValue
<a name="aws-properties-quicksight-dashboard-datapathvalue"></a>

The data path that needs to be sorted.

## Syntax
<a name="aws-properties-quicksight-dashboard-datapathvalue-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-quicksight-dashboard-datapathvalue-syntax.json"></a>

```
{
  "[DataPathType](#cfn-quicksight-dashboard-datapathvalue-datapathtype)" : {{DataPathType}},
  "[FieldId](#cfn-quicksight-dashboard-datapathvalue-fieldid)" : {{String}},
  "[FieldValue](#cfn-quicksight-dashboard-datapathvalue-fieldvalue)" : {{String}}
}
```

### YAML
<a name="aws-properties-quicksight-dashboard-datapathvalue-syntax.yaml"></a>

```
  [DataPathType](#cfn-quicksight-dashboard-datapathvalue-datapathtype): {{
    DataPathType}}
  [FieldId](#cfn-quicksight-dashboard-datapathvalue-fieldid): {{String}}
  [FieldValue](#cfn-quicksight-dashboard-datapathvalue-fieldvalue): {{String}}
```

## Properties
<a name="aws-properties-quicksight-dashboard-datapathvalue-properties"></a>

`DataPathType`  <a name="cfn-quicksight-dashboard-datapathvalue-datapathtype"></a>
The type configuration of the field.
*Required*: No
*Type*: [DataPathType](aws-properties-quicksight-dashboard-datapathtype.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`FieldId`  <a name="cfn-quicksight-dashboard-datapathvalue-fieldid"></a>
The field ID of the field that needs to be sorted.
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `512`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`FieldValue`  <a name="cfn-quicksight-dashboard-datapathvalue-fieldvalue"></a>
The actual value of the field that needs to be sorted.
*Required*: No
*Type*: String
*Minimum*: `0`
*Maximum*: `2048`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
