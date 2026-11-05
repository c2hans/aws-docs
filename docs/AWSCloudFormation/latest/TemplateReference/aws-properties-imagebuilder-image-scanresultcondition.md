---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-imagebuilder-image-scanresultcondition.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::ImageBuilder::Image ScanResultCondition
<a name="aws-properties-imagebuilder-image-scanresultcondition"></a>

<a name="aws-properties-imagebuilder-image-scanresultcondition-description"></a>The `ScanResultCondition` property type specifies Property description not available. for an [AWS::ImageBuilder::Image](aws-resource-imagebuilder-image.md).

## Syntax
<a name="aws-properties-imagebuilder-image-scanresultcondition-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-imagebuilder-image-scanresultcondition-syntax.json"></a>

```
{
  "[FixAvailable](#cfn-imagebuilder-image-scanresultcondition-fixavailable)" : {{Boolean}},
  "[MaximumSeverityLabel](#cfn-imagebuilder-image-scanresultcondition-maximumseveritylabel)" : {{String}}
}
```

### YAML
<a name="aws-properties-imagebuilder-image-scanresultcondition-syntax.yaml"></a>

```
  [FixAvailable](#cfn-imagebuilder-image-scanresultcondition-fixavailable): {{Boolean}}
  [MaximumSeverityLabel](#cfn-imagebuilder-image-scanresultcondition-maximumseveritylabel): {{String}}
```

## Properties
<a name="aws-properties-imagebuilder-image-scanresultcondition-properties"></a>

`FixAvailable`  <a name="cfn-imagebuilder-image-scanresultcondition-fixavailable"></a>
Property description not available.
*Required*: No
*Type*: Boolean
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`MaximumSeverityLabel`  <a name="cfn-imagebuilder-image-scanresultcondition-maximumseveritylabel"></a>
Property description not available.
*Required*: Yes
*Type*: String
*Allowed values*: `INFORMATIONAL | LOW | MEDIUM | HIGH`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)
