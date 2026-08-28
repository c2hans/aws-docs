---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-invoicing-invoiceunit.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Invoicing::InvoiceUnit
<a name="aws-resource-invoicing-invoiceunit"></a>

An invoice unit is a set of mutually exclusive account that correspond to your business entity. Invoice units allow you separate AWS account costs and configures your invoice for each business entity going forward.

## Syntax
<a name="aws-resource-invoicing-invoiceunit-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-invoicing-invoiceunit-syntax.json"></a>

```
{
  "Type" : "AWS::Invoicing::InvoiceUnit",
  "Properties" : {
      "[Description](#cfn-invoicing-invoiceunit-description)" : {{String}},
      "[InvoiceReceiver](#cfn-invoicing-invoiceunit-invoicereceiver)" : {{String}},
      "[Name](#cfn-invoicing-invoiceunit-name)" : {{String}},
      "[ResourceTags](#cfn-invoicing-invoiceunit-resourcetags)" : {{[ ResourceTag, ... ]}},
      "[Rule](#cfn-invoicing-invoiceunit-rule)" : {{Rule}},
      "[TaxInheritanceDisabled](#cfn-invoicing-invoiceunit-taxinheritancedisabled)" : {{Boolean}}
    }
}
```

### YAML
<a name="aws-resource-invoicing-invoiceunit-syntax.yaml"></a>

```
Type: AWS::Invoicing::InvoiceUnit
Properties:
  [Description](#cfn-invoicing-invoiceunit-description): {{String}}
  [InvoiceReceiver](#cfn-invoicing-invoiceunit-invoicereceiver): {{String}}
  [Name](#cfn-invoicing-invoiceunit-name): {{String}}
  [ResourceTags](#cfn-invoicing-invoiceunit-resourcetags): {{
    - ResourceTag}}
  [Rule](#cfn-invoicing-invoiceunit-rule): {{
    Rule}}
  [TaxInheritanceDisabled](#cfn-invoicing-invoiceunit-taxinheritancedisabled): {{Boolean}}
```

## Properties
<a name="aws-resource-invoicing-invoiceunit-properties"></a>

`Description`  <a name="cfn-invoicing-invoiceunit-description"></a>
The assigned description for an invoice unit. This information can't be modified or deleted.
*Required*: No
*Type*: String
*Pattern*: `^[\S\s]*$`
*Minimum*: `0`
*Maximum*: `500`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`InvoiceReceiver`  <a name="cfn-invoicing-invoiceunit-invoicereceiver"></a>
The account that receives invoices related to the invoice unit.
*Required*: Yes
*Type*: String
*Pattern*: `^\d{12}$`
*Minimum*: `12`
*Maximum*: `12`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Name`  <a name="cfn-invoicing-invoiceunit-name"></a>
 A unique name that is distinctive within your AWS.
*Required*: Yes
*Type*: String
*Pattern*: `^(?! )[\p{L}\p{N}\p{Z}-_]*(?<! )$`
*Minimum*: `1`
*Maximum*: `50`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`ResourceTags`  <a name="cfn-invoicing-invoiceunit-resourcetags"></a>
The tag structure that contains a tag key and value.
*Required*: No
*Type*: Array of [ResourceTag](aws-properties-invoicing-invoiceunit-resourcetag.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Rule`  <a name="cfn-invoicing-invoiceunit-rule"></a>
An `InvoiceUnitRule` object used the categorize invoice units.
*Required*: Yes
*Type*: [Rule](aws-properties-invoicing-invoiceunit-rule.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`TaxInheritanceDisabled`  <a name="cfn-invoicing-invoiceunit-taxinheritancedisabled"></a>
Whether the invoice unit based tax inheritance is/ should be enabled or disabled.
*Required*: No
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-invoicing-invoiceunit-return-values"></a>

### Ref
<a name="aws-resource-invoicing-invoiceunit-return-values-ref"></a>

For more information about using the `Ref` function, see [`Ref`](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-ref.html).

### Fn::GetAtt
<a name="aws-resource-invoicing-invoiceunit-return-values-fn--getatt"></a>

####
<a name="aws-resource-invoicing-invoiceunit-return-values-fn--getatt-fn--getatt"></a>

`InvoiceUnitArn`  <a name="InvoiceUnitArn-fn::getatt"></a>
The ARN to identify an invoice unit. This information can't be modified or deleted.

`LastModified`  <a name="LastModified-fn::getatt"></a>
 The last time the invoice unit was updated. This is important to determine the version of invoice unit configuration used to create the invoices. Any invoice created after this modified time will use this invoice unit configuration.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
