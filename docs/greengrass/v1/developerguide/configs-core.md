---
source_url: https://docs.aws.amazon.com/greengrass/v1/developerguide/configs-core.html
---

End of support notice: On October 7th, 2026, AWS will discontinue support for AWS IoT Greengrass Version 1. After October 7th, 2026, you will no longer be able to access the AWS IoT Greengrass V1 resources. For more information, please visit [Migrate from AWS IoT Greengrass Version 1](https://docs.aws.amazon.com/greengrass/v2/developerguide/migrate-from-v1.html).

# Deploy cloud configurations to a Greengrass core device
<a name="configs-core"></a>

1. Make sure that your Greengrass core device is connected to the internet. For example, try successfully navigating to a webpage.

1. Make sure that the Greengrass daemon is running on your core device. In your core device terminal, run the following commands to check whether the daemon is running and start it, if needed.

   1. To check whether the daemon is running:

      ```
      ps aux | grep -E 'greengrass.*daemon'
      ```

      If the output contains a `root` entry for `/greengrass/ggc/packages/1.11.6/bin/daemon`, then the daemon is running.

   1. To start the daemon:

      ```
      cd /greengrass/ggc/core/
      sudo ./greengrassd start
      ```

   Now you're ready to deploy the Lambda function and subscription configurations to your Greengrass core device.

1. <a name="console-gg-groups"></a>In the AWS IoT console navigation pane, under **Manage**, expand **Greengrass devices**, and then choose **Groups (V1)**.

1. Under **Greengrass groups**, choose the group that you created in [Module 2](module2.md).

1. On the group configuration page, choose **Deploy**.

1. On the **Lambda functions** tab, in the **System Lambda functions** section, choose **IP detector**.

1. Choose **Edit** and select **Automatically detect and override MQTT broker endpoints**. This enables devices to automatically acquire connectivity information for the core, such as IP address, DNS, and port number. Automatic detection is recommended, but AWS IoT Greengrass also supports manually specified endpoints. You're only prompted for the discovery method the first time that the group is deployed.

The first deployment might take a few minutes. When the deployment is complete, you should see **Successfully completed** in the **Status** column on the **Deployments** page:

**Note**
The deployment status is also displayed below the group's name on the page header.

For troubleshooting help, see [Troubleshooting AWS IoT Greengrass](gg-troubleshooting.md).
