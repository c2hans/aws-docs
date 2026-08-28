---
source_url: https://docs.aws.amazon.com/greengrass/v1/developerguide/module2.html
---

End of support notice: On October 7th, 2026, AWS will discontinue support for AWS IoT Greengrass Version 1. After October 7th, 2026, you will no longer be able to access the AWS IoT Greengrass V1 resources. For more information, please visit [Migrate from AWS IoT Greengrass Version 1](https://docs.aws.amazon.com/greengrass/v2/developerguide/migrate-from-v1.html).

# Module 2: Installing the AWS IoT Greengrass Core software
<a name="module2"></a>

This module shows you how to install the AWS IoT Greengrass Core software on your chosen device. In this module, you first create a Greengrass group and core. Then, you download, configure, and start the software on your core device. For more information about AWS IoT Greengrass Core software functionality, see [Configure the AWS IoT Greengrass core](gg-core.md).

Before you begin, make sure that you have completed the setup steps in [Module 1](module1.md) for your chosen device.

**Tip**
<a name="ggc-install-options"></a>AWS IoT Greengrass also provides other options for installing the AWS IoT Greengrass Core software. For example, you can use [Greengrass device setup](quick-start.md) to configure your environment and install the latest version of the AWS IoT Greengrass Core software. Or, on supported Debian platforms, you can use the [APT package manager](install-ggc.md#ggc-package-manager) to install or upgrade the AWS IoT Greengrass Core software. For more information, see [Install the AWS IoT Greengrass Core software](install-ggc.md).

This module should take less than 30 minutes to complete.

**Topics**
+ [Provision an AWS IoT thing to use as a Greengrass core](provision-core.md)
+ [Create an AWS IoT Greengrass group for the core](create-group.md)
+ [Install and run AWS IoT Greengrass on the core device](start-greengrass.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS IoT Greengrass. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query greengrass` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
