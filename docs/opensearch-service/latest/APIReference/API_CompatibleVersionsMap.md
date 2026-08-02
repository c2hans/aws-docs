---
source_url: https://docs.aws.amazon.com/opensearch-service/latest/APIReference/API_CompatibleVersionsMap.html
---

# CompatibleVersionsMap
<a name="API_CompatibleVersionsMap"></a>

A map of OpenSearch or Elasticsearch versions and the versions you can upgrade them to.

## Contents
<a name="API_CompatibleVersionsMap_Contents"></a>

 ** SourceVersion **   <a name="opensearchservice-Type-CompatibleVersionsMap-SourceVersion"></a>
The current version that the OpenSearch Service domain is running.
Type: String
Length Constraints: Minimum length of 14. Maximum length of 18.
Pattern: `^Elasticsearch_[0-9]{1}\.[0-9]{1,2}$|^OpenSearch_[0-9]{1,2}\.[0-9]{1,2}$`
Required: No

 ** TargetVersions **   <a name="opensearchservice-Type-CompatibleVersionsMap-TargetVersions"></a>
The possible versions that you can upgrade the domain to.
Type: Array of strings
Length Constraints: Minimum length of 14. Maximum length of 18.
Pattern: `^Elasticsearch_[0-9]{1}\.[0-9]{1,2}$|^OpenSearch_[0-9]{1,2}\.[0-9]{1,2}$`
Required: No

## See Also
<a name="API_CompatibleVersionsMap_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/opensearch-2021-01-01/CompatibleVersionsMap)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/opensearch-2021-01-01/CompatibleVersionsMap)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/opensearch-2021-01-01/CompatibleVersionsMap)
