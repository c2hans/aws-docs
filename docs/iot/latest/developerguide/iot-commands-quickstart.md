---
source_url: https://docs.aws.amazon.com/iot/latest/developerguide/iot-commands-quickstart.html
---

# Quick start
<a name="iot-commands-quickstart"></a>

Complete these steps to send your first command:

1. **Prerequisites** - Ensure you are onboarded to IoT Core, a device connected to IoT Core, IAM permissions for Commands API operations, and an MQTT client library installed on your device.

1. **Create a command** - Define a command with a static payload, or a payload template specifying device actions. See [Create a command resource](iot-remote-command-create-manage.md#iot-remote-command-create).

1. **Identify your device** - Register your device as an IoT thing or note its MQTT client ID. See [Target device considerations](iot-remote-command-execution-start-monitor.md#iot-command-execution-target).

1. **Configure permissions** - Set up IAM policies allowing your device to receive commands and publish responses.

1. **Subscribe to topics** - Configure your device to subscribe to commands request and response topics. See [Choose target device for your commands and subscribe to MQTT topics](iot-remote-command-workflow.md#command-choose-target).

1. **Execute the command** - Start the command execution on your target device. See [Start a command execution](iot-remote-command-execution-start-monitor.md#iot-remote-command-execution-start).

**Common use cases:**
+ *Remote diagnostics* - Retrieve logs, run diagnostics, check device health
+ *Configuration updates* - Change settings, update parameters, toggle features
+ *Device control* - Lock/unlock, power on/off, mode changes

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS IoT Core. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query iot` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
