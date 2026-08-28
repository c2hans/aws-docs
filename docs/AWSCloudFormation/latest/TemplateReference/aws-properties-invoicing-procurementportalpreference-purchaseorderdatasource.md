---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-invoicing-procurementportalpreference-purchaseorderdatasource.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Invoicing::ProcurementPortalPreference PurchaseOrderDataSource
<a name="aws-properties-invoicing-procurementportalpreference-purchaseorderdatasource"></a>

<a name="aws-properties-invoicing-procurementportalpreference-purchaseorderdatasource-description"></a>The `PurchaseOrderDataSource` property type specifies Property description not available. for an [AWS::Invoicing::ProcurementPortalPreference](aws-resource-invoicing-procurementportalpreference.md).

## Syntax
<a name="aws-properties-invoicing-procurementportalpreference-purchaseorderdatasource-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-invoicing-procurementportalpreference-purchaseorderdatasource-syntax.json"></a>

```
{
  "[EinvoiceDeliveryDocumentType](#cfn-invoicing-procurementportalpreference-purchaseorderdatasource-einvoicedeliverydocumenttype)" : {{String}},
  "[PurchaseOrderDataSourceType](#cfn-invoicing-procurementportalpreference-purchaseorderdatasource-purchaseorderdatasourcetype)" : {{String}}
}
```

### YAML
<a name="aws-properties-invoicing-procurementportalpreference-purchaseorderdatasource-syntax.yaml"></a>

```
  [EinvoiceDeliveryDocumentType](#cfn-invoicing-procurementportalpreference-purchaseorderdatasource-einvoicedeliverydocumenttype): {{String}}
  [PurchaseOrderDataSourceType](#cfn-invoicing-procurementportalpreference-purchaseorderdatasource-purchaseorderdatasourcetype): {{String}}
```

## Properties
<a name="aws-properties-invoicing-procurementportalpreference-purchaseorderdatasource-properties"></a>

`EinvoiceDeliveryDocumentType`  <a name="cfn-invoicing-procurementportalpreference-purchaseorderdatasource-einvoicedeliverydocumenttype"></a>
Property description not available.
*Required*: No
*Type*: String
*Allowed values*: `AWS_CLOUD_INVOICE | AWS_CLOUD_CREDIT_MEMO | AWS_MARKETPLACE_INVOICE | AWS_MARKETPLACE_CREDIT_MEMO | AWS_REQUEST_FOR_PAYMENT`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`PurchaseOrderDataSourceType`  <a name="cfn-invoicing-procurementportalpreference-purchaseorderdatasource-purchaseorderdatasourcetype"></a>
Property description not available.
*Required*: No
*Type*: String
*Allowed values*: `ASSOCIATED_PURCHASE_ORDER_REQUIRED | PURCHASE_ORDER_NOT_REQUIRED`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
