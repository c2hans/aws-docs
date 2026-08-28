---
source_url: https://docs.aws.amazon.com/iot-mi/latest/devguide/process-job-documents-implementation.html
---

# Process job documents
<a name="process-job-documents-implementation"></a>

When you create an OTA task, the jobs handler runs the following steps on your device. When an update is available, it requests the job document over MQTT.

1. Subscribes to the MQTT notification topics.

1. Calls the [StartNextPendingJobExecution](https://docs.aws.amazon.com/iot-mi/latest/APIReference/API_StartNextPendingJobExecution.html) API for pending jobs.

1. Receives available job documents.

1. Processes updates based on your specified timeouts.

Using the jobs handler, the application can determine whether to take action immediately or wait until a specified timeout period.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Managed integrations. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query iot-mi` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
