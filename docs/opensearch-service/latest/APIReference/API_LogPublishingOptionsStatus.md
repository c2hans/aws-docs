---
source_url: https://docs.aws.amazon.com/opensearch-service/latest/APIReference/API_LogPublishingOptionsStatus.html
---

# LogPublishingOptionsStatus
<a name="API_LogPublishingOptionsStatus"></a>

The configured log publishing options for the domain and their current status.

## Contents
<a name="API_LogPublishingOptionsStatus_Contents"></a>

 ** Options **   <a name="opensearchservice-Type-LogPublishingOptionsStatus-Options"></a>
The log publishing options configured for the domain.
Type: String to [LogPublishingOption](API_LogPublishingOption.md) object map
Valid Keys: `INDEX_SLOW_LOGS | SEARCH_SLOW_LOGS | ES_APPLICATION_LOGS | AUDIT_LOGS`
Required: No

 ** Status **   <a name="opensearchservice-Type-LogPublishingOptionsStatus-Status"></a>
The status of the log publishing options for the domain.
Type: [OptionStatus](API_OptionStatus.md) object
Required: No

## See Also
<a name="API_LogPublishingOptionsStatus_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/opensearch-2021-01-01/LogPublishingOptionsStatus)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/opensearch-2021-01-01/LogPublishingOptionsStatus)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/opensearch-2021-01-01/LogPublishingOptionsStatus)
