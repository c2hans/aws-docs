---
source_url: https://docs.aws.amazon.com/migrationhub-orchestrator/latest/userguide/event-bridge-notifications.html
---

AWS Migration Hub is no longer open to new customers as of November 7, 2025. For capabilities similar to AWS Migration Hub, explore [AWS Transform](https://aws.amazon.com/transform).

# Configure User Notifications for Migration Hub Orchestrator status change events
<a name="event-bridge-notifications"></a>

You can configure AWS User Notifications to send notifications in response to status changes that occur in Migration Hub Orchestrator. User Notifications uses EventBridge to send notifications about events from AWS services to the AWS Management Console Notifications Center and your chosen delivery channels. For more information about Migration Hub Orchestrator events in EventBridge, see [Migration Hub Orchestrator events in EventBridge](event-bridge.md).

When you are creating a notification configuration, you can specify an **Advanced filter** per event rule to receive notifications that fit specific use cases. For more information on how to create a notification configuring in User Notifications, see [Creating your first notification configuration in AWS User Notifications](https://docs.aws.amazon.com/notifications/latest/userguide/getting-started.html) in the *AWS User Notifications User Guide*.

**JSON samples**
The following JSON samples can be used as advanced filters for your notification configurations to support common use cases.
+ Receive a notification when a workflow fails:

  ```
  {
    "detail": {
      "$or": [
        {
          "status": [
          "WORKFLOW_FAILED"
          ]
        },
        {
          "status": [
              "FAILED"
          ]
        }
      ]
    }
  }
  ```
+ Receive a notification when a workflow’s step changes:

  ```
  {
    "detail": {
      "resourceType": [
        "Workflow Step"
      ]
    }
  }
  ```
+ Receive a notification when a workflow requires manual input:

  ```
  {
    "detail": {
      "status": [
        "USER_ATTENTION_REQUIRED"
      ]
    }
  }
  ```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Migration Hub Orchestrator. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query migrationhub-orchestrator` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
