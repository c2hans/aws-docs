---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-invoicing-procurementportalpreference.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Invoicing::ProcurementPortalPreference
<a name="aws-resource-invoicing-procurementportalpreference"></a>

<a name="aws-resource-invoicing-procurementportalpreference-description"></a>The `AWS::Invoicing::ProcurementPortalPreference` resource Property description not available. for Invoicing.

## Syntax
<a name="aws-resource-invoicing-procurementportalpreference-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-invoicing-procurementportalpreference-syntax.json"></a>

```
{
  "Type" : "AWS::Invoicing::ProcurementPortalPreference",
  "Properties" : {
      "[BuyerDomain](#cfn-invoicing-procurementportalpreference-buyerdomain)" : {{String}},
      "[BuyerIdentifier](#cfn-invoicing-procurementportalpreference-buyeridentifier)" : {{String}},
      "[Contacts](#cfn-invoicing-procurementportalpreference-contacts)" : {{[ Contact, ... ]}},
      "[EinvoiceDeliveryEnabled](#cfn-invoicing-procurementportalpreference-einvoicedeliveryenabled)" : {{Boolean}},
      "[EinvoiceDeliveryPreference](#cfn-invoicing-procurementportalpreference-einvoicedeliverypreference)" : {{EinvoiceDeliveryPreference}},
      "[ProcurementPortalInstanceEndpoint](#cfn-invoicing-procurementportalpreference-procurementportalinstanceendpoint)" : {{String}},
      "[ProcurementPortalName](#cfn-invoicing-procurementportalpreference-procurementportalname)" : {{String}},
      "[ProcurementPortalSharedSecret](#cfn-invoicing-procurementportalpreference-procurementportalsharedsecret)" : {{String}},
      "[PurchaseOrderRetrievalEnabled](#cfn-invoicing-procurementportalpreference-purchaseorderretrievalenabled)" : {{Boolean}},
      "[Selector](#cfn-invoicing-procurementportalpreference-selector)" : {{ProcurementPortalPreferenceSelector}},
      "[SupplierDomain](#cfn-invoicing-procurementportalpreference-supplierdomain)" : {{String}},
      "[SupplierIdentifier](#cfn-invoicing-procurementportalpreference-supplieridentifier)" : {{String}},
      "[Tags](#cfn-invoicing-procurementportalpreference-tags)" : {{[ Tag, ... ]}},
      "[TestEnvPreference](#cfn-invoicing-procurementportalpreference-testenvpreference)" : {{TestEnvPreference}}
    }
}
```

### YAML
<a name="aws-resource-invoicing-procurementportalpreference-syntax.yaml"></a>

```
Type: AWS::Invoicing::ProcurementPortalPreference
Properties:
  [BuyerDomain](#cfn-invoicing-procurementportalpreference-buyerdomain): {{String}}
  [BuyerIdentifier](#cfn-invoicing-procurementportalpreference-buyeridentifier): {{String}}
  [Contacts](#cfn-invoicing-procurementportalpreference-contacts): {{
    - Contact}}
  [EinvoiceDeliveryEnabled](#cfn-invoicing-procurementportalpreference-einvoicedeliveryenabled): {{Boolean}}
  [EinvoiceDeliveryPreference](#cfn-invoicing-procurementportalpreference-einvoicedeliverypreference): {{
    EinvoiceDeliveryPreference}}
  [ProcurementPortalInstanceEndpoint](#cfn-invoicing-procurementportalpreference-procurementportalinstanceendpoint): {{String}}
  [ProcurementPortalName](#cfn-invoicing-procurementportalpreference-procurementportalname): {{String}}
  [ProcurementPortalSharedSecret](#cfn-invoicing-procurementportalpreference-procurementportalsharedsecret): {{String}}
  [PurchaseOrderRetrievalEnabled](#cfn-invoicing-procurementportalpreference-purchaseorderretrievalenabled): {{Boolean}}
  [Selector](#cfn-invoicing-procurementportalpreference-selector): {{
    ProcurementPortalPreferenceSelector}}
  [SupplierDomain](#cfn-invoicing-procurementportalpreference-supplierdomain): {{String}}
  [SupplierIdentifier](#cfn-invoicing-procurementportalpreference-supplieridentifier): {{String}}
  [Tags](#cfn-invoicing-procurementportalpreference-tags): {{
    - Tag}}
  [TestEnvPreference](#cfn-invoicing-procurementportalpreference-testenvpreference): {{
    TestEnvPreference}}
```

## Properties
<a name="aws-resource-invoicing-procurementportalpreference-properties"></a>

