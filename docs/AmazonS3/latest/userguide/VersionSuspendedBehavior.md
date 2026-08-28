---
source_url: https://docs.aws.amazon.com/AmazonS3/latest/userguide/VersionSuspendedBehavior.html
---

# Working with objects in a versioning-suspended bucket
<a name="VersionSuspendedBehavior"></a>

In Amazon S3, you can suspend versioning to stop accruing new versions of the same object in a bucket. You might do this because you only want a single version of an object in a bucket. Or, you might not want to accrue charges for multiple versions.

When you suspend versioning, existing objects in your bucket do not change. What changes is how Amazon S3 handles objects in future requests. The topics in this section explain various object operations in a versioning-suspended bucket, including adding, retrieving, and deleting objects.

For more information about S3 Versioning, see [Retaining multiple versions of objects with S3 Versioning](Versioning.md). For more information about retrieving object versions, see [Retrieving object versions from a versioning-enabled bucket](RetrievingObjectVersions.md).

**Topics**
+ [Adding objects to versioning-suspended buckets](AddingObjectstoVersionSuspendedBuckets.md)
+ [Retrieving objects from versioning-suspended buckets](RetrievingObjectsfromVersioningSuspendedBuckets.md)
+ [Deleting objects from versioning-suspended buckets](DeletingObjectsfromVersioningSuspendedBuckets.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Simple Storage Service (S3). To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonS3` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
