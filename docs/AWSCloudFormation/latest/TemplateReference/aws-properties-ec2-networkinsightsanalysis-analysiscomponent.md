---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-ec2-networkinsightsanalysis-analysiscomponent.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::EC2::NetworkInsightsAnalysis AnalysisComponent
<a name="aws-properties-ec2-networkinsightsanalysis-analysiscomponent"></a>

Describes a path component.

## Syntax
<a name="aws-properties-ec2-networkinsightsanalysis-analysiscomponent-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-ec2-networkinsightsanalysis-analysiscomponent-syntax.json"></a>

```
{
  "[Arn](#cfn-ec2-networkinsightsanalysis-analysiscomponent-arn)" : {{String}},
  "[Id](#cfn-ec2-networkinsightsanalysis-analysiscomponent-id)" : {{String}}
}
```

### YAML
<a name="aws-properties-ec2-networkinsightsanalysis-analysiscomponent-syntax.yaml"></a>

```
  [Arn](#cfn-ec2-networkinsightsanalysis-analysiscomponent-arn): {{String}}
  [Id](#cfn-ec2-networkinsightsanalysis-analysiscomponent-id): {{String}}
```

## Properties
<a name="aws-properties-ec2-networkinsightsanalysis-analysiscomponent-properties"></a>

`Arn`  <a name="cfn-ec2-networkinsightsanalysis-analysiscomponent-arn"></a>
The Amazon Resource Name (ARN) of the component.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Id`  <a name="cfn-ec2-networkinsightsanalysis-analysiscomponent-id"></a>
The ID of the component.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
