---
source_url: https://docs.aws.amazon.com/ses/latest/APIReference/API_IdentityVerificationAttributes.html
---

# IdentityVerificationAttributes
<a name="API_IdentityVerificationAttributes"></a>

Represents the verification attributes of a single identity.

## Contents
<a name="API_IdentityVerificationAttributes_Contents"></a>

 ** VerificationStatus **
The verification status of the identity: "Pending", "Success", "Failed", or "TemporaryFailure".
Type: String
Valid Values: `Pending | Success | Failed | TemporaryFailure | NotStarted`
Required: Yes

 ** VerificationToken **
The verification token for a domain identity. Null for email address identities.
Type: String
Required: No

## See Also
<a name="API_IdentityVerificationAttributes_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/email-2010-12-01/IdentityVerificationAttributes)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/email-2010-12-01/IdentityVerificationAttributes)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/email-2010-12-01/IdentityVerificationAttributes)
