---
source_url: https://docs.aws.amazon.com/networkmanager/latest/APIReference/API_ContextStoreAssociation.html
---

# ContextStoreAssociation

Describes the association between a context store and a transit gateway.

## Contents
<a name="API_ContextStoreAssociation_Contents"></a>

 ** ContextStoreId **   <a name="networkmanager-Type-ContextStoreAssociation-ContextStoreId"></a>
The ID of the context store.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 50.
Pattern: `^context-store-([0-9a-f]{8,17})$`
Required: No

 ** CreatedAt **   <a name="networkmanager-Type-ContextStoreAssociation-CreatedAt"></a>
The date and time that the association was created.
Type: Timestamp
Required: No

 ** State **   <a name="networkmanager-Type-ContextStoreAssociation-State"></a>
The state of the association. The possible values are the following:
+  `ASSOCIATING`: The transit gateway is being associated with the context store.
+  `ASSOCIATED`: The transit gateway is associated with the context store.
+  `DISASSOCIATING`: The transit gateway is being disassociated from the context store.
+  `FAILED`: The association failed. To remove it, disassociate the transit gateway.
Type: String
Valid Values: `ASSOCIATING | ASSOCIATED | DISASSOCIATING | FAILED`
Required: No

 ** TransitGatewayArn **   <a name="networkmanager-Type-ContextStoreAssociation-TransitGatewayArn"></a>
The Amazon Resource Name (ARN) of the transit gateway.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 500.
Pattern: `[\s\S]*`
Required: No

## See Also
<a name="API_ContextStoreAssociation_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/networkmanager-2019-07-05/ContextStoreAssociation)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/networkmanager-2019-07-05/ContextStoreAssociation)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/networkmanager-2019-07-05/ContextStoreAssociation)
