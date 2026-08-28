---
source_url: https://docs.aws.amazon.com/redshift/latest/mgmt/serverless-snapshot-update.html
---

 Amazon Redshift will no longer support the use of Python UDFs after June 30, 2026. We will start enforcing it in phases. For more information on the details of Python end of life and migration options, see the [ blog post ](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/) that was published on June 30, 2025.

# Updating a snapshot retention period
<a name="serverless-snapshot-update"></a>

To update a snapshot retention period, perform the following procedure.

**To update a snapshot retention period**

1. On the Amazon Redshift Serverless console, choose **Data backup**.

1. Choose a snapshot to update.

1. Choose **Actions**, **Set manual snapshot settings.**

1. Choose a retention period. If you choose **Custom value**, choose the number of days.

1. Choose **Save changes**.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Redshift. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query redshift` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
