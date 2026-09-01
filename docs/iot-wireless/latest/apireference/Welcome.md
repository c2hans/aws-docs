---
source_url: https://docs.aws.amazon.com/iot-wireless/latest/apireference/Welcome.html
---

# Welcome
<a name="Welcome"></a>

AWS IoT Wireless provides bi-directional communication between internet-connected wireless devices and the AWS Cloud. To onboard both [LoRaWAN](https://docs.aws.amazon.com/iot-wireless/latest/developerguide/iot-lorawan.html) and [Sidewalk](https://docs.aws.amazon.com/iot-wireless/latest/developerguide/iot-sidewalk.html) devices to AWS IoT, use the IoT Wireless API. These wireless devices use the Low Power Wide Area Networking (LPWAN) communication protocol to communicate with AWS IoT.

Using the API, you can perform create, read, update, and delete operations for your wireless devices, gateways, destinations, and profiles. After onboarding your devices, you can use the API operations to set log levels and monitor your devices with CloudWatch.

You can also use the API operations to create multicast groups and schedule a multicast session for sending a downlink message to devices in the group. By using Firmware Updates Over-The-Air (FUOTA) API operations, you can create a FUOTA task and schedule a session to update the firmware of individual devices or an entire group of devices in a multicast group.

To connect to the AWS IoT Wireless Service, use the Service endpoints as described in [IoT Wireless Service endpoints](https://docs.aws.amazon.com/general/latest/gr/iot-lorawan.html#iot-wireless_region). You can use both IPv4 and IPv6 protocols to connect to the endpoints and send requests to the AWS IoT Wireless service. For more information, see [Using IPv6 with AWS IoT Wireless](https://docs.aws.amazon.com/iot-wireless/latest/developerguide/wireless-ipv6-access.html).

This document was last published on September 1, 2026.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS IoT Wireless. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query iot-wireless` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
