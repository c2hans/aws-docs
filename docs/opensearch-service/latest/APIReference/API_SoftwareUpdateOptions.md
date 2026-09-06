---
source_url: https://docs.aws.amazon.com/opensearch-service/latest/APIReference/API_SoftwareUpdateOptions.html
---

# SoftwareUpdateOptions
<a name="API_SoftwareUpdateOptions"></a>

Options for configuring service software updates for a domain.

## Contents
<a name="API_SoftwareUpdateOptions_Contents"></a>

 ** AutoSoftwareUpdateEnabled **   <a name="opensearchservice-Type-SoftwareUpdateOptions-AutoSoftwareUpdateEnabled"></a>
Whether automatic service software updates are enabled for the domain.
Type: Boolean
Required: No

 ** UseLatestServiceSoftwareForBlueGreen **   <a name="opensearchservice-Type-SoftwareUpdateOptions-UseLatestServiceSoftwareForBlueGreen"></a>
Whether the domain should use the latest service software version during a blue/green deployment. If enabled, the domain will automatically use the latest available service software when a blue/green deployment is triggered.
Type: Boolean
Required: No

## See Also
<a name="API_SoftwareUpdateOptions_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/opensearch-2021-01-01/SoftwareUpdateOptions)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/opensearch-2021-01-01/SoftwareUpdateOptions)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/opensearch-2021-01-01/SoftwareUpdateOptions)
