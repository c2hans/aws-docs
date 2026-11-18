---
source_url: https://docs.aws.amazon.com/AmazonECR/latest/APIReference/API_DeleteReplication.html
---

# DeleteReplication
<a name="API_DeleteReplication"></a>

The delete replication configuration for a replication rule. When delete replication is enabled, the service replicates image deletions and image tag removals in the source registry to the replication destinations.

## Contents
<a name="API_DeleteReplication_Contents"></a>

 ** enabled **   <a name="ECR-Type-DeleteReplication-enabled"></a>
Specifies whether delete replication is enabled. If set to `true`, the service replicates image deletions and image tag removals from the source registry to each replication destination. If set to `false`, the service does not replicate image deletions or image tag removals.
Type: Boolean
Required: Yes

## See Also
<a name="API_DeleteReplication_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ecr-2015-09-21/DeleteReplication)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ecr-2015-09-21/DeleteReplication)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ecr-2015-09-21/DeleteReplication)
