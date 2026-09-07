---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/set-up-and-troubleshoot-aws-iot-greengrass-with-client-devices.html
---

# Set up and troubleshoot AWS IoT Greengrass with client devices
<a name="set-up-and-troubleshoot-aws-iot-greengrass-with-client-devices"></a>

*Marouane Sefiani and Akalanka De Silva, Amazon Web Services*

## Summary
<a name="set-up-and-troubleshoot-aws-iot-greengrass-with-client-devices-summary"></a>

AWS IoT Greengrass is an open-source edge runtime and cloud service for building, deploying, and managing Internet of Things (IoT) software on edge devices. Use cases for AWS IoT Greengrass include:
+ Smart homes where an AWS IoT Greengrass gateway is used as a hub for home automation
+ Smart factories where AWS IoT Greengrass can facilitate ingestion and local processing of data from the shop floor

AWS IoT Greengrass can act as a secure, authenticated, MQTT connection endpoint for other edge devices (also known as *client devices*), which otherwise would typically connect directly to AWS IoT Core. This capability is useful when client devices do not have direct network access to the AWS IoT Core endpoint.

You can set up AWS IoT Greengrass for use with client devices for the following use cases:
+ For client devices to send data to AWS IoT Greengrass
+ For AWS IoT Greengrass to forward data to AWS IoT Core
+ To take advantage of advanced AWS IoT Core rules engine features

These capabilities require installing and configuring the following components on the AWS IoT Greengrass device:
+ MQTT broker
+ MQTT bridge
+ Client device authentication
+ IP detector

