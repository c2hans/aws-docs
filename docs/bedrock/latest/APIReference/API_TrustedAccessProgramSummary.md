---
source_url: https://docs.aws.amazon.com/bedrock/latest/APIReference/API_TrustedAccessProgramSummary.html
---

# TrustedAccessProgramSummary

Program details and participation resolved for the calling account and optional named project.

## Contents
<a name="API_TrustedAccessProgramSummary_Contents"></a>

 ** description **   <a name="bedrock-Type-TrustedAccessProgramSummary-description"></a>
Description of the program and its effects on model access or data handling.
Type: String
Required: Yes

 ** detailsUrl **   <a name="bedrock-Type-TrustedAccessProgramSummary-detailsUrl"></a>
URL with program details, terms, and instructions for obtaining access.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 4096.
Pattern: `https://[^\s]+`
Required: Yes

 ** name **   <a name="bedrock-Type-TrustedAccessProgramSummary-name"></a>
Display name of the program.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Required: Yes

 ** optIn **   <a name="bedrock-Type-TrustedAccessProgramSummary-optIn"></a>
Resolved customer preference, preserved independently of eligibility, including while revoked.
Type: String
Valid Values: `inherit | enabled | disabled`
Required: Yes

 ** programId **   <a name="bedrock-Type-TrustedAccessProgramSummary-programId"></a>
Identifier of the trusted access program.
Type: String
Length Constraints: Minimum length of 3. Maximum length of 64.
Pattern: `[a-z0-9]+-[a-z0-9-]+`
Required: Yes

 ** providerName **   <a name="bedrock-Type-TrustedAccessProgramSummary-providerName"></a>
Name of the model provider offering the program.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 20.
Pattern: `.*`
Required: Yes

 ** resolvedFor **   <a name="bedrock-Type-TrustedAccessProgramSummary-resolvedFor"></a>
Account and optional project context for which participation was resolved.
Type: [TrustedAccessResolutionContext](API_TrustedAccessResolutionContext.md) object
Required: Yes

 ** source **   <a name="bedrock-Type-TrustedAccessProgramSummary-source"></a>
Scope deciding the status. This can differ from the scope supplying the resolved opt-in preference and enrollment timestamps.
Type: String
Valid Values: `organization | account | project | program_default`
Required: Yes

 ** status **   <a name="bedrock-Type-TrustedAccessProgramSummary-status"></a>
Participation status resolved for the account and optional project context.
Type: String
Valid Values: `requestable | eligible | enabled | disabled | revoked`
Required: Yes

 ** eligibilityScope **   <a name="bedrock-Type-TrustedAccessProgramSummary-eligibilityScope"></a>
Scope supplying the applicable approval or most-specific revocation. Omitted when no approval or revocation applies.
Type: String
Valid Values: `organization | account | project | program_default`
Required: No

 ** enrollmentUrl **   <a name="bedrock-Type-TrustedAccessProgramSummary-enrollmentUrl"></a>
Provider application intake URL. Omitted when the program has no customer-facing intake URL.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 4096.
Pattern: `https://[^\s]+`
Required: No

 ** statusReason **   <a name="bedrock-Type-TrustedAccessProgramSummary-statusReason"></a>
Nonempty explanation for requestable or revoked status. Omitted for other statuses.
Type: String
Required: No

 ** updatedAt **   <a name="bedrock-Type-TrustedAccessProgramSummary-updatedAt"></a>
Last change to the enrollment supplying the resolved opt-in. Present for enabled or disabled, including while revoked; omitted for inherit.
Type: Timestamp
Required: No

## See Also
<a name="API_TrustedAccessProgramSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-2023-04-20/TrustedAccessProgramSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-2023-04-20/TrustedAccessProgramSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-2023-04-20/TrustedAccessProgramSummary)
