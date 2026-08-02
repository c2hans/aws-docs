---
source_url: https://docs.aws.amazon.com/opensearch-service/latest/APIReference/API_StorageTypeLimit.html
---

# StorageTypeLimit
<a name="API_StorageTypeLimit"></a>

Limits that are applicable for the given Amazon OpenSearch Service storage type.

## Contents
<a name="API_StorageTypeLimit_Contents"></a>

 ** LimitName **   <a name="opensearchservice-Type-StorageTypeLimit-LimitName"></a>
 Name of storage limits that are applicable for the given storage type. If `StorageType` is `ebs`, the following options are available:
+  **MinimumVolumeSize** - Minimum volume size that is available for the given storage type. Can be empty if not applicable.
+  **MaximumVolumeSize** - Maximum volume size that is available for the given storage type. Can be empty if not applicable.
+  **MaximumIops** - Maximum amount of IOPS that is available for the given the storage type. Can be empty if not applicable.
+  **MinimumIops** - Minimum amount of IOPS that is available for the given the storage type. Can be empty if not applicable.
+  **MaximumThroughput** - Maximum amount of throughput that is available for the given the storage type. Can be empty if not applicable.
+  **MinimumThroughput** - Minimum amount of throughput that is available for the given the storage type. Can be empty if not applicable.
Type: String
Required: No

 ** LimitValues **   <a name="opensearchservice-Type-StorageTypeLimit-LimitValues"></a>
The limit values.
Type: Array of strings
Required: No

## See Also
<a name="API_StorageTypeLimit_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/opensearch-2021-01-01/StorageTypeLimit)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/opensearch-2021-01-01/StorageTypeLimit)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/opensearch-2021-01-01/StorageTypeLimit)
