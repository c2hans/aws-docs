---
source_url: https://docs.aws.amazon.com/greengrass/v2/developerguide/install-greengrass-v2.html
---

# Step 3: Install the AWS IoT Greengrass Core software
<a name="install-greengrass-v2"></a>

**Tip**
We recommend you try out [AWS IoT Greengrass AI Agents Context Pack](https://github.com/aws-greengrass/greengrass-agent-context-pack) to quickly set up and experiment with AWS IoT Greengrass. The agent context pack will enable AI agents to set up Greengrass Nucleus and Nucleus Lite, deploy components, and troubleshoot common issues.

Follow the steps in this section to set up your Raspberry Pi as a AWS IoT Greengrass core device that you can use for local development. In this section, you download and run an installer that does the following to configure the AWS IoT Greengrass Core software for your device:
+ Installs the Greengrass nucleus component. The nucleus is a mandatory component and is the minimum requirement to run the AWS IoT Greengrass Core software on a device. For more information, see [Greengrass nucleus component](greengrass-nucleus-component.md).
+ Registers your device as an AWS IoT thing and downloads a digital certificate that allows your device to connect to AWS. For more information, see [Device authentication and authorization for AWS IoT Greengrass](device-auth.md).
+ Adds the device's AWS IoT thing to a thing group, which is a group or fleet of AWS IoT things. Thing groups enable you to manage fleets of Greengrass core devices. When you deploy software components to your devices, you can choose to deploy to individual devices or to groups of devices. For more information, see [Managing devices with AWS IoT](https://docs.aws.amazon.com/iot/latest/developerguide/iot-thing-management.html) in the *AWS IoT Core Developer Guide*.
+ Creates the IAM role that allows your Greengrass core device to interact with AWS services. By default, this role allows your device to interact with AWS IoT and send logs to Amazon CloudWatch Logs. For more information, see [Authorize core devices to interact with AWS services](device-service-role.md).
+ Installs the AWS IoT Greengrass command line interface (`greengrass-cli`), which you can use to test custom components that you develop on the core device. For more information, see [Greengrass Command Line Interface](gg-cli.md).

The AWS IoT Greengrass Core software and local development tools run on your device. Next, you can develop a Hello World AWS IoT Greengrass component on your device.
