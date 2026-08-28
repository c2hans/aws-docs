---
source_url: https://docs.aws.amazon.com/opensearch-service/latest/APIReference/API_StorageType.html
---

# StorageType
<a name="API_StorageType"></a>

A list of storage types for an Amazon OpenSearch Service domain that are available for a given intance type.

## Contents
<a name="API_StorageType_Contents"></a>

 ** StorageSubTypeName **   <a name="opensearchservice-Type-StorageType-StorageSubTypeName"></a>
The storage sub-type, such as `gp3` or `io1`.
Type: String
Required: No

 ** StorageTypeLimits **   <a name="opensearchservice-Type-StorageType-StorageTypeLimits"></a>
Limits that are applicable for the given storage type.
Type: Array of [StorageTypeLimit](API_StorageTypeLimit.md) objects
Required: No

 ** StorageTypeName **   <a name="opensearchservice-Type-StorageType-StorageTypeName"></a>
The name of the storage type.
Type: String
Required: No

## See Also
<a name="API_StorageType_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/opensearch-2021-01-01/StorageType)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/opensearch-2021-01-01/StorageType)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/opensearch-2021-01-01/StorageType)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon OpenSearch Service. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query opensearch-service` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
