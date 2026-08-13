---
source_url: https://docs.aws.amazon.com/securityagent/latest/APIReference/API_IntegratedRepository.html
---

# IntegratedRepository
<a name="API_IntegratedRepository"></a>

Represents a code repository that is integrated with the service through a third-party provider.

## Contents
<a name="API_IntegratedRepository_Contents"></a>

 ** integrationId **   <a name="securityagent-Type-IntegratedRepository-integrationId"></a>
The unique identifier of the integration that provides access to the repository.
Type: String
Required: Yes

 ** providerResourceId **   <a name="securityagent-Type-IntegratedRepository-providerResourceId"></a>
The provider-specific resource identifier for the repository.
Type: String
Required: Yes

 ** branch **   <a name="securityagent-Type-IntegratedRepository-branch"></a>
An optional override for the repository branch.
Type: String
Required: No

## See Also
<a name="API_IntegratedRepository_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securityagent-2025-09-06/IntegratedRepository)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securityagent-2025-09-06/IntegratedRepository)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securityagent-2025-09-06/IntegratedRepository)
