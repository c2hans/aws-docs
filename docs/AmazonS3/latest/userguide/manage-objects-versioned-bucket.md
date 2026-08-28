---
source_url: https://docs.aws.amazon.com/AmazonS3/latest/userguide/manage-objects-versioned-bucket.html
---

# Working with objects in a versioning-enabled bucket
<a name="manage-objects-versioned-bucket"></a>

Objects that are stored in an Amazon S3 bucket before you set the versioning state have a version ID of `null`. When you enable versioning, existing objects in your bucket do not change. What changes is how Amazon S3 handles the objects in future requests.

**Transitioning object versions**
You can define lifecycle configuration rules for objects that have a well-defined lifecycle to transition object versions to the S3 Glacier Flexible Retrieval storage class at a specific time in the object's lifetime. For more information, see [Managing the lifecycle of objects](object-lifecycle-mgmt.md).

The topics in this section explain various object operations in a versioning-enabled bucket. For more information about versioning, see [Retaining multiple versions of objects with S3 Versioning](Versioning.md).

**Topics**
+ [Adding objects to versioning-enabled buckets](AddingObjectstoVersioningEnabledBuckets.md)
+ [Listing objects in a versioning-enabled bucket](list-obj-version-enabled-bucket.md)
+ [Retrieving object versions from a versioning-enabled bucket](RetrievingObjectVersions.md)
+ [Deleting object versions from a versioning-enabled bucket](DeletingObjectVersions.md)
+ [Configuring versioned object permissions](VersionedObjectPermissionsandACLs.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Simple Storage Service (S3). To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonS3` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
