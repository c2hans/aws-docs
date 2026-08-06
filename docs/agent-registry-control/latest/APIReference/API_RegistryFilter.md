---
source_url: https://docs.aws.amazon.com/agent-registry-control/latest/APIReference/API_RegistryFilter.html
---

# RegistryFilter
<a name="API_RegistryFilter"></a>

A single filter applied to a ListRegistries request.

## Contents
<a name="API_RegistryFilter_Contents"></a>

 ** name **   <a name="agentregistrycontrol-Type-RegistryFilter-name"></a>
The attribute to filter on
Type: String
Valid Values: `status | discoveryConfiguration.authorizerType`
Required: Yes

 ** values **   <a name="agentregistrycontrol-Type-RegistryFilter-values"></a>
The values to match for the attribute
Type: Array of strings
Array Members: Fixed number of 1 item.
Length Constraints: Minimum length of 1. Maximum length of 255.
Required: Yes

## See Also
<a name="API_RegistryFilter_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/vestry-control-plane-2025-12-01/RegistryFilter)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/vestry-control-plane-2025-12-01/RegistryFilter)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/vestry-control-plane-2025-12-01/RegistryFilter)
