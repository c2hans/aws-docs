---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-iotsitewise-dataset-datasetsource.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::IoTSiteWise::Dataset DatasetSource
<a name="aws-properties-iotsitewise-dataset-datasetsource"></a>

The data source for the dataset.

## Syntax
<a name="aws-properties-iotsitewise-dataset-datasetsource-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-iotsitewise-dataset-datasetsource-syntax.json"></a>

```
{
  "[SourceDetail](#cfn-iotsitewise-dataset-datasetsource-sourcedetail)" : {{SourceDetail}},
  "[SourceFormat](#cfn-iotsitewise-dataset-datasetsource-sourceformat)" : {{String}},
  "[SourceType](#cfn-iotsitewise-dataset-datasetsource-sourcetype)" : {{String}}
}
```

### YAML
<a name="aws-properties-iotsitewise-dataset-datasetsource-syntax.yaml"></a>

```
  [SourceDetail](#cfn-iotsitewise-dataset-datasetsource-sourcedetail): {{
    SourceDetail}}
  [SourceFormat](#cfn-iotsitewise-dataset-datasetsource-sourceformat): {{String}}
  [SourceType](#cfn-iotsitewise-dataset-datasetsource-sourcetype): {{String}}
```

## Properties
<a name="aws-properties-iotsitewise-dataset-datasetsource-properties"></a>

`SourceDetail`  <a name="cfn-iotsitewise-dataset-datasetsource-sourcedetail"></a>
The details of the dataset source associated with the dataset.
*Required*: No
*Type*: [SourceDetail](aws-properties-iotsitewise-dataset-sourcedetail.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SourceFormat`  <a name="cfn-iotsitewise-dataset-datasetsource-sourceformat"></a>
The format of the dataset source associated with the dataset.
*Required*: Yes
*Type*: String
*Allowed values*: `KNOWLEDGE_BASE`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SourceType`  <a name="cfn-iotsitewise-dataset-datasetsource-sourcetype"></a>
The type of data source for the dataset.
*Required*: Yes
*Type*: String
*Allowed values*: `KENDRA`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
