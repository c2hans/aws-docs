---
source_url: https://docs.aws.amazon.com/greengrass/v1/developerguide/module4.html
---

End of support notice: On October 7th, 2026, AWS will discontinue support for AWS IoT Greengrass Version 1. After October 7th, 2026, you will no longer be able to access the AWS IoT Greengrass V1 resources. For more information, please visit [Migrate from AWS IoT Greengrass Version 1](https://docs.aws.amazon.com/greengrass/v2/developerguide/migrate-from-v1.html).

# Module 4: Interacting with client devices in an AWS IoT Greengrass group
<a name="module4"></a>

This module shows you how local IoT devices, called *client devices* or *devices*, can connect to and communicate with an AWS IoT Greengrass core device. Client devices that connect to an AWS IoT Greengrass core are part of an AWS IoT Greengrass group and can participate in the AWS IoT Greengrass programming paradigm. In this module, one client device sends a Hello World message to another client device in the Greengrass group.

![AWS IoT connected to an AWS IoT Greengrass core, which is connected to client device #1 and client device #2.](http://docs.aws.amazon.com/greengrass/v1/developerguide/images/gg-get-started-065.5.png)

Before you begin, run the [Greengrass device setup](quick-start.md) script or complete [Module 1](module1.md) and [Module 2](module2.md). This module creates two simulated client devices. You do not need other components or devices.

This module should take less than 30 minutes to complete.

**Topics**
+ [Create client devices in an AWS IoT Greengrass group](device-group.md)
+ [Configure subscriptions](config-subs.md)
+ [Install the AWS IoT Device SDK for Python](IoT-SDK.md)
+ [Test communications](test-comms.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS IoT Greengrass. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query greengrass` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
