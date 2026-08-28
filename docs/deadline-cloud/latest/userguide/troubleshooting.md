---
source_url: https://docs.aws.amazon.com/deadline-cloud/latest/userguide/troubleshooting.html
---

# Troubleshooting
<a name="troubleshooting"></a>

The following procedures and tips can help you troubleshoot issues with your AWS Deadline Cloud farms and resources.

**Topics**
+ [Why can a user not see my farm, fleet, or queue?](#troubleshooting_user_not_seeing_farm)
+ [Why are workers not picking up my jobs?](#troubleshooting_workers_not_picking_jobs)
+ [Why is my worker stuck running?](#troubleshooting_worker_stuck_running)
+ [Troubleshooting Deadline Cloud jobs](#jobs-troubleshooting)
+ [Deadline Cloud monitor desktop application logs](#troubleshooting-desktop-logs)
+ [Additional resources](#troubleshooting_additional_resources)

## Why can a user not see my farm, fleet, or queue?
<a name="troubleshooting_user_not_seeing_farm"></a>

### User access
<a name="troubleshooting_user_access"></a>

When your users are not seeing your farms, fleets, or queues in the Deadline Cloud monitor, there might be an issue with their access to your farm and resources.

Users without access to any farms receive the message "No farms available" in the Deadline Cloud monitor.

**To confirm you have the correct user or group assigned to your farm, fleet, or queue**

1. In the AWS Deadline Cloud console, find your farm, fleet, or queue, and then choose **Access management**.

1. The groups tab is selected by default. If you're assigning permissions by groups, which is recommended, your group should display in the list and have an assigned access level.

   If the group is not in the list, choose **Add group** to assign permission for the group.

1. If you're assigning permissions by user, select the **Users** tab. Your user should display in the list and have an assigned access level.

   If your user is not in the list, choose **Add user** to assign permission for the user.

**To confirm you have the user assigned to your group**

1. In the AWS Deadline Cloud console, find your farm, fleet, or queue, and then choose **Access management**.

1. The groups tab is selected by default. Select the group name to view its members.

1. If the user is not listed in the group, they must be added.

   If you're using the default identity setup, you can directly add the user to the group in the Identity Center console. If you're connected to an external identity provider such as Okta or Google Workspace, you can add your user to the group in your identity provider.
**Note**
Some external identity providers sync users but not groups to Identity Center. In this case, consider assigning permissions to a user directly instead of by group.

For more information about managing user access to Deadline Cloud, see [Managing users in Deadline Cloud](managing-users.md).

## Why are workers not picking up my jobs?
<a name="troubleshooting_workers_not_picking_jobs"></a>

### Fleet role configuration
<a name="troubleshooting_workers_fleet_role_config"></a>

Sometimes when workers are created but do not complete initialization and do not start working on jobs, it's because the fleet role was not configured correctly.

To verify this cause, check your CloudTrail logs for any access denied errors. After you confirm the access denied issue, go to your fleet and update the role configuration to the correct permissions. For more information, see [CloudTrail logs](https://docs.aws.amazon.com/deadline-cloud/latest/developerguide/logging-using-cloudtrail.html) in the Deadline Cloud developer guide.

## Why is my worker stuck running?
<a name="troubleshooting_worker_stuck_running"></a>

### Worker stuck exiting OpenJD environment
<a name="troubleshooting_worker_fleet_role_config"></a>

Workers can get stuck in long-running `envExit` session actions. This problem might happen if you use a job template that overrides the OpenJD template and sets the environment exit actions timeout to more than 5 minutes. The Deadline Cloud monitor provides some visibility into workers stuck in this situation, but it requires cross-referencing `RUNNING` workers against available work in the associated queues.

To find stuck workers, go through all fleets in the Deadline Cloud monitor and complete the following steps:

1. In the worker status column, find `RUNNING` workers.

1. From the Fleet details section, navigate to each associated queue.

1. In each associated queue, search for jobs that are `RUNNING`, `READY`, or `PENDING`. If all associated queues don't have any jobs in those states, then the worker is running an environment exit.

To stop a worker stuck in this state, use the following AWS CLI command:

```
aws deadline update-worker \
    --farm-id $FARM_ID     \
    --fleet-id $FLEET_ID   \
    --worker-id $WORKER_ID \
    --status STOPPED
```

After running the command, the worker agent restarts when the program exits. Workers then come back online and run more jobs from associated queues. If the queue contains more jobs with environment exit action timeouts longer than 5 minutes, the worker will get stuck again. If this happens, you will need to repeat this process until no more workers are stuck exiting.

To avoid this issue, set the timeout option to no more than 5 minutes when using a job template.

## Troubleshooting Deadline Cloud jobs
<a name="jobs-troubleshooting"></a>

For information about common problems with jobs in AWS Deadline Cloud, see the following topics.

### Why did creating my job fail?
<a name="troubleshooting-create-failed"></a>

#### Quota validation
<a name="troubleshooting-quota-validation"></a>

Some possible reasons that a job can fail validation checks include the following:
+ The job template doesn't follow the OpenJD specification.
+ The job contains too many steps.
+ The job contains too many total tasks.
+ There was an internal service error that prevents the job from being created.

To see the quotas for the maximum number of steps and tasks in a job, use the Service Quotas console. For more information, see [Service quotas and throttling for Deadline Cloud](deadline-cloud-quotas.md).

#### CHUNK[INT] task parameter error
<a name="troubleshooting-task-chunking-extension"></a>

If job creation fails with the following error message, you need to add the `TASK_CHUNKING` extension to your job template.

```
The CHUNK[INT] task parameter requires the TASK_CHUNKING extension.
```

To resolve this issue, add the following to your job template:

```
extensions:
  - TASK_CHUNKING
```

For more information, see [Add task chunking to a job template](https://docs.aws.amazon.com/deadline-cloud/latest/developerguide/build-job-bundle-chunking-add.html) in the *AWS Deadline Cloud Developer Guide*.

### Why is my job not compatible?
<a name="troubleshooting-not-compatible"></a>

Common reasons that jobs are not compatible with queues include the following:
+ No fleets are associated with the queue that the job was submitted to. Open the Deadline Cloud monitor, and check that the queue has associated fleets. For more information about how to view queues, see [View queue and fleet details in Deadline Cloud](view-queue-and-fleet.md).
+ The job has host requirements that are not satisfied by any of the fleets associated with the queue. To check, compare the `hostRequirements` entry in the job template with the configuration of the fleets in your farm. Make sure that one of the fleets satisfies the host requirements. For more information about fleet compatibility, see [Determine fleet compatibility](https://docs.aws.amazon.com/deadline-cloud/latest/developerguide/build-jobs-scheduling.html#jobs-scheduling-compatibility). To view fleet configuration, see [View queue and fleet details in Deadline Cloud](view-queue-and-fleet.md).

Deadline Cloud checks compatibility when you submit the job. If you associate a compatible fleet with the queue later, existing `NOT_COMPATIBLE` jobs don't automatically restart. To run those jobs, requeue them. For more information, see [Requeue a job](view-a-job.md#view-jobs-steps-tasks-requeue).

### Why is my job stuck in ready?
<a name="troubleshooting-stuck-ready"></a>

Possible reasons for your job appearing to be stuck in the `READY` state include the following:
+ The maximum worker count for fleets associated with the queue is set to zero. To check, see [View queue and fleet details in Deadline Cloud](view-queue-and-fleet.md).
+ There is a higher priority job in the queue. To check, see [View queue and fleet details in Deadline Cloud](view-queue-and-fleet.md).
+ For customer-managed fleets, check the auto scaling configuration. For more information, see [Create fleet infrastructure with an Amazon EC2 Auto Scaling group](https://docs.aws.amazon.com/deadline-cloud/latest/developerguide/create-auto-scaling.html) in the *Deadline Cloud Developer Guide*.

### Why did my job fail?
<a name="troubleshooting-job-failed"></a>

A job can fail for many reasons. To search for the issue, open the Deadline Cloud monitor and choose the failing job. Choose a task that failed and then view the logs for the task. For instructions, see [View session and worker logs in Deadline Cloud](view-logs.md).
+ If you see license errors or if you get a watermark that occurs because the software doesn't have a valid license, make sure that the worker can connect to the required license server. For more information, see [Connect customer-managed fleets to a license endpoint](https://docs.aws.amazon.com/deadline-cloud/latest/developerguide/cmf-ubl.html) in the *Deadline Cloud Developer Guide*.
+ The last session action message or the process exit code may provide information about why you job failed. If you are using Windows and your exit code is negative, try searching for the unsigned version of your exit code:

  ```
  2,147,483,647 - |{{your exit code}}|
  ```

### Why is my step pending?
<a name="troubleshooting-pending-failed"></a>

Steps may stay in the `PENDING` state when one or more of their dependencies are not complete. You can check the state of dependencies using the Deadline Cloud monitor. For instructions, see [View a step in Deadline Cloud](view-a-step.md).

## Deadline Cloud monitor desktop application logs
<a name="troubleshooting-desktop-logs"></a>

The Deadline Cloud monitor desktop application writes diagnostic logs that you can use to investigate crashes or other unexpected behavior. When reporting an issue with the desktop application, include the relevant log files to help with diagnosis.

The location of the log files depends on your operating system:

Windows

```
%APPDATA%\com.amazonaws.deadline.monitor\logs
```

macOS

```
~/Library/Logs/com.amazonaws.deadline.monitor/
```

Linux

```
~/.config/com.amazonaws.deadline.monitor/logs
```

## Additional resources
<a name="troubleshooting_additional_resources"></a>

You can find additional information and resources on [GitHub](https://github.com/aws-deadline).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Deadline Cloud. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query deadline-cloud` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
