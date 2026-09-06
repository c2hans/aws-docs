---
source_url: https://docs.aws.amazon.com/opensearch-service/latest/APIReference/API_OffPeakWindowOptions.html
---

# OffPeakWindowOptions
<a name="API_OffPeakWindowOptions"></a>

Options for a domain's [off-peak window](https://docs.aws.amazon.com/opensearch-service/latest/APIReference/API_OffPeakWindow.html), during which OpenSearch Service can perform mandatory configuration changes on the domain.

## Contents
<a name="API_OffPeakWindowOptions_Contents"></a>

 ** Enabled **   <a name="opensearchservice-Type-OffPeakWindowOptions-Enabled"></a>
Whether to enable an off-peak window.
This option is only available when modifying a domain created prior to February 16, 2023, not when creating a new domain. All domains created after this date have the off-peak window enabled by default. You can't disable the off-peak window after it's enabled for a domain.
Type: Boolean
Required: No

 ** OffPeakWindow **   <a name="opensearchservice-Type-OffPeakWindowOptions-OffPeakWindow"></a>
Off-peak window settings for the domain.
Type: [OffPeakWindow](API_OffPeakWindow.md) object
Required: No

## See Also
<a name="API_OffPeakWindowOptions_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/opensearch-2021-01-01/OffPeakWindowOptions)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/opensearch-2021-01-01/OffPeakWindowOptions)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/opensearch-2021-01-01/OffPeakWindowOptions)
