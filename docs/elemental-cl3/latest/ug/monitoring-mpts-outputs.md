---
source_url: https://docs.aws.amazon.com/elemental-cl3/latest/ug/monitoring-mpts-outputs.html
---

# Monitoring MPTS outputs
<a name="monitoring-mpts-outputs"></a>

**Topics**
+ [Monitoring the progress of all MPTSes](#monitoring-the-progress-of-all-mpts-outputs)
+ [Monitoring the muxing performance of an MPTS](#monitoring-the-muxing-performance)
+ [Modifying the MPTS while it is running](#modifying-the-mpts-output-while-it-is-running)

## Monitoring the progress of all MPTSes
<a name="monitoring-the-progress-of-all-mpts-outputs"></a>

You should monitor every MPTS constantly to ensure that none has failed.

1. On the AWS Elemental Conductor Live main menu, choose **Status**, then choose **Overview**. Information about the MPTS appears.

1. If at least one MPTS is in error, go to the **MPTS** page.

1. Look for any MPTS that has an orange icon in the **Status** column.

1. Choose an orange icon to go to the **Status – Alerts & Messages** page. This page appears with the filter set to show only the information for this MPTS output.

1. Review the alerts and messages to determine why the MPTS failed.

## Monitoring the muxing performance of an MPTS
<a name="monitoring-the-muxing-performance"></a>

To monitor the muxing of an individual MPTS, display the **MPTS** page and choose **Performance** (graph icon) beside the item.The MPTS** Details** appears with the **Performance** tab on top.

## Modifying the MPTS while it is running
<a name="modifying-the-mpts-output-while-it-is-running"></a>

You can modify the MPTS ouput even when it is running:
+ You can modify its properties.
+ To add or remove channels.

See [Modifying an MPTS](modifying-an-mpts.md).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Elemental Conductor Live 3. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query elemental-cl3` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
