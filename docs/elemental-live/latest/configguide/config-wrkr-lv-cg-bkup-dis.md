---
source_url: https://docs.aws.amazon.com/elemental-live/latest/configguide/config-wrkr-lv-cg-bkup-dis.html
---

# Disable database backups
<a name="config-wrkr-lv-cg-bkup-dis"></a>

Follow these steps to disable automatic backups of the AWS Elemental Live database.

1. On the AWS Elemental Live web interface, go to the **Settings** page and choose **General**.

1. In the **Cluster Tasks** section, change the value in **Minutes between management database backups** to **0**.

1. Choose **Save**.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Elemental Live. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query elemental-live` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
