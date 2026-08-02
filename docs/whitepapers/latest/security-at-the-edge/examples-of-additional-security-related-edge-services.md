---
source_url: https://docs.aws.amazon.com/whitepapers/latest/security-at-the-edge/examples-of-additional-security-related-edge-services.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Examples of additional security-related edge services
<a name="examples-of-additional-security-related-edge-services"></a>

 AWS offers a range of other security-related edge services, which customers can use to help secure their individual edge environments. These include IoT and hybrid services, as well as services that can be used at the rugged and disconnected edge.

## Internet of Things
<a name="internet-of-things"></a>

 If edge takes computing closer to where the data is generated, AWS IoT services enable the user to enable devices to take actions, aggregate data, and filter it locally on the device. AWS IoT offers integrated edge services for all layers of security, including preventive security mechanisms, like encryption and access control to device data, and a service that continuously monitors and audits configurations through [AWS IoT Device Defender](https://aws.amazon.com/iot-device-defender/).

 Other IoT services support customers to connect their devices and operate them at the edge. For example, [AWS IoT Greengrass](https://aws.amazon.com/greengrass/) seamlessly extends AWS to edge devices so they can act locally on the data they generate, while still using the cloud for management, analytics, and durable storage. AWS IoT Greengrass is an IoT open-source edge runtime and cloud service that helps build, deploy, and manage device software.

 AWS IoT Greengrass authenticates and encrypts device data for both local and cloud communications, so that data is never exchanged between devices and the cloud without proven identity. Another example is [FreeRTOS](https://www.freertos.org/). FreeRTOS is an open-source, real-time operating system for microcontrollers that makes small, low-power edge devices easy to program, deploy, secure, connect, and manage. FreeRTOS provides the kernel to run low-power devices as well as software libraries that make it easy to connect securely to the cloud or other edge devices, so you can collect data for IoT applications and take action.

 FreeRTOS includes support for Transport Layer Security (TLS v1.2) and PKCS \#11 to help your devices connect securely to AWS. FreeRTOS also includes an over-the-air (OTA) update library to remotely update devices with feature enhancements or security patches and a code signing feature to ensure your device code is not compromised during deployment and OTA updates.

**AWS Outposts: Security, low latency, and data residency**
 Sometimes data is required to remain in a specific geographical location for regulatory, contractual, or security reasons. Additionally, some industries, such as financial services, require business applications with single digit millisecond latencies. Customers in the financial services industry use [AWS Outposts](https://aws.amazon.com/outposts/) to deliver high-frequency trading, banking, payments processing, and risk management services while meeting data locality requirements.

## Hybrid services at the edge
<a name="hybrid-services-at-the-edge"></a>
+  [https://aws.amazon.com/outposts/](https://aws.amazon.com/outposts/) — While on your cloud adoption journey, you may find that certain workloads are better suited for on-premises management, whether for lower latency or other local processing needs, and require a hybrid cloud approach. For these workloads, AWS Outposts extends AWS infrastructure and services to your environments. This enables you to support workloads, including sensitive works, which need to remain on-premises, while leveraging the security and operational capabilities of cloud services.

   AWS encourages customers to assess their data classification approach and hone in on which data needs to stay within their country or Region, and why. For more information on data residency, see the AWS whitepaper [https://d1.awsstatic.com/whitepapers/compliance/Data_Residency_Whitepaper.pdf](https://d1.awsstatic.com/whitepapers/compliance/Data_Residency_Whitepaper.pdf).

   For more information on data classification, see the AWS whitepaper [https://d1.awsstatic.com/whitepapers/compliance/AWS_Data_Classification.pdf](https://d1.awsstatic.com/whitepapers/compliance/AWS_Data_Classification.pdf).

  With AWS Outposts, you can control where your workloads run and where your data resides, while using local operational tooling for things like monitoring and stability.
+  [https://aws.amazon.com/wavelength/](https://aws.amazon.com/wavelength/) — AWS Wavelength is an AWS Infrastructure offering which minimizes latency. AWS Wavelength enables developers to build applications that deliver single-digit millisecond latencies to mobile devices and end users. AWS developers can deploy their applications to [Wavelength Zones](https://docs.aws.amazon.com/wavelength/latest/developerguide/wavelength-quotas.html#concepts-available-zones), AWS infrastructure deployments that embed AWS compute and storage services within the telecommunications providers’ data centers at the edge of the 5G networks, and seamlessly access the breadth of AWS services in the Region. This enables developers to deliver applications that require single-digit millisecond latencies, such as game and live video streaming, ML inference at the edge, and augmented reality/virtual reality (AR/VR).
+  [https://aws.amazon.com/storagegateway](https://aws.amazon.com/storagegateway) — For customers in hybrid environments, AWS Storage Gateway seamlessly connects and extends on-premises applications to AWS Cloud storage, caching data locally for low-latency access and optimizing data transfers to AWS.

   By integrating with AWS services such as Amazon CloudWatch, Storage Gateway enables secure access to AWS services, easy management and monitoring, and tracking of user activity on AWS resources. Customers with data in the cloud can distribute the data to multiple edge locations, or capture data from multiple edge locations, perform in-cloud processing and analytics, and provide access to endpoints in distributed locations.

 Customers with hybrid environments can use [AWS Direct Connect](https://aws.amazon.com/directconnect), a VPN, or the public internet to connect their on-premises environment to the core AWS Cloud.

## Rugged and disconnected edge
<a name="rugged-and-disconnected-edge"></a>

 The edge is continually expanding, even into austere environments without data centers, and in locations without consistent network connectivity. These environments are called the rugged and disconnected edge. For customers running workloads at the rugged and disconnected edge, there is the [AWS Snow Family](https://aws.amazon.com/snow/). The AWS Snow Family is comprised of a number of highly secure, portable devices and capacity points, most with built-in computing capabilities, which help you run operations. These services help physically transport up to exabytes of data into and out of AWS. AWS Snow Family devices are owned and managed by AWS and integrate with AWS security, monitoring, storage management, and computing capabilities.

**Process data locally with AWS Snowball Edge**
 [AWS Snowball Edge Edge](https://docs.aws.amazon.com/snowball/latest/developer-guide/whatisedge.html) computing applications enable you to collect and process data that is continuously generated by sensors or machines in hospitals, factory floors, or other edge locations, before transferring the data back to AWS. For example, by using tamper-evident enclosures, encryption, and other methods designed to ensure full chain of custody for your data, Snowball Edge can provide a secure path for health customers to migrate their HIPAA-compliant data to the cloud, where they can centrally manage the configuration and operation of Snowball Edge devices deployed across worldwide customers and organizations.

 For more details about the services mentioned in this section, see the [Appendix](appendix-aws-services-for-edge-computing.md).
