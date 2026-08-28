---
source_url: https://docs.aws.amazon.com/iot-sitewise/latest/userguide/trigger-custom-actions-anomalous-behavior.html
---

# Trigger custom actions on anomalous behavior (AWS Management Console)
<a name="trigger-custom-actions-anomalous-behavior"></a>

You can enable **custom actions in response to anomalous behavior** by using **AWS IoT SiteWise MQTT notifications** in combination with **AWS IoT Core**.

Follow these steps to configure MQTT notifications in AWS IoT SiteWise, and trigger a custom action in AWS IoT Core based on inference results:
+ Locate the asset in AWS IoT SiteWise, where the inference runs.
+ Identify the property you used as the `resultProperty` when creating the computation model. Enable **MQTT Notification** for this property.
+ Once you enable **MQTT Notification**, copy the **Notification Topic** that AWS IoT SiteWise generates.
+ Navigate to AWS IoT Core. Under MQTT test client, subscribe to the copied **Notification Topic** to monitor the incoming messages.
+ Create an **AWS IoT Core Rule** to **Process Inference Results**. (This ensures that actions are triggered only if the system detects an anomaly). Replace `notification-topic` with the **Notification Topic** that AWS IoT SiteWise generates.

```
SELECT * FROM "notification-topic"
  WHERE indexof(get(get(payload.values, 0).value, 'stringValue'), "NO_ANOMALY_DETECTED") < 0
```

Configure the rule to trigger any of the actions that AWS IoT Core supports. Learn more about the actions supported by [AWS IoT Core](https://docs.aws.amazon.com/iot/latest/developerguide/iot-rule-actions.html).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS IoT SiteWise. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query iot-sitewise` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
