---
source_url: https://docs.aws.amazon.com/continuum/latest/APIReference/API_IssueArtifactBody.html
---

# IssueArtifactBody
<a name="API_IssueArtifactBody"></a>

The projected body of an artifact. The active member is selected by the artifact's artifactType, and for a type that carries more than one payload kind by the stored content's own discriminator; `raw` carries content for types with no defined shape yet and for content that did not match its shape.

## Contents
<a name="API_IssueArtifactBody_Contents"></a>

**Important**
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** patch **   <a name="continuum-Type-IssueArtifactBody-patch"></a>
Projected content for a PATCH artifact: the remediation patch for one repository, with the descriptors needed to verify and apply it and the state of its delivery to the customer's own bucket or repository.
Type: [PatchBody](API_PatchBody.md) object
Required: No

 ** prevalidationSignals **   <a name="continuum-Type-IssueArtifactBody-prevalidationSignals"></a>
Projected content for an EVIDENCE artifact carrying prioritization's prevalidation signals.
Type: [PrevalidationSignalsBody](API_PrevalidationSignalsBody.md) object
Required: No

 ** raw **   <a name="continuum-Type-IssueArtifactBody-raw"></a>
The raw.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 5242880.
Required: No

 ** remediationProposal **   <a name="continuum-Type-IssueArtifactBody-remediationProposal"></a>
Projected content for a REMEDIATION\_PROPOSAL artifact: the patch the remediation agent produced, with the descriptors needed to apply and verify it.
Type: [RemediationProposalBody](API_RemediationProposalBody.md) object
Required: No

 ** validationEvidence **   <a name="continuum-Type-IssueArtifactBody-validationEvidence"></a>
Projected content for a VALIDATION\_EVIDENCE artifact: the validation agent's durable proof of exploitability.
Type: [ValidationEvidenceBody](API_ValidationEvidenceBody.md) object
Required: No

## See Also
<a name="API_IssueArtifactBody_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/continuum-2022-07-26/IssueArtifactBody)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/continuum-2022-07-26/IssueArtifactBody)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/continuum-2022-07-26/IssueArtifactBody)
