---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-iotsitewise-dataset-kendrasourcedetail.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::IoTSiteWise::Dataset KendraSourceDetail
<a name="aws-properties-iotsitewise-dataset-kendrasourcedetail"></a>

The source details for the Kendra dataset source.

## Syntax
<a name="aws-properties-iotsitewise-dataset-kendrasourcedetail-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-iotsitewise-dataset-kendrasourcedetail-syntax.json"></a>

```
{
  "[KnowledgeBaseArn](#cfn-iotsitewise-dataset-kendrasourcedetail-knowledgebasearn)" : {{String}},
  "[RoleArn](#cfn-iotsitewise-dataset-kendrasourcedetail-rolearn)" : {{String}}
}
```

### YAML
<a name="aws-properties-iotsitewise-dataset-kendrasourcedetail-syntax.yaml"></a>

```
  [KnowledgeBaseArn](#cfn-iotsitewise-dataset-kendrasourcedetail-knowledgebasearn): {{String}}
  [RoleArn](#cfn-iotsitewise-dataset-kendrasourcedetail-rolearn): {{String}}
```

## Properties
<a name="aws-properties-iotsitewise-dataset-kendrasourcedetail-properties"></a>

`KnowledgeBaseArn`  <a name="cfn-iotsitewise-dataset-kendrasourcedetail-knowledgebasearn"></a>
The `knowledgeBaseArn` details for the Kendra dataset source.
*Required*: Yes
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`RoleArn`  <a name="cfn-iotsitewise-dataset-kendrasourcedetail-rolearn"></a>
The `roleARN` details for the Kendra dataset source.
*Required*: Yes
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
