---
source_url: https://docs.aws.amazon.com/whitepapers/latest/implementing-lpwan-solutions-with-aws/building-a-private-lorawan-network.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Building a private LoRaWAN network
<a name="building-a-private-lorawan-network"></a>

 When deploying and operating a private LoRaWAN network, there are three major components to consider: LoRaWAN devices, LoRaWAN gateways, and LoRaWAN software components. Examples of components are LoRaWAN network server, join server, and application server as described in the *LoRaWAN network architecture* section of this document.

 The following figure provides an overview of various deployment patterns for private LoRaWAN networks:

![First diagram showing patterns for deployment of private LoRaWAN networks](https://docs.aws.amazon.com/whitepapers/latest/implementing-lpwan-solutions-with-aws/images/lorawan-network-patterns-1.png)![First diagram showing patterns for deployment of private LoRaWAN networks](https://docs.aws.amazon.com/whitepapers/latest/implementing-lpwan-solutions-with-aws/images/lorawan-network-patterns-2.png)

 The following sections will describe each of the individual options.

## Managed LoRaWAN server with AWS IoT Core for LoRaWAN
<a name="managed-lorawan-server-with-aws-iot-core-for-lorawan"></a>

![Diagram showing AWS IoT Core for LoRaWAN architecture](https://docs.aws.amazon.com/whitepapers/latest/implementing-lpwan-solutions-with-aws/images/iotcore-lorawan-arch.png)

 The first pattern is to use AWS IoT Core for LoRaWAN. AWS IoT Core for LoRaWAN is a fully managed feature that enables customers to connect wireless devices that use low-power, long-range wide-area network (LoRaWAN) protocol with AWS Cloud. Using AWS IoT Core, customers can now set up a private LoRaWAN network by connecting their own LoRaWAN devices and gateways to AWS Cloud, without developing or operating a LoRaWAN network server, join server, or application server.

 AWS IoT Core for LoRaWAN supports open-source gateway–network server protocol software called LoRa Basics Station. The IoT Core for LoRaWAN partner gateway qualification program enables customers to source pre-qualified LoRaWAN gateways. You can get an overview of pre-qualified LoRaWAN gateways by using [AWS Partner Device Catalog](https://devices.amazonaws.com/search?page=1&sv=iotclorawan).

 Customers can also buy any off-the-shelf sensor or actuator compliant with LoRaWAN specification 1.0.x or 1.1 and connect it to AWS IoT Core. This creates a plug and play experience that reduces the device on-boarding friction. As an introduction to AWS IoT Core for LoRaWAN, AWS recommends the following resources:
+  [AWS IoT Core for LoRaWAN](https://aws.amazon.com/iot-core/lorawan/) overview
+  [Introducing AWS IoT Core for LoRaWAN](https://aws.amazon.com/blogs/iot/introducing-aws-iot-core-for-lorawan/)
+  [AWS IoT Core for LoRaWAN workshop](https://iotwireless.workshop.aws/en/)
+  [Sample solutions for AWS IoT Core for LoRaWAN](https://github.com/aws-samples/aws-iot-core-lorawan) with examples for an implementation of binary decoding, device and gateway monitoring, downlink transmission, telemetry dashboarding, and device provisioning automation

### Device authentication
<a name="device-authentication"></a>

 IoT Core for LoRaWAN supports both approved methods of device activation as specified by LoRa Alliance: OTA and activation by personalization.

### Telemetry ingestion
<a name="telemetry-ingestion"></a>

 LoRaWAN devices transmit binary encoded data, increasing transmission efficiency and improving battery lifetime. However, as the data arrive in the cloud, many use cases require a structured format. Transforming the binary data into JSON, for example, enables filtering and enrichment using [AWS IoT SQL](https://docs.aws.amazon.com/iot/latest/developerguide/iot-sql-reference.html) and acting on the data using [AWS IoT rule actions](https://docs.aws.amazon.com/iot/latest/developerguide/iot-rule-actions.html).

 Refer to the code sample [AWS IoT Core for LoRaWAN - deployable reference architecture for binary decoding with examples](https://github.com/aws-samples/aws-iot-core-lorawan/tree/main/transform_binary_payload) to receive guidelines on implementing and deploying binary decoders for your LoRaWAN devices.

### Device commands
<a name="device-commands-1"></a>

 Because LoRaWAN protocol supports a bidirectional communication, you can send messages to your LoRaWAN devices. AWS IoT Core for LoRaWAN provides an API [SendDataToWirelessDevice](https://docs.aws.amazon.com/iot-wireless/2020-11-22/apireference/API_SendDataToWirelessDevice.html) and related SDK functions (for example, [AWS SDK for Python](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotwireless.html#IoTWireless.Client.send_data_to_wireless_device), [AWS SDK for Java](https://sdk.amazonaws.com/java/api/latest/software/amazon/awssdk/services/iotwireless/IotWirelessClient.html#sendDataToWirelessDevice-software.amazon.awssdk.services.iotwireless.model.SendDataToWirelessDeviceRequest-), and [AWS SDK for Javascript](https://docs.aws.amazon.com/AWSJavaScriptSDK/latest/AWS/IoTWireless.html#sendDataToWirelessDevice-property)).

 Refer to the code sample [Send a downlink payload to a LoRaWAN device](https://github.com/aws-samples/aws-iot-core-lorawan/tree/main/send_downlink_payload) to receive implementation guidelines for sending downlink payloads.

### Device provisioning
<a name="device-provisioning"></a>

 AWS IoT Core for LoRaWAN simplifies device provisioning by offering APIs to provision and manage LoRaWAN gateways and devices. Refer to the [developer guide](https://docs.aws.amazon.com/iot/latest/developerguide/connect-iot-lorawan-end-devices-add.html) and [API documentation](https://docs.aws.amazon.com/iot-wireless/2020-11-22/apireference/Welcome.html?icmpid=docs_iot_console) for details. You can also access [guidelines for automation of provisioning tasks.](https://github.com/aws-samples/aws-iot-core-lorawan/tree/main/automation)

### Gateway firmware updates
<a name="gateway-firmware-updates"></a>

 For LoRaWAN gateway firmware update guidance, please refer to the qualified gateway documentation. You can find an example of such guidelines for one specific gateway vendor using [Update gateway firmware using CUPS service with AWS IoT Core for LoRaWAN](https://docs.aws.amazon.com/iot/latest/developerguide/connect-iot-lorawan-update-firmware.html).

### OTA firmware updates
<a name="ota-firmware-updates"></a>

 With AWS IoT Core for LoRaWAN’s OTA firmware updates, you can deploy new firmware images or delta images to a single device or a group of devices, verify the authenticity and integrity of new firmware after it's deployed to devices, and monitor the progress of a deployment and debug issues in case of a failed deployment. You can find more information on FUOTA with AWS IoT Core for LoRaWAN in the [Firmware Updates Over-The-Air (FUOTA) for AWS IoT Core for LoRaWAN devices](https://docs.aws.amazon.com/iot/latest/developerguide/connect-iot-lorawan-mc-fuota-overview.html) section of the developer documentation.

### Multicast
<a name="multicast"></a>

 With AWS IoT Core for LoRaWAN, you can send a downlink payload to multiple devices by sending data to a single multicast address, which is then distributed to an entire group of recipient devices. You can find more information on multicast with AWS IoT Core for LoRaWAN in the [Create multicast groups to send a downlink payload to multiple devices](https://docs.aws.amazon.com/iot/latest/developerguide/connect-iot-lorawan-multicast-groups.html) section of the developer documentation.

### Customer-operated LoRaWAN network server in AWS Cloud
<a name="customer-operated-lorawan-network-server-in-aws-cloud"></a>

![Diagram showing LoRaWAN server provided by AWS Partner, operated by customer](https://docs.aws.amazon.com/whitepapers/latest/implementing-lpwan-solutions-with-aws/images/cust-lorawan-server.png)

 In this pattern, customers deploy and operate LoRaWAN server components in their own AWS account. Examples of LoRaWAN server components are LoRaWAN network server, join server, and application server. When using AWS Partner solutions, the deployment of necessary software components is simplified by using AWS CloudFormation templates provided by AWS Partners.

 You can find further information for implementing a customer-operated LoRaWAN server using these resources:
+  [LoRaWAN customer-operated solutions in AWS marketplace](https://aws.amazon.com/marketplace/search/results?searchTerms=lora+OR+lorawan&FULFILLMENT_OPTION_TYPE=CLOUDFORMATION_TEMPLATE&filters=FULFILLMENT_OPTION_TYPE)
+  [Connecting Your LoRaWAN Devices from The Things Stack to AWS IoT Core](https://aws.amazon.com/blogs/apn/connecting-your-lorawan-devices-from-the-things-stack-to-aws-iot-core/)

## LoRaWAN server as an AWS Partner software as a service (SaaS) solution
<a name="lorawan-server-as-an-aws-partner-software-as-a-service-saas-solution"></a>

![Diagram showing LoRaWAN server provided and operated by an AWS Partner](https://docs.aws.amazon.com/whitepapers/latest/implementing-lpwan-solutions-with-aws/images/partner-lorawan-server.png)

 The next pattern uses a LoRaWAN network server of an AWS Partner as an SaaS solution. In this pattern, the AWS Partner is responsible for operating LoRaWAN components such as LoRaWAN network server, join server, and application server.

 To enable a customer’s application to act upon the telemetry from LoRaWAN devices and send commands to LoRaWAN devices, the SaaS solution providers offer integration capabilities. An example of integration is a feature enabling customers to forward the uplink messages from their LoRaWAN devices to AWS IoT Core service in their AWS account.

 After the payload arrives on IoT Core MQTT topic or AWS IoT rule, it can be integrated with more than [20 AWS services supported by AWS IoT rules](https://docs.aws.amazon.com/iot/latest/developerguide/iot-rule-actions.html).

 Visit AWS Marketplace to find examples of AWS Partner [LoRaWAN SaaS solutions](https://aws.amazon.com/marketplace/search/results?searchTerms=lora+OR+lorawan&FULFILLMENT_OPTION_TYPE=SAAS&filters=FULFILLMENT_OPTION_TYPE).

## Customer-operated LoRaWAN server on the edge device
<a name="customer-operated-lorawan-server-on-the-edge-device"></a>

![Diagram showing LoRaWAN server operated by customer on the edge device](https://docs.aws.amazon.com/whitepapers/latest/implementing-lpwan-solutions-with-aws/images/edge-lorawan-server.png)

 In this pattern, customers source, deploy, and operate LoRaWAN gateways and LoRaWAN server components. The LoRaWAN server integrates with AWS IoT Core, enabling cloud applications to process data from and to send commands to LoRaWAN devices. Using this pattern results in higher development and operational efforts compared to the patterns previously described.

 One of the challenges when implementing this pattern is a need to remotely provision, update, and configure software components of LoRaWAN server. [AWS IoT Greengrass](https://aws.amazon.com/greengrass/) can be used to support faster implementation and simplified operation of these tasks. In particular, the following capabilities of AWS IoT Greengrass will be considered: deploying and updating LoRaWAN server components, managing sensitive configuration, and integrating with AWS IoT Core.

### Deploying and updating LoRaWAN server components
<a name="deploying-and-updating-lorawan-server-components"></a>

 Customers can use AWS IoT Greengrass components mechanism to deploy LoRaWAN server components. For example, by using AWS IoT Greengrass [Docker application manager component](https://docs.aws.amazon.com/greengrass/v2/developerguide/docker-application-manager-component.html) it is possible to download Docker images from public image registries or private repository in Amazon Elastic Container Registry.

### Managing sensitive information
<a name="managing-sensitive-information"></a>

 A LoRaWAN server configuration contains sensitive information. Customers can use AWS IoT Greengrass [secret manager component](https://docs.aws.amazon.com/greengrass/v2/developerguide/secret-manager-component.html) to securely use credentials such as passwords on AWS IoT Greengrass core devices.

### Integrating with AWS IoT Core
<a name="integrating-with-aws-iot-core"></a>

 Integration between LoRaWAN server and AWS IoT allows users to forward LoRaWAN device payloads to cloud applications, and send commands from cloud application to LoRaWAN devices. To implement this integration, customers can use AWS IoT Greengrass [AWS IoT Core Messaging IPC service](https://docs.aws.amazon.com/greengrass/v2/developerguide/ipc-iot-core-mqtt.html).

 For more information for implementing a customer-operated LoRaWAN server on the edge device, refer to [AWS IoT Greengrass V2 Community Component - The Things Stack LoRaWAN](https://github.com/awslabs/aws-greengrass-labs-component-for-the-things-stack-lorawan).
