---
source_url: https://docs.aws.amazon.com/freertos/latest/userguide/ota-prereqs.html
---

# OTA update prerequisites
<a name="ota-prereqs"></a>

To use over-the-air (OTA) updates, do the following:
+ Check the [Prerequisites for OTA updates using HTTP](ota-http-freertos.md) or the [Prerequisites for OTA updates using MQTT](ota-mqtt-freertos.md).
+ [Create an Amazon S3 bucket to store your update](dg-ota-bucket.md).
+ [Create an OTA Update service role](create-service-role.md).
+ [Create an OTA user policy](create-ota-user-policy.md).
+ [Create a code-signing certificate](ota-code-sign-cert.md).
+ If you are using Code Signing for AWS IoT, [Grant access to code signing for AWS IoT](code-sign-policy.md).
+ [Download FreeRTOS with the OTA library](ota-download-freertos.md).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for FreeRTOS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query freertos` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
