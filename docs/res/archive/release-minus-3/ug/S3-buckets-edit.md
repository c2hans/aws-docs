---
source_url: https://docs.aws.amazon.com/res/archive/release-minus-3/ug/S3-buckets-edit.html
---

# Edit an Amazon S3 bucket
<a name="S3-buckets-edit"></a>

1. Select an S3 bucket in the S3 buckets list.

1. From the **Actions** menu, select **Edit**.

1. Enter your updates.
**Important**
Associating a project with an S3 bucket will **not** mount the bucket to that project's existing virtual desktop infrastructure (VDI) instances. The bucket will only be mounted to VDI sessions launched in a project after the bucket has been associated with that project.
Disassociating a project from an S3 bucket will not impact the data in the S3 bucket, but will result in desktop users losing access to that data.

1. Choose **Save bucket setup**.
![The Edit S3 Bucket page with display name and project association fields entered and Save bucket setup button highlighted](http://docs.aws.amazon.com/res/archive/release-minus-3/ug/images/docs-edit-bucket.png)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Research and Engineering Studio. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query res` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
