---
source_url: https://docs.aws.amazon.com/systems-manager/latest/APIReference/API_OpsItemRelatedItemSummary.html
---

# OpsItemRelatedItemSummary
<a name="API_OpsItemRelatedItemSummary"></a>

Summary information about related-item resources for an OpsItem.

## Contents
<a name="API_OpsItemRelatedItemSummary_Contents"></a>

 ** AssociationId **   <a name="systemsmanager-Type-OpsItemRelatedItemSummary-AssociationId"></a>
The association ID.
Type: String
Required: No

 ** AssociationType **   <a name="systemsmanager-Type-OpsItemRelatedItemSummary-AssociationType"></a>
The association type.
Type: String
Required: No

 ** CreatedBy **   <a name="systemsmanager-Type-OpsItemRelatedItemSummary-CreatedBy"></a>
Information about the user or resource that created an OpsItem event.
Type: [OpsItemIdentity](API_OpsItemIdentity.md) object
Required: No

 ** CreatedTime **   <a name="systemsmanager-Type-OpsItemRelatedItemSummary-CreatedTime"></a>
The time the related-item association was created.
Type: Timestamp
Required: No

 ** LastModifiedBy **   <a name="systemsmanager-Type-OpsItemRelatedItemSummary-LastModifiedBy"></a>
Information about the user or resource that created an OpsItem event.
Type: [OpsItemIdentity](API_OpsItemIdentity.md) object
Required: No

 ** LastModifiedTime **   <a name="systemsmanager-Type-OpsItemRelatedItemSummary-LastModifiedTime"></a>
The time the related-item association was last updated.
Type: Timestamp
Required: No

 ** OpsItemId **   <a name="systemsmanager-Type-OpsItemRelatedItemSummary-OpsItemId"></a>
The OpsItem ID.
Type: String
Pattern: `^(oi)-[0-9a-f]{12}$`
Required: No

 ** ResourceType **   <a name="systemsmanager-Type-OpsItemRelatedItemSummary-ResourceType"></a>
The resource type.
Type: String
Required: No

 ** ResourceUri **   <a name="systemsmanager-Type-OpsItemRelatedItemSummary-ResourceUri"></a>
The Amazon Resource Name (ARN) of the related-item resource.
Type: String
Required: No

## See Also
<a name="API_OpsItemRelatedItemSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ssm-2014-11-06/OpsItemRelatedItemSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ssm-2014-11-06/OpsItemRelatedItemSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ssm-2014-11-06/OpsItemRelatedItemSummary)
