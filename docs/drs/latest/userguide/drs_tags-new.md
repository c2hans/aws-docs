---
source_url: https://docs.aws.amazon.com/drs/latest/userguide/drs_tags-new.html
---

# Managing tags with AWS DRS
<a name="drs_tags-new"></a>

The Tags section shows any tags that have been assigned to the server. A tag is a label that you assign to an AWS resource. Each tag consists of a key and an optional value. You can use tags to search and filter your resources or track your AWS costs. Learn more about AWS tags in [this Amazon EC2 article](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/Using_Tags.html).

**Important**
**Do not** alter the **Name** tag of resources created by AWS DRS (replication servers, EBS volumes, EBS snapshots, Conversion servers).

Choose **Manage tags** to open the **Manage tags** page to add or remove tags.
+ Choose **Add new tag** to add a new tag. Add a tag **Key** and an optional tag **Value**. Choose **Save** to save your added tags.
+ To remove a tag, choose **Remove** to the right of the tag you want to remove, and then choose **Save**.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Elastic Disaster Recovery. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query drs` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
