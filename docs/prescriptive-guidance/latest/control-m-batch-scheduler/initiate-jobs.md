---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/control-m-batch-scheduler/initiate-jobs.html
---

# Initiate jobs by using a workflow
<a name="initiate-jobs"></a>

Create a flow of jobs called a workflow. Jobs in the workflow are interconnected with dependencies on successful completion of the previous jobs.

## Using Control-M Web
<a name="control-m-web"></a>

To initiate a job from the Control-M user interface, do the following:

1. In the Planning domain, add a new Workspace. This opens a canvas with an empty folder object.

1. On the Menu bar, choose **Add Job**, choose the Micro Focus Windows or Micro Focus Linux job, and drag it onto the face of the folder.

1. After the color of the job changes to green, drop it. The pane on the right contains the **General**, **Scheduling**, **Prerequisites**, and **Actions** sections. To create the job, see the standard instructions in the [Control-M documentation](https://documents.bmc.com/supportu/9.0.21/en-US/Documentation/Creating_a_Job.htm).

1. For instructions on building a Control-M for Micro Focus job, see the [Control-M documentation](https://documents.bmc.com/supportu/9.0.21/en-US/Documentation/Jobs_for_Mainframe_Modernization.htm#MicroFocusJob). For this pilot, repeat steps 2–4 for five jobs, naming each one from `aws-mf-job1` to `aws-mf-job5`.

1. To connect these jobs into the flow that you want, choose the condition triangle under the job object, and drag it onto the next job. For example, choose the condition triangle under `aws-mf-job1`, and drag it onto `aws-mf-job2`. This action makes `aws-mf-job1` the predecessor of `aws-mf-job2`. By default, `aws-mf-job1` must now be completed successfully before `aws-mf-job2` becomes eligible to run.

The following diagram shows the Control-M Planning view of the basic job flow.

![Workflow diagram, with properties in the right-side pane.](https://docs.aws.amazon.com/prescriptive-guidance/latest/control-m-batch-scheduler/images/guide-img/ca7d4793-feac-4eba-a6cd-6ca4d6395925/images/a4c6d6cd-5914-42c6-96f7-4e180d022b33.png)

*Image provided courtesy of BMC Software, Inc. ©2022*

## Using JSON
<a name="json"></a>

The same flow can be coded in JSON. In the GitHub repo, the example code is in the file `Folder-Custom-M2-Replatform.json`:

```
{
  "aws-custom-m2": {
    "Type": "Folder",
    "ControlmServer": "psctm",
    "OrderMethod": "Manual",
    "Application": "AWSM2",
    "SubApplication": "Replatform-Custom",
    "aws-mf-job1": {
      "Type": "Job:Micro Focus Windows",
      "ConnectionProfile": "MICROFOCUS-WINDOWS",
      "Enable JCL Variables": "unchecked",
      "Restart on Rerun": "unchecked",
      "Recapture ABEND Codes": "Ignore",
      "Recapture COND Codes": "Ignore",
      "Auto Adjust Restart": "Ignore",
      "Set MF_UCC11": "Ignore",
      "Restart with Modified JCL": "No",
      "Application": "AWSM2",
      "SubApplication": "Replatform-Custom",
      "Host": "microfocus-es-host",
      "Output": {}
    },
    "aws-mf-job2": {
      "Type": "Job:Micro Focus Windows",
      "ConnectionProfile": "MICROFOCUS-WINDOWS",
      "Enable JCL Variables": "unchecked",
      "Restart on Rerun": "unchecked",
      "Recapture ABEND Codes": "Ignore",
      "Recapture COND Codes": "Ignore",
      "Auto Adjust Restart": "Ignore",
      "Set MF_UCC11": "Ignore",
      "Restart with Modified JCL": "No",
      "Application": "AWSM2",
      "SubApplication": "Replatform-Custom",
      "Host": "microfocus-es-host",
      "Output": {}
    },
    "aws-mf-job3": {
      "Type": "Job:Micro Focus Windows",
      "ConnectionProfile": "MICROFOCUS-WINDOWS",
      "Enable JCL Variables": "unchecked",
      "Restart on Rerun": "unchecked",
      "Recapture ABEND Codes": "Ignore",
      "Recapture COND Codes": "Ignore",
      "Auto Adjust Restart": "Ignore",
      "Set MF_UCC11": "Ignore",
      "Restart with Modified JCL": "No",
      "Application": "AWSM2",
      "SubApplication": "Replatform-Custom",
      "Host": "microfocus-es-host",
      "Output": {}
    },
    "aws-mf-job4": {
      "Type": "Job:Micro Focus Windows",
      "ConnectionProfile": "MICROFOCUS-WINDOWS",
      "Enable JCL Variables": "unchecked",
      "Restart on Rerun": "unchecked",
      "Recapture ABEND Codes": "Ignore",
      "Recapture COND Codes": "Ignore",
      "Auto Adjust Restart": "Ignore",
      "Set MF_UCC11": "Ignore",
      "Restart with Modified JCL": "No",
      "Application": "AWSM2",
      "SubApplication": "Replatform-Custom",
      "Host": "microfocus-es-host",
      "Output": {}
    },
    "aws-mf-job5": {
      "Type": "Job:Micro Focus Windows",
      "ConnectionProfile": "MICROFOCUS-WINDOWS",
      "Enable JCL Variables": "unchecked",
      "Restart on Rerun": "unchecked",
      "Recapture ABEND Codes": "Ignore",
      "Recapture COND Codes": "Ignore",
      "Auto Adjust Restart": "Ignore",
      "Set MF_UCC11": "Ignore",
      "Restart with Modified JCL": "No",
      "Application": "AWSM2",
      "SubApplication": "Replatform-Custom",
      "Host": "microfocus-es-host",
      "Output": {}
    },
    "leftbranch": {
      "Type": "Flow",
      "Sequence": [
        "aws-mf-job1",
        "aws-mf-job2",
        "aws-mf-job3",
        "aws-mf-job5"
      ]
    },
    "rightbranch": {
      "Type": "Flow",
      "Sequence": [
        "aws-mf-job2",
        "aws-mf-job4",
        "aws-mf-job5"
      ]
    }
  }
}
```

To deploy this flow, use the Control-M Automation API:

```
ctm deploy Folder-Custom-M2-Replatform.json
```
