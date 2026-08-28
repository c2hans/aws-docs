---
source_url: https://docs.aws.amazon.com/whitepapers/latest/implementing-lpwan-solutions-with-aws/managing-cellular-connectivity.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Managing cellular connectivity
<a name="managing-cellular-connectivity"></a>

 Customers can use FreeRTOS connectivity libraries for Wi-Fi and cellular to enable their applications to interact with the communication interfaces on the MCUs. The [FreeRTOS Cellular library](https://www.freertos.org/cellular/index.html) exposes the capability of a few popular cellular modems through a uniform API. That API hides the complexity of AT commands, and exposes a socket-like interface to C programmers. The [FreeRTOS Wi-Fi library](https://docs.aws.amazon.com/freertos/latest/userguide/freertos-wifi.html) abstracts port-specific Wi-Fi implementations into a common API. Using this API, applications can communicate with their lower-level wireless stack through a common interface.

**Note**
Applications are typically not using these libraries directly, but are using higher level libraries (for example, [coreMQTT](https://docs.aws.amazon.com/freertos/latest/userguide/coremqtt.html) for ingesting MQTT payloads).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Whitepapers. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query whitepapers` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
