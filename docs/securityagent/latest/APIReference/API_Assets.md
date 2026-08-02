---
source_url: https://docs.aws.amazon.com/securityagent/latest/APIReference/API_Assets.html
---

# Assets
<a name="API_Assets"></a>

The collection of assets used in a pentest configuration, including endpoints, actors, documents, source code repositories, and integrated repositories.

## Contents
<a name="API_Assets_Contents"></a>

 ** actors **   <a name="securityagent-Type-Assets-actors"></a>
The list of actors used during penetration testing.
Type: Array of [Actor](API_Actor.md) objects
Required: No

 ** documents **   <a name="securityagent-Type-Assets-documents"></a>
The list of documents that provide context for the pentest.
Type: Array of [DocumentInfo](API_DocumentInfo.md) objects
Required: No

 ** endpoints **   <a name="securityagent-Type-Assets-endpoints"></a>
The list of endpoints to test during the pentest.
Type: Array of [Endpoint](API_Endpoint.md) objects
Required: No

 ** integratedRepositories **   <a name="securityagent-Type-Assets-integratedRepositories"></a>
The list of integrated repositories associated with the pentest.
Type: Array of [IntegratedRepository](API_IntegratedRepository.md) objects
Required: No

 ** sourceCode **   <a name="securityagent-Type-Assets-sourceCode"></a>
The list of source code repositories to analyze during the pentest.
Type: Array of [SourceCodeRepository](API_SourceCodeRepository.md) objects
Required: No

## See Also
<a name="API_Assets_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securityagent-2025-09-06/Assets)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securityagent-2025-09-06/Assets)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securityagent-2025-09-06/Assets)
