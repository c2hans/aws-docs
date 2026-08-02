---
source_url: https://docs.aws.amazon.com/whitepapers/latest/hybrid-architectures-to-address-personal-data-processing-requirements/industrial-iot-with-aws-iot-greengrass.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# 2.3 Industrial IoT with AWS IoT Greengrass
<a name="industrial-iot-with-aws-iot-greengrass"></a>

 Requirements addressed:
+  **REQ1** (data residency)
+  **REQ4** (availability and durability)
+  **Customer-REQ1** (reliable connectivity)

 AWS services – [AWS IoT Greengrass](https://aws.amazon.com/greengrass/) and [AWS IoT Core](https://aws.amazon.com/iot-core/)

![Industrial IoT with AWS IoT Greengrass](http://docs.aws.amazon.com/whitepapers/latest/hybrid-architectures-to-address-personal-data-processing-requirements/images/industrial-iot-with-aws-iot-greengrass.png)

 Industrial IoT with AWS IoT Greengrass

 AWS offers an IoT extension called [AWS IoT Greengrass](https://aws.amazon.com/greengrass/). AWS IoT Greengrass devices can work autonomously on-premises, and in disconnected mode from the internet and AWS. The primary function of AWS IoT Greengrass is to act as a proxy or a buffer between edge devices or IoT sensors and the AWS Cloud. Additionally, it is possible to run Docker containers, use AWS Lambda functions, and run inference models using Amazon SageMaker AI.

 AWS IoT Greengrass can communicate with AWS IoT Core using public networks, such as the internet, as well as through Site-to-Site VPN or Direct Connect (refer to the dotted arrows in the preceding figure). Connectivity through Site-to-Site VPN or Direct Connect helps customers to not expose their local factory networks to the public internet, for safety and security reasons. By using VPC endpoints, customers can enable their devices to connect to AWS IoT Core using an endpoint that resolves to a private IP address within their VPC subnet. In addition, customers can restrict access to IoT Core to allow only connections over their VPC endpoint.

 This lets you fulfill the following requirements:
+  **REQ1** – The device can process (remove or anonymize personal data) and dump data to local storage on a device (local volumes or device resources) to provide a first data copy in the local country.
+  **REQ4** – The ability to operate offline in situations when an online connection to AWS is not accessible, or intermittent. AWS IoT Greengrass buffers the data from devices for a period of time, and uploads the data when the connection is re-established.
+  **Customer-REQ1** – Edge devices and IoT sensors are connected to local IoT AWS IoT Greengrass devices to decrease latency and improve reliability for intermittent connections.

 Requirements **REQ2** (data protection) and **Customer-REQ1** (reliable connectivity) can be met through complimentary use of Architecture 1.1: [Hybrid network connectivity from a data center to the AWS Cloud](hybrid-network-connectivity-from-a-data-center-to-the-aws-cloud.md).
