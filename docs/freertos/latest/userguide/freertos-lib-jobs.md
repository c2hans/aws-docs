---
source_url: https://docs.aws.amazon.com/freertos/latest/userguide/freertos-lib-jobs.html
---

# AWS IoT Jobs library
<a name="freertos-lib-jobs"></a>

**Note**  <a name="out-of-date-message"></a>
The content on this page may not be up-to-date. Please refer to the [FreeRTOS.org library page](https://www.freertos.org/Documentation/03-Libraries/01-Library-overview/01-All-libraries) for the latest update.

## Introduction
<a name="freertos-lib-jobs-introduction"></a>

AWS IoT Jobs is a service that notifies one or more connected devices of a pending *job*. You can use a job to manage your fleet of devices, update firmware and security certificates on your devices, or perform administrative tasks such as restarting devices and performing diagnostics. For more information, see [Jobs](https://docs.aws.amazon.com/iot/latest/developerguide/iot-jobs.html) in the *AWS IoT Developer Guide*. Interactions with the AWS IoT Jobs service use [MQTT](https://freertos.org/mqtt/index.html), a lightweight publish-subscribe protocol. This library provides an API to compose and recognize the MQTT topic strings used by the AWS IoT Jobs service.

The AWS IoT Jobs library is written in C and designed to be compliant with [ISO C90](https://en.wikipedia.org/wiki/ANSI_C#C90) and [MISRA C:2012](https://misra.org.uk/product/misra-c2012-third-edition-first-revision/). The library has no dependencies on any additional libraries other than the standard C library. It can be used with any MQTT library and any JSON library. The library has [proofs](https://www.cprover.org/cbmc/) showing safe memory use and no heap allocation, making it suitable for IoT microcontrollers, but also fully portable to other platforms.

This library can be freely used and is distributed under the [MIT open source license](https://freertos.org/a00114.html).

<a name="jobs-memory-estimate"></a>
<table>
<thead>
  <tr><th colspan="3">Code Size of AWS IoT Jobs (example generated with GCC for ARM Cortex-M)</th></tr>
  <tr><th>File</th><th>With -O1 Optimization</th><th>With -Os Optimization</th></tr>
</thead>
<tbody>
  <tr><td>jobs.c</td><td>1.9K</td><td>1.6K</td></tr>
  <tr><td><b>Total estimates</b></td><td><b>1.9K</b></td><td><b>1.6K</b></td></tr>
</tbody>
</table>
