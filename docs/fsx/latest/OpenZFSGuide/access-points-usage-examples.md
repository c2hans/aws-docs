---
source_url: https://docs.aws.amazon.com/fsx/latest/OpenZFSGuide/access-points-usage-examples.html
---

# Using access points
<a name="access-points-usage-examples"></a>

The following examples demonstrate how to use access points to access file data stored on an FSx for OpenZFS volume using the S3 API. For a full list of the Amazon S3 API operations supported by access points attached to an FSx for OpenZFS volume, see [Access point compatibility](access-points-object-api-support.md).

**Note**
Files on FSx for OpenZFS volumes are identified with a `StorageClass` of `FSX_OPENZFS`.

**Topics**
+ [Downloading a file using an S3 access point](get-object-ap.md)
+ [Uploading a file using an S3 access point](put-object-ap.md)
+ [Listing files using an S3 access point](list-object-ap.md)
+ [Tagging a file using an S3 access point](add-tag-set-ap.md)
+ [Deleting a file using an S3 access point](delete-object-ap.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon FSx. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query fsx` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
