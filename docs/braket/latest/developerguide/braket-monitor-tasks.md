---
source_url: https://docs.aws.amazon.com/braket/latest/developerguide/braket-monitor-tasks.html
---

# Logging and monitoring
<a name="braket-monitor-tasks"></a>

After you submit a quantum task through the Amazon Braket service, you can closely monitor the status and progression of that task through the Amazon Braket SDK and console. This provides you with a centralized interface to track the implementation of your workloads, identify any potential bottlenecks or issues, and take appropriate actions to optimize the performance and reliability of your quantum applications. When the quantum task completes, Braket saves the results in your specified Amazon S3 location. Completion time for quantum tasks can vary, especially for those running on quantum processing unit (QPU) devices. This is largely due to the length of the execution queue, as quantum hardware resources are shared among multiple users.

**List of status types:**
+  `CREATED` – Amazon Braket received your quantum task.
+  `QUEUED` – Amazon Braket processed your quantum task and it is now waiting to run on the device.
+  `RUNNING` – Your quantum task is running on a QPU or on-demand simulator.
+  `COMPLETED` – Your quantum task finished running on the QPU or on-demand simulator.
+  `FAILED` – Your quantum task attempted to run and failed. Depending on the reason your quantum task failed, try submitting your quantum task again.
+  `CANCELLED` – You cancelled the quantum task. The quantum task did not run.

**Topics**
+ [Tracking quantum tasks from the Amazon Braket SDK](braket-monitor-tasks-sdk.md)
+ [Monitoring quantum tasks through the Amazon Braket console](braket-monitor-console.md)
+ [Tagging Amazon Braket resources](braket-tagging-resources.md)
+ [Monitoring your Braket resources with EventBridge](braket-monitor-eventbridge.md)
+ [Monitoring your metrics with CloudWatch](braket-monitor-metrics.md)
+ [Logging your Braket actions with CloudTrail](braket-ctlogs.md)
+ [Advanced logging with Amazon Braket](braket-monitor-logging.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Braket. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query braket` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
