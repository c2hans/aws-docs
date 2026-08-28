---
source_url: https://docs.aws.amazon.com/whitepapers/latest/monitoring-river-levels-using-lorawan/configuring-a-lorawan-gateway.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Configuring a LoRaWAN gateway
<a name="configuring-a-lorawan-gateway"></a>

 Laird Connectivity Sentrius RG1xx is an 8-channel LoRaWAN gateway with \+27 dBm maximum transmit power, with support for multiple wireless and wired interfaces such as LoRaWAN, 802.11a/b/g/n, Bluetooth v4.0 and Ethernet. The gateway has been qualified by AWS, and is [available from the AWS Partner Device Catalog](https://devices.amazonaws.com/detail/a3G0h000007dhzqEAA/Sentrius-RG1xx-LoRaWAN-Gateway). It runs the LoRaWAN Basics Station software, allowing it to use both the CUPS protocol for the management plane, and the LNS protocol for the data plane.

![Photograph of the Laird Connectivity Sentrius RG1xx](http://docs.aws.amazon.com/whitepapers/latest/monitoring-river-levels-using-lorawan/images/laird-sentrius-rg1xx.jpg)

**Note**
 This guide uses firmware version **93.8.5.25**. For gateway firmware versions and update procedures, refer to the [Laird Connectivity Sentrius RG1xx User Guide](https://www.digikey.com/htmldatasheets/production/2845666/0/0/1/rg1xx-series-user-guide.html).

 Initial setup and configuration of the Sentrius RG1xx is not in scope of this document. For the purposes of this guide, it is expected that you have followed the [Quick Start Guide](https://www.lairdconnect.com/documentation/quick-start-guide-sentrius-rg1xx-v30) from Laird Connectivity, and that the device is connected to the internet through either 802.11a/b/g/n wireless, or wired Ethernet networking.

![Screen capture showing viewing the RG1xx dashboard after setup](http://docs.aws.amazon.com/whitepapers/latest/monitoring-river-levels-using-lorawan/images/rg1xx-dashboard.png)

 With the gateway operational, you are now able to register it with the AWS IoT Core console, using the Extended Unique Identifier (EUI) assigned to the hardware.

**Note**
 Before proceeding, follow the steps outlined in the [AWS IoT Developer Guide](https://docs.aws.amazon.com/iot/latest/developerguide/connect-iot-lorawan.html) to configure an IAM role that will allow the Configuration and Update Server (CUPS) to manage gateway credentials.

 Once the role exists, you can successfully add the gateway using the console under **Wireless connectivity > Gateways**.

![Screen capture showing adding a gateway in the AWS IoT console](http://docs.aws.amazon.com/whitepapers/latest/monitoring-river-levels-using-lorawan/images/adding-a-gateway.png)

 During the next step in the gateway registration, you will generate and download certificates that allow the gateway to securely communicate with the CUPS server, and to authenticate itself.

1.  First, generate and download the `*.cert.pem` personal certificate and `*.private.key` personal private key files required to authenticate the gateway with the CUPS server running in AWS.
![Screenshot showing generating CUPS certificates](http://docs.aws.amazon.com/whitepapers/latest/monitoring-river-levels-using-lorawan/images/generating-cups-certificates.png)

1.  Download the certificate of the trusted certificate authority (CA) – `cups.trust` – and note the assigned CUPS server endpoint for the gateway.
![Screen showing noting the CUPS endpoint.](http://docs.aws.amazon.com/whitepapers/latest/monitoring-river-levels-using-lorawan/images/noting-the-cups-endpoint.png)

1.  Back on the RG1xx gateway, choose the `Semtech Basics Station` mode under **LoRa > Forwarder**, and enter the HTTPS endpoint of the CUPS server endpoint which you noted earlier.

    You do not require any LoRaWAN Network Server (LNS) configuration, as the LNS WebSocket Secure endpoint details and the certificates required to secure the data plane are downloaded automatically by the gateway using the CUPS protocol.
![Screen showing configuring the gateway with a CUPS server](http://docs.aws.amazon.com/whitepapers/latest/monitoring-river-levels-using-lorawan/images/configuring-gateway-with-cups-server.png)

1.  Upload the previously downloaded `*.cert.pem` personal certificate and `*.private.key` personal private key files, together with the `cups.trust` server trust certificate, to the gateway to secure the CUPS communication.
![Sccreen showing Configuring the gateway with CUPS certificates](http://docs.aws.amazon.com/whitepapers/latest/monitoring-river-levels-using-lorawan/images/configuring-gateway-cups-certificates.png)

    After the gateway successfully communicates with the CUPS server running in AWS, it can retrieve LNS configurations and establish a secure WebSocket connection. This can be confirmed on the gateway under **Dashboard**.
![Screen showing confirming gateway connectivity to AWS IoT](http://docs.aws.amazon.com/whitepapers/latest/monitoring-river-levels-using-lorawan/images/confirming-gateway-connectivity.png)

    In the AWS IoT Core for LoRaWAN console, the gateway now registers recent uplink activity from the gateway under **Wireless connectivity > Gateways**.
![Screen showing validating gateway connectivity in AWS IoT console](http://docs.aws.amazon.com/whitepapers/latest/monitoring-river-levels-using-lorawan/images/validating-gateway-connectivity.png)

    You are now ready to send LoRaWAN payloads to the gateway using the microprocessor.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Whitepapers. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query whitepapers` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
