---
source_url: https://docs.aws.amazon.com/signer/latest/api/API_SigningProfileRevocationRecord.html
---

# SigningProfileRevocationRecord
<a name="API_SigningProfileRevocationRecord"></a>

Revocation information for a signing profile.

## Contents
<a name="API_SigningProfileRevocationRecord_Contents"></a>

 ** revocationEffectiveFrom **   <a name="signer-Type-SigningProfileRevocationRecord-revocationEffectiveFrom"></a>
The time when revocation becomes effective.
Type: Timestamp
Required: No

 ** revokedAt **   <a name="signer-Type-SigningProfileRevocationRecord-revokedAt"></a>
The time when the signing profile was revoked.
Type: Timestamp
Required: No

 ** revokedBy **   <a name="signer-Type-SigningProfileRevocationRecord-revokedBy"></a>
The identity of the revoker.
Type: String
Required: No

## See Also
<a name="API_SigningProfileRevocationRecord_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/signer-2017-08-25/SigningProfileRevocationRecord)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/signer-2017-08-25/SigningProfileRevocationRecord)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/signer-2017-08-25/SigningProfileRevocationRecord)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Signer. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query signer` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
