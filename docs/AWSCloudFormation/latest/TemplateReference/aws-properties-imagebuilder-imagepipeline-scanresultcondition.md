---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-imagebuilder-imagepipeline-scanresultcondition.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::ImageBuilder::ImagePipeline ScanResultCondition
<a name="aws-properties-imagebuilder-imagepipeline-scanresultcondition"></a>

<a name="aws-properties-imagebuilder-imagepipeline-scanresultcondition-description"></a>The `ScanResultCondition` property type specifies Property description not available. for an [AWS::ImageBuilder::ImagePipeline](aws-resource-imagebuilder-imagepipeline.md).

## Syntax
<a name="aws-properties-imagebuilder-imagepipeline-scanresultcondition-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-imagebuilder-imagepipeline-scanresultcondition-syntax.json"></a>

```
{
  "[FixAvailable](#cfn-imagebuilder-imagepipeline-scanresultcondition-fixavailable)" : {{Boolean}},
  "[MaximumSeverityLabel](#cfn-imagebuilder-imagepipeline-scanresultcondition-maximumseveritylabel)" : {{String}}
}
```

### YAML
<a name="aws-properties-imagebuilder-imagepipeline-scanresultcondition-syntax.yaml"></a>

```
  [FixAvailable](#cfn-imagebuilder-imagepipeline-scanresultcondition-fixavailable): {{Boolean}}
  [MaximumSeverityLabel](#cfn-imagebuilder-imagepipeline-scanresultcondition-maximumseveritylabel): {{String}}
```

## Properties
<a name="aws-properties-imagebuilder-imagepipeline-scanresultcondition-properties"></a>

`FixAvailable`  <a name="cfn-imagebuilder-imagepipeline-scanresultcondition-fixavailable"></a>
Property description not available.
*Required*: No
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`MaximumSeverityLabel`  <a name="cfn-imagebuilder-imagepipeline-scanresultcondition-maximumseveritylabel"></a>
Property description not available.
*Required*: Yes
*Type*: String
*Allowed values*: `INFORMATIONAL | LOW | MEDIUM | HIGH`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
