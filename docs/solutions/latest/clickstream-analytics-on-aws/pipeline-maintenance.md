---
source_url: https://docs.aws.amazon.com/solutions/latest/clickstream-analytics-on-aws/pipeline-maintenance.html
---

# Pipeline maintenance
<a name="pipeline-maintenance"></a>

 This guidance provides three features to help you manage and operate the data pipeline after it gets created.

## Monitoring and Alarms
<a name="monitoring-and-alarms"></a>

 The guidance collects metrics from each resource in the data pipeline and creates monitoring dashboards in CloudWatch, which provides you a comprehensive view into the pipeline status. It also provides a set of alarms that will notify project owner if anything goes abnormal.

 Following are steps to view monitoring dashboards and alarms.

### Monitoring dashboards
<a name="monitoring-dashboards"></a>

 To view monitoring dashboard for a data pipeline, follows below steps:

1.  Go to project detail page.

1.  Choose project id or **View Details**, which will direct to the pipeline detail page.

1.  Select the "**Monitoring**" tab.

1.  In the tab, choose **View in CloudWatch**, which will direct you to the monitoring dashboard.

### Alarms
<a name="alarms"></a>

 To view alarms for a data pipeline, follows below steps:

1.  Go to project detail page.

1.  Choose project id or **View Details**, which will direct to the pipeline detail page.

1.  Select the "**Alarms**" tab.

1.  In the tab, you can view all the alarms. You can also choose **View in CloudWatch**, which will direct you to CloudWatch alarm pages to view alarm details.

1.  You can also enable or disable an alarm by selecting the alarm then choosing **Enable** or **Disable**.

## Pipeline modification
<a name="pipeline-modification"></a>

 You are able to modify some configuration the data pipeline after it created, follow below steps to update a pipeline.

1.  Go to project detail page.

1.  Choose project id or **View Details**, which will direct to the pipeline detail page.

1.  In the project details page, choose **Edit**, which will bring you to the pipeline creation wizard page. Note that some configuration are in disable mode, which means they cannot be updated after creation.

1.  If needed, update those configuration options which are editable.

1.  After editing the configuration, choose **Next** until you reach last page, and choose **Save**.

 You will see pipeline is in Updating status.

## Pipeline upgrade
<a name="pipeline-upgrade"></a>

For detailed procedure, see [upgrade the guidance](upgrade-the-solution.md).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Guidance for Clickstream Analytics on AWS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query solutions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
