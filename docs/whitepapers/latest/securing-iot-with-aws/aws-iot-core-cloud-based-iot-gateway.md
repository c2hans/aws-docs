---
source_url: https://docs.aws.amazon.com/whitepapers/latest/securing-iot-with-aws/aws-iot-core-cloud-based-iot-gateway.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# AWS IoT Core – Cloud-based IoT gateway
<a name="aws-iot-core-cloud-based-iot-gateway"></a>

 [AWS IoT Core](https://aws.amazon.com/iot/) is a managed cloud service that lets connected devices easily and securely interact with cloud applications and other devices. AWS IoT Core provides secure communication and data processing across different kinds of connected devices and locations so customers can build IoT applications. Examples of customer use cases include industrial solutions and connected home solutions, with the ability to support billions of devices and trillions of messages that can be processed and routed to AWS endpoints and other devices reliably and securely.

## Security capabilities
<a name="cap-3"></a>

 AWS IoT Core offers a number of solutions to customers that help enable and maintain security. AWS Cloud security mechanisms protect data as it moves between AWS IoT and other devices or AWS services. Devices can connect using a variety of identity options (X.509 certificates, users and groups, Amazon Cognito identities, or custom authentication tokens) over a secure connection. Although customers perform the client-side validations (such as chain of trust validation, hostname verification, secure storage, and distribution of their private keys), AWS IoT Core provides secure transportation channels using TLS. The AWS IoT rules engine also forwards device data to other devices and AWS services according to customer-defined rules. AWS access management systems are used to securely transfer data to its final destination. Another AWS IoT authorization feature worth noting is AWS IoT policy variables, which helps avoid the provisioning of over-privileged credentials to a device. These features, used in conjunction with general cybersecurity best practices, work to protect customer data.
