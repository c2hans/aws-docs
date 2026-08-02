---
source_url: https://docs.aws.amazon.com/singlesignon/latest/IdentityStoreAPIReference/API_ExternalId.html
---

# ExternalId
<a name="API_ExternalId"></a>

The identifier issued to this resource by an external identity provider.

## Contents
<a name="API_ExternalId_Contents"></a>

 ** Id **   <a name="singlesignon-Type-ExternalId-Id"></a>
The identifier issued to this resource by an external identity provider.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[\p{L}\p{M}\p{S}\p{N}\p{P}]+`
Required: Yes

 ** Issuer **   <a name="singlesignon-Type-ExternalId-Issuer"></a>
The issuer for an external identifier.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[\p{L}\p{M}\p{S}\p{N}\p{P}]+`
Required: Yes

## See Also
<a name="API_ExternalId_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/identitystore-2020-06-15/ExternalId)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/identitystore-2020-06-15/ExternalId)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/identitystore-2020-06-15/ExternalId)
