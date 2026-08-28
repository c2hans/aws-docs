---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/control-m-batch-scheduler/monitor-jobs.html
---

# Monitor jobs
<a name="monitor-jobs"></a>

You can monitor and validate the processing of jobs within the Control-M Monitoring domain and through the AWS Management Console, ensuring comprehensive observation and verification across both these platforms.

## Control-M Monitoring
<a name="control-m-monitoring"></a>

Job submissions and runs can be monitored in the *Control-M Monitoring domain.* By default, AWS Mainframe Modernization service jobs will appear together with all other Control-M work. If you want to see only the AWS Mainframe Modernization service jobs without any other workload (or any other filtering requirements), you can create a *Viewpoint*.

Viewpoints show not only job information but also relationships with upstream and downstream dependencies. Additionally, if your workflow includes AWS Mainframe Modernization and other Control-M job types, you can see and manage the entire flow in the Monitoring domain.

To follow detailed steps, see the [Viewpoints section of Monitoring](https://documents.bmc.com/supportu/9.0.21/en-US/Documentation/Viewpoints.htm) in the Control-M documentation.

The following screenshot shows the outputs of two workflows. On the left side, the workflow is completed successfully with all jobs in green. On the right side, the workflow is only partially successful because job `CURRRENCY` returned the **Failed** status, which is indicated by the red color. The workflow stopped there, leaving the remaining jobs in the **Wait Schedule** state.

![Diagrams of workflows on the left, job properties on the right.](http://docs.aws.amazon.com/prescriptive-guidance/latest/control-m-batch-scheduler/images/guide-img/ca7d4793-feac-4eba-a6cd-6ca4d6395925/images/86cb2cf3-3033-4774-8dbd-3bd233446615.png)

*Image provided courtesy of BMC Software, Inc. ©2022*

## Monitoring on the console
<a name="console"></a>

To view job and log information on AWS, sign in to the AWS Management Console, and then navigate to the [AWS Mainframe Modernization console](https://console.aws.amazon.com/m2/home?region=us-east-1#/applications).

![Jobs and statuses listed on the AWS Mainframe Modernization console.](http://docs.aws.amazon.com/prescriptive-guidance/latest/control-m-batch-scheduler/images/guide-img/ca7d4793-feac-4eba-a6cd-6ca4d6395925/images/cc3bd6fa-88a2-4ff0-9007-a8b6dc4901ca.png)

This view doesn't include dependencies nor any workload that isn't managed by the AWS Mainframe Modernization service.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