`BuyerDomain`  <a name="cfn-invoicing-procurementportalpreference-buyerdomain"></a>
Property description not available.
*Required*: Yes
*Type*: String
*Allowed values*: `NetworkID`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`BuyerIdentifier`  <a name="cfn-invoicing-procurementportalpreference-buyeridentifier"></a>
Property description not available.
*Required*: Yes
*Type*: String
*Pattern*: `^\S+$`
*Minimum*: `0`
*Maximum*: `1024`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Contacts`  <a name="cfn-invoicing-procurementportalpreference-contacts"></a>
Property description not available.
*Required*: Yes
*Type*: Array of [Contact](aws-properties-invoicing-procurementportalpreference-contact.md)
*Minimum*: `1`
*Maximum*: `1`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`EinvoiceDeliveryEnabled`  <a name="cfn-invoicing-procurementportalpreference-einvoicedeliveryenabled"></a>
Property description not available.
*Required*: Yes
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`EinvoiceDeliveryPreference`  <a name="cfn-invoicing-procurementportalpreference-einvoicedeliverypreference"></a>
Property description not available.
*Required*: No
*Type*: [EinvoiceDeliveryPreference](aws-properties-invoicing-procurementportalpreference-einvoicedeliverypreference.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ProcurementPortalInstanceEndpoint`  <a name="cfn-invoicing-procurementportalpreference-procurementportalinstanceendpoint"></a>
Property description not available.
*Required*: No
*Type*: String
*Pattern*: `^\S+$`
*Minimum*: `0`
*Maximum*: `1024`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ProcurementPortalName`  <a name="cfn-invoicing-procurementportalpreference-procurementportalname"></a>
Property description not available.
*Required*: Yes
*Type*: String
*Allowed values*: `SAP_BUSINESS_NETWORK | COUPA`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`ProcurementPortalSharedSecret`  <a name="cfn-invoicing-procurementportalpreference-procurementportalsharedsecret"></a>
Property description not available.
*Required*: No
*Type*: String
*Pattern*: `^\S+$`
*Minimum*: `0`
*Maximum*: `1024`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`PurchaseOrderRetrievalEnabled`  <a name="cfn-invoicing-procurementportalpreference-purchaseorderretrievalenabled"></a>
Property description not available.
*Required*: Yes
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Selector`  <a name="cfn-invoicing-procurementportalpreference-selector"></a>
Property description not available.
*Required*: No
*Type*: [ProcurementPortalPreferenceSelector](aws-properties-invoicing-procurementportalpreference-procurementportalpreferenceselector.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SupplierDomain`  <a name="cfn-invoicing-procurementportalpreference-supplierdomain"></a>
Property description not available.
*Required*: Yes
*Type*: String
*Allowed values*: `NetworkID`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`SupplierIdentifier`  <a name="cfn-invoicing-procurementportalpreference-supplieridentifier"></a>
Property description not available.
*Required*: Yes
*Type*: String
*Pattern*: `^\S+$`
*Minimum*: `0`
*Maximum*: `1024`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Tags`  <a name="cfn-invoicing-procurementportalpreference-tags"></a>
Property description not available.
*Required*: No
*Type*: Array of [Tag](aws-properties-invoicing-procurementportalpreference-tag.md)
*Minimum*: `0`
*Maximum*: `200`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`TestEnvPreference`  <a name="cfn-invoicing-procurementportalpreference-testenvpreference"></a>
Property description not available.
*Required*: No
*Type*: [TestEnvPreference](aws-properties-invoicing-procurementportalpreference-testenvpreference.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-invoicing-procurementportalpreference-return-values"></a>

### Ref
<a name="aws-resource-invoicing-procurementportalpreference-return-values-ref"></a>

### Fn::GetAtt
<a name="aws-resource-invoicing-procurementportalpreference-return-values-fn--getatt"></a>

####
<a name="aws-resource-invoicing-procurementportalpreference-return-values-fn--getatt-fn--getatt"></a>

`AwsAccountId`  <a name="AwsAccountId-fn::getatt"></a>
Property description not available.

`CreateDate`  <a name="CreateDate-fn::getatt"></a>
Property description not available.

`EinvoiceDeliveryPreferenceStatus`  <a name="EinvoiceDeliveryPreferenceStatus-fn::getatt"></a>
Property description not available.

`LastUpdateDate`  <a name="LastUpdateDate-fn::getatt"></a>
Property description not available.

`ProcurementPortalPreferenceArn`  <a name="ProcurementPortalPreferenceArn-fn::getatt"></a>
Property description not available.

`PurchaseOrderRetrievalEndpoint`  <a name="PurchaseOrderRetrievalEndpoint-fn::getatt"></a>
Property description not available.

`PurchaseOrderRetrievalPreferenceStatus`  <a name="PurchaseOrderRetrievalPreferenceStatus-fn::getatt"></a>
Property description not available.

`Version`  <a name="Version-fn::getatt"></a>
Property description not available.
