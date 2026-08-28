---
source_url: https://docs.aws.amazon.com/freertos/latest/portingguide/afr-porting.html
---

# Porting the FreeRTOS libraries
<a name="afr-porting"></a>

Before you start porting, follow the instructions at [Setting up your workspace and project for porting](porting-set-up-project.md).

The [FreeRTOS porting flowchart](porting-chart.md) describes the libraries required for porting.

To port FreeRTOS to your device, follow the instructions in the topics below.

1. [Configuring a FreeRTOS kernel port](afr-porting-kernel.md)

1. [Implementing the library logging macros](afr-library-logging-macros.md)

1. [Porting a TCP/IP stack](afr-porting-tcp.md)

1. [Porting the Network Transport Interface](afr-porting-network-transport-interface.md)

1. [Porting the corePKCS11 library](afr-porting-pkcs.md)

1. [Configuring the coreMQTT library](afr-porting-mqtt.md)

1. [Configuring the coreHTTP library](afr-porting-corehttp.md)

1. [Porting the AWS IoT over-the-air (OTA) update library](afr-porting-ota.md)

1. [Porting the Cellular Interface library](freertos-porting-cellular.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for FreeRTOS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query freertos` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