In addition, published messages from client devices must be in JSON format or [Protocol Buffers (protobuf)](https://protobuf.dev/) format.

This pattern describes how to install and configure these required components, and provides troubleshooting tips and best practices.

## Prerequisites and limitations
<a name="set-up-and-troubleshoot-aws-iot-greengrass-with-client-devices-prereqs"></a>

**Prerequisites**
+ An active AWS account
+ [AWS Command Line Interface (AWS CLI) version 2](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-getting-started.html)
+ Two client devices running Python 3.7 or later
+ One core device running Java Runtime Environment (JRE) version 8 or later, and [Amazon Corretto 11](https://aws.amazon.com/corretto/) or [OpenJDK 11](https://openjdk.java.net/)

**Limitations**
+ You must choose an AWS Region where AWS IoT Core is available. For the current list of Regions for AWS IoT Core, see [AWS Services by Region](https://aws.amazon.com/about-aws/global-infrastructure/regional-product-services/).
+ The core device must have at least 172 MB RAM and 512 MB of disk space.

## Architecture
<a name="set-up-and-troubleshoot-aws-iot-greengrass-with-client-devices-architecture"></a>

The following diagram shows the solution architecture for this pattern.

![Solution architecture for setting up AWS IoT Greengrass with client devices](https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/images/pattern-img/a340e6ea-dcfa-42a4-a370-c16ee08a6842/images/0656c5ae-d979-4cf7-be92-a46fa81cab0d.png)

The architecture includes:
+ Two client devices. Each device contains a private key, a device certificate, and a root certificate authority (CA) certificate. The AWS IoT Device SDK, which contains an MQTT client, is also installed on each client device.
+ A core device that has AWS IoT Greengrass deployed with the following components:
  + MQTT broker
  + MQTT bridge
  + Client device authentication
  + IP detector

This architecture supports the following scenarios:
+ Client devices can use their MQTT client to communicate with one another through the core device’s MQTT broker.
+ Client devices can also communicate with AWS IoT Core in the cloud through the core device’s MQTT broker and the MQTT bridge.
+ AWS IoT Core in the cloud can send messages to client devices through the MQTT test client and the core device’s MQTT bridge and MQTT broker.

For more information about the communications between client devices and the core device, see the [Additional information](#set-up-and-troubleshoot-aws-iot-greengrass-with-client-devices-additional) section.

## Tools
<a name="set-up-and-troubleshoot-aws-iot-greengrass-with-client-devices-tools"></a>

**AWS services**
+ [AWS IoT Greengrass](https://docs.aws.amazon.com/greengrass/v2/developerguide/what-is-iot-greengrass.html) is an open source Internet of Things (IoT) edge runtime and cloud service that helps you build, deploy, and manage IoT applications on your devices.
+ [AWS IoT Core](https://docs.aws.amazon.com/iot/latest/developerguide/what-is-aws-iot.html) provides secure, bidirectional communication for internet-connected devices to connect to the AWS Cloud.
+ [AWS IoT Device SDK](https://boto3.amazonaws.com/v1/documentation/api/latest/guide/quickstart.html) is a software development kit that includes open-source libraries, developer guides with samples, and porting guides so that you can build innovative IoT products or solutions on your choice of hardware platforms.
+ [AWS Identity and Access Management (IAM)](https://docs.aws.amazon.com/IAM/latest/UserGuide/introduction.html) helps you securely manage access to your AWS resources by controlling who is authenticated and authorized to use them.

## Best practices
<a name="set-up-and-troubleshoot-aws-iot-greengrass-with-client-devices-best-practices"></a>
+ The payload of the messages from client devices should be in either JSON or Protobuf format in order to take advantage of the advanced features of the AWS IoT Core rules engine, such as transformation and conditional actions.
+ Configure the MQTT bridge to allow bidirectional communication.
+ Configure and deploy the IP detector component in AWS IoT Greengrass to ensure that the core device’s IP addresses are included in the subject alternative name (SAN) field of the MQTT broker certificate.

## Epics
<a name="set-up-and-troubleshoot-aws-iot-greengrass-with-client-devices-epics"></a>

### Set up the core device
<a name="set-up-the-core-device"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Set up AWS IoT Greengrass on your core device. | Install the AWS IoT Greengrass Core software by following the instructions in the [developer guide](https://docs.aws.amazon.com/greengrass/v2/developerguide/install-greengrass-core-v2.html). | AWS IoT Greengrass |
| Check the status of your installation. | Use the following command to check the status of the AWS IoT Greengrass service on your core device:<pre>sudo systemctl status greengrass.service</pre><br />The expected output of the command is:<pre>Launched Nucleus successfully</pre> | General AWS |
| Set up an IAM policy and attach it to the Greengrass service role. | 1. Create an IAM policy to allow communications to and from the MQTT bridge. Here’s an example policy:<pre>{<br />    "Version": "2012-10-17",		 	 	 <br />    "Statement": [<br /><br />        {<br />            "Effect": "Allow",<br />            "Action": [<br />                "iot:*"<br />            ],<br />            "Resource": "*"<br />        },<br />        {<br />            "Sid": "GreengrassActions",<br />            "Effect": "Allow",<br />            "Action": [<br />                "greengrass:*"<br />            ],<br />            "Resource": "*"<br />        }<br />    ]<br />}</pre><br />2. Attach the policy to the Greengrass service role. To get the service role, use the command:<pre>aws greengrassv2 get-service-role-for-account --region <region> </pre><br />where `<region>` refers to your AWS Region. | General AWS |
| Configure and deploy required components in the AWS IoT Greengrass core device. | Configure and deploy the following components:+ `greengrass.clientdevices.mqtt.Moquette` (see [configuration details](https://docs.aws.amazon.com/greengrass/v2/developerguide/mqtt-broker-moquette-component.html))<br />+ `greengrass.clientdevices.mqtt.Bridge` (see [configuration details](https://docs.aws.amazon.com/greengrass/v2/developerguide/mqtt-bridge-component.html) and the next task)<br />+ `greengrass.clientdevices.Auth` (see [configuration details](https://docs.aws.amazon.com/greengrass/v2/developerguide/client-device-auth-component.html) and the task after the next one)<br />+ `aws.greengrass.clientdevices.IPDetector` (see [configuration details](https://docs.aws.amazon.com/greengrass/v2/developerguide/ip-detector-component.html)) | AWS IoT Greengrass |
| Confirm that the MQTT bridge allows bidirectional communication. | To relay MQTT messages between client devices and AWS IoT Core, configure and deploy the MQTT bridge component and specify the topics to relay. Here’s an example:<pre>{<br />  "mqttTopicMapping": {<br />    "ClientDevicesToCloud": {<br />      "topic": "dt/#",<br />      "source": "LocalMqtt",<br />      "target": "IotCore"<br />    },<br />    "CloudToClientDevices": {<br />      "topic": "cmd/#",<br />      "source": "IotCore",<br />      "target": "LocalMqtt"<br />    }<br />  }<br />}</pre> | AWS IoT Greengrass |
| Confirm that the auth component allows client devices to connect and publish or subscribe to topics.  | The following `aws.greengrass.clientdevices.Auth` configuration allows all client devices to connect, publish messages, and subscribe to all topics.<pre>{<br />  "deviceGroups": {<br />    "formatVersion": "2021-03-05",<br />    "definitions": {<br />      "MyPermissiveDeviceGroup": {<br />        "selectionRule": "thingName: *",<br />        "policyName": "MyPermissivePolicy"<br />      }<br />    },<br />    "policies": {<br />      "MyPermissivePolicy": {<br />        "AllowAll": {<br />          "statementDescription": "Allow client devices to perform all actions.",<br />          "operations": [<br />            "*"<br />          ],<br />          "resources": [<br />            "*"<br />          ]<br />        }<br />      }<br />    }<br />  }<br />}</pre> | AWS IoT Greengrass |

### Set up client devices
<a name="set-up-client-devices"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Install the AWS IoT Device SDK. | Install the AWS IoT Device SDK on client devices. For a full list of supported languages and the associated SDKs, see the [AWS IoT Core documentation](https://docs.aws.amazon.com/iot/latest/developerguide/iot-sdks.html).<br />For example, the AWS IoT Device SDK for Python SDK is [located on GitHub](https://github.com/aws/aws-iot-device-sdk-python-v2). To install this SDK:1. Confirm that Python 3.7 or later is installed, as instructed on the [Prerequisites page](https://github.com/aws/aws-iot-device-sdk-python-v2/blob/main/documents/PREREQUISITES.md) of the GitHub repository.<br />2. Use the **pip** command to install the SDK.<br />For MacOS and Linux::<pre>python3 -m pip install awsiotsdk</pre><br />For Windows:<pre>python -m pip install awsiotsdk</pre><br />Alternatively, you can install the SDK from the source repository:<pre># Create a workspace directory to hold all the SDK files<br />mkdir sdk-workspace<br />cd sdk-workspace<br /># Clone the repository<br />git clone https://github.com/aws/aws-iot-device-sdk-python-v2.git<br /># Install using Pip (use 'python' instead of 'python3' on Windows)<br />python3 -m pip install ./aws-iot-device-sdk-python-v2</pre> | General AWS IoT |
| Create a thing. | 1. In the [AWS IoT console](https://console.aws.amazon.com/iot), if a **Get started** button appears, choose it. Otherwise, in the navigation pane, choose **Security**, **Policies**.<br />2. If the **You don't have any policies yet** dialog box appears, choose **Create a policy**. Otherwise, choose **Create**.<br />3. Enter a name for the AWS IoT policy (for example, `ClientDevicePolicy`).<br />4. In the **Add statements** section, replace the existing policy with the following JSON code. Replace `<region>` and `<account>` with your AWS Region and AWS account number.<pre>{<br />   "Version": "2012-10-17",		 	 	 <br />   "Statement": [{<br />         "Effect": "Allow",<br />         "Action": "iot:Connect",<br />         "Resource": "arn:aws:iot:region:account:client/*"<br />      },<br />      {<br />         "Effect": "Allow",<br />         "Action": "iot:Publish",<br />         "Resource": "*"<br />      },<br />      {<br />         "Effect": "Allow",<br />         "Action": "iot:Receive",<br />         "Resource": "*"<br />      },<br />      {<br />         "Effect": "Allow",<br />         "Action": "iot:Subscribe",<br />         "Resource": "*"<br />      },<br />      {<br />         "Effect": "Allow",<br />         "Action": [<br />            "iot:GetThingShadow",<br />            "iot:UpdateThingShadow",<br />            "iot:DeleteThingShadow"<br />         ],<br />         "Resource": "arn:aws:iot:region:account:thing/*"<br /><br />      }<br />   ]<br />}</pre><br />5. Choose **Create**.<br />6. On the [AWS IoT console, ](https://console.aws.amazon.com/iot/home)in the navigation pane, choose **Manage**, **Things**.<br />7. If the **You don't have any things yet** dialog box is displayed, choose **Register a thing**. Otherwise, choose **Create**.<br />8. On the **Creating AWS IoT things** page, choose **Create a single thing**.<br />9. On the **Add your device to the device registry** page, enter a name for your IoT thing (for example, `ClientDevice1`), and then choose **Next**.You can't change the name of a thing after you create it. To change the name, you must create a new thing, give it the new name, and then delete the old thing.<br />10. On the **Add a certificate for your thing** page, choose **Create certificate**.<br />11. Choose the **Download **links to download the certificate, private key, and root CA certificate.This is your only opportunity to download your certificate and private key.<br />12. To activate the certificate, choose **Activate**. The certificate must be active for a device to connect to AWS IoT.<br />13. Choose **Attach a policy**.<br />14. For **Add a policy for your thing**, choose **ClientDevicePolicy**, **Register Thing**. | AWS IoT Core |
| Download the CA certificate from the Greengrass core device. | If you expect the Greengrass core device to work in offline environments, you have to make the Greengrass core CA certificate available to the client device so it can verify the MQTT broker’s certificate (which is issued by the Greengrass core CA). Therefore, it is important to obtain a copy of this certificate. Use one of the following approaches to download the CA certificate:+ If you have network access to the AWS IoT Greengrass device from your PC, enter `https://<device IP>:8883` in your web browser and view the MQTT broker certificate and the CA certificate. You can also save the CA certificate to the client device.<br />+ Alternatively, you can use the OpenSSL command line:<pre>openssl s_client -showcerts -connect <device IP>:8883</pre> | General AWS |
| Copy credentials in the client devices. | Copy the Greengrass core CA certificate, the device certificate, and the private key in the client devices. | General AWS |
| Associate client devices with the core device. | Associate client devices with a core device so that they can discover the core device. The client devices can then use the [Greengrass discovery API](https://docs.aws.amazon.com/greengrass/v2/developerguide/greengrass-discover-api.html) to retrieve connectivity information and certificates for their associated core devices. For more information, see [Associate client devices](https://docs.aws.amazon.com/greengrass/v2/developerguide/associate-client-devices.html) in the AWS IoT Greengrass documentation.1. On the [AWS IoT Greengrass console](https://console.aws.amazon.com/greengrass), choose **Core devices**.<br />2. Choose the core device to manage.<br />3. On the core device's details page, choose the **Client devices** tab.<br />4. In the **Associated client devices** section, choose **Associate client devices**.<br />5. In the **Associate client devices with core device** modal, do the following for each client device to associate:Enter the name of the AWS IoT thing to associate as a client device.Choose **Add**.<br />6. Choose **Associate**.<br />The client devices that you associated can now use the Greengrass discovery API to discover this core device. | AWS IoT Greengrass |

### Send and receive data
<a name="send-and-receive-data"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Send data from one client device to another client device. | Use the MQTT client in your device to publish a message on the `dt/client1/sensor` topic. | General AWS |
| Send data from the client device to AWS IoT Core. | Use the MQTT client in your device to publish a message on the `dt/client1/sensor` topic.<br />In the MQTT test client, subscribe to the topic that the device is sending messages on, or subscribe to **\#** for all topics (see [details](https://docs.aws.amazon.com/iot/latest/developerguide/view-mqtt-messages.html)). | General AWS |
| Send messages from AWS IoT Core to client devices. | On the MQTT test client page, in the **Publish to a topic** tab, in the **Topic name** field, enter the topic name of your message. In this example, use `cmd/client1` for the topic. | General AWS |

## Troubleshooting
<a name="set-up-and-troubleshoot-aws-iot-greengrass-with-client-devices-troubleshooting"></a>

| Issue | Solution |
| --- | --- |
| **Unable to verify server certificate error** | This error occurs when the MQTT client cannot verify the certificate that’s presented by the MQTT broker during the TLS handshake. The most common reason is that the MQTT client doesn’t have the CA certificate. Follow these steps to make sure that the CA certificate is provided to the MQTT client.1. If you have network access to the AWS IoT Greengrass device from your PC, enter `https://<device IP>:8883` in a browser window to view the MQTT broker certificate and the CA certificate. You can also save the CA certificate to the client device.<br />Alternatively use the OpenSSL command line:<pre>openssl s_client -showcerts -connect <device IP>:8883</pre><br />2. Save the contents of the Moquette CA and Greengrass Core CA certificates into files, and then view the decoded contents by using the command:<pre>openssl x509 -in <Name of CA>.pem -text</pre><br />The Moquette CA certificate should show the SAN field as in this example:<pre> X509v3 Subject Alternative Name:  IP Address:XXX.XXX.XXX.XXX, IP Address:127.0.0.1, DNS:localhost</pre> |
| **Unable to verify server name error** | This errors occurs when the MQTT client can’t verify that it’s connecting to the correct server. The most common reason is that the IP address of the Greengrass device isn’t listed in the SAN field of the certificate.<br />Follow the instructions in the previous solution to obtain the MQTT broker certificate and verify that the SAN field contains the IP address of the AWS IoT Greengrass device, as explained in the [Additional information](#set-up-and-troubleshoot-aws-iot-greengrass-with-client-devices-additional) section. If not, confirm that the IP detector component is installed correctly and restart the core device. |
| **Unable to verify server name only when connecting from an embedded client device** | Mbed TLS, which is a popular TLS library used in embedded devices, currently supports DNS name verification only in the SAN field of the certificate, as shown in the Mbed TLS library code. Because the core device doesn’t have its own domain name and depends on the IP address, TLS clients that use Mbed TLS will fail the server name verification during the TLS handshake, causing a connection failure. We recommend that you add the SAN IP address verification to your Mbed TLS library at the [x509\_crt\_check\_san function](https://github.com/Mbed-TLS/mbedtls/blob/6a327a5fdc2786cb50b4dbe5e3a75884a1f8435a/library/x509_crt.c#L2548). |

## Related resources
<a name="set-up-and-troubleshoot-aws-iot-greengrass-with-client-devices-resources"></a>
+ [AWS IoT Greengrass documentation](https://docs.aws.amazon.com/greengrass/v2/developerguide/what-is-iot-greengrass.html)
+ [AWS IoT Core documentation](https://docs.aws.amazon.com/iot/latest/developerguide/what-is-aws-iot.html)
+ [MQTT broker component](https://docs.aws.amazon.com/greengrass/v2/developerguide/mqtt-broker-moquette-component.html)
+ [MQTT bridge component](https://docs.aws.amazon.com/greengrass/v2/developerguide/mqtt-bridge-component.html)
+ [Client device auth component](https://docs.aws.amazon.com/greengrass/v2/developerguide/client-device-auth-component.html)
+ [IP detector component](https://docs.aws.amazon.com/greengrass/v2/developerguide/ip-detector-component.html)
+ [AWS IoT Device SDK](https://docs.aws.amazon.com/iot/latest/developerguide/iot-sdks.html)s
+ [Implementing Local Client Devices with AWS IoT Greengrass](https://aws.amazon.com/blogs/iot/implementing-local-client-devices-with-aws-iot-greengrass/) (AWS blog post)
+ [RFC 5280 – Internet X.509 Public Key Infrastructure Certificate and Certificate Revocation List (CRL) Profile](https://www.rfc-editor.org/rfc/rfc5280)

## Additional information
<a name="set-up-and-troubleshoot-aws-iot-greengrass-with-client-devices-additional"></a>

This section provides additional information about the communications between the client devices and the core device.

The MQTT broker listens on port 8883 in the core device for a TLS client connection attempt. The following illustration shows an example MQTT broker’s server certificate.

![Example of MQTT broker server certificate](https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/images/pattern-img/a340e6ea-dcfa-42a4-a370-c16ee08a6842/images/b2c324a1-60cd-4194-80e7-e5184662146a.png)

The example certificate displays the following details:
+ The certificate is issued by the AWS IoT Greengrass Core CA, which is local and specific to the core device; that is, it acts as a local CA.
+ This certificate is automatically rotated every week by the client auth component as shown in the following illustration. You can set this interval in the client auth component configuration.

![Rotating the MQTT broker's server certificate](https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/images/pattern-img/a340e6ea-dcfa-42a4-a370-c16ee08a6842/images/65bcdc5c-a71c-4f52-adcd-21910fabfc2a.png)

+ The subject alternative name (SAN) plays a critical role in the server name verification on the TLS client end. It helps the TLS client ensure that it connects to the correct server and helps avoid man-in-the-middle attacks during TLS session setup. In the example certificate, the SAN field indicates that this server is listening on localhost (the local Unix domain socket), and the network interface has the IP address 192.168.1.12.

The TLS client uses the SAN field in the certificate to verify that it’s connecting to a legitimate server during server verification. In contrast, during a typical TLS handshake between an HTTP server and a browser, the domain name in the common name (CN) field or SAN field is used to cross-check the domain that the browser is actually connecting to during the server verification process. If the core device doesn’t have a domain name, the IP address included in the SAN field serves the same purpose. For more information, see the [Subject Alternative Name section](https://www.rfc-editor.org/rfc/rfc5280#section-4.2.1.6) of *RFC 5280 – Internet X.509 Public Key Infrastructure Certificate and Certificate Revocation List (CRL) Profile*.

Th IP detector component in AWS IoT Greengrass ensures that the correct IP addresses are included in the SAN field of the certificate.

The certificate in the example is signed by the AWS IoT Greengrass device acting as a local CA. The TLS client (MQTT client) isn’t aware of this CA, so we must provide a CA certificate that looks like the following.

![Example CA certificate](https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/images/pattern-img/a340e6ea-dcfa-42a4-a370-c16ee08a6842/images/b08b3bcb-9e12-4f5a-9204-cf65ea32902f.png)
