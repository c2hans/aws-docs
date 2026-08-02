---
source_url: https://docs.aws.amazon.com/freertos/latest/userguide/core-http.html
---

# coreHTTP library
<a name="core-http"></a>

**Note**  <a name="out-of-date-message"></a>
The content on this page may not be up-to-date. Please refer to the [FreeRTOS.org library page](https://www.freertos.org/Documentation/03-Libraries/01-Library-overview/01-All-libraries) for the latest update.

**HTTP C client library for small IoT devices (MCU or small MPU)**

## Introduction
<a name="core-http-introduction"></a>

The coreHTTP library is a client implementation of a subset of the [HTTP/1.1](https://en.wikipedia.org/wiki/Hypertext_Transfer_Protocol) standard. The HTTP standard provides a stateless protocol that runs on top of TCP/IP and is often used in distributed, collaborative, hypertext information systems.

The coreHTTP library implements a subset of the [HTTP/1.1 ](https://tools.ietf.org/html/rfc2616) protocol standard. This library has been optimized for a low memory footprint. The library provides a fully synchronous API so applications can completely manage their concurrency. It uses fixed buffers only, so that applications have complete control of their memory allocation strategy.

The library is written in C and designed to be compliant with [ISO C90](https://en.wikipedia.org/wiki/ANSI_C#C90) and [MISRA C:2012](https://misra.org.uk/product/misra-c2012-third-edition-first-revision/). The library's only dependencies are the standard C library and [LTS version (v12.19.1) of the http-parser](https://github.com/nodejs/node/tree/v12.19.1/deps/http_parser) from Node.js. The library has [proofs](https://www.cprover.org/cbmc/) showing safe memory use and no heap allocation, making it suitable for IoT microcontrollers, but also fully portable to other platforms.

When using HTTP connections in IoT applications, we recommend that you use a secure transport interface, such as one that uses the TLS protocol as demonstrated in the [coreHTTP mutual authentication demo](core-http-ma-demo.md).

This library can be freely used and is distributed under the [MIT open source license](https://freertos.org/a00114.html).

****
<a name="coreHTTP-memory-estimate"></a>
<table>
<thead>
  <tr><th colspan="3">Code Size of coreHTTP (example generated with GCC for ARM Cortex-M)</th></tr>
  <tr><th>File</th><th>With -O1 Optimization</th><th>With -Os Optimization</th></tr>
</thead>
<tbody>
  <tr><td>core\_http\_client.c</td><td>3.2K</td><td>2.6K</td></tr>
  <tr><td>api.c (llhttp)</td><td>2.6K</td><td>2.0K</td></tr>
  <tr><td>http.c (llhttp)</td><td>0.3K</td><td>0.3K</td></tr>
  <tr><td>llhttp.c (llhttp)</td><td>17.9</td><td>15.9</td></tr>
  <tr><td>Total estimates</td><td>23.9K</td><td>20.7K</td></tr>
</tbody>
</table>
