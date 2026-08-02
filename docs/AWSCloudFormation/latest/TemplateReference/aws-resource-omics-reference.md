---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-omics-reference.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Omics::Reference
<a name="aws-resource-omics-reference"></a>

<a name="aws-resource-omics-reference-description"></a>The `AWS::Omics::Reference` resource Property description not available. for Omics.

## Syntax
<a name="aws-resource-omics-reference-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-omics-reference-syntax.json"></a>

```
{
  "Type" : "AWS::Omics::Reference",
  "Properties" : {
      "[Description](#cfn-omics-reference-description)" : {{String}},
      "[Name](#cfn-omics-reference-name)" : {{String}},
      "[ReferenceStoreId](#cfn-omics-reference-referencestoreid)" : {{String}},
      "[Tags](#cfn-omics-reference-tags)" : {{[ TagsItems, ... ]}}
    }
}
```

### YAML
<a name="aws-resource-omics-reference-syntax.yaml"></a>

```
Type: AWS::Omics::Reference
Properties:
  [Description](#cfn-omics-reference-description): {{String}}
  [Name](#cfn-omics-reference-name): {{String}}
  [ReferenceStoreId](#cfn-omics-reference-referencestoreid): {{String}}
  [Tags](#cfn-omics-reference-tags): {{
    - TagsItems}}
```

## Properties
<a name="aws-resource-omics-reference-properties"></a>

`Description`  <a name="cfn-omics-reference-description"></a>
The reference's description.
*Required*: No
*Type*: String
*Pattern*: `^[\p{L}||\p{M}||\p{Z}||\p{S}||\p{N}||\p{P}]+$`
*Minimum*: `1`
*Maximum*: `255`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Name`  <a name="cfn-omics-reference-name"></a>
The reference's name.
*Required*: No
*Type*: String
*Pattern*: `^[\p{L}||\p{M}||\p{Z}||\p{S}||\p{N}||\p{P}]+$`
*Minimum*: `3`
*Maximum*: `255`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`ReferenceStoreId`  <a name="cfn-omics-reference-referencestoreid"></a>
The reference's store ID.
*Required*: No
*Type*: String
*Pattern*: `^[0-9]+$`
*Minimum*: `10`
*Maximum*: `36`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Tags`  <a name="cfn-omics-reference-tags"></a>
The source's tags.
*Required*: No
*Type*: Array of [TagsItems](aws-properties-omics-reference-tagsitems.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## Return values
<a name="aws-resource-omics-reference-return-values"></a>

### Ref
<a name="aws-resource-omics-reference-return-values-ref"></a>

### Fn::GetAtt
<a name="aws-resource-omics-reference-return-values-fn--getatt"></a>

####
<a name="aws-resource-omics-reference-return-values-fn--getatt-fn--getatt"></a>

`Arn`  <a name="Arn-fn::getatt"></a>
The reference's ARN.

`CreationJobId`  <a name="CreationJobId-fn::getatt"></a>
Property description not available.

`CreationTime`  <a name="CreationTime-fn::getatt"></a>
When the reference was created.

`CreationType`  <a name="CreationType-fn::getatt"></a>
Property description not available.

`Id`  <a name="Id-fn::getatt"></a>
The reference's ID.

`Md5`  <a name="Md5-fn::getatt"></a>
The reference's MD5 checksum.

`Status`  <a name="Status-fn::getatt"></a>
The reference's status.

`UpdateTime`  <a name="UpdateTime-fn::getatt"></a>
When the reference was updated.
