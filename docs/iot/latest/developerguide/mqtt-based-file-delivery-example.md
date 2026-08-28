---
source_url: https://docs.aws.amazon.com/iot/latest/developerguide/mqtt-based-file-delivery-example.html
---

# An example use case in FreeRTOS OTA
<a name="mqtt-based-file-delivery-example"></a>

The FreeRTOS OTA (over-the-air) agent uses AWS IoT MQTT-based file delivery to transfer FreeRTOS firmware images to FreeRTOS devices. To send the initial data set to a device, it uses the AWS IoT Job service to schedule an OTA update job to FreeRTOS devices.

For a reference implementation of an MQTT-based file delivery client, see [FreeRTOS OTA agent codes](https://docs.aws.amazon.com/freertos/latest/userguide/freertos-ota-dev.html) in the FreeRTOS documentation.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS IoT Core. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query iot` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
