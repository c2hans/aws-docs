---
source_url: https://docs.aws.amazon.com/elemental-statmux/latest/configguide/config-wrkr-sm-cg-bkup-dis.html
---

This is version 2.20 of the AWS Elemental Statmux documentation. This is the latest version. For prior versions, see the *Previous Versions* section of [AWS Elemental Statmux and AWS Elemental Live Documentation](https://docs.aws.amazon.com/elemental-live).

# Disable Database Backups
<a name="config-wrkr-sm-cg-bkup-dis"></a>

Follow these steps to disable automatic backups.

1. On the AWS Elemental Statmux web interface, go to the **Settings** page and choose **General**.

1. In the **Cluster Tasks** section, change the value in **Minutes between management database backups** to **0**.

1. Choose **Save**.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Elemental Statmux. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query elemental-statmux` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
