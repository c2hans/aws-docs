---
source_url: https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/Investigations-Restart.html
---

# Restart an archived investigation
<a name="Investigations-Restart"></a>

You can restart archived investigations.

**To restart an archived investigation**

1. Open the CloudWatch console at [https://console.aws.amazon.com/cloudwatch/](https://console.aws.amazon.com/cloudwatch/).

1. In the left navigation pane, choose **AI Operations**, **Investigations**.

1. Choose the name of an archived investigation.

1. Choose **Restart investigation**.

1. (Optional)Update incident reports.

   Any incident reports generated from the original investigation remain available in the investigation history. You can access these reports from the investigation details page. If the restarted investigation discovers more facts, you can regenerate the incident report using the following steps:

   1. Choose **Incident report** to regenerate your incident report with new or updated facts.

   1. From the **Incident report** page, review updated facts.

   1. Choose **Regenerate** to update your incident report. If the **Regenerate** button is disabled, no new facts are present.

   We recommend that you don't leave investigations open indefinitely, because alarm state transitions related to the investigation will keep being added to the investigation as long as it is open.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon CloudWatch. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonCloudWatch` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
