---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-sagemaker-modelbiasjobdefinition-csv.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::SageMaker::ModelBiasJobDefinition Csv
<a name="aws-properties-sagemaker-modelbiasjobdefinition-csv"></a>

The CSV dataset format configuration.

## Syntax
<a name="aws-properties-sagemaker-modelbiasjobdefinition-csv-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-sagemaker-modelbiasjobdefinition-csv-syntax.json"></a>

```
{
  "[Header](#cfn-sagemaker-modelbiasjobdefinition-csv-header)" : {{Boolean}}
}
```

### YAML
<a name="aws-properties-sagemaker-modelbiasjobdefinition-csv-syntax.yaml"></a>

```
  [Header](#cfn-sagemaker-modelbiasjobdefinition-csv-header): {{Boolean}}
```

## Properties
<a name="aws-properties-sagemaker-modelbiasjobdefinition-csv-properties"></a>

`Header`  <a name="cfn-sagemaker-modelbiasjobdefinition-csv-header"></a>
Indicates whether the CSV data has a header row.
*Required*: No
*Type*: Boolean
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)
