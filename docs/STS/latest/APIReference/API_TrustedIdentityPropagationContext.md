---
source_url: https://docs.aws.amazon.com/STS/latest/APIReference/API_TrustedIdentityPropagationContext.html
---

# TrustedIdentityPropagationContext

The trusted identity propagation context that AWS STS set in a session from the identity provider's token. A member is absent when the session has none of its keys.

## Contents
<a name="API_TrustedIdentityPropagationContext_Contents"></a>

 ** OriginIdentity **
The identity of the end user on whose behalf the session acts.
Type: [OriginIdentity](API_OriginIdentity.md) object
Required: No

 ** TransactionContext **
Additional claims about the request that the identity provider asserted.
Type: [TransactionContext](API_TransactionContext.md) object
Required: No

## See Also
<a name="API_TrustedIdentityPropagationContext_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sts-2011-06-15/TrustedIdentityPropagationContext)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sts-2011-06-15/TrustedIdentityPropagationContext)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sts-2011-06-15/TrustedIdentityPropagationContext)
