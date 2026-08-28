---
source_url: https://docs.aws.amazon.com/greengrass/v1/developerguide/config-subs.html
---

End of support notice: On October 7th, 2026, AWS will discontinue support for AWS IoT Greengrass Version 1. After October 7th, 2026, you will no longer be able to access the AWS IoT Greengrass V1 resources. For more information, please visit [Migrate from AWS IoT Greengrass Version 1](https://docs.aws.amazon.com/greengrass/v2/developerguide/migrate-from-v1.html).

# Configure subscriptions
<a name="config-subs"></a>

In this step, you enable the HelloWorld\_Publisher client device to send MQTT messages to the HelloWorld\_Subscriber client device.

1. On the group configuration page, choose the **Subscriptions** tab, and then choose **Add**.

1. On the **Create a subscription** page, do the following to configure the subscription:

   1. For **Source type**, choose **Client device**, and then choose **HelloWorld\_Publisher**.

   1. Under **Target type**, choose **Client device**, and then choose **HelloWorld\_Subscriber**.

   1. For **Topic filter**, enter **hello/world/pubsub**.
**Note**
You can delete subscriptions from the previous modules. On the group's **Subscriptions** page, select the subscriptions to delete, and then choose **Delete**.

   1. Choose **Create subscription**.

1. <a name="enable-automatic-detection"></a>Make sure that automatic detection is enabled so the Greengrass core can publish a list of its IP addresses. Client devices use this information to discover the core. Do the following:

   1. On the group configuration page, choose the **Lambda functions** tab.

   1. Under **System Lambda functions**, choose **IP detector**, and then choose **Edit**.

   1. In the **Edit IP detector settings**, choose **Automatically detect and override MQTT broker endpoints**, and then choose **Save**.

1. Make sure that the Greengrass daemon is running, as described in [Deploy cloud configurations to a core device](configs-core.md).

1. <a name="console-actions-deploy"></a>On the group configuration page, choose **Deploy**.

The deployment status is displayed below the group name on the page header. To see deployment details, choose the **Deployments** tab.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS IoT Greengrass. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query greengrass` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
