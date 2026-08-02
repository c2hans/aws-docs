---
source_url: https://docs.aws.amazon.com/resilience-hub/v2/APIReference/API_DependencyDiscoveryConfig.html
---

# DependencyDiscoveryConfig
<a name="API_DependencyDiscoveryConfig"></a>

Configuration for dependency discovery on a service.

## Contents
<a name="API_DependencyDiscoveryConfig_Contents"></a>

 ** status **   <a name="ngresiliencehub-Type-DependencyDiscoveryConfig-status"></a>
The current status of dependency discovery.
Type: String
Valid Values: `ENABLED | INITIALIZING | DISABLED`
Required: Yes

 ** eligibleResourceCount **   <a name="ngresiliencehub-Type-DependencyDiscoveryConfig-eligibleResourceCount"></a>
The count of resources eligible for dependency attribution.
Type: Integer
Valid Range: Minimum value of 0.
Required: No

 ** message **   <a name="ngresiliencehub-Type-DependencyDiscoveryConfig-message"></a>
A status message for dependency discovery, displayed during the initialization state.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Required: No

 ** updatedAt **   <a name="ngresiliencehub-Type-DependencyDiscoveryConfig-updatedAt"></a>
The timestamp when dependency discovery was last updated.
Type: Timestamp
Required: No

## See Also
<a name="API_DependencyDiscoveryConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/resiliencehubv2-2026-02-17/DependencyDiscoveryConfig)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/resiliencehubv2-2026-02-17/DependencyDiscoveryConfig)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/resiliencehubv2-2026-02-17/DependencyDiscoveryConfig)
