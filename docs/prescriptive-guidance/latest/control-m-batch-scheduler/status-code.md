---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/control-m-batch-scheduler/status-code.html
---

# Initiate jobs based on the status of previous jobs
<a name="status-code"></a>

Create a flow of jobs called a workflow. Jobs in the workflow are interconnected with dependencies on successful completion of the previous jobs.

## Using the Control-M Web GUI
<a name="using-gui"></a>

To initiate a job from the Control-M user interface, do the following:

1. In the **Planning** domain, add a new **Workspace**. This opens a canvas with an empty folder object.

1. Select the AWS Mainframe Modernization job type (if you are using the supplied job type template, this is called [M2JOB](https://github.com/aws-samples/aws-mainframe-modernization-controlm-integration/blob/main/assets/AWS-jobs.json)), and drag it onto the folder.

1. After the color of the job type changes to green, drop it. The pane on the right contains the **General**, **Scheduling**, **Prerequisites**, and **Actions** sections. To create the job, see the standard instructions in the [Control-M documentation](https://documents.bmc.com/supportu/9.0.21/en-US/Documentation/Creating_a_Job.htm).

1. Next, you need the **Job Name** values to configure the job types. You can find the **Job Name** values on the **Application** definition screen of the AWS Mainframe Modernization console or by running the [ListBatchJobDefinitions API](https://docs.aws.amazon.com/m2/latest/APIReference/API_ListBatchJobDefinitions.html). For this pilot, repeat steps 2–4 for several jobs, naming each one with any names you choose. Example names are `CBANK`, `CURRENCY`, I`NVFUNDS`, `BROKERAGE`, `RISKMGMT`, and `BANK-SERVICE-Managed-M2`.

1. To connect these jobs into the flow that you want, choose the condition triangle under the job object, and drag it onto the next job. For example, choose the condition triangle under `CBANK`, and drag it onto `CURRENCY`. This action makes `CBANK` the predecessor of `CURRENCY`. By default, `CBANK` must now be completed successfully before CURRENCY becomes eligible to run.

The following screenshot shows the Control-M Planning view of the basic job flow.

![Job flow on the left and properties on the right.](https://docs.aws.amazon.com/prescriptive-guidance/latest/control-m-batch-scheduler/images/guide-img/ca7d4793-feac-4eba-a6cd-6ca4d6395925/images/8de53763-0da1-4c96-a2ff-e82966d9cfe5.png)

*Image provided courtesy of BMC Software, Inc. ©2022*

## Using JSON
<a name="using-json"></a>

The same flow can be coded in JSON:

```
{
  "Defaults": {
    "Application": "AWSM2",
    "SubApplication": "Replatform-Managed",
    "Job": {
      "Host": "ctm-worker",
      "Output": {}
    }
  },
  "jog-managed-m2": {
    "Type": "Folder",
    "ControlmServer": "psctm",
    "OrderMethod": "Manual",
    "SiteStandard": "_z_DemoBusinessFlows",
    "CBANK": {
      "Type": "Job:AWS Mainframe Modernization",
      "ConnectionProfile": "MANAGED-M2-REPLATFORM",
      "JCL Name": "iefbr14",
      "Retrieve CloudWatch Logs": "checked",
      "Action": "Start Batch Job",
      "Application Version": "1"
    },
    "CURRENCY": {
      "Type": "Job:AWS Mainframe Modernization",
      "ConnectionProfile": "MANAGED-M2-REPLATFORM",
      "JCL Name": "iefbr14",
      "Retrieve CloudWatch Logs": "checked",
      "Action": "Start Batch Job",
      "Application Version": "1"
    },
    "BROKERAGE": {
      "Type": "Job:AWS Mainframe Modernization",
      "ConnectionProfile": "MANAGED-M2-REPLATFORM",
      "JCL Name": "iefbr14",
      "Retrieve CloudWatch Logs": "checked",
      "Action": "Start Batch Job",
      "Application Version": "1"
    },
    "INVFUNDS": {
      "Type": "Job:AWS Mainframe Modernization",
      "ConnectionProfile": "MANAGED-M2-REPLATFORM",
      "JCL Name": "iefbr14",
      "Retrieve CloudWatch Logs": "checked",
      "Action": "Start Batch Job",
      "Application Version": "1"
    },
    "RISKMGMT": {
      "Type": "Job:AWS Mainframe Modernization",
      "ConnectionProfile": "MANAGED-M2-REPLATFORM",
      "JCL Name": "iefbr14",
      "Retrieve CloudWatch Logs": "checked",
      "Action": "Start Batch Job",
      "Application Version": "1"
    },
    "BANK-SERVICE-Managed-M2": {
      "Type": "Job:SLAManagement",
      "ServiceName": "Bank Service - Managed M2",
      "RunAs": "ctmagent",
      "CompleteBy": {
        "Time": "12:00",
        "Days": "0"
      }
    },
    "leftbranch": {
      "Type": "Flow",
      "Sequence": [
        "CURRENCY",
        "RISKMGMT",
        "BANK-SERVICE-Managed-M2"
      ]
    },
    "middlebranch": {
      "Type": "Flow",
      "Sequence": [
        "CBANK",
        "CURRENCY",
        "INVFUNDS",
        "BANK-SERVICE-Managed-M2"
      ]
    },
    "rightbranch": {
      "Type": "Flow",
      "Sequence": [
        "CURRENCY",
        "BROKERAGE",
        "BANK-SERVICE-Managed-M2"
      ]
    }
  }
}
```

To deploy this flow, use the deploy service:

```
ctm deploy folder-MANAGED-M2-REPLATFORM.json
```
