---
source_url: https://docs.aws.amazon.com/freertos/latest/portingguide/freertos-porting-cellular.html
---

# Porting the Cellular Interface library
<a name="freertos-porting-cellular"></a>

FreeRTOS supports the AT commands of a TCP offloaded cellular abstraction layer. For more information, see the [Cellular Interface Library](https://freertos.org/cellular/index.html) and [Porting the Cellular Interface Library](https://freertos.org/cellular-porting-guide.html) on freertos.org.

## Prerequisites
<a name="freertos-porting-cellular-prereqs"></a>

There is no direct dependency for the Cellular Interface library. However, in the FreeRTOS network stack, Ethernet, Wi-Fi and cellular cannot co-exist, so developers must choose one of them to integrate with the [Porting the Network Transport Interface](afr-porting-network-transport-interface.md).

**Note**
If the cellular module is able to support TLS offload, or does not support AT commands, developers can implement their own cellular abstraction to integrate with the [Porting the Network Transport Interface](afr-porting-network-transport-interface.md).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for FreeRTOS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query freertos` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
