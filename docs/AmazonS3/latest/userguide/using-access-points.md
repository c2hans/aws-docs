---
source_url: https://docs.aws.amazon.com/AmazonS3/latest/userguide/using-access-points.html
---

# Using Amazon S3 access points for general purpose buckets
<a name="using-access-points"></a>

The following examples demonstrate how to use access points for general purpose buckets with compatible operations in Amazon S3.

**Note**
S3 automatically generate access point aliases for all access points and these aliases can be used anywhere a bucket name is used to perform object-level operations. For more information, see [Access point aliases](access-points-naming.md#access-points-alias).

You can only use access points for general purpose buckets to perform operations on objects. You can't use access points to perform other Amazon S3 operations, such as modifying or deleting buckets. For a complete list of S3 operations that support access points, see [Access point compatibility](access-points-service-api-support.md).

**Topics**
+ [List objects through an access point for a general purpose bucket](list-object-ap.md)
+ [Download an object through an access point for a general purpose bucket](get-object-ap.md)
+ [Configure access control lists (ACLs) through an access point for a general purpose bucket](put-acl-permissions-ap.md)
+ [Upload an object through an access point for a general purpose bucket](put-object-ap.md)
+ [Add a tag-set through an access point for a general purpose bucket](add-tag-set-ap.md)
+ [Delete an object through an access point for a general purpose bucket](delete-object-ap.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Simple Storage Service (S3). To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonS3` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
