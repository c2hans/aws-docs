---
source_url: https://docs.aws.amazon.com/greengrass/v1/developerguide/module3-I.html
---

End of support notice: On October 7th, 2026, AWS will discontinue support for AWS IoT Greengrass Version 1. After October 7th, 2026, you will no longer be able to access the AWS IoT Greengrass V1 resources. For more information, please visit [Migrate from AWS IoT Greengrass Version 1](https://docs.aws.amazon.com/greengrass/v2/developerguide/migrate-from-v1.html).

# Module 3 (part 1): Lambda functions on AWS IoT Greengrass
<a name="module3-I"></a>

This module shows you how to create and deploy a Lambda function that sends MQTT messages from your AWS IoT Greengrass core device. The module describes Lambda function configurations, subscriptions used to allow MQTT messaging, and deployments to a core device.

[Module 3 (Part 2)](module3-II.md) covers the differences between on-demand and long-lived Lambda functions running on the AWS IoT Greengrass core.

Before you begin, make sure that you have completed [Module 1](module1.md) and [Module 2](module2.md) and have a running AWS IoT Greengrass core device.

**Tip**
Or, to use a script that sets up your core device for you, see [Quick start: Greengrass device setup](quick-start.md). The script can also create and deploy the Lambda function used in this module.

This module should take about 30 minutes to complete.

**Topics**
+ [Create and package a Lambda function](create-lambda.md)
+ [Configure the Lambda function for AWS IoT Greengrass](config-lambda.md)
+ [Deploy cloud configurations to a Greengrass core device](configs-core.md)
+ [Verify the Lambda function is running on the core device](lambda-check.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS IoT Greengrass. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query greengrass` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
