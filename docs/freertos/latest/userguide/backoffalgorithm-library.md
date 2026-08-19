---
source_url: https://docs.aws.amazon.com/freertos/latest/userguide/backoffalgorithm-library.html
---

# backoffAlgorithm library
<a name="backoffalgorithm-library"></a>

**Note**  <a name="out-of-date-message"></a>
The content on this page may not be up-to-date. Please refer to the [FreeRTOS.org library page](https://www.freertos.org/Documentation/03-Libraries/01-Library-overview/01-All-libraries) for the latest update.

## Introduction
<a name="freertos-boa-introduction"></a>

The [backoffAlgorithm](https://github.com/FreeRTOS/backoffAlgorithm) library is a utility library that is used to space out repeated retransmissions of the same block of data, to avoid network congestion. This library calculates the backoff period for retrying network operations (like a failed network connection with the server) using an [ exponential backoff with jitter](https://aws.amazon.com/blogs/architecture/exponential-backoff-and-jitter/) algorithm.

Exponential backoff with jitter is typically used when retrying a failed connection or network request to a server that is caused by network congestion or high loads on the server. It is used to spread out the timing of the retry requests created by multiple devices attempting network connections at the same time. In an environment with poor connectivity, a client can get disconnected at any time; so a backoff strategy also helps the client to conserve battery by not repeatedly attempting reconnections when they are unlikely to succeed.

The library is written in C and designed to be compliant with [ISO C90](https://en.wikipedia.org/wiki/ANSI_C#C90) and [MISRA C:2012](https://misra.org.uk/product/misra-c2012-third-edition-first-revision/). The library has no dependencies on any additional libraries other than the standard C library and has no heap allocation, making it suitable for IoT microcontrollers, but also fully portable to other platforms.

This library can be freely used and is distributed under the [MIT open source license](https://freertos.org/a00114.html).

<a name="backoffalgorithm-memory-estimate"></a>
<table>
<thead>
  <tr><th colspan="3">Code Size of backoffAlgorithm (example generated with GCC for ARM Cortex-M)</th></tr>
  <tr><th>File</th><th>With -O1 Optimization</th><th>With -Os Optimization</th></tr>
</thead>
<tbody>
  <tr><td>backoff_algorithm.c</td><td>0.1K</td><td>0.1K</td></tr>
  <tr><td><b>Total estimates</b></td><td><b>0.1K</b></td><td><b>0.1K</b></td></tr>
</tbody>
</table>
