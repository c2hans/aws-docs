---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-cleanrooms-analysistemplate-syntheticdataparameters.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::CleanRooms::AnalysisTemplate SyntheticDataParameters
<a name="aws-properties-cleanrooms-analysistemplate-syntheticdataparameters"></a>

The parameters that control how synthetic data is generated, including privacy settings, column classifications, and other configuration options that affect the data synthesis process.

## Syntax
<a name="aws-properties-cleanrooms-analysistemplate-syntheticdataparameters-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-cleanrooms-analysistemplate-syntheticdataparameters-syntax.json"></a>

```
{
  "[MlSyntheticDataParameters](#cfn-cleanrooms-analysistemplate-syntheticdataparameters-mlsyntheticdataparameters)" : {{MLSyntheticDataParameters}}
}
```

### YAML
<a name="aws-properties-cleanrooms-analysistemplate-syntheticdataparameters-syntax.yaml"></a>

```
  [MlSyntheticDataParameters](#cfn-cleanrooms-analysistemplate-syntheticdataparameters-mlsyntheticdataparameters): {{
    MLSyntheticDataParameters}}
```

## Properties
<a name="aws-properties-cleanrooms-analysistemplate-syntheticdataparameters-properties"></a>

`MlSyntheticDataParameters`  <a name="cfn-cleanrooms-analysistemplate-syntheticdataparameters-mlsyntheticdataparameters"></a>
The machine learning-specific parameters for synthetic data generation.
*Required*: Yes
*Type*: [MLSyntheticDataParameters](aws-properties-cleanrooms-analysistemplate-mlsyntheticdataparameters.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)
