---
source_url: https://docs.aws.amazon.com/continuum/latest/APIReference/API_RemediationProposalBody.html
---

# RemediationProposalBody
<a name="API_RemediationProposalBody"></a>

Projected content for a REMEDIATION\_PROPOSAL artifact: the patch the remediation agent produced, with the descriptors needed to apply and verify it.

## Contents
<a name="API_RemediationProposalBody_Contents"></a>

 ** patch **   <a name="continuum-Type-RemediationProposalBody-patch"></a>
The patch.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 5242880.
Required: Yes

 ** filename **   <a name="continuum-Type-RemediationProposalBody-filename"></a>
The filename.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Required: No

 ** format **   <a name="continuum-Type-RemediationProposalBody-format"></a>
The format.
Type: String
Valid Values: `GIT_MAILBOX_PATCH | GIT_BINARY_DIFF | GIT_DIFF`
Required: No

 ** patchSha256 **   <a name="continuum-Type-RemediationProposalBody-patchSha256"></a>
The patch Sha256.
Type: String
Length Constraints: Fixed length of 64.
Pattern: `[0-9a-f]{64}`
Required: No

## See Also
<a name="API_RemediationProposalBody_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/continuum-2022-07-26/RemediationProposalBody)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/continuum-2022-07-26/RemediationProposalBody)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/continuum-2022-07-26/RemediationProposalBody)
