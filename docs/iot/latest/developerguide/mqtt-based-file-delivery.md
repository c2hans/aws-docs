---
source_url: https://docs.aws.amazon.com/iot/latest/developerguide/mqtt-based-file-delivery.html
---

# MQTT-based file delivery
<a name="mqtt-based-file-delivery"></a>

One option you can use to manage files and transfer them to AWS IoT devices in your fleet is MQTT-based file delivery. With this feature in the AWS Cloud you can create a *stream* that contains multiple files, you can update stream data (the file list and descriptions), get the stream data, and more. AWS IoT MQTT-based file delivery can transfer data in small blocks to your IoT devices, using the MQTT protocol with support for request and response messages in JSON or CBOR.

For more information on ways to transfer data to and from IoT devices using AWS IoT, see [Connect devices to AWS IoT](iot-connect-devices.md).

**Topics**
+ [What is a stream?](mqtt-based-file-delivery-what-is.md)
+ [Managing a stream in the AWS Cloud](mqtt-based-file-delivery-managing.md)
+ [Using AWS IoT MQTT-based file delivery in devices](mqtt-based-file-delivery-in-devices.md)
+ [An example use case in FreeRTOS OTA](mqtt-based-file-delivery-example.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS IoT Core. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query iot` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
