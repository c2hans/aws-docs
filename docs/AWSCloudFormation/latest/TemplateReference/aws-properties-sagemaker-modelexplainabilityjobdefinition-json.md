---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-sagemaker-modelexplainabilityjobdefinition-json.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::SageMaker::ModelExplainabilityJobDefinition Json
<a name="aws-properties-sagemaker-modelexplainabilityjobdefinition-json"></a>

The JSON dataset format configuration.

## Syntax
<a name="aws-properties-sagemaker-modelexplainabilityjobdefinition-json-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-sagemaker-modelexplainabilityjobdefinition-json-syntax.json"></a>

```
{
  "[Line](#cfn-sagemaker-modelexplainabilityjobdefinition-json-line)" : {{Boolean}}
}
```

### YAML
<a name="aws-properties-sagemaker-modelexplainabilityjobdefinition-json-syntax.yaml"></a>

```
  [Line](#cfn-sagemaker-modelexplainabilityjobdefinition-json-line): {{Boolean}}
```

## Properties
<a name="aws-properties-sagemaker-modelexplainabilityjobdefinition-json-properties"></a>

`Line`  <a name="cfn-sagemaker-modelexplainabilityjobdefinition-json-line"></a>
Indicates whether the JSON data is in line-delimited format.
*Required*: No
*Type*: Boolean
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)
