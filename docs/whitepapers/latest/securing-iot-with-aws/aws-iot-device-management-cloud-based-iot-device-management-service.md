---
source_url: https://docs.aws.amazon.com/whitepapers/latest/securing-iot-with-aws/aws-iot-device-management-cloud-based-iot-device-management-service.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# AWS IoT Device Management – Cloud-based IoT device management service
<a name="aws-iot-device-management-cloud-based-iot-device-management-service"></a>

 [AWS IoT Device Management](https://aws.amazon.com/iot-device-management/) helps customers onboard, organize, monitor, and remotely manage IoT devices at scale. AWS IoT Device Management integrates with AWS IoT Core to easily connect devices to the cloud and other devices so customers can remotely manage their fleets of devices. AWS IoT Device Management helps customers onboard new devices by using AWS IoT within the AWS Management Console or an API to upload templates that they populate with information like device manufacturer and serial number, X.509 identity certificates, or security policies. Following this, customers can then configure the entire fleet of devices with this information with a few clicks in AWS IoT within the AWS Management Console.

## Security capabilities
<a name="cap-4"></a>

 With AWS IoT Device Management, customers can group their device fleet into a hierarchical structure based on function, security requirements, or similar categories. They can group a single device in a room, multiple devices on the same floor, or all the devices that operate within a building. These groups can then be used to manage access policies, view operational metrics, or perform actions across the entire group. Additionally, a feature known as dynamic thing groups can automatically add devices that meet the customer-defined criteria and remove devices that no longer match the requirements. This securely streamlines the process while maintaining operational integrity. Dynamic thing groups also makes it easy to find device records based on any combination of device attributes and allows customers to perform bulk updates.

 With AWS IoT Device Management, customers can also push software and firmware to devices in the field to patch security vulnerabilities and improve device functionality; implement bulk updates; control deployment velocity; set failure thresholds; and define continuous jobs to update device software automatically so that they are always running the latest version of software. Customers can remotely send actions (such as device reboots or factory resets) to fix software issues in the device or restore the device to its original settings. Customers can also digitally sign files that are sent to their devices, helping to ensure the devices are not compromised.

 The ability to push software updates isn’t limited to cloud services. OTA update jobs in FreeRTOS allow customers to use AWS IoT Device Management to schedule software updates. Similarly, customers can also create an AWS IoT Greengrass core update job for one or more AWS IoT Greengrass core devices using AWS IoT Device Management to deploy security updates, bug fixes, and new AWS IoT Greengrass features to connected devices.

 With the secure tunneling feature, customers can establish a secure remote communications session to a device. This provides secure connectivity to individual devices, which you can then use to diagnose issues and act to solve in just a few clicks. You can also make multiple, concurrent client connections over a single secure tunnel, enabling you to perform more advanced device troubleshooting, such as issuing remote shell commands to a device while simultaneously debugging a web application on the same device.
