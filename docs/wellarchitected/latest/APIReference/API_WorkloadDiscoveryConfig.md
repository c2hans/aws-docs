---
source_url: https://docs.aws.amazon.com/wellarchitected/latest/APIReference/API_WorkloadDiscoveryConfig.html
---

# WorkloadDiscoveryConfig
<a name="API_WorkloadDiscoveryConfig"></a>

Discovery configuration associated to the workload.

## Contents
<a name="API_WorkloadDiscoveryConfig_Contents"></a>

 ** TrustedAdvisorIntegrationStatus **   <a name="wellarchitected-Type-WorkloadDiscoveryConfig-TrustedAdvisorIntegrationStatus"></a>
Discovery integration status in respect to Trusted Advisor for the workload.
Type: String
Valid Values: `ENABLED | DISABLED`
Required: No

 ** WorkloadResourceDefinition **   <a name="wellarchitected-Type-WorkloadDiscoveryConfig-WorkloadResourceDefinition"></a>
The mode to use for identifying resources associated with the workload.
You can specify `WORKLOAD_METADATA`, `APP_REGISTRY`, or both.
Type: Array of strings
Valid Values: `WORKLOAD_METADATA | APP_REGISTRY`
Required: No

## See Also
<a name="API_WorkloadDiscoveryConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/wellarchitected-2020-03-31/WorkloadDiscoveryConfig)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/wellarchitected-2020-03-31/WorkloadDiscoveryConfig)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/wellarchitected-2020-03-31/WorkloadDiscoveryConfig)
