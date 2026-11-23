---
source_url: https://docs.aws.amazon.com/bedrock/latest/APIReference/API_TrustedAccessProgramProviderHandoff.html
---

# TrustedAccessProgramProviderHandoff

Information needed to continue an application with the provider.

## Contents
<a name="API_TrustedAccessProgramProviderHandoff_Contents"></a>

 ** applicationToken **   <a name="bedrock-Type-TrustedAccessProgramProviderHandoff-applicationToken"></a>
Opaque token binding the application to the authenticated customer, requested program, and scope.
Type: String
Length Constraints: Minimum length of 1.
Required: Yes

 ** applicationTokenExpiresAt **   <a name="bedrock-Type-TrustedAccessProgramProviderHandoff-applicationTokenExpiresAt"></a>
Deadline for the provider to accept the application context. Start another application handoff if the token expires before acceptance.
Type: Timestamp
Required: Yes

 ** enrollmentUrl **   <a name="bedrock-Type-TrustedAccessProgramProviderHandoff-enrollmentUrl"></a>
Provider intake URL. When present, open it and paste the complete application token into the provider's token field. Omitted when the provider receives the application token through a separate integration.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 4096.
Pattern: `https://[^\s]+`
Required: No

## See Also
<a name="API_TrustedAccessProgramProviderHandoff_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-2023-04-20/TrustedAccessProgramProviderHandoff)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-2023-04-20/TrustedAccessProgramProviderHandoff)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-2023-04-20/TrustedAccessProgramProviderHandoff)
