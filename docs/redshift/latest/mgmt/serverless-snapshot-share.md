---
source_url: https://docs.aws.amazon.com/redshift/latest/mgmt/serverless-snapshot-share.html
---

 Amazon Redshift will no longer support the use of Python UDFs after June 30, 2026. We will start enforcing it in phases. For more information on the details of Python end of life and migration options, see the [ blog post ](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/) that was published on June 30, 2025.

# Sharing a snapshot or removing snapshot permissions
<a name="serverless-snapshot-share"></a>

To share a snapshot with another AWS account or remove an account's access to a snapshot, perform the following procedure.

**To share or remove access to a snapshot**

1. On the Amazon Redshift Serverless console, choose **Data backup**.

1. Choose a snapshot to share.

1. Choose **Actions**, **Manage access**.

1. To share a snapshot with another account, enter an **AWS account ID**. To remove access from an account, choose **Remove**.

1. Choose **Save changes**.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Redshift. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query redshift` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
