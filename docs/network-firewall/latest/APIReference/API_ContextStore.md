---
source_url: https://docs.aws.amazon.com/network-firewall/latest/APIReference/API_ContextStore.html
---

# ContextStore
<a name="API_ContextStore"></a>

Contains details about a context store, including its unique identifier and the account that owns it.

## Contents
<a name="API_ContextStore_Contents"></a>

 ** ContextStoreId **   <a name="networkfirewall-Type-ContextStore-ContextStoreId"></a>
The unique identifier of the context store. Use this value in `ListResourcesInContextStore` to list the resources that the context store records.
Type: String
Required: Yes

 ** ContextStoreOwnerAccountId **   <a name="networkfirewall-Type-ContextStore-ContextStoreOwnerAccountId"></a>
The ID of the AWS account that owns the context store.
Type: String
Length Constraints: Fixed length of 12.
Pattern: `^\d{12}$`
Required: Yes

## See Also
<a name="API_ContextStore_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/network-firewall-2020-11-12/ContextStore)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/network-firewall-2020-11-12/ContextStore)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/network-firewall-2020-11-12/ContextStore)
