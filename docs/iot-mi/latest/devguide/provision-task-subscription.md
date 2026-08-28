---
source_url: https://docs.aws.amazon.com/iot-mi/latest/devguide/provision-task-subscription.html
---

# Provision task subscription
<a name="provision-task-subscription"></a>

Use these methods to subscribe to provision-related tasks from the managed integrations components.

```
iotmi_statusCode_t iotmi_provision_subscribe_to_tasks(DeviceSDKClient_SubscriberCallback callback, char* context)
```

Subscribes to provision-related tasks, such as device onboarding and deprovisioning, from the managed integrations components.

**Parameters**
+ `callback` (DeviceSDKClient\_SubscriberCallback) - A callback function that executes when a task is received.
+ `context` (char\*) - A custom context passed to the callback function.

**Returns**
+ `IOTMI_STATUS_OK` - The subscription was successful.
+ `IOTMI_STATUS_CUSTOM_PLUGIN_CLIENT_NOT_CONNECTED` - The DeviceSDKClient instance is not connected to managed integrations.
+ `IOTMI_STATUS_CUSTOM_PLUGIN_SUBSCRIBE_ERROR` - An error occurred while subscribing to the tasks.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Managed integrations. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query iot-mi` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
