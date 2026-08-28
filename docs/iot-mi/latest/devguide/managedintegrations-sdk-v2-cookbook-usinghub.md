---
source_url: https://docs.aws.amazon.com/iot-mi/latest/devguide/managedintegrations-sdk-v2-cookbook-usinghub.html
---

# Onboard your hubs to Managed Integrations
<a name="managedintegrations-sdk-v2-cookbook-usinghub"></a>

Set up your hub devices to communicate with Managed Integrations by configuring the required directory structure, certificates, and device configuration files. This section describes how the hub onboarding subsystem components work together, where to store certificates and configuration files, how to create and modify the device configuration file, and the steps to complete the hub provisioning process.

## Hub onboarding subsystem
<a name="managedintegrations-sdk-v2-cookbook-hubsubsystem"></a>

The hub onboarding subsystem uses these core components to manage device provisioning and configuration:

**Hub onboarding component**
Manages the hub onboarding process by coordinating hub state, provisioning approach, and authentication materials.

**Device config file**
Stores essential hub configuration data on the device, including:
+ Device provisioning state (provisioned or non-provisioned)
+ Certificate and key locations
+ Authentication information Other SDK processes, such as the MQTT proxy, reference this file to determine hub state and connection settings.

**Certificate handler interface**
Provides a utility interface for reading and writing device certificates and keys. You can implement this interface to work with:
+ File system storage
+ Hardware security modules (HSM)
+ Trusted platform modules (TPM)
+ Custom secure storage solutions

**MQTT proxy component**
Manages device-to-cloud communication using:
+ Provisioned client certificates and keys
+ Device state information from the config file
+ MQTT connections to Managed Integrations

The following diagram describes the hub onboarding subsystem architecture and its components. If you're not using AWS IoT Greengrass, you can disregard that component of the diagram.

![Hub onboarding subsystem architecture.](http://docs.aws.amazon.com/iot-mi/latest/devguide/images/iot-managedintegrations-hub-onboarding-subsystem.png)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Managed integrations. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query iot-mi` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
