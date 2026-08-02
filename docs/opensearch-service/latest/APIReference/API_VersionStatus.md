---
source_url: https://docs.aws.amazon.com/opensearch-service/latest/APIReference/API_VersionStatus.html
---

# VersionStatus
<a name="API_VersionStatus"></a>

The status of the the OpenSearch or Elasticsearch version options for the specified Amazon OpenSearch Service domain.

## Contents
<a name="API_VersionStatus_Contents"></a>

 ** Options **   <a name="opensearchservice-Type-VersionStatus-Options"></a>
The OpenSearch or Elasticsearch version for the specified domain.
Type: String
Length Constraints: Minimum length of 14. Maximum length of 18.
Pattern: `^Elasticsearch_[0-9]{1}\.[0-9]{1,2}$|^OpenSearch_[0-9]{1,2}\.[0-9]{1,2}$`
Required: Yes

 ** Status **   <a name="opensearchservice-Type-VersionStatus-Status"></a>
The status of the version options for the specified domain.
Type: [OptionStatus](API_OptionStatus.md) object
Required: Yes

## See Also
<a name="API_VersionStatus_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/opensearch-2021-01-01/VersionStatus)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/opensearch-2021-01-01/VersionStatus)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/opensearch-2021-01-01/VersionStatus)
