---
source_url: https://docs.aws.amazon.com/emr/latest/EMR-on-EKS-DevelopmentGuide/emr-eks-jobs-console.html
---

# Viewing jobs in the Amazon EMR console
<a name="emr-eks-jobs-console"></a>

Job run data is avilable to view, so you can monitor each job as it passes through the states. To view jobs in the Amazon EMR console, perform the following steps.

1. In the Amazon EMR console lefthand menu, under Amazon EMR on EKS, choose **Virtual clusters**.

1. From the list of virtual clusters, select the virtual cluster for which you want to view jobs.

1. On the **Job runs** table, select **View logs** to view the details of a job run.

**Note**
Support for the one-click experience is enabled by default. It can be turned off by setting `persistentAppUI` to `DISABLED` in `monitoringConfiguration` during job submission. For more information, see [View Persistent Application User Interfaces](https://docs.aws.amazon.com/emr/latest/ManagementGuide/app-history-spark-UI.html).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon EMR Documentation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query emr` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
