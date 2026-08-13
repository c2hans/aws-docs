---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-omics-readset.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Omics::ReadSet
<a name="aws-resource-omics-readset"></a>

<a name="aws-resource-omics-readset-description"></a>The `AWS::Omics::ReadSet` resource Property description not available. for Omics.

## Syntax
<a name="aws-resource-omics-readset-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-omics-readset-syntax.json"></a>

```
{
  "Type" : "AWS::Omics::ReadSet",
  "Properties" : {
      "[Description](#cfn-omics-readset-description)" : {{String}},
      "[FileType](#cfn-omics-readset-filetype)" : {{String}},
      "[Name](#cfn-omics-readset-name)" : {{String}},
      "[ReferenceArn](#cfn-omics-readset-referencearn)" : {{String}},
      "[SampleId](#cfn-omics-readset-sampleid)" : {{String}},
      "[SequenceStoreId](#cfn-omics-readset-sequencestoreid)" : {{String}},
      "[SubjectId](#cfn-omics-readset-subjectid)" : {{String}}
    }
}
```

### YAML
<a name="aws-resource-omics-readset-syntax.yaml"></a>

```
Type: AWS::Omics::ReadSet
Properties:
  [Description](#cfn-omics-readset-description): {{String}}
  [FileType](#cfn-omics-readset-filetype): {{String}}
  [Name](#cfn-omics-readset-name): {{String}}
  [ReferenceArn](#cfn-omics-readset-referencearn): {{String}}
  [SampleId](#cfn-omics-readset-sampleid): {{String}}
  [SequenceStoreId](#cfn-omics-readset-sequencestoreid): {{String}}
  [SubjectId](#cfn-omics-readset-subjectid): {{String}}
```

## Properties
<a name="aws-resource-omics-readset-properties"></a>

`Description`  <a name="cfn-omics-readset-description"></a>
The read set's description.
*Required*: No
*Type*: String
*Pattern*: `^[\p{L}||\p{M}||\p{Z}||\p{S}||\p{N}||\p{P}]+$`
*Minimum*: `1`
*Maximum*: `255`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`FileType`  <a name="cfn-omics-readset-filetype"></a>
The read set's file type.
*Required*: No
*Type*: String
*Allowed values*: `FASTQ | BAM | CRAM | UBAM`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Name`  <a name="cfn-omics-readset-name"></a>
The read set's name.
*Required*: No
*Type*: String
*Pattern*: `^[\p{L}||\p{M}||\p{Z}||\p{S}||\p{N}||\p{P}]+$`
*Minimum*: `1`
*Maximum*: `127`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`ReferenceArn`  <a name="cfn-omics-readset-referencearn"></a>
The read set's genome reference ARN.
*Required*: No
*Type*: String
*Pattern*: `^arn:.+$`
*Minimum*: `1`
*Maximum*: `127`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`SampleId`  <a name="cfn-omics-readset-sampleid"></a>
The read set's sample ID.
*Required*: No
*Type*: String
*Pattern*: `^[\p{L}||\p{M}||\p{Z}||\p{S}||\p{N}||\p{P}]+$`
*Minimum*: `1`
*Maximum*: `127`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`SequenceStoreId`  <a name="cfn-omics-readset-sequencestoreid"></a>
The read set's sequence store ID.
*Required*: No
*Type*: String
*Pattern*: `^[0-9]+$`
*Minimum*: `10`
*Maximum*: `36`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`SubjectId`  <a name="cfn-omics-readset-subjectid"></a>
The read set's subject ID.
*Required*: No
*Type*: String
*Pattern*: `^[\p{L}||\p{M}||\p{Z}||\p{S}||\p{N}||\p{P}]+$`
*Minimum*: `1`
*Maximum*: `127`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## Return values
<a name="aws-resource-omics-readset-return-values"></a>

### Ref
<a name="aws-resource-omics-readset-return-values-ref"></a>

### Fn::GetAtt
<a name="aws-resource-omics-readset-return-values-fn--getatt"></a>

####
<a name="aws-resource-omics-readset-return-values-fn--getatt-fn--getatt"></a>

`Arn`  <a name="Arn-fn::getatt"></a>
The read set's ARN.

`CreationJobId`  <a name="CreationJobId-fn::getatt"></a>
Property description not available.

`CreationTime`  <a name="CreationTime-fn::getatt"></a>
When the read set was created.

`CreationType`  <a name="CreationType-fn::getatt"></a>
 The creation type of the read set.

`ReadSetId`  <a name="ReadSetId-fn::getatt"></a>
The source's read set ID.

`Status`  <a name="Status-fn::getatt"></a>
The read set's status.

`Tags`  <a name="Tags-fn::getatt"></a>
The source's tags.
