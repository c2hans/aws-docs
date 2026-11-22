---
source_url: https://docs.aws.amazon.com/STS/latest/APIReference/API_TransactionContext.html
---

# TransactionContext

The session's `aws:TransactionContext/IdentityProvider/*` keys.

## Contents
<a name="API_TransactionContext_Contents"></a>

 ** IdentityProvider **  IdentityProvider.entry.N.key (key)  IdentityProvider.entry.N.value (value)
The session's `aws:TransactionContext/IdentityProvider/*` keys, keyed by the part of the key name after `aws:TransactionContext/IdentityProvider/`. Each value is up to 128 characters.
The number of entries is bounded twice. IAM limits how many keys a context provider maps when you configure it on the identity provider, and AWS STS rejects a session whose session token exceeds the maximum size with `PackedPolicyTooLarge`.
Type: String to string map
Value Length Constraints: Maximum length of 128.
Required: No

## See Also
<a name="API_TransactionContext_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sts-2011-06-15/TransactionContext)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sts-2011-06-15/TransactionContext)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sts-2011-06-15/TransactionContext)
