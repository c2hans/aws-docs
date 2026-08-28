---
source_url: https://docs.aws.amazon.com/elemental-cl3/latest/configguide/conductor-live-config-bkup-dis.html
---

# Disabling database backups
<a name="conductor-live-config-bkup-dis"></a>

    Disable database backups on the AWS Elemental Conductor Live interface.  disable database backup

Follow these steps to disable automatic backups in a AWS Elemental Conductor Live cluster.

1. On the Conductor Live web interface, go to the **Settings** page and choose **General**.

1. In the **Cluster Tasks** section, change the value in **Minutes between management database backups** to **0**.

1. Choose **Save**.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Elemental Conductor Live 3. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query elemental-cl3` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
