---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-omics-readset-sequenceinformation.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Omics::ReadSet SequenceInformation
<a name="aws-properties-omics-readset-sequenceinformation"></a>

<a name="aws-properties-omics-readset-sequenceinformation-description"></a>The `SequenceInformation` property type specifies Property description not available. for an [AWS::Omics::ReadSet](aws-resource-omics-readset.md).

## Syntax
<a name="aws-properties-omics-readset-sequenceinformation-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-omics-readset-sequenceinformation-syntax.json"></a>

```
{
  "[Alignment](#cfn-omics-readset-sequenceinformation-alignment)" : {{String}},
  "[GeneratedFrom](#cfn-omics-readset-sequenceinformation-generatedfrom)" : {{String}},
  "[TotalBaseCount](#cfn-omics-readset-sequenceinformation-totalbasecount)" : {{Integer}},
  "[TotalReadCount](#cfn-omics-readset-sequenceinformation-totalreadcount)" : {{Integer}}
}
```

### YAML
<a name="aws-properties-omics-readset-sequenceinformation-syntax.yaml"></a>

```
  [Alignment](#cfn-omics-readset-sequenceinformation-alignment): {{String}}
  [GeneratedFrom](#cfn-omics-readset-sequenceinformation-generatedfrom): {{String}}
  [TotalBaseCount](#cfn-omics-readset-sequenceinformation-totalbasecount): {{Integer}}
  [TotalReadCount](#cfn-omics-readset-sequenceinformation-totalreadcount): {{Integer}}
```

## Properties
<a name="aws-properties-omics-readset-sequenceinformation-properties"></a>

`Alignment`  <a name="cfn-omics-readset-sequenceinformation-alignment"></a>
Property description not available.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`GeneratedFrom`  <a name="cfn-omics-readset-sequenceinformation-generatedfrom"></a>
Property description not available.
*Required*: No
*Type*: String
*Pattern*: `^[\p{L}||\p{M}||\p{Z}||\p{S}||\p{N}||\p{P}]+$`
*Minimum*: `1`
*Maximum*: `127`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`TotalBaseCount`  <a name="cfn-omics-readset-sequenceinformation-totalbasecount"></a>
Property description not available.
*Required*: No
*Type*: Integer
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`TotalReadCount`  <a name="cfn-omics-readset-sequenceinformation-totalreadcount"></a>
Property description not available.
*Required*: No
*Type*: Integer
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
