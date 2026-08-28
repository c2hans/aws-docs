---
source_url: https://docs.aws.amazon.com/freertos/latest/userguide/coremqtt.html
---

# coreMQTT library
<a name="coremqtt"></a>

**Note**  <a name="out-of-date-message"></a>
The content on this page may not be up-to-date. Please refer to the [FreeRTOS.org library page](https://www.freertos.org/Documentation/03-Libraries/01-Library-overview/01-All-libraries) for the latest update.

## Introduction
<a name="coremqtt-introduction"></a>

The coreMQTT library is a client implementation of the [MQTT](https://en.wikipedia.org/wiki/MQTT) (Message Queue Telemetry Transport) standard. The MQTT standard provides a lightweight publish/subscribe (or [PubSub](https://en.wikipedia.org/wiki/Publish%E2%80%93subscribe_pattern)) messaging protocol that runs on top of TCP/IP and is often used in Machine to Machine (M2M) and Internet of Things (IoT) use cases.

The coreMQTT library is compliant with the [ MQTT 3.1.1](http://docs.oasis-open.org/mqtt/mqtt/v3.1.1/mqtt-v3.1.1.html) protocol standard. This library has been optimized for a low memory footprint. The design of this library embraces different use-cases, ranging from resource-constrained platforms using only QoS 0 MQTT PUBLISH messages to resource-rich platforms using QoS 2 MQTT PUBLISH over TLS (Transport Layer Security) connections. The library provides a menu of composable functions, which can be chosen and combined to precisely fit the needs of a particular use-case.

The library is written in **C** and designed to be compliant with [ISO C90](https://en.wikipedia.org/wiki/ANSI_C#C90) and [MISRA C:2012](https://misra.org.uk/product/misra-c2012-third-edition-first-revision/). This MQTT library has no dependencies on any additional libraries except for the following:
+ The standard C library
+ A customer-implemented network transport interface
+ (Optional) A user-implemented platform time function

The library is decoupled from the underlying network drivers through the provision of a simple send and receive transport interface specification. The application writer can select an existing transport interface, or implement their own as appropriate for their application.

The library provides a high-level API to connect to an MQTT broker, subscribe/unsubscribe to a topic, publish a message to a topic and receive incoming messages. This API takes the transport interface described above as a parameter and uses that to send and receive messages to and from the MQTT broker.

The library also exposes low level serializer/deserializer API. This API can be used to build a simple IoT application consisting of only the required a subset of MQTT functionality, without any other overhead. The serializer/deserializer API can be used in conjunction with any available transport layer API, like sockets, to send and receive messages to and from the broker.

When using MQTT connections in IoT applications, we recommended that you use a secure transport interface, such as one that uses the TLS protocol.

This MQTT library doesn't have platform dependencies, such as threading or synchronization. This library does have [proofs](https://www.cprover.org/cbmc/) that demonstrate safe memory use and no heap allocation, which makes it suitable for IoT microcontrollers, but also fully portable to other platforms. It can be freely used, and is distributed under the [MIT open source license](https://freertos.org/a00114.html).

<a name="coreMQTT-memory-estimate"></a>
<table>
<thead>
  <tr><th colspan="3">Code Size of coreMQTT (example generated with GCC for ARM Cortex-M)</th></tr>
  <tr><th>File</th><th>With -O1 Optimization</th><th>With -Os Optimization</th></tr>
</thead>
<tbody>
  <tr><td>core_mqtt.c</td><td>4.0K</td><td>3.4K</td></tr>
  <tr><td>core_mqtt_state.c</td><td>1.7K</td><td>1.3K</td></tr>
  <tr><td>core_mqtt_serializer.c</td><td>2.8K</td><td>2.2K</td></tr>
  <tr><td><b>Total estimates</b></td><td><b>8.5K</b></td><td><b>6.9K</b></td></tr>
</tbody>
</table>

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for FreeRTOS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query freertos` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
