---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-invoicing-procurementportalpreference-einvoicedeliverypreference.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Invoicing::ProcurementPortalPreference EinvoiceDeliveryPreference
<a name="aws-properties-invoicing-procurementportalpreference-einvoicedeliverypreference"></a>

<a name="aws-properties-invoicing-procurementportalpreference-einvoicedeliverypreference-description"></a>The `EinvoiceDeliveryPreference` property type specifies Property description not available. for an [AWS::Invoicing::ProcurementPortalPreference](aws-resource-invoicing-procurementportalpreference.md).

## Syntax
<a name="aws-properties-invoicing-procurementportalpreference-einvoicedeliverypreference-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-invoicing-procurementportalpreference-einvoicedeliverypreference-syntax.json"></a>

```
{
  "[ConnectionTestingMethod](#cfn-invoicing-procurementportalpreference-einvoicedeliverypreference-connectiontestingmethod)" : {{String}},
  "[EinvoiceDeliveryActivationDate](#cfn-invoicing-procurementportalpreference-einvoicedeliverypreference-einvoicedeliveryactivationdate)" : {{String}},
  "[EinvoiceDeliveryAttachmentTypes](#cfn-invoicing-procurementportalpreference-einvoicedeliverypreference-einvoicedeliveryattachmenttypes)" : {{[ String, ... ]}},
  "[EinvoiceDeliveryDocumentTypes](#cfn-invoicing-procurementportalpreference-einvoicedeliverypreference-einvoicedeliverydocumenttypes)" : {{[ String, ... ]}},
  "[Protocol](#cfn-invoicing-procurementportalpreference-einvoicedeliverypreference-protocol)" : {{String}},
  "[PurchaseOrderDataSources](#cfn-invoicing-procurementportalpreference-einvoicedeliverypreference-purchaseorderdatasources)" : {{[ PurchaseOrderDataSource, ... ]}}
}
```

### YAML
<a name="aws-properties-invoicing-procurementportalpreference-einvoicedeliverypreference-syntax.yaml"></a>

```
  [ConnectionTestingMethod](#cfn-invoicing-procurementportalpreference-einvoicedeliverypreference-connectiontestingmethod): {{String}}
  [EinvoiceDeliveryActivationDate](#cfn-invoicing-procurementportalpreference-einvoicedeliverypreference-einvoicedeliveryactivationdate): {{String}}
  [EinvoiceDeliveryAttachmentTypes](#cfn-invoicing-procurementportalpreference-einvoicedeliverypreference-einvoicedeliveryattachmenttypes): {{
    - String}}
  [EinvoiceDeliveryDocumentTypes](#cfn-invoicing-procurementportalpreference-einvoicedeliverypreference-einvoicedeliverydocumenttypes): {{
    - String}}
  [Protocol](#cfn-invoicing-procurementportalpreference-einvoicedeliverypreference-protocol): {{String}}
  [PurchaseOrderDataSources](#cfn-invoicing-procurementportalpreference-einvoicedeliverypreference-purchaseorderdatasources): {{
    - PurchaseOrderDataSource}}
```

## Properties
<a name="aws-properties-invoicing-procurementportalpreference-einvoicedeliverypreference-properties"></a>

`ConnectionTestingMethod`  <a name="cfn-invoicing-procurementportalpreference-einvoicedeliverypreference-connectiontestingmethod"></a>
Property description not available.
*Required*: No
*Type*: String
*Allowed values*: `PROD_ENV_DOLLAR_TEST | TEST_ENV_REPLAY_TEST`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`EinvoiceDeliveryActivationDate`  <a name="cfn-invoicing-procurementportalpreference-einvoicedeliverypreference-einvoicedeliveryactivationdate"></a>
Property description not available.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`EinvoiceDeliveryAttachmentTypes`  <a name="cfn-invoicing-procurementportalpreference-einvoicedeliverypreference-einvoicedeliveryattachmenttypes"></a>
Property description not available.
*Required*: No
*Type*: Array of String
*Allowed values*: `INVOICE_PDF | RFP_PDF`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`EinvoiceDeliveryDocumentTypes`  <a name="cfn-invoicing-procurementportalpreference-einvoicedeliverypreference-einvoicedeliverydocumenttypes"></a>
Property description not available.
*Required*: No
*Type*: Array of String
*Allowed values*: `AWS_CLOUD_INVOICE | AWS_CLOUD_CREDIT_MEMO | AWS_MARKETPLACE_INVOICE | AWS_MARKETPLACE_CREDIT_MEMO | AWS_REQUEST_FOR_PAYMENT`
*Minimum*: `0`
*Maximum*: `10`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Protocol`  <a name="cfn-invoicing-procurementportalpreference-einvoicedeliverypreference-protocol"></a>
Property description not available.
*Required*: No
*Type*: String
*Allowed values*: `CXML`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`PurchaseOrderDataSources`  <a name="cfn-invoicing-procurementportalpreference-einvoicedeliverypreference-purchaseorderdatasources"></a>
Property description not available.
*Required*: No
*Type*: Array of [PurchaseOrderDataSource](aws-properties-invoicing-procurementportalpreference-purchaseorderdatasource.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
