---
source_url: https://docs.aws.amazon.com/greengrass/v2/developerguide/defer-component-updates-tutorial.html
---

# Tutorial: Develop a Greengrass component that defers component updates
<a name="defer-component-updates-tutorial"></a>

You can complete this tutorial to develop a component that defers over-the-air deployment updates. When you deploy updates to your devices, you might want to delay updates based on conditions, such as the following:
+ The device has a low battery level.
+ The device is running a process or job that can't be interrupted.
+ The device has a limited or expensive internet connection.

**Note**
A *component* is a software module that runs on AWS IoT Greengrass core devices. Components enable you to create and manage complex applications as discrete building blocks that you can reuse from one Greengrass core device to another.

In this tutorial, you do the following:

1. Install the Greengrass Development Kit CLI (GDK CLI) on your development computer. The GDK CLI provides features that help you develop custom Greengrass components.

1. Develop a Hello World component that defers component updates when the core device's battery level is below a threshold. This component subscribes to update notifications using the [SubscribeToComponentUpdates](ipc-component-lifecycle.md#ipc-operation-subscribetocomponentupdates) IPC operation. When it receives the notification, it checks if the battery level is lower than a customizable threshold. If the battery level is below the threshold, it defers the update for 30 seconds using the [DeferComponentUpdate](ipc-component-lifecycle.md#ipc-operation-defercomponentupdate) IPC operation. You develop this component on your development computer using the GDK CLI.
**Note**
This component reads battery level from a file that you create on the core device to imitate a real battery, so you can complete this tutorial on a core device without a battery.

1. Publish that component to the AWS IoT Greengrass service.

1. Deploy that component from the AWS Cloud to a Greengrass core device to test it. Then, you modify the virtual battery level on the core device, and create additional deployments to see how the core device defers updates when the battery level is low.

You can expect to spend 20–30 minutes on this tutorial.

You've completed this tutorial. The Hello World component defers or acknowledges updates based on the core device's battery level. For more information about the topics that this tutorial explores, see the following:
+ [Develop AWS IoT Greengrass components](develop-greengrass-components.md)
+ [Deploy AWS IoT Greengrass components to devices](manage-deployments.md)
+ [Use the AWS IoT Device SDK to communicate with the Greengrass nucleus, other components, and AWS IoT Core](interprocess-communication.md)
+ [AWS IoT Greengrass Development Kit Command-Line Interface](greengrass-development-kit-cli.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS IoT Greengrass. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query greengrass` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
