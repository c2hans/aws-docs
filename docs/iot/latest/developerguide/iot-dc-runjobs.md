---
source_url: https://docs.aws.amazon.com/iot/latest/developerguide/iot-dc-runjobs.html
---

# Tutorial: Demonstrate remote actions (jobs) with the AWS IoT Device Client
<a name="iot-dc-runjobs"></a>

In these tutorials, you'll configure and deploy jobs to your Raspberry Pi to demonstrate how you can send remote operations to your IoT devices.

**To start this tutorial:**
+ Have your local host computer an Raspberry Pi configured as used in [the previous section](iot-dc-testconn.md).
+ If you haven't completed the tutorial in the previous section, you can try this tutorial by using the Raspberry Pi with a microSD card that has the image you saved after you installed the AWS IoT Device Client in [(Optional) Save the microSD card image](iot-dc-install-download.md#iot-dc-install-dc-save).
+ If you have run this demo before, review [Step 2: Cleaning up your AWS account after building demos with the AWS IoT Device Client](iot-dc-cleanup.md#iot-dc-cleanup-cloud) to delete all AWS IoT resources that you created in earlier runs to avoid duplicate resource errors.

This tutorial takes about 45 minutes to complete.

**When you're finished with this topic:**
+ You'll have demonstrated different ways that your IoT device can use the AWS IoT Core to run remote operations that are managed by AWS IoT .

**Required equipment:**
+ Your local development and testing environment that you tested in [a previous section](iot-dc-install-dc.md)
+ The Raspberry Pi that you tested in [a previous section](iot-dc-install-dc.md)
+ The microSD memory card from the Raspberry Pi that you tested in [a previous section](iot-dc-install-dc.md)

**Topics**
+ [Prepare the Raspberry Pi to run jobs](iot-dc-runjobs-prepare.md)
+ [Create and run the job in AWS IoT with AWS IoT Device Client](iot-dc-runjobs-prepare-define.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS IoT Core. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query iot` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
