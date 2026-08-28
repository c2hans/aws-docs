---
source_url: https://docs.aws.amazon.com/iot-sitewise/latest/userguide/sa-update-config.html
---

# Update the AWS IoT SiteWise Edge application configuration
<a name="sa-update-config"></a>

There are a few things to consider when updating an AWS IoT SiteWise Edge application configuration on **Siemens Industrial Edge**.

**Note**
Any change to the AWS IoT SiteWise Edge application configuration requires a restart of the application.

**Reasons to restart the AWS IoT SiteWise Edge application**
+ A new Siemens Databus user for the AWS IoT SiteWise Edge application.
+ A change to the gateway configuration file (your **SiteWise\_Edge\_Gateway\_Config** file).
+ A proxy configuration update (which also requires a full IEVD reboot)
+ To enable debug logs for debugging issues

## Restarting the application
<a name="sa-restart-app"></a>

1. In your Siemens Industrial Edge Management instance, choose **Edge Management** in the **Platform Applications** section.

1. Choose **My Installed Apps**.

1. Select the AWS IoT SiteWise Edge application.

1. Choose **Restart**.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS IoT SiteWise. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query iot-sitewise` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
