---
source_url: https://docs.aws.amazon.com/whitepapers/latest/device-manufacturing-provisioning/provisioning-identity-in-aws-iot-core-for-device-connections.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Provisioning identity in AWS IoT Core for device connections
<a name="provisioning-identity-in-aws-iot-core-for-device-connections"></a>

 AWS IoT Core has different options to provision and onboard a large number of devices, depending on the capabilities of the device, and if the devices have their unique X.509 certificate and private keys on them before being sold to the end customer.

 If the manufacturing chain allows the device maker to provision unique credentials into the device at manufacturing time or in distribution, device makers can use Just in Time Provisioning (JITP), Just in Time Registration (JITR), or Multi-Account Registration (MAR).

 If it is not possible to establish unique credentials on the device before it is sold to the end customers, device makers may use Fleet Provisioning to onboard their devices.

## Just-in-Time Provisioning
<a name="just-in-time-provisioning"></a>

 Devices that use Just-in-Time Provisioning (JITP) have certificates and private keys present on the device before onboarding to AWS IoT. The certificates must be signed with the customer’s designated CA, and that CA must be registered in AWS IoT. Certificates generated on AWS IoT cannot be used with the just-in-time method. The customer must know which account the device will connect to before provisioning.

### Setup
<a name="setup"></a>

 Using JITP, the device connects to AWS IoT Core, and the certificate’s signature is verified against the registered CA. After verification, a provisioning template registers the Thing and certificate, and assigns a policy to the device. The device maker is responsible for registering the signer CA and attaching a provisioning template to the CA.

