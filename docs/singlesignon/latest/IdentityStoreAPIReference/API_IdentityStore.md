---
source_url: https://docs.aws.amazon.com/singlesignon/latest/IdentityStoreAPIReference/API_IdentityStore.html
---

# IdentityStore
<a name="API_IdentityStore"></a>

A structure that contains the identifiers for an identity store: its globally unique identifier (ID) and Amazon Resource Name (ARN).

## Contents
<a name="API_IdentityStore_Contents"></a>

 ** IdentityStoreArn **   <a name="singlesignon-Type-IdentityStore-IdentityStoreArn"></a>
The Amazon Resource Name (ARN) of the identity store. For example, `arn:aws:identitystore::111122223333:identitystore/d-1234567890`.
Type: String
Length Constraints: Minimum length of 62. Maximum length of 93.
Pattern: `arn:aws[a-z-]*:identitystore::\d{12}:identitystore/(d-[0-9a-f]{10}|[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12})`
Required: Yes

 ** IdentityStoreId **   <a name="singlesignon-Type-IdentityStore-IdentityStoreId"></a>
The globally unique identifier for the identity store.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 93.
Pattern: `(arn:aws[a-z-]*:identitystore::\d{12}:identitystore/)?(d-[0-9a-f]{10}|[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12})`
Required: Yes

## See Also
<a name="API_IdentityStore_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/identitystore-2020-06-15/IdentityStore)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/identitystore-2020-06-15/IdentityStore)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/identitystore-2020-06-15/IdentityStore)
