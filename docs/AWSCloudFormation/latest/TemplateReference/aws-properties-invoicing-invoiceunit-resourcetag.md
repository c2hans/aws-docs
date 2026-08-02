---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-invoicing-invoiceunit-resourcetag.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Invoicing::InvoiceUnit ResourceTag
<a name="aws-properties-invoicing-invoiceunit-resourcetag"></a>

 The tag structure that contains a tag key and value.

## Syntax
<a name="aws-properties-invoicing-invoiceunit-resourcetag-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-invoicing-invoiceunit-resourcetag-syntax.json"></a>

```
{
  "[Key](#cfn-invoicing-invoiceunit-resourcetag-key)" : {{String}},
  "[Value](#cfn-invoicing-invoiceunit-resourcetag-value)" : {{String}}
}
```

### YAML
<a name="aws-properties-invoicing-invoiceunit-resourcetag-syntax.yaml"></a>

```
  [Key](#cfn-invoicing-invoiceunit-resourcetag-key): {{String}}
  [Value](#cfn-invoicing-invoiceunit-resourcetag-value): {{String}}
```

## Properties
<a name="aws-properties-invoicing-invoiceunit-resourcetag-properties"></a>

`Key`  <a name="cfn-invoicing-invoiceunit-resourcetag-key"></a>
The object key of your of your resource tag.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `256`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Value`  <a name="cfn-invoicing-invoiceunit-resourcetag-value"></a>
 The specific value of the resource tag.
*Required*: Yes
*Type*: String
*Minimum*: `0`
*Maximum*: `200`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
