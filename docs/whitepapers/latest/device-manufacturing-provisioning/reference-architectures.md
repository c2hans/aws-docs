---
source_url: https://docs.aws.amazon.com/whitepapers/latest/device-manufacturing-provisioning/reference-architectures.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Reference architectures
<a name="reference-architectures"></a>

 The provisioning approaches described in this whitepaper provide the building blocks for a device provisioning and onboarding solution to AWS IoT Core. Device makers might require additional components or a combination of these approaches in order to meet their requirements. AWS provides several open-source device onboarding and provisioning architectures that are deployable and extensible for device makers and service providers. This section explores two onboarding architectures that build upon these: zero-touch provisioning (ZTP) and the Device Lobby.

## Zero-Touch Provisioning
<a name="zero-touch-provisioning"></a>

 Device makers may use a ZTP service provider to manage their public key infrastructure, and provision certificates and private keys to their device. ZTP service providers allow device makers to manage device security, identity and registration independent from the device manufacturing supply chain. Devices will be manufactured with a unique identifier known to the ZTP service provider and stored on a secure location on the device. This unique identifier is traded for a device certificate during the onboarding stage of the device’s lifecycle over the air and automatically.

 ZTP provides several benefits to the device maker. The device maker can manage their device manufacturing supply chain without prior knowledge of where the device will ultimately connect. The onboarding and registration of the devices are done programmatically and in large quantities, usually separated by manufacturing batches. This simplifies onboarding a large number of devices to multiple AWS accounts. The service provider’s ZTP service is a known and trusted authority that the device can fall back to during factory resets, transfer of device ownership, and decommissioning. The service provider may also provide value-add services such as remote attestation, third-party Certificate Authorities, and secure manufacturing infrastructure.

 ZTP is a common design pattern implemented by telecommunications providers for cellular IoT devices and hardware security module vendors.

 **ZTP implementation**

 ZTP service providers provision identities into devices in their own secure infrastructure. Devices first connect to the service provider’s ZTP service, usually through a device agent that the service provider provides. The service provider is responsible for managing the customer’s Public Key Infrastructure, device certificates, and connectivity management.

 The ZTP service provider is also responsible for registering the device to the device maker’s AWS account. In this scenario, the device maker must have a secure API for the service provider to register the X.509 certificate, Thing name, and IoT Policy into their account. Once the service provider registers the certificate to the customer’s account, the device can securely connect to the customer’s AWS IoT broker endpoint.

 AWS has mechanisms to keep this transaction secure, robust, and reliable. The customer creates an AWS Identity and Access Management (IAM) role for the service provider to assume. IAM provides fine-grained access control across all of AWS. With IAM, you can specify who can access which services and resources, and under which conditions. The IAM Role implements a policy that ensures the service provider can only access specific APIs and actions within the device maker’s account, such as registering an IoT Thing and Certificate.

 A ZTP reference implementation is provided on the `aws-samples` Github repository, which includes a CloudFormation template, AWS Lambda sample code, a sample third-party CA, a deployment script, and a testing script. The reference implementation sets up a secure API and IAM role in the device maker’s account. The ZTP service provider assumes the IAM role and sends an HTTP POST to the secure API with a device certificate. The device certificate is verified against a known certificate authority. The device certificate, IoT Thing name, and an IoT Policy are set up in the device maker’s account. The device maker’s AWS IoT broker endpoint is returned to the ZTP service provider to forward to the device. The device can then connect to the device maker’s AWS IoT endpoint.

