---
source_url: https://docs.aws.amazon.com/whitepapers/latest/implementing-lpwan-solutions-with-aws/lorawan-network-architecture.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# LoRaWAN network architecture
<a name="lorawan-network-architecture"></a>

 The following figure shows a simplified representation of a LoRaWAN network architecture:

![Diagram showing a LoRaWAN network architecture (simplified)](http://docs.aws.amazon.com/whitepapers/latest/implementing-lpwan-solutions-with-aws/images/lorawan-network-architecture.png)

 **LoRaWAN radio gateway**

 The radio gateway forwards all received LoRaWAN radio packets to the network server that is connected through an IP backbone. Its role is to decode uplink radio packets from the air and forward them unprocessed to the network server. For downlinks, the radio gateway forwards the packet transmission requests coming from the LoRaWAN network server without any interpretation of the packet payload.

## LoRaWAN network server
<a name="lorawan-network-server"></a>

 The network server shuts down the LoRaWAN layer for the LoRaWAN end devices connected to the network. Some functions of the network server include:
+  Deduplicating uplink messages from the devices. Deduplication is necessary in case several gateways within reach of the device receive and forward the message to the LoRaWAN network server.
+  Forwarding uplink application payloads to the appropriate application servers.
+  Queueing of downlink payloads.
+  Interacting with the join server during the join procedure.

## LoRaWAN application server
<a name="lorawan-application-server"></a>

 The application server handles all of the application layer payloads from the end devices. It also generates all the application layer downlink payloads towards the connected end devices.

## LoRaWAN join server
<a name="lorawan-join-server"></a>

 The join server manages the OTA end device activation process.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Whitepapers. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query whitepapers` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
