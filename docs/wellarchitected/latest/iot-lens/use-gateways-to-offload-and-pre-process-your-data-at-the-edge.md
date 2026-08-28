---
source_url: https://docs.aws.amazon.com/wellarchitected/latest/iot-lens/use-gateways-to-offload-and-pre-process-your-data-at-the-edge.html
---

# Use gateways to offload and pre-process your data at the edge
<a name="use-gateways-to-offload-and-pre-process-your-data-at-the-edge"></a>

 The decision to connect a device directly to the cloud or via a gateway will depend on a variety of factors, including the specific requirements of the application and the characteristics of the sensor and network.   It may be more power-efficient to use a gateway to receive and preprocess data locally, reducing the need for higher power radios on the device, reducing long-haul communications traffic and extending battery life.

 If the device generates a large amount of data, it may be more efficient to use a gateway to pre-process and filter the data before sending it to the cloud, reducing long-haul network traffic. In addition, if the long-haul network connection is unreliable, it may be more practical to use a gateway with [AWS IoT Greengrass](https://docs.aws.amazon.com/greengrass/v2/developerguide/what-is-iot-greengrass.html) to buffer data and make sure that it is delivered reliably to the cloud.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Well-Architected. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query wellarchitected` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
