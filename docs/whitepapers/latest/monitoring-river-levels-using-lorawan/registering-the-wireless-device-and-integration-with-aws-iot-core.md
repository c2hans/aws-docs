---
source_url: https://docs.aws.amazon.com/whitepapers/latest/monitoring-river-levels-using-lorawan/registering-the-wireless-device-and-integration-with-aws-iot-core.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Registering the wireless device and integration with AWS IoT Core
<a name="registering-the-wireless-device-and-integration-with-aws-iot-core"></a>

 AWS IoT Core for LoRaWAN service profiles describes the parameters the device needs to communicate with the LoRaWAN application server.

1.  For the purposes of this demonstration, create a service profile with default configuration parameters under **Wireless connectivity > Profiles**.
![Screen showing adding a service profile](https://docs.aws.amazon.com/whitepapers/latest/monitoring-river-levels-using-lorawan/images/adding-a-service-profile.png)

    Device profiles contain the parameters the device needs to communicate with the LoRaWAN network server.

1.  Select the LoRa frequency band in your Region, the desired media access control (MAC) version, the Regional parameters version, and the maximum equivalent isotropic radiated power (EIRP) value.
![Screen showing adding a device profile](https://docs.aws.amazon.com/whitepapers/latest/monitoring-river-levels-using-lorawan/images/adding-a-device-profile.png)

    AWS IoT Core for LoRaWAN destinations found in **Wireless connectivity > Destinations** describe the AWS IoT rule that processes a device's data for use by other AWS services.

1.  Provision a destination that identifies the AWS IoT rule that will be created later, and also associate this destination with an IAM role.

1.  Attach this IAM role to an IAM policy that has the ability to send messages to the rule.
**Note**
Before proceeding with the creation of the destination, follow the steps described in the AWS IoT Core Developer Guide to [create an IAM role](https://docs.aws.amazon.com/iot/latest/developerguide/connect-iot-lorawan-create-destinations.html#connect-iot-lorawan-create-destinations-roles) that gives AWS IoT Core for LoRaWAN the permissions necessary to send data to the rule.
![Screen showing adding a destination](https://docs.aws.amazon.com/whitepapers/latest/monitoring-river-levels-using-lorawan/images/adding-a-destination.png)
**Note**
This architecture can be modified to take advantage of [basic ingest](https://docs.aws.amazon.com/iot/latest/developerguide/iot-basic-ingest.html) to optimize messaging costs. By creating a destination with the option `Publish to AWS IoT Core message broker`, with a destination MQTT topic of `$aws/rules/{{rule-name}}` (where `{{rule-name}}` is the name of an AWS IoT Core rule with accompanying actions), received payloads can be dispatched directly to an AWS IoT Core rule, bypassing the MQTT broker. This may be desirable, for example, if the inline Lambda decoder function or MQTT publishing steps can be removed altogether.

1.  Register the microcontroller you are using in the console as a wireless device under **Wireless connectivity > Devices**. You will use the OTAA v1.1 wireless device specification.

1.  Enter further unique identifiers and security keys related to the wireless device, as specified in the dialog. These parameters must match the actual configurations set on the microcontroller, as this is the method through which the arriving payload is mapped to your registered wireless device.
**Note**
Although AWS IoT Core for LoRaWAN supports both Activation by Personalization (ABP) and Over the Air Activation (OTAA), it is recommended that you use OTAA for better security posture.
![Screen showing adding a wireless device](https://docs.aws.amazon.com/whitepapers/latest/monitoring-river-levels-using-lorawan/images/adding-a-wireless-device.png)

1.  When registering the wireless device, link it to the previously created wireless device and service profiles.
![Screen showing associating a wireless device with profiles](https://docs.aws.amazon.com/whitepapers/latest/monitoring-river-levels-using-lorawan/images/associating-wireless-device-with-profiles.png)

1.  Assign the device to the destination you created earlier.
![Screen showing choosing a destination for the wireless device](https://docs.aws.amazon.com/whitepapers/latest/monitoring-river-levels-using-lorawan/images/choosing-wireless-device-destination.png)

    If the microcontroller is already broadcasting OTAA join requests over LoRaWAN, the newly registered device is now able to join the network, and its status reflects the last uplink data received.
![Screen showing confirming uplink from wireless device](https://docs.aws.amazon.com/whitepapers/latest/monitoring-river-levels-using-lorawan/images/confirming-uplink-from-wireless-device.png)

 You are now ready to complete the final step required for your LoRaWAN payloads to be forwarded to other AWS services.
