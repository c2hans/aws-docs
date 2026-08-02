---
source_url: https://docs.aws.amazon.com/outposts/latest/APIReference/API_LineItem.html
---

# LineItem
<a name="API_LineItem"></a>

Information about a line item.

## Contents
<a name="API_LineItem_Contents"></a>

 ** AssetInformationList **   <a name="outposts-Type-LineItem-AssetInformationList"></a>
 Information about assets.
Type: Array of [LineItemAssetInformation](API_LineItemAssetInformation.md) objects
Required: No

 ** CatalogItemId **   <a name="outposts-Type-LineItem-CatalogItemId"></a>
 The ID of the catalog item.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 10.
Pattern: `OR-[A-Z0-9]{7}`
Required: No

 ** LineItemId **   <a name="outposts-Type-LineItem-LineItemId"></a>
The ID of the line item.
Type: String
Pattern: `ooi-[a-f0-9]{17}`
Required: No

 ** PreviousLineItemId **   <a name="outposts-Type-LineItem-PreviousLineItemId"></a>
The ID of the previous line item.
Type: String
Pattern: `ooi-[a-f0-9]{17}`
Required: No

 ** PreviousOrderId **   <a name="outposts-Type-LineItem-PreviousOrderId"></a>
The ID of the previous order.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 20.
Pattern: `oo-[a-f0-9]{17}$`
Required: No

 ** Quantity **   <a name="outposts-Type-LineItem-Quantity"></a>
The quantity of the line item.
Type: Integer
Valid Range: Minimum value of 1.
Required: No

 ** ShipmentInformation **   <a name="outposts-Type-LineItem-ShipmentInformation"></a>
 Information about a line item shipment.
Type: [ShipmentInformation](API_ShipmentInformation.md) object
Required: No

 ** Status **   <a name="outposts-Type-LineItem-Status"></a>
The status of the line item.
Type: String
Valid Values: `PREPARING | BUILDING | SHIPPED | DELIVERED | INSTALLING | INSTALLED | ERROR | CANCELLED | REPLACED`
Required: No

## See Also
<a name="API_LineItem_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/outposts-2019-12-03/LineItem)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/outposts-2019-12-03/LineItem)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/outposts-2019-12-03/LineItem)
