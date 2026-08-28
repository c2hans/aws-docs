---
source_url: https://docs.aws.amazon.com/mediaconvert/latest/ug/adjusting-the-status-update-interval.html
---

# Adjust the status update interval
<a name="adjusting-the-status-update-interval"></a>

By default, AWS Elemental MediaConvert sends `STATUS_UPDATE` events to Amazon EventBridge approximately once per minute. These status updates provide information about how your job is progressing. You can adjust the status update interval by specifying a different update frequency in your job.

**To specify the STATUS\_UPDATE frequency**

1. On the **Create job** page, in the **Job** pane on the left, in the **Job settings** section, choose **AWS integration**.

1. In the **AWS integration** section on the right, for **Status update interval (sec)**, choose **interval, in seconds, between updates**.

If you use the API or an SDK, you can find this setting in the JSON file of your job. The setting name is [statusUpdateInterval](https://docs.aws.amazon.com/mediaconvert/latest/apireference/jobs.html#jobs-prop-createjobrequest-statusupdateinterval).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for MediaConvert. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query mediaconvert` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
