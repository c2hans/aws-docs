---
source_url: https://docs.aws.amazon.com/AmazonS3/latest/API/API_ReplicationRule.html
---

# ReplicationRule
<a name="API_ReplicationRule"></a>

Specifies which Amazon S3 objects to replicate and where to store the replicas.

## Contents
<a name="API_ReplicationRule_Contents"></a>

 ** Destination **   <a name="AmazonS3-Type-ReplicationRule-Destination"></a>
A container for information about the replication destination and its configurations including enabling the S3 Replication Time Control (S3 RTC).
Type: [Destination](API_Destination.md) data type
Required: Yes

 ** Status **   <a name="AmazonS3-Type-ReplicationRule-Status"></a>
Specifies whether the rule is enabled.
Type: String
Valid Values: `Enabled | Disabled`
Required: Yes

 ** DeleteMarkerReplication **   <a name="AmazonS3-Type-ReplicationRule-DeleteMarkerReplication"></a>
Specifies whether Amazon S3 replicates delete markers. If you specify a `Filter` in your replication configuration, you must also include a `DeleteMarkerReplication` element. If your `Filter` includes a `Tag` element, the `DeleteMarkerReplication` `Status` must be set to Disabled, because Amazon S3 does not support replicating delete markers for tag-based rules. For an example configuration, see [Basic Rule Configuration](https://docs.aws.amazon.com/AmazonS3/latest/dev/replication-add-config.html#replication-config-min-rule-config).
For more information about delete marker replication, see [Basic Rule Configuration](https://docs.aws.amazon.com/AmazonS3/latest/dev/delete-marker-replication.html).
If you are using an earlier version of the replication configuration, Amazon S3 handles replication of delete markers differently. For more information, see [Backward Compatibility](https://docs.aws.amazon.com/AmazonS3/latest/dev/replication-add-config.html#replication-backward-compat-considerations).
Type: [DeleteMarkerReplication](API_DeleteMarkerReplication.md) data type
Required: No

 ** ExistingObjectReplication **   <a name="AmazonS3-Type-ReplicationRule-ExistingObjectReplication"></a>
Optional configuration to replicate existing source bucket objects.
This parameter is no longer supported. To replicate existing objects, see [Replicating existing objects with S3 Batch Replication](https://docs.aws.amazon.com/AmazonS3/latest/userguide/s3-batch-replication-batch.html) in the *Amazon S3 User Guide*.
Type: [ExistingObjectReplication](API_ExistingObjectReplication.md) data type
Required: No

 ** Filter **   <a name="AmazonS3-Type-ReplicationRule-Filter"></a>
A filter that identifies the subset of objects to which the replication rule applies. A `Filter` must specify exactly one `Prefix`, `Tag`, or an `And` child element.
Type: [ReplicationRuleFilter](API_ReplicationRuleFilter.md) data type
Required: No

 ** ID **   <a name="AmazonS3-Type-ReplicationRule-ID"></a>
A unique identifier for the rule. The maximum value is 255 characters.
Type: String
Required: No

 ** Prefix **   <a name="AmazonS3-Type-ReplicationRule-Prefix"></a>
 *This member has been deprecated.*
An object key name prefix that identifies the object or objects to which the rule applies. The maximum prefix length is 1,024 characters. To include all objects in a bucket, specify an empty string.
Replacement must be made for object keys containing special characters (such as carriage returns) when using XML requests. For more information, see [ XML related object key constraints](https://docs.aws.amazon.com/AmazonS3/latest/userguide/object-keys.html#object-key-xml-related-constraints).
Type: String
Required: No

 ** Priority **   <a name="AmazonS3-Type-ReplicationRule-Priority"></a>
The priority indicates which rule has precedence whenever two or more replication rules conflict. Amazon S3 will attempt to replicate objects according to all replication rules. However, if there are two or more rules with the same destination bucket, then objects will be replicated according to the rule with the highest priority. The higher the number, the higher the priority.
For more information, see [Replication](https://docs.aws.amazon.com/AmazonS3/latest/dev/replication.html) in the *Amazon S3 User Guide*.
Type: Integer
Required: No

 ** SourceSelectionCriteria **   <a name="AmazonS3-Type-ReplicationRule-SourceSelectionCriteria"></a>
A container that describes additional filters for identifying the source objects that you want to replicate. You can choose to enable or disable the replication of these objects. Currently, Amazon S3 supports only the filter that you can specify for objects created with server-side encryption using a customer managed key stored in AWS Key Management Service (SSE-KMS).
Type: [SourceSelectionCriteria](API_SourceSelectionCriteria.md) data type
Required: No

## See Also
<a name="API_ReplicationRule_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/s3-2006-03-01/ReplicationRule)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/s3-2006-03-01/ReplicationRule)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/s3-2006-03-01/ReplicationRule)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Simple Storage Service (S3). To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonS3` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
