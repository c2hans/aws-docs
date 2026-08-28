---
source_url: https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_SourceSelectionCriteria.html
---

# SourceSelectionCriteria
<a name="API_control_SourceSelectionCriteria"></a>

A container that describes additional filters for identifying the source objects that you want to replicate. You can choose to enable or disable the replication of these objects.

## Contents
<a name="API_control_SourceSelectionCriteria_Contents"></a>

 ** ReplicaModifications **   <a name="AmazonS3-Type-control_SourceSelectionCriteria-ReplicaModifications"></a>
A filter that you can use to specify whether replica modification sync is enabled. S3 on Outposts replica modification sync can help you keep object metadata synchronized between replicas and source objects. By default, S3 on Outposts replicates metadata from the source objects to the replicas only. When replica modification sync is enabled, S3 on Outposts replicates metadata changes made to the replica copies back to the source object, making the replication bidirectional.
To replicate object metadata modifications on replicas, you can specify this element and set the `Status` of this element to `Enabled`.
You must enable replica modification sync on the source and destination buckets to replicate replica metadata changes between the source and the replicas.
Type: [ReplicaModifications](API_control_ReplicaModifications.md) data type
Required: No

 ** SseKmsEncryptedObjects **   <a name="AmazonS3-Type-control_SourceSelectionCriteria-SseKmsEncryptedObjects"></a>
A filter that you can use to select Amazon S3 objects that are encrypted with server-side encryption by using AWS Key Management Service (AWS KMS) keys. If you include `SourceSelectionCriteria` in the replication configuration, this element is required.
This is not supported by Amazon S3 on Outposts buckets.
Type: [SseKmsEncryptedObjects](API_control_SseKmsEncryptedObjects.md) data type
Required: No

## See Also
<a name="API_control_SourceSelectionCriteria_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/s3control-2018-08-20/SourceSelectionCriteria)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/s3control-2018-08-20/SourceSelectionCriteria)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/s3control-2018-08-20/SourceSelectionCriteria)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Simple Storage Service (S3). To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonS3` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
