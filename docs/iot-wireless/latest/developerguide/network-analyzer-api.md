---
source_url: https://docs.aws.amazon.com/iot-wireless/latest/developerguide/network-analyzer-api.html
---

# Stream network analyzer trace messages with WebSockets
<a name="network-analyzer-api"></a>

Using the network analyzer API provided by AWS IoT Core for LoRaWAN, you can gain insights into the health and performance of your LoRaWAN network. This API provides visibility into various network metrics, including packet delivery rates, signal strengths, and device connectivity. Using the network analyzer API, you can identify and address potential issues in advance, which ensures reliable and efficient communication between your LoRaWAN devices and the cloud.

Network analyzer trace messages capture detailed information about uplink and downlink transmissions, including packet metadata, signal strengths, and timing information. For example, you can use these trace messages to gain invaluable insights into the root cause of network performance issues or device connectivity problems.

When you use the WebSocket protocol, you can stream network analyzer trace messages in real time. When you send a request, the service responds with a JSON structure. After you activate trace messaging, you can use the message logs to get information about your resources and troubleshoot errors. For more information, see [WebSocket protocol](https://tools.ietf.org/html/rfc6455).

The following topics show how to stream network analyzer trace messages with WebSockets.

**Topics**
+ [Generate a presigned request with the WebSocket library](network-analyzer-generate-request.md)
+ [Sample Python code to generate presigned URL](network-analyzer-request-sample.md)
+ [WebSocket messages and status codes](network-analyzer-messages-status.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS IoT Wireless. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query iot-wireless` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
