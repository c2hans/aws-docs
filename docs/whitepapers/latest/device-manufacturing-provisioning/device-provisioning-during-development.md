---
source_url: https://docs.aws.amazon.com/whitepapers/latest/device-manufacturing-provisioning/device-provisioning-during-development.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Device provisioning during development
<a name="device-provisioning-during-development"></a>

 In the early phases of an IoT project, a small number of devices are provisioned to AWS IoT for development and testing purposes. During this phase, developers often choose convenience over security and scalability.

 For convenience, AWS IoT gives developers the ability to create a device certificate and keys in the cloud from [AWS Management Console](https://aws.amazon.com/console/), [AWS IoT Control Plane APIs](https://docs.aws.amazon.com/iot/index.html), or the AWS Command Line Interface (AWS CLI). The certificate is issued by an ephemeral AWS intermediate CA, and the private key is generated on the AWS Cloud. The certificate, private key, and public key are then downloaded onto the developer’s local machine.

 The developer is responsible for manually provisioning the certificate and private key provided by AWS IoT Core to the device, where they are either added to the device’s file system or stored in the device’s firmware image.

![A diagram that shows the process to provision devices during development using AWS IoT Core.](http://docs.aws.amazon.com/whitepapers/latest/device-manufacturing-provisioning/images/provision-devices.png)

This process should never be used in production because the private key is transmitted through an insecure environment such as the developer’s laptop. If the private key is stored on the developer’s local machine, even temporarily, it could be compromised by social engineering, user error, or a weak password. In production, the device private key should be generated on the device from a strong source of entropy and never exported.

Security risks are mitigated because the devices are not deployed in the field. The devices are tightly controlled by a developer or in a lab environment. A compromised device can be re-programmed and the certificate can be revoked.

The process of creating all resources in the AWS Cloud and copying the necessary keys to the device is manual and time consuming. Unique firmware and files need to be programmed into each device by the developer. For testing and development, most operations are performed in the lab environment, but the process is not scalable when entering the pilot or production phase of an IoT project. To scale an IoT project, there is typically a much more complex supply chain.
