---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-omics-variantstore.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Omics::VariantStore
<a name="aws-resource-omics-variantstore"></a>

Create a store for variant data.

## Syntax
<a name="aws-resource-omics-variantstore-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-omics-variantstore-syntax.json"></a>

```
{
  "Type" : "AWS::Omics::VariantStore",
  "Properties" : {
      "[Description](#cfn-omics-variantstore-description)" : {{String}},
      "[Name](#cfn-omics-variantstore-name)" : {{String}},
      "[Reference](#cfn-omics-variantstore-reference)" : {{ReferenceItem}},
      "[SseConfig](#cfn-omics-variantstore-sseconfig)" : {{SseConfig}},
      "[Tags](#cfn-omics-variantstore-tags)" : {{{{{Key}}: {{Value}}, ...}}}
    }
}
```

### YAML
<a name="aws-resource-omics-variantstore-syntax.yaml"></a>

```
Type: AWS::Omics::VariantStore
Properties:
  [Description](#cfn-omics-variantstore-description): {{String}}
  [Name](#cfn-omics-variantstore-name): {{String}}
  [Reference](#cfn-omics-variantstore-reference): {{
    ReferenceItem}}
  [SseConfig](#cfn-omics-variantstore-sseconfig): {{
    SseConfig}}
  [Tags](#cfn-omics-variantstore-tags): {{
    {{Key}}: {{Value}}}}
```

## Properties
<a name="aws-resource-omics-variantstore-properties"></a>

`Description`  <a name="cfn-omics-variantstore-description"></a>
A description for the store.
*Required*: No
*Type*: String
*Minimum*: `0`
*Maximum*: `500`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Name`  <a name="cfn-omics-variantstore-name"></a>
A name for the store.
*Required*: Yes
*Type*: String
*Pattern*: `^([a-z]){1}([a-z0-9_]){2,254}`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Reference`  <a name="cfn-omics-variantstore-reference"></a>
The genome reference for the store's variants.
*Required*: Yes
*Type*: [ReferenceItem](aws-properties-omics-variantstore-referenceitem.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`SseConfig`  <a name="cfn-omics-variantstore-sseconfig"></a>
Server-side encryption (SSE) settings for the store.
*Required*: No
*Type*: [SseConfig](aws-properties-omics-variantstore-sseconfig.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Tags`  <a name="cfn-omics-variantstore-tags"></a>
Tags for the store.
*Required*: No
*Type*: Object of String
*Pattern*: `.+`
*Minimum*: `0`
*Maximum*: `256`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## Return values
<a name="aws-resource-omics-variantstore-return-values"></a>

### Ref
<a name="aws-resource-omics-variantstore-return-values-ref"></a>

When you pass the logical ID of this resource to the intrinsic `Ref` function, `Ref` returns the details of this resource. For example:

 `{ "Ref": "VariantStore.Status" }`

For the Amazon Omics resource`VariantStore.Status`, `Ref` returns the status of the variant store.

For more information about using the `Ref` function, see [https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-ref.html](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-ref.html).

### Fn::GetAtt
<a name="aws-resource-omics-variantstore-return-values-fn--getatt"></a>

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-getatt.html](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-getatt.html).

####
<a name="aws-resource-omics-variantstore-return-values-fn--getatt-fn--getatt"></a>

`CreationTime`  <a name="CreationTime-fn::getatt"></a>
When the store was created.

`Id`  <a name="Id-fn::getatt"></a>
The store's ID.

`Status`  <a name="Status-fn::getatt"></a>
 The store's status.

`StatusMessage`  <a name="StatusMessage-fn::getatt"></a>
The store's status message.

`StoreArn`  <a name="StoreArn-fn::getatt"></a>
The store's ARN.

`StoreSizeBytes`  <a name="StoreSizeBytes-fn::getatt"></a>
The store's size in bytes.

`UpdateTime`  <a name="UpdateTime-fn::getatt"></a>
When the store was updated.
