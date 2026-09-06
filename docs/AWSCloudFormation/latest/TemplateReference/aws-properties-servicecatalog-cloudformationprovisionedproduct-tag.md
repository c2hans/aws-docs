---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-servicecatalog-cloudformationprovisionedproduct-tag.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::ServiceCatalog::CloudFormationProvisionedProduct Tag
<a name="aws-properties-servicecatalog-cloudformationprovisionedproduct-tag"></a>

Information about a tag. A tag is a key-value pair. Tags are propagated to the resources created when provisioning a product.

## Syntax
<a name="aws-properties-servicecatalog-cloudformationprovisionedproduct-tag-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-servicecatalog-cloudformationprovisionedproduct-tag-syntax.json"></a>

```
{
  "[Key](#cfn-servicecatalog-cloudformationprovisionedproduct-tag-key)" : {{String}},
  "[Value](#cfn-servicecatalog-cloudformationprovisionedproduct-tag-value)" : {{String}}
}
```

### YAML
<a name="aws-properties-servicecatalog-cloudformationprovisionedproduct-tag-syntax.yaml"></a>

```
  [Key](#cfn-servicecatalog-cloudformationprovisionedproduct-tag-key): {{String}}
  [Value](#cfn-servicecatalog-cloudformationprovisionedproduct-tag-value): {{String}}
```

## Properties
<a name="aws-properties-servicecatalog-cloudformationprovisionedproduct-tag-properties"></a>

`Key`  <a name="cfn-servicecatalog-cloudformationprovisionedproduct-tag-key"></a>
The tag key.
*Required*: Yes
*Type*: String
*Pattern*: `^([\p{L}\p{Z}\p{N}_.:/=+\-@]*)$`
*Minimum*: `1`
*Maximum*: `128`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Value`  <a name="cfn-servicecatalog-cloudformationprovisionedproduct-tag-value"></a>
The value for this key.
*Required*: Yes
*Type*: String
*Pattern*: `^([\p{L}\p{Z}\p{N}_.:/=+\-@]*)$`
*Minimum*: `1`
*Maximum*: `256`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
