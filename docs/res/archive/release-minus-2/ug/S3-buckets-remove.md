---
source_url: https://docs.aws.amazon.com/res/archive/release-minus-2/ug/S3-buckets-remove.html
---

# Remove an Amazon S3 bucket
<a name="S3-buckets-remove"></a>

1. Select an S3 bucket in the S3 buckets list.

1. From the **Actions** menu, select **Remove**.
**Important**
You must first remove all project associations from the bucket.
The remove operation does not impact the data in the S3 bucket. It only removes the S3 bucket’s association with RES.
Removing a bucket will cause existing VDI sessions to lose access to the contents of that bucket at the expiration of that session’s credentials (\~1 hour).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Research and Engineering Studio. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query res` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
