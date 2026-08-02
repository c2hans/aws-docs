---
source_url: https://docs.aws.amazon.com/freertos/latest/userguide/freertos-lib-corejson.html
---

# coreJSON library
<a name="freertos-lib-corejson"></a>

**Note**  <a name="out-of-date-message"></a>
The content on this page may not be up-to-date. Please refer to the [FreeRTOS.org library page](https://www.freertos.org/Documentation/03-Libraries/01-Library-overview/01-All-libraries) for the latest update.

## Introduction
<a name="freertos-corejson-introduction"></a>

JSON (JavaScript Object Notation) is a human-readable data serialization format. It is widely used to exchange data, such as with the [AWS IoT Device Shadow service](https://docs.aws.amazon.com/iot/latest/developerguide/iot-device-shadows.html), and is part of many APIs, such as the GitHub REST API. JSON is maintained as a standard by Ecma International.

The coreJSON library provides a parser that supports key lookups while strictly enforcing the [ECMA-404 Standard JSON Data Interchange syntax](http://www.ecma-international.org/publications/files/ECMA-ST/ECMA-404.pdf). The library is written in C and designed to comply with ISO C90 and MISRA C:2012. It has [proofs](https://www.cprover.org/cbmc/) showing safe memory use and no heap allocation, making it suitable for IoT microcontrollers, but also fully portable to other platforms.

## Memory use
<a name="freertos-corejson-memory"></a>

The coreJSON library uses an internal stack to track nested structures in a JSON document. The stack exists for the duration of a single function call; it is not preserved. Stack size may be specified by defining the macro, `JSON_MAX_DEPTH`, which defaults to 32 levels. Each level consumes a single byte.

****
<a name="coreJSON-memory-estimate"></a>
<table>
<thead>
  <tr><th colspan="3">Code Size of coreJSON (example generated with GCC for ARM Cortex-M)</th></tr>
  <tr><th>File</th><th>With -O1 Optimization</th><th>With -Os Optimization</th></tr>
</thead>
<tbody>
  <tr><td>core\_json.c</td><td>2.9K</td><td>2.4K</td></tr>
  <tr><td>Total estimates</td><td>2.9K</td><td>2.4K</td></tr>
</tbody>
</table>