### Device logic
<a name="device-logic"></a>

 When the device connects to AWS IoT Core for the first time, the device certificate must be sent during the [TLS handshake](https://www.ssl.com/article/ssl-tls-handshake-overview/). The signer CA must also be sent during the TLS handshake if the device does not send the Service Name Indicator (SNI) during the connection. The TLS handshake will fail at the first connection. This happens because the certificate has not been pre-loaded into the AWS IoT account. The device-supplied certificate is registered and activated in AWS IoT Core during the provisioning process. The device must have logic to reconnect to AWS IoT Core after a short time period. If the provisioning operation has succeeded, the device will connect to AWS IoT Core successfully.

![A diagram that shows Just-in-Time Provisioning process.](http://docs.aws.amazon.com/whitepapers/latest/device-manufacturing-provisioning/images/JustInTimeProvisioning-Nov22Refresh.png)

## Just-in-Time Registration
<a name="just-in-time-registration"></a>

 Just-in-Time Registration (JITR) should be used if additional custom logic is required when the device is registered on AWS IoT Core. Like JITP, certificates and private keys must be present on the device before onboarding and the signer CA must be loaded into the AWS account before the device onboards.

### Setup
<a name="setup-1"></a>

 When the device first connects to AWS IoT Core, the certificate’s signature is verified against the Certificate Authority and the certificate is registered in an inactive state. AWS IoT Core generates a Lifecycle event on the [MQTT](https://mqtt.org/) topic `$aws/events/certificates/registered/<caCertificateID>`. The device maker sets up an IoT Rule that cues an [AWS Lambda](https://aws.amazon.com/lambda/) function whenever a message is published on that topic.

 The Lambda function can perform actions such as secondary validation against an allow list or Certificate Revocation List, register the device to a particular user on the cloud platform, or initiate additional onboarding workflows. The Lambda function sets the certificate’s state to Active after additional validation is completed. The Lambda function should also create the IoT Thing, set up the Policy, and associate both with the certificate.

### Device logic
<a name="device-logic-1"></a>

 Just like JITP, the client certificate must be sent during the TLS handshake, and the signer CA must be sent if the device does not support SNI. The device will fail to make the first connection to AWS IoT Core. The device must contain logic to reconnect to AWS IoT Core after the first failed connection. If the Lambda function activates the certificate, the second device connection will succeed.

![A diagram that shows the Just-in-Time Registration process.](http://docs.aws.amazon.com/whitepapers/latest/device-manufacturing-provisioning/images/JustInTimeRegistration-Nov22Refresh.png)

### Use cases for Just-in-Time Provisioning and Registration
<a name="use-cases-for-just-in-time-provisioning-and-registration"></a>

 JITP and JITR are used when the device maker knows at manufacturing time into which AWS accounts and/or Regions the device will be onboarded. The CA must be registered in the account and Region before the devices attempt a first connection. The just-in-time process requires a one-time setup and scales to millions of devices.

## Manual registration without a CA
<a name="manual-registration-without-a-ca"></a>

 Existing device client certificates can be registered manually, without requiring a registered CA in one or more [AWS IoT Core](https://aws.amazon.com/iot-core/) accounts. Once a unique certificate and private key are provisioned on the device, the certificate can be registered to IoT Core to enable the device to connect. Certificates are typically signed with a CA, but that CA is not required to be registered with AWS IoT Core with this manual registration method. Certificates can be registered in any Region and in any AWS account where the device maker has access. This method is often referred to as Multi-Account Registration, or MAR.

### Setup
<a name="setup-2"></a>

 Device makers are required to set up the necessary resources in AWS for each device. The resources are set up before the device connects to AWS IoT Core for the first time.

 Some vendors provide hardware security modules that are pre-provisioned with a private key and certificate. The certificate is signed with the vendor’s own CA, and the vendor provides a manifest of certificates to the device maker. The device maker is responsible for registering the certificates in each account and Region using the [AWS Management Console](https://aws.amazon.com/console/), [AWS IoT Control Plane API](https://docs.aws.amazon.com/iot/latest/apireference/Welcome.html), or the [AWS Command Line Interface](https://aws.amazon.com/cli/) (AWS CLI).

### Device logic
<a name="device-logic-2"></a>

 The device’s TLS stack must support the SNI extension, and the AWS IoT Core endpoint is passed in the SNI string from the device. No additional device logic is required.

![A diagram that shows manual registration without a CA process.](http://docs.aws.amazon.com/whitepapers/latest/device-manufacturing-provisioning/images/MultiAccountRegistration_sequence.png)

### Use cases for manual registration without a CA
<a name="use-cases-for-manual-registration-without-a-ca"></a>

 Manual registration without a CA is used if flexibility is needed when determining which account and Regions a device may connect to. Device makers and service providers might have multiple AWS accounts used for sandbox, testing and production. Certificates can be pre-registered in each AWS account, and the device can connect to different accounts throughout its lifecycle by changing the IoT endpoint on the device. Devices can be sold globally, and the certificate can be registered in multiple [AWS Regions](https://aws.amazon.com/about-aws/global-infrastructure/regions_az/) as well as multiple AWS accounts within the same Region. This method allows the device makers to provide the public X.509 client certificate of a device to an IoT service provider so that they may manually register it to one or more their accounts.

## Fleet provisioning
<a name="fleet-provisioning"></a>

 There are cases when provisioning unique credentials to a device at manufacturing time is not feasible due to technical limitations, cost, or application specific requirements. Devices that are not customized from the manufacturer are sold to customers without a unique identity. Fleet provisioning provides two ways to provision devices with unique credentials after they are delivered to end customers: by trusted user or by claim.

### Fleet provisioning by trusted user
<a name="fleet-provisioning-by-trusted-user"></a>

 AWS IoT Core provides an application programming interface (API) that allows mobile applications to generate temporary certificates and private keys. The device leaves the manufacturing facility with no unique credentials, and only trusted users are able to provision the device with its unique credentials.

 An installer uses a mobile application and authenticates with AWS. The mobile application should call the [CreateProvisioningClaim API](https://docs.aws.amazon.com/iot/latest/apireference/API_CreateProvisioningClaim.html) that returns a temporary X.509 certificate and private key that is valid for five minutes. Using the mobile application, these temporary credentials are delivered to the device. The device connects to AWS IoT and exchanges the temporary credentials for a unique X.509 certificate signed with an ephemeral AWS CA and corresponding private key. During this workflow, the AWS resources including Thing, Policy, and Certificate are set up in the AWS account.

#### Setup
<a name="setup-3"></a>

 Device makers that use the Trusted User flow must develop and maintain a mobile application that uses the `CreateProvisioningClaim` API. The fleet provisioning template must be set up and maintained in AWS IoT Core by the device maker. Optionally, a pre-provisioning AWS Lambda function is recommended to provide additional authentication steps during the provisioning process.

#### Device logic
<a name="device-logic-3"></a>

 Devices must have the ability to accept temporary credentials over a secure connection such as Bluetooth Low Energy, WiFi, or USB. Devices must implement the logic necessary to publish and subscribe to fleet provisioning MQTT topics, accept the permanent credentials, and write the credentials to secure storage.

![A diagram that shows fleet provisioning by Trusted User process.](http://docs.aws.amazon.com/whitepapers/latest/device-manufacturing-provisioning/images/FleetProvisioningTrustedUser.png)

#### Use cases for fleet provisioning by trusted user
<a name="use-cases-for-fleet-provisioning-by-trusted-user"></a>

 The credentials are never exposed to the manufacturing supply chain. Fleet provisioning by trusted user is the recommended approach when a high degree of security is needed, when the manufacturing chain is not trusted, or when it is not possible to provision devices in the manufacturing chain. Trusted users must be authorized to perform the provisioning operations and the device used to generate the temporary credentials should be secure.

### Fleet provisioning by claim
<a name="fleet-provisioning-by-claim"></a>

 If a device does not have the capability to securely generate unique keys or the manufacturing supply chain is not equipped to uniquely provision devices at manufacturing time, the device maker should use a shared claim certificate that gets loaded on the devices. AWS IoT Core provides a path for these devices to receive a unique identity when they first connect to AWS IoT Core.

 Fleet provisioning by claim requires device makers to use a shared claim certificate and key on all devices. The claim certificate should be unique per batch of devices to limit the number of devices affected in the event that the claim certificate’s private key is compromised and the certificate needs to be revoked. If the claim certificate is revoked, devices that share this certificate will no longer be able to use it to complete the provisioning process. The firmware containing the claim certificate is loaded by the contract manufacturer without the need to perform any customization. When the device establishes a connection with AWS IoT Core for the first time, it exchanges the claim certificate for a unique X.509 certificate signed by the AWS certificate authority and a private key. The device should send a unique token, such as an embedded hardware secret with its provisioning request that the fleet provisioning service can use to verify against an allow list using the pre-provisioning Lambda in order to validate the authenticity of the device.

#### Setup
<a name="setup-4"></a>

 Device makers that use fleet provisioning by claim must maintain a fleet provisioning template and AWS Lambda function with additional verification logic. The claim certificates must be protected and frequently audited to prevent misuse.

#### Device logic
<a name="device-logic-4"></a>

 Devices must implement the logic necessary to publish and subscribe to fleet provisioning MQTT topics, accept the permanent credentials, and write the credentials to secure storage.

![A diagram depicting fleet provisioning by claim process.](http://docs.aws.amazon.com/whitepapers/latest/device-manufacturing-provisioning/images/FleetProvisioningByClaim.png)

#### Use cases for fleet provisioning by claim
<a name="use-cases-for-fleet-provisioning-by-claim"></a>

 Fleet provisioning by claim should only be used when it is not possible to provision unique credentials in the device, and when it is not possible to use the provisioning by trusted user option. Devices that enter insecure channels such as a third-party distributor should not use fleet provisioning by claim because of the risk in exposing the claim credentials that are common to every device prior to the initial connection to AWS IoT Core.
