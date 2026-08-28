---
source_url: https://docs.aws.amazon.com/elemental-server/latest/configguide/config-wrkr-srvr-cg-bkup-dis.html
---

This is version 2.18 of the AWS Elemental Server documentation. This is the latest version. For prior versions, see the *Previous Versions* section of [AWS Elemental Conductor File and AWS Elemental Server Documentation](https://docs.aws.amazon.com/elemental-server/).

# Disable Automatic Database Backups
<a name="config-wrkr-srvr-cg-bkup-dis"></a>

Follow these steps to disable automatic backups.

1. On the AWS Elemental Server web interface, go to the **Settings** page and choose **General**.

1. In the **Cluster Tasks** section, change the value in **Minutes between management database backups** to **0**.

1. Choose **Save**.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Elemental Server. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query elemental-server` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
