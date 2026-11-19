---
source_url: https://docs.aws.amazon.com/networkmanager/latest/APIReference/API_ContextStore.html
---

# ContextStore

Describes a context store.

## Contents
<a name="API_ContextStore_Contents"></a>

 ** ContextStoreArn **   <a name="networkmanager-Type-ContextStore-ContextStoreArn"></a>
The Amazon Resource Name (ARN) of the context store.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 500.
Pattern: `[\s\S]*`
Required: No

 ** ContextStoreId **   <a name="networkmanager-Type-ContextStore-ContextStoreId"></a>
The ID of the context store.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 50.
Pattern: `^context-store-([0-9a-f]{8,17})$`
Required: No

 ** CreatedAt **   <a name="networkmanager-Type-ContextStore-CreatedAt"></a>
The date and time that the context store was created.
Type: Timestamp
Required: No

 ** Description **   <a name="networkmanager-Type-ContextStore-Description"></a>
The description of the context store.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Pattern: `[\s\S]*`
Required: No

 ** GlobalNetworkId **   <a name="networkmanager-Type-ContextStore-GlobalNetworkId"></a>
The ID of the global network that the context store belongs to.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 50.
Pattern: `[\s\S]*`
Required: No

 ** State **   <a name="networkmanager-Type-ContextStore-State"></a>
The state of the context store. The possible values are the following:
+  `PENDING`: The context store is being created.
+  `AVAILABLE`: The context store is ready to use.
+  `UPDATING`: The context store is being updated.
+  `DELETING`: The context store is being deleted.
+  `DELETED`: The context store is deleted.
Type: String
Valid Values: `PENDING | AVAILABLE | UPDATING | DELETING | DELETED`
Required: No

 ** Tags **   <a name="networkmanager-Type-ContextStore-Tags"></a>
The tags associated with the context store.
Type: Array of [Tag](API_Tag.md) objects
Required: No

## See Also
<a name="API_ContextStore_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/networkmanager-2019-07-05/ContextStore)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/networkmanager-2019-07-05/ContextStore)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/networkmanager-2019-07-05/ContextStore)
