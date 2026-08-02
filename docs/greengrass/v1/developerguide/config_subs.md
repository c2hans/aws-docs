---
source_url: https://docs.aws.amazon.com/greengrass/v1/developerguide/config_subs.html
---

End of support notice: On October 7th, 2026, AWS will discontinue support for AWS IoT Greengrass Version 1. After October 7th, 2026, you will no longer be able to access the AWS IoT Greengrass V1 resources. For more information, please visit [Migrate from AWS IoT Greengrass Version 1](https://docs.aws.amazon.com/greengrass/v2/developerguide/migrate-from-v1.html).

# Configure subscriptions
<a name="config_subs"></a>

In this step, you create a subscription that enables the GG\_TrafficLight shadow to send updated state information to the GG\_Car\_Aggregator Lambda function. This subscription is added to the subscriptions that you created in [Module 5](module5.md), which are all required for this module.

1. On the group configuration page, choose the **Subscriptions** tab, and then choose **Add**.

1. On the **Create a subscription** page, do the following:

   1. For **Source type**, choose **Service**, and then choose **Local Shadow Service**.

   1. For **Target type**, choose **Lambda function**, and then choose **GG\_Car\_Aggregator**.

   1. For **Topic filter**, enter **$aws/things/GG\_TrafficLight/shadow/update/documents**

   1. Choose **Create subscription**.

   This module requires the new subscription and the [subscriptions](config-dev-subs.md#module5-subscriptions) that you created in Module 5.

1. Make sure that the Greengrass daemon is running, as described in [Deploy cloud configurations to a core device](configs-core.md).

1. <a name="console-actions-deploy"></a>On the group configuration page, choose **Deploy**.