![A diagram that shows zero-touch provisioning reference architecture.](http://docs.aws.amazon.com/whitepapers/latest/device-manufacturing-provisioning/images/ZTPCloudDemoArchitecture.png)

## Device lobby
<a name="device-lobby"></a>

 The IoT device lobby architecture establishes an entry point in AWS Cloud infrastructure to route or bootstrap devices to end cloud services. It provides a serverless infrastructure to associate a device identity by using the X.509 fingerprint to a target AWS account or Region, regardless of whether a device is turned on. The device fingerprint can be printed as a QR code for easy scanning and onboarding of devices to target accounts and Regions by the administrator APIs at any point in a device lifecycle without reprovisioning. This helps fleet operators take advantage of the AWS IoT global footprint, and can effectively decouple the manufacturing and provisioning of devices from the end cloud services where they connect once deployed in the field.

![A diagram that shows device lobby onboarding architecture.](http://docs.aws.amazon.com/whitepapers/latest/device-manufacturing-provisioning/images/device-lobby.png)

 The architecture combines JITR and manual registration methods described earlier in this whitepaper with the inclusion of a global Amazon DynamoDB table to act as the device ledger and an administrative interface for managing the ledger to claim and route devices. JITR enables the initial connection to the lobby for previously unseen devices when they present a certificate signed by a CA trusted by the Device Lobby account. Manual registration without a CA is then used by the backend to register devices into target accounts or Regions once claimed by an administrator. MQTT topics are used to control the interaction with the device and service.

### Use cases for the Device lobby:
<a name="use-cases-for-the-device-lobby"></a>
+  **Commissioning devices for a target account or Region during installation -** A technician or user installs the device, and the customer account or Region must be associated at the time of install – for example, technicians claiming devices at time of install using authorized mobile device or app.
+  **Offline commissioning of devices in the supply chain** - Devices are delivered to a customer and need to connect to the correct endpoint when powered up. The customer account or Region is known at time of shipment, but the device is in a box and not powered on – for example, offline binding in the supply chain.
+  **Account or Region migration of previously fielded devices** - Devices need to be moved among accounts, environments, or Regions without changing credentials for factory returns, refurbishment, redeployment, or simply moving devices during development between dev/staging/prod environments.
+  **Disaster recovery orchestration** - A given Region becomes unavailable and devices need to be dynamically routed in the field to another account or Region with functioning application infrastructure.

### Device lobby implementation
<a name="device-lobby-implementation"></a>

 Building a device lobby implementation on AWS requires both device application logic and AWS Cloud components.

#### Device logic
<a name="device-logic-5"></a>

 The device onboarding logic required to work with the Device Lobby service is intended to be simple and present a minimal impact to the ROM/RAM footprint of the device. Two MQTT topics are used to control the interaction with the service in order for the most constrained devices to not require any additional protocol stacks.

 The device is required to implement an onboarding state machine that determines its operational mode and whether to connect to the Device Lobby endpoint(s) to be commissioned, or to the target account endpoint to perform its end function. The commissioned state and target IoT endpoint can be kept in non-volatile storage, so passage through the lobby for the routing happens only once or until cleared by a factory reset. A factory fresh device could be provisioned with one or more lobby account IoT endpoints to use by default, or the endpoint could be configured by the end user.

 The device should always inform the cloud of its core identity presented as the X.509 device certificate. As the identity of a device is not known to the Device Lobby prior to first connection, the X.509 certificate provisioned to the device should contain everything needed to uniquely identify the device and establish the source of trust. The device needs to be provisioned with the keys and X.509 certificate issued by the manufacturer’s PKI. The certificate should contain the unique name of the device in the CN field of the certificate Subject and have a long-lived expiration that exceeds the expected lifecycle of the device.

 With properly established credentials and lobby endpoint configured, the device can then be routed to any end AWS account at any point in its lifecycle with the Device Lobby administrator APIs or console.

#### Cloud service components:
<a name="cloud-service-components"></a>
+  Device ledger table – The device ledger table is implemented as a global DynamoDB table that holds the device identity and target account/Region association. The device certificate fingerprint serves as the primary key for the table. New fingerprint entries are made by either:
+  The Bouncer Lambda for new, unclaimed devices connecting to the service, or
+  Administrators using the AppSync APIs and/or web console.
+  **Bouncer Lambda** – This Lambda function is responsible for admitting devices to connect to the Device Lobby account. In the example implementation, the Just-in-time Registration flow is used to verify a device’s certificate against a trusted CA, register the device certificate, extract the Thing name and register or activate the device so it can connect to the Device Lobby account with minimal permissions. Other access methods to the lobby are possible, such as fleet provisioning or the custom authorizer feature of IoT Core.
+  **Receptionist Lambda –** Once a device has successfully connected to the lobby account, this Lambda function is cued through the basic ingest lobby rule, where the device publishes to announce its presence in the lobby. The lobby rule extracts the certificate ID or fingerprint from the certificate used for the connection and device name from the MQTT client ID, and passes any other MQTT payload data on to the Receptionist Lambda. When initiated by a device announcement, the Lambda function will attempt to retrieve the commissioned IoT endpoint for the fingerprint and will publish it back on the device-specific lobby topic. If no endpoint exists in the ledger table, the function does nothing and the device can loiter in the lobby indefinitely, periodically announcing its presence until a commissioned IoT endpoint is returned.
+  **Commissioner Lambda –** This function is responsible for watching the stream from the device ledger table and registering devices into the target account or Region using manual registration without a CA. The function registers a device only when a complete commissioning entry is available in the table. A complete entry includes the device certificate and Thing name provided by the device in the initial connection to the lobby, and a target account or Region that has been written by the administrative APIs. The function assumes a role in the target account with the appropriate permissions to read the target IoT endpoint and register certificates, Thing names, and policies. Once the device and certificate are registered in the target account, the function writes the commissioned IoT endpoint to the device entry in the ledger table, indicating that the device has been successfully registered in the target.
+  **Administrative APIs and web portal** – Administration of the device ledger table is performed through AWS AppSync GraphQL APIs that are authenticated by Amazon Cognito. The enables strict access control to the device ledger table using administrator-specified user pools. From an administrative standpoint, only the device fingerprint (QR code) and the target account or Region are needed to claim and route devices through the lobby. The sample web portal provides a basic, authenticated React application for monitoring devices in the lobby, and claiming them with using a built in QR code reader function.
+  **Target AWS account –** To receive devices routed by the lobby, the target account must have a role defined for the Commissioner Lambda function to assume and the trust linkage established back to the Commissioner Lambda function [Amazon Resource Name](https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html) (ARN) in the lobby account.

 The goal of the device lobby architecture is to enable device manufacturers or product teams to produce single-SKU IoT devices that can be easily and securely onboarded by service operators to any AWS account/Region by simply scanning a QR code.

 A reference implementation and quickstart guide for the Device Lobby architecture is available on the `aws-samples` Github repository, which includes a CloudFormation template, deployment scripts, admin console web app with QR reader, and sample device implementations.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Whitepapers. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query whitepapers` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
