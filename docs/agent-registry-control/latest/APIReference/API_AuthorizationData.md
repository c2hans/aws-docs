---
source_url: https://docs.aws.amazon.com/agent-registry-control/latest/APIReference/API_AuthorizationData.html
---

# AuthorizationData

The authorization that a user must complete before a registry record can synchronize from its source. Only `CreateRegistryRecord` and `UpdateRegistryRecord` return it. `GetRegistryRecord` and `ListRegistryRecords` never do.

## Contents
<a name="API_AuthorizationData_Contents"></a>

**Important**
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** oauth2 **   <a name="agentregistrycontrol-Type-AuthorizationData-oauth2"></a>
The OAuth 2.0 authorization that a GitHub user must approve.
Type: [OAuth2AuthorizationData](API_OAuth2AuthorizationData.md) object
Required: No

## See Also
<a name="API_AuthorizationData_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/agent-registry-control-2025-12-01/AuthorizationData)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/agent-registry-control-2025-12-01/AuthorizationData)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/agent-registry-control-2025-12-01/AuthorizationData)
