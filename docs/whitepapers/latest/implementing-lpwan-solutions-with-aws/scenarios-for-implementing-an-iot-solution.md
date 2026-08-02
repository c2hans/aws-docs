---
source_url: https://docs.aws.amazon.com/whitepapers/latest/implementing-lpwan-solutions-with-aws/scenarios-for-implementing-an-iot-solution.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Scenarios for implementing an IoT solution
<a name="scenarios-for-implementing-an-iot-solution"></a>

 A wireless connectivity technology is not a purpose by itself, but a means for achieving a business goal by implementing an IoT solution. When architecting and implementing an IoT solution, AWS suggests that you consider the following scenarios: device provisioning, device authentication, telemetry ingestion, device commands, firmware updates, and connectivity management. In this section, these scenarios will be defined, whereas they will be used in the following sections to structure the implementation guidance for individual LPWAN technologies.
+  **Device provisioning** – This scenario refers to a mechanism that provides unique device identities and configuration data to a device. Device provisioning is also involved with ongoing maintenance, and eventual decommissioning, of devices over time.
+  **Device authentication** – This scenario refers to mechanisms used to reliably verify the identity of an IoT device, because IoT devices communicate with your cloud application.
+  **Telemetry ingestion** – An IoT device collects telemetry (for example, read-only data) and transmits this data to an IoT application for further processing. Examples of such data include sensor measurements or device health metrics.
+  **Device commands** – An IoT application in the AWS Cloud must be capable of sending commands to an IoT device remotely. Examples of such commands can be a trigger for an actor connected to the device, a configuration update for the device or a trigger to initiate a firmware update.
+  **Firmware updates** – A capability to remotely update firmware on IoT devices is critical in ensuring the security and adding new capabilities to your IoT solution.
+  **Connectivity management** – This scenario refers to the capability of your device software to configure, establish, and manages a wireless connection.

## Integration with AWS Partners
<a name="integration-with-aws-partners"></a>

 If a connection between the IoT device and [AWS IoT Core](https://aws.amazon.com/iot-core/) endpoint is not secured, for example, through TLS, Datagram Transport Layer Security (DTLS), or virtual private network (VPN), an additional security consideration is necessary. For example, such a situation could arise if a software component in customer’s AWS account acts as an intermediary, receives data from the IoT device, and forwards data to AWS IoT Core. To ingest messages between software components in customer’s AWS account to AWS IoT Core, AWS recommends always using [AWS IoT Data Plane application programming interfaces (APIs)](https://docs.aws.amazon.com/iot/latest/apireference/API_Operations_AWS_IoT_Data_Plane.html) authorized by IAM mechanisms.
