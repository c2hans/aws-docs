---
source_url: https://docs.aws.amazon.com/whitepapers/latest/securing-iot-with-aws/freertos-device-software.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# FreeRTOS – Device software
<a name="freertos-device-software"></a>

 FreeRTOS is an open source operating system for microcontrollers that makes small, low-power edge devices easy to program, deploy, secure, connect, and manage. FreeRTOS is a popular open source operating system for microcontrollers that has been extended with software libraries that make it easy to securely connect customers’ small, low-power devices directly to AWS Cloud services (such as AWS IoT Core) or to more powerful edge devices running AWS IoT Greengrass.

## Security capabilities
<a name="cap-1"></a>

 FreeRTOS comes with libraries to help secure device data and connections, including support for data encryption and key management. FreeRTOS includes support for Transport Layer Security (TLS v1.2) to help devices connect securely to the cloud. FreeRTOS also has a code signing feature to ensure customer device code is not compromised during deployment as well as capabilities for OTA updates to remotely update devices with feature enhancements or security patches.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Whitepapers. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query whitepapers` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
