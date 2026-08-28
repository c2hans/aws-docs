---
source_url: https://docs.aws.amazon.com/iot/latest/developerguide/iot-moisture-create-thing.html
---

# Step 2: Create the AWS IoT thing, certificate, and private key
<a name="iot-moisture-create-thing"></a>

Create a thing in the AWS IoT registry to represent your Raspberry Pi.

1. In the [AWS IoT console](https://console.aws.amazon.com/iot/home), in the navigation pane, choose **Manage**, and then choose **Things**.

1. If a **You don't have any things yet** dialog box is displayed, choose **Register a thing**. Otherwise, choose **Create**.

1. On the **Creating AWS IoT things** page, choose **Create a single thing**.

1. On the **Add your device to the device registry** page, enter a name for your IoT thing (for example, **RaspberryPi**), and then choose **Next**. You can't change the name of a thing after you create it. To change a thing's name, you must create a new thing, give it the new name, and then delete the old thing.

1. On the **Add a certificate for your thing** page, choose **Create certificate**.

1. Choose the **Download** links to download the certificate, private key, and root CA certificate.
**Important**
This is the only time you can download your certificate and private key.

1. To activate the certificate, choose **Activate**. The certificate must be active for a device to connect to AWS IoT.

1. Choose **Attach a policy**.

1. For **Add a policy for your thing**, choose **MoistureSensorPolicy**, and then choose **Register Thing**.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS IoT Core. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query iot` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
