---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-omics-readset-fileinformation.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Omics::ReadSet FileInformation
<a name="aws-properties-omics-readset-fileinformation"></a>

<a name="aws-properties-omics-readset-fileinformation-description"></a>The `FileInformation` property type specifies Property description not available. for an [AWS::Omics::ReadSet](aws-resource-omics-readset.md).

## Syntax
<a name="aws-properties-omics-readset-fileinformation-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-omics-readset-fileinformation-syntax.json"></a>

```
{
  "[ContentLength](#cfn-omics-readset-fileinformation-contentlength)" : {{Integer}},
  "[PartSize](#cfn-omics-readset-fileinformation-partsize)" : {{Integer}},
  "[S3Access](#cfn-omics-readset-fileinformation-s3access)" : {{ReadSetS3Access}},
  "[TotalParts](#cfn-omics-readset-fileinformation-totalparts)" : {{Integer}}
}
```

### YAML
<a name="aws-properties-omics-readset-fileinformation-syntax.yaml"></a>

```
  [ContentLength](#cfn-omics-readset-fileinformation-contentlength): {{Integer}}
  [PartSize](#cfn-omics-readset-fileinformation-partsize): {{Integer}}
  [S3Access](#cfn-omics-readset-fileinformation-s3access): {{
    ReadSetS3Access}}
  [TotalParts](#cfn-omics-readset-fileinformation-totalparts): {{Integer}}
```

## Properties
<a name="aws-properties-omics-readset-fileinformation-properties"></a>

`ContentLength`  <a name="cfn-omics-readset-fileinformation-contentlength"></a>
Property description not available.
*Required*: No
*Type*: Integer
*Minimum*: `1`
*Maximum*: `5497558138880`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`PartSize`  <a name="cfn-omics-readset-fileinformation-partsize"></a>
Property description not available.
*Required*: No
*Type*: Integer
*Minimum*: `1`
*Maximum*: `5368709120`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`S3Access`  <a name="cfn-omics-readset-fileinformation-s3access"></a>
Property description not available.
*Required*: No
*Type*: [ReadSetS3Access](aws-properties-omics-readset-readsets3access.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`TotalParts`  <a name="cfn-omics-readset-fileinformation-totalparts"></a>
Property description not available.
*Required*: No
*Type*: Integer
*Minimum*: `1`
*Maximum*: `10000`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
