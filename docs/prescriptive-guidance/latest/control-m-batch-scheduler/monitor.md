---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/control-m-batch-scheduler/monitor.html
---

# Monitor jobs
<a name="monitor"></a>

You can monitor and verify jobs in the Control-M Monitoring domain and in the Micro Focus Enterprise Server Common Web Administration user interface.

## Control-M Monitoring
<a name="monitoring"></a>

Job submissions and runs can be monitored in the Control-M Monitoring domain. By default, AWS Mainframe Modernization service jobs will appear together with all other Control-M work. If you want to see only the AWS Mainframe Modernization service jobs without any other workload (or any other filtering requirements), you can create a Viewpoint.

Viewpoints show not only job information but also relationships with upstream and downstream dependencies. Additionally, if your workflow includes AWS Mainframe Modernization and other types of Control-M jobs, you can see and manage the entire flow in the Monitoring domain.

You can follow detailed steps by visiting [Viewpoints section of Monitoring](https://documents.bmc.com/supportu/9.0.21/en-US/Documentation/Viewpoints.htm) in the Control-M documentation.

The following screenshot shows the outputs of two workflows. On the left side, the workflow is completed successfully with all five jobs in green. On the right side, the workflow is only partially successful because `aws-mf-job3` returned the **Failed** status, and the workflow stopped there, leaving `aws-mf-job5` in **Wait Schedule** state.

![Workflow diagrams on the left side, monitoring output on the Output tab on the right-side pane.](http://docs.aws.amazon.com/prescriptive-guidance/latest/control-m-batch-scheduler/images/guide-img/ca7d4793-feac-4eba-a6cd-6ca4d6395925/images/79df78be-b653-4fc8-861d-5d06174a246a.png)

*Image provided courtesy of BMC Software, Inc. ©2022*
