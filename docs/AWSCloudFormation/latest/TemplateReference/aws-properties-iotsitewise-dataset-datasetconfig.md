---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-iotsitewise-dataset-datasetconfig.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::IoTSiteWise::Dataset DatasetConfig
<a name="aws-properties-iotsitewise-dataset-datasetconfig"></a>

The configuration for the dataset.

## Syntax
<a name="aws-properties-iotsitewise-dataset-datasetconfig-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-iotsitewise-dataset-datasetconfig-syntax.json"></a>

```
{
  "[Session](#cfn-iotsitewise-dataset-datasetconfig-session)" : {{SessionConfig}}
}
```

### YAML
<a name="aws-properties-iotsitewise-dataset-datasetconfig-syntax.yaml"></a>

```
  [Session](#cfn-iotsitewise-dataset-datasetconfig-session): {{
    SessionConfig}}
```

## Properties
<a name="aws-properties-iotsitewise-dataset-datasetconfig-properties"></a>

`Session`  <a name="cfn-iotsitewise-dataset-datasetconfig-session"></a>
The session configuration for a `SESSION` dataset.
*Required*: No
*Type*: [SessionConfig](aws-properties-iotsitewise-dataset-sessionconfig.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
