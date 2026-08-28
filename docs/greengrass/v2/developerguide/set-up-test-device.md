---
source_url: https://docs.aws.amazon.com/greengrass/v2/developerguide/set-up-test-device.html
---

# Set up a new device to test V1 applications on V2
<a name="set-up-test-device"></a>

To minimize risk to your devices in production, create a new device to test your V1 applications on V2 before upgrading your production devices.

Choose one of the following setup guides based on your runtime selection from the previous step:
+ **Option A - Greengrass nucleus runtime**: Follow [Set up a new device to test V1 applications on V2](set-up-v2-test-device.md) if you chose Greengrass nucleus. With this option, you can import Lambda functions as Lambda components with minimal code changes and supports V1 features like local shadow service, client devices, and connectors.
+ **Option B - Greengrass nucleus lite runtime**: Follow [Set up a new device to test V1 applications on V2 (Greengrass nucleus lite)](set-up-v2-test-device-lite.md) if you chose Greengrass nucleus lite. This option requires converting Lambda functions to generic components using the AWS IoT Device SDK V2 or AWS IoT Greengrass Component SDK, but is optimized for resource-constrained devices.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS IoT Greengrass. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query greengrass` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
