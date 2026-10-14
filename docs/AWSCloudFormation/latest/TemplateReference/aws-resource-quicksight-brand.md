---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-quicksight-brand.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::Brand
<a name="aws-resource-quicksight-brand"></a>

<a name="aws-resource-quicksight-brand-description"></a>The `AWS::QuickSight::Brand` resource Property description not available. for QuickSight.

## Syntax
<a name="aws-resource-quicksight-brand-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-quicksight-brand-syntax.json"></a>

```
{
  "Type" : "AWS::QuickSight::Brand",
  "Properties" : {
      "[BrandDefinition](#cfn-quicksight-brand-branddefinition)" : {{BrandDefinition}},
      "[BrandId](#cfn-quicksight-brand-brandid)" : {{String}},
      "[Tags](#cfn-quicksight-brand-tags)" : {{[ Tag, ... ]}}
    }
}
```

### YAML
<a name="aws-resource-quicksight-brand-syntax.yaml"></a>

```
Type: AWS::QuickSight::Brand
Properties:
  [BrandDefinition](#cfn-quicksight-brand-branddefinition): {{
    BrandDefinition}}
  [BrandId](#cfn-quicksight-brand-brandid): {{String}}
  [Tags](#cfn-quicksight-brand-tags): {{
    - Tag}}
```

## Properties
<a name="aws-resource-quicksight-brand-properties"></a>

`BrandDefinition`  <a name="cfn-quicksight-brand-branddefinition"></a>
Property description not available.
*Required*: No
*Type*: [BrandDefinition](aws-properties-quicksight-brand-branddefinition.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`BrandId`  <a name="cfn-quicksight-brand-brandid"></a>
The ID of the Quick brand.
*Required*: Yes
*Type*: String
*Pattern*: `^[\w\-]+$`
*Minimum*: `1`
*Maximum*: `512`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Tags`  <a name="cfn-quicksight-brand-tags"></a>
Property description not available.
*Required*: No
*Type*: Array of [Tag](aws-properties-quicksight-brand-tag.md)
*Minimum*: `1`
*Maximum*: `200`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-quicksight-brand-return-values"></a>

### Ref
<a name="aws-resource-quicksight-brand-return-values-ref"></a>

### Fn::GetAtt
<a name="aws-resource-quicksight-brand-return-values-fn--getatt"></a>

####
<a name="aws-resource-quicksight-brand-return-values-fn--getatt-fn--getatt"></a>

`Arn`  <a name="Arn-fn::getatt"></a>
The Amazon Resource Name (ARN) of the brand.

`AwsAccountId`  <a name="AwsAccountId-fn::getatt"></a>
Property description not available.

`BrandStatus`  <a name="BrandStatus-fn::getatt"></a>
The status of the brand.

`CreatedTime`  <a name="CreatedTime-fn::getatt"></a>
The time that the brand was created.

`LastUpdatedTime`  <a name="LastUpdatedTime-fn::getatt"></a>
The last time the brand was updated.

`VersionId`  <a name="VersionId-fn::getatt"></a>
The ID of the version.

`VersionStatus`  <a name="VersionStatus-fn::getatt"></a>
The status of the version.
