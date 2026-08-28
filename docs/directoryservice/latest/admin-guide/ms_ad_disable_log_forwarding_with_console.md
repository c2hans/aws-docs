---
source_url: https://docs.aws.amazon.com/directoryservice/latest/admin-guide/ms_ad_disable_log_forwarding_with_console.html
---

# Disabling Amazon CloudWatch log forwarding for AWS Managed Microsoft AD
<a name="ms_ad_disable_log_forwarding_with_console"></a>

You can disable CloudWatch Logs log forwarding for your AWS Managed Microsoft AD in the AWS Management Console. For more information on log forwarding, see [Using CloudWatch to monitor the performance of your AWS Managed Microsoft AD domain controllers](ms_ad_monitor_dc_performance.md).

1. In the [Directory Service console](https://console.aws.amazon.com/directoryservicev2/) navigation pane, choose **Directories**.

1. Choose the directory ID of the AWS Managed Microsoft AD directory that you want to share.

1. On the **Directory details** page, do one of the following:
   + If you have multiple Regions showing under **Multi-Region replication**, select the Region where you want to disable log forwarding, and then choose the **Networking & security** tab. For more information, see [Primary vs additional Regions](multi-region-global-primary-additional.md).
   + If you do not have any Regions showing under **Multi-Region replication**, choose the **Networking & security** tab.

1. In the **Log forwarding** section, choose **Disable**.

1. Once you've read the information in the **Disable log forwarding** dialog, choose **Disable**.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Directory Service. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query directoryservice` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
