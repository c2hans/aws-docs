---
source_url: https://docs.aws.amazon.com/bedrock/latest/APIReference/API_TrustedAccessProgramApplicationResult.html
---

# TrustedAccessProgramApplicationResult

Result of preparing an application. A provider handoff does not submit an application, grant eligibility, or change enrollment. Clients must tolerate unknown union members.

## Contents
<a name="API_TrustedAccessProgramApplicationResult_Contents"></a>

**Important**
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** providerHandoff **   <a name="bedrock-Type-TrustedAccessProgramApplicationResult-providerHandoff"></a>
Information for continuing the application with the provider.
Type: [TrustedAccessProgramProviderHandoff](API_TrustedAccessProgramProviderHandoff.md) object
Required: No

## See Also
<a name="API_TrustedAccessProgramApplicationResult_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-2023-04-20/TrustedAccessProgramApplicationResult)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-2023-04-20/TrustedAccessProgramApplicationResult)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-2023-04-20/TrustedAccessProgramApplicationResult)
