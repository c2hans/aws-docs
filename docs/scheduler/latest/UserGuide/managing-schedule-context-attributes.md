---
source_url: https://docs.aws.amazon.com/scheduler/latest/UserGuide/managing-schedule-context-attributes.html
---

# Adding context attributes in EventBridge Scheduler
<a name="managing-schedule-context-attributes"></a>

 Use of the following keywords in the payload you pass to the target to collect metadata about the schedule. EventBridge Scheduler replaces each keyword with its respective value when your schedule invokes the target.
+  **`<aws.scheduler.schedule-arn>`** – The ARN of the schedule.
+  **`<aws.scheduler.scheduled-time>`** – The time you specified for the schedule to invoke its target, for example, `2022-03-22T18:59:43Z`.
+  **`<aws.scheduler.execution-id>`** – The unique ID that EventBridge Scheduler assigns for each attempted invocation of a target, for example, `d32c5kddcf5bb8c3`.
+  **`<aws.scheduler.attempt-number>`** – A counter that identifies the attempt number for the current invocation, for example, `1`.

 This example shows creating a schedule that fires every five minutes, and invokes the Amazon SQS `SendMessage` operation as a universal target. The message body includes the value for `schedule-time`.

**Example AWS CLI**

```
$ aws scheduler create-schedule --name {{your-schedule}} \
    --schedule-expression 'rate(5 minutes)' \
    --target '{"RoleArn": "{{ROLE_ARN}}", \
        "Arn": "arn:aws:scheduler:::aws-sdk:sqs:sendMessage", \
        "Input": "{\"MessageBody\":\"<aws.scheduler.scheduled-time>\",\"QueueUrl\":\"https://sqs.us-west-2.amazonaws.com/123456789012/scheduler-cli-test\"}"}' \
    --flexible-time-window '{ "Mode": "OFF"}'
```

**Example Python SDK**

```
import boto3
scheduler = boto3.client('scheduler')

sqs_universal= {
    "RoleArn": "<ROLE_ARN>",
    "Arn": "arn:aws:scheduler:::aws-sdk:sqs:sendMessage",
    "Input": "{\"MessageBody\":\"<aws.scheduler.scheduled-time>\",\"QueueUrl\":\"https://sqs.us-west-2.amazonaws.com/123456789012/scheduler-cli-test\"}"
}

flex_window = { "Mode": "OFF" }

scheduler.update_schedule(Name="your-schedule",
    ScheduleExpression="rate(5 minutes)",
    Target=sqs_universal,
    FlexibleTimeWindow=flex_window)
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon EventBridge Scheduler. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query scheduler` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
