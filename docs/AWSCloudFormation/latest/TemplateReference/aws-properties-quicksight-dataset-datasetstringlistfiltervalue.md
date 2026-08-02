---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-quicksight-dataset-datasetstringlistfiltervalue.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::DataSet DataSetStringListFilterValue
<a name="aws-properties-quicksight-dataset-datasetstringlistfiltervalue"></a>

Represents a list of string values used in filter conditions.

## Syntax
<a name="aws-properties-quicksight-dataset-datasetstringlistfiltervalue-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-quicksight-dataset-datasetstringlistfiltervalue-syntax.json"></a>

```
{
  "[StaticValues](#cfn-quicksight-dataset-datasetstringlistfiltervalue-staticvalues)" : {{[ String, ... ]}}
}
```

### YAML
<a name="aws-properties-quicksight-dataset-datasetstringlistfiltervalue-syntax.yaml"></a>

```
  [StaticValues](#cfn-quicksight-dataset-datasetstringlistfiltervalue-staticvalues): {{
    - String}}
```

## Properties
<a name="aws-properties-quicksight-dataset-datasetstringlistfiltervalue-properties"></a>

`StaticValues`  <a name="cfn-quicksight-dataset-datasetstringlistfiltervalue-staticvalues"></a>
A list of static string values used for filtering.
*Required*: No
*Type*: Array of String
*Minimum*: `0 | 0`
*Maximum*: `512 | 1000`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
