---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-iotsitewise-dataset-sourcedetail.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::IoTSiteWise::Dataset SourceDetail
<a name="aws-properties-iotsitewise-dataset-sourcedetail"></a>

The details of the dataset source associated with the dataset.

## Syntax
<a name="aws-properties-iotsitewise-dataset-sourcedetail-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-iotsitewise-dataset-sourcedetail-syntax.json"></a>

```
{
  "[Kendra](#cfn-iotsitewise-dataset-sourcedetail-kendra)" : {{KendraSourceDetail}}
}
```

### YAML
<a name="aws-properties-iotsitewise-dataset-sourcedetail-syntax.yaml"></a>

```
  [Kendra](#cfn-iotsitewise-dataset-sourcedetail-kendra): {{
    KendraSourceDetail}}
```

## Properties
<a name="aws-properties-iotsitewise-dataset-sourcedetail-properties"></a>

`Kendra`  <a name="cfn-iotsitewise-dataset-sourcedetail-kendra"></a>
Contains details about the Kendra dataset source.
*Required*: No
*Type*: [KendraSourceDetail](aws-properties-iotsitewise-dataset-kendrasourcedetail.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
