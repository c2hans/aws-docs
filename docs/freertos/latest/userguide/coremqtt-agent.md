---
source_url: https://docs.aws.amazon.com/freertos/latest/userguide/coremqtt-agent.html
---

# coreMQTT Agent library
<a name="coremqtt-agent"></a>

**Note**  <a name="out-of-date-message"></a>
The content on this page may not be up-to-date. Please refer to the [FreeRTOS.org library page](https://www.freertos.org/Documentation/03-Libraries/01-Library-overview/01-All-libraries) for the latest update.

## Introduction
<a name="coremqtt-agent-introduction"></a>

The coreMQTT Agent library is a high level API that adds thread safety to the [coreMQTT library](coremqtt.md). It lets you create a dedicated MQTT agent task that manages an MQTT connection in the background and doesn't need any intervention from other tasks. The library provides thread safe equivalents to the coreMQTT's APIs, so it can be used in multi-threaded environments.

The MQTT agent is an independent task (or thread of execution). It achieves thread safety by being the only task that is permitted to access the MQTT library's API. It serializes access by isolating all MQTT API calls to a single task, and it removes the need for semaphores or any other synchronization primitives.

The library uses a thread safe messaging queue (or other inter-process communication mechanism) to serialize all requests to call MQTT APIs. The messaging implementation is decoupled from the library through a messaging interface, which allows the library to be ported to other operating systems. The messaging interface is composed of functions to send and receive pointers to the agent's command structures, and functions to allocate these command objects, which allows the application writer to decide the memory allocation strategy appropriate for their application.

The library is written in C and designed to be compliant with [ISO C90](https://en.wikipedia.org/wiki/ANSI_C#C90) and [MISRA C:2012](https://misra.org.uk/product/misra-c2012-third-edition-first-revision/). The library has no dependencies on any additional libraries other than [coreMQTT library](coremqtt.md) and the standard C library. The library has [proofs](https://www.cprover.org/cbmc/) that show safe memory use and no heap allocation, so it can be used for IoT microcontrollers, but is also fully portable to other platforms.

This library can be freely used and is distributed under the [ MIT open source license](https://www.freertos.org/a00114.html).

****
<a name="coreMQTTAgent-memory-estimate"></a>
<table>
<thead>
  <tr><th colspan="3">Code Size of coreMQTT Agent (example generated with GCC for ARM Cortex-M)</th></tr>
  <tr><th>File</th><th>With -O1 Optimization</th><th>With -Os Optimization</th></tr>
</thead>
<tbody>
  <tr><td>core_mqtt_agent.c</td><td>1.7K</td><td>1.5K</td></tr>
  <tr><td>core_mqtt_agent_command_functions.c</td><td>0.3K</td><td>0.2K</td></tr>
  <tr><td>core_mqtt.c (coreMQTT)</td><td>4.0K</td><td>3.4K</td></tr>
  <tr><td>core_mqtt_state.c (coreMQTT)</td><td>1.7K</td><td>1.3K</td></tr>
  <tr><td>core_mqtt_serializer.c (coreMQTT)</td><td>2.8K</td><td>2.2K</td></tr>
  <tr><td><b>Total estimates</b></td><td><b>10.5K</b></td><td><b>8.6K</b></td></tr>
</tbody>
</table>
