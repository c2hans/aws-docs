---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-omics-variantstore-referenceitem.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Omics::VariantStore ReferenceItem
<a name="aws-properties-omics-variantstore-referenceitem"></a>

The read set's genome reference ARN.

## Syntax
<a name="aws-properties-omics-variantstore-referenceitem-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-omics-variantstore-referenceitem-syntax.json"></a>

```
{
  "[ReferenceArn](#cfn-omics-variantstore-referenceitem-referencearn)" : {{String}}
}
```

### YAML
<a name="aws-properties-omics-variantstore-referenceitem-syntax.yaml"></a>

```
  [ReferenceArn](#cfn-omics-variantstore-referenceitem-referencearn): {{String}}
```

## Properties
<a name="aws-properties-omics-variantstore-referenceitem-properties"></a>

`ReferenceArn`  <a name="cfn-omics-variantstore-referenceitem-referencearn"></a>
 The reference's ARN.
*Required*: Yes
*Type*: String
*Pattern*: `^arn:.+$`
*Minimum*: `1`
*Maximum*: `127`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)
