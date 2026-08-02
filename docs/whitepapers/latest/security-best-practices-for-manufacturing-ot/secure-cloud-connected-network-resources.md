---
source_url: https://docs.aws.amazon.com/whitepapers/latest/security-best-practices-for-manufacturing-ot/secure-cloud-connected-network-resources.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Secure cloud connected network resources
<a name="secure-cloud-connected-network-resources"></a>

Cloud connected network resources, such as edge gateways, agent software, and IoT devices, need to be hardened to reduce the risk of inadvertent access. Credentials and permissions to access local resources from cloud connected resources should also be managed to limit the scope of impact of an adverse event. Figure 12 highlights some of these best practices.
+  **Harden cloud connected compute resources** — While specific hardening guidelines are dependent on the edge gateway’s operating system, [general guidelines](https://nvlpubs.nist.gov/nistpubs/Legacy/SP/nistspecialpublication800-123.pdf) to harden and securely configure an OS include:
+  Remove unnecessary service, applications, and network protocols.
+  Configure OS user authentication (remove unneeded accounts, disable non-interactive accounts, configure automatic time synchronization).
+  Configure resource controls appropriately (allow access to only needed resources).
+  Install and configure additional security control (anti-malware, intrusion detection, host-based firewalls).

Access to unnecessary hardware ports such as USB and serial should also be disabled using both physical and software means.

When edge gateway is purchased from the vendor, you may not have direct access to the OS; consult the vendor’s documentation to ensure the vendor has taken appropriate steps to harden the underlying OS.
+  **Use hardware security features like TPM to secure devices** — Leverage hardware security features like Trusted Platform Module (TPM) whenever possible. A TPM is a cryptographic processor present on most commercial PCs and servers. Ubiquitous in nature, it can be used for a wide variety of use cases, such as storing keys for VPN access and encryption keys for hard disks, or preventing dictionary attacks to retrieve private keys.

AWS IoT Greengrass, for example, supports the use of hardware security modules (HSM) for secure storage and offloading of private keys (see Figure 8). Private keys can be securely stored on hardware modules, such as HSMs, Trusted Platform Modules (TPM), or other cryptographic elements. Search for devices that are qualified for this feature in the [AWS Partner Device Catalog](https://devices.amazonaws.com/search?kw=%22HSI%22&page=1).

On a standard installation, AWS IoT Greengrass uses two private keys. One key is used by the AWS IoT client (IoT client) component during the Transport Layer Security (TLS) handshake when a AWS IoT Greengrass core connects to AWS IoT Core. (This key is also referred to as the core private key.) The other key is used by the local MQTT server, which enables AWS IoT Greengrass devices to communicate with the AWS IoT Greengrass core. Hardware security can be used for both components using shared or separate private keys. For more information, see [Provisioning Practices for AWS IoT Greengrass Hardware Security](https://docs.aws.amazon.com/greengrass/latest/developerguide/hardware-security.html#optional-provisioning).

![A diagram showing hardware security architecture for AWS IoT Greengrass.](http://docs.aws.amazon.com/whitepapers/latest/security-best-practices-for-manufacturing-ot/images/hw-security-arch.png)

* Hardware security architecture for AWS IoT Greengrass *
+  **Plan and manage security lifecycle of devices** — Planning the device and solution security lifecycle at design time reduces business risk and provides an opportunity to perform upfront infrastructure security analysis.

One way to approach the device security lifecycle is through supply chain analysis. A large number of suppliers can be involved in the supply chain of devices, whether directly or indirectly. To maximize solution lifetime and reliability, ensure that you are receiving authentic components.

Software is also a part of the supply chain. Analyze each software provider in the supply chain to determine if it offers support and how it delivers patches. Have a plan to validate firmware, patches, or any other software, to ensure their authenticity and validity.
+  **Prefer IAM roles / device certificates over IAM credentials** — Edge software requires AWS credentials to access AWS resources. Depending on the service, the device can use IAM roles, X.509 certificates, or even custom authentication methods. Avoid using hard coded long-term credentials and prioritize using IAM roles or X.509 certificates for authentication.

In case of AWS IoT, devices can connect using X.509 certificates or Amazon Cognito identities over a secure TLS connection (see Figure 10). During research and development, and for some applications that make API calls or use WebSockets, authentication can also be done using IAM users and groups or custom authentication tokens. When using custom authentication, a custom authorizer is responsible for authenticating devices and granting or denying access permissions specified for devices using AWS IoT or IAM policies.

Unique identities should be assigned to each device and permissions should be managed for each device or group of devices. If device certificate or static credentials are used, those credentials should be rotated as appropriate, given the current best practices.

![A diagram showing AWS IoT authentication and authorization.](http://docs.aws.amazon.com/whitepapers/latest/security-best-practices-for-manufacturing-ot/images/iot-authentication-auth.png)

* AWS IoT authentication and authorization *
+  **Implement certificate rotation for AWS IoT, AWS IoT Greengrass core and AWS IoT Greengrass aware devices** — X.509 certificates used by AWS IoT, AWS IoT Greengrass Core, and AWS IoT Greengrass aware devices provide stronger client authentication over other schemes, such as sign-in credentials or bearer tokens, because the private key never leaves the device. The clock on the device is used to verify that a server certificate is still valid and not expired, therefore it is important to maintain accurate time on the device.

Each device or client should be given a unique certificate to enable fine-grained client management actions, including certificate revocation. Devices and clients should also support rotation and replacement of certificates to help ensure smooth operation as certificates expire or if they are inadvertently disclosed.

Rotate certificates under the following circumstances:
+  Just before the certificate expires
+  Based on violations detected by [AWS IoT Device Defender](https://aws.amazon.com/iot-device-defender/)
+  In case of inadvertent disclosure

For example, AWS IoT Device Defender audit can be used to identify if a device certificate is expiring soon. This is reported to an SNS topic that triggers a Lambda function that schedules an IoT job to rotate the certificate.

AWS IoT Greengrass-connected devices use the local MQTT server certificate for mutual authentication with the AWS IoT Greengrass core device. By default, this certificate expires in seven days. This limited period is based on security best practices. The MQTT server certificate is signed by the group CA certificate, which is stored in the cloud. The expiration can be set for up to 30 days directly, or even longer duration by contacting AWS Support. More frequent rotation requires more frequent cloud connection. Less frequent rotation can pose security concerns. Certificates can also be rotated manually. Customers should create and follow a certificate rotation policy suiting to their needs.
+  **Avoid hardcoding or storing local credentials** — The edge software may need credentials to access local resources like databases, OPC UA servers. Instead of storing and managing credentials locally, store credentials within a secure vault store such as [AWS Secrets Manager](https://aws.amazon.com/secrets-manager/). AWS Secret Manager is service to securely store and manage secrets in the cloud. Code can retrieve the secrets via an API call. AWS Secrets Manager can also be set to automatically update and rotate credentials. The secrets are encrypted with the [AWS Key Management Service](https://aws.amazon.com/kms/) (KMS) key of choice, and administrators can explicitly grant access to these secrets with granular IAM policies for individual roles or users.

[AWS IoT Greengrass](https://aws.amazon.com/greengrass/) offers built in integration with Secrets Manager. AWS IoT Greengrass extends Secrets Manager to AWS IoT Greengrass core devices, so [connectors](https://docs.aws.amazon.com/greengrass/latest/developerguide/connectors.html) and Lambda functions can use local secrets to interact with services and applications. For example, the [Twilio Notifications](https://www.twilio.com/) connector uses a locally stored authentication token. To integrate a secret into an AWS IoT Greengrass group, create a group resource that references the Secrets Manager secret. This secret resource references the cloud secret by ARN. To learn how to create, manage, and use secret resources, see [Working with secret resources](https://docs.aws.amazon.com/greengrass/latest/developerguide/secrets-using.html). AWS IoT Greengrass encrypts secrets while in transit and at rest. During group deployment, AWS IoT Greengrass fetches the secret from Secrets Manager and creates a local, encrypted copy on the AWS IoT Greengrass Core. After rotating the cloud secrets in Secrets Manager, redeploy the group to propagate the updated values to the core. Figure 10 shows the high-level process of deploying a secret to the core. Secrets are encrypted in transit and at rest.

![A diagram that shows deploying a secret to AWS IoT Greengrass Core.](http://docs.aws.amazon.com/whitepapers/latest/security-best-practices-for-manufacturing-ot/images/deploy-secret-greengrass.png)

*Deploying a secret to AWS IoT Greengrass Core *
+  **Ensure least privilege access controls for “edge gateways” and “agent software” accessing local and AWS resources** — Edge gateways and agent software should be configured to allow only the required access to both local and AWS resources. For edge gateways, access to local resources should be controlled via firewall on the southbound side to limit access only the needed local resources (for example, access to only required PLCs / OPC servers, IP addresses, and protocols). OS / Active Directory permissions should also be used to prevent access to local network resources like file servers.

Agent software is often installed on the host machine, generating the data to be collected. The agent software access to the host machine resources should be restricted using the operating systems access controls. The agent software daemon (or service) should run under its own account with only the necessary permissions. Just like edge gateway, firewalls and operating system/active directory permissions should to be used to prevent access to local network resources.

Access to AWS resources should be controlled with appropriate IAM policies attached to the edge gateway, or the agent software AWS identity/role. [AWS Systems Manager](https://aws.amazon.com/systems-manager/), along with [AWS Config](https://aws.amazon.com/config/), can be used to gain visibility and track changes to OS configurations, system-level updates, installed applications, network configuration, and more.

![A diagram that shows secure cloud connected network resources.](http://docs.aws.amazon.com/whitepapers/latest/security-best-practices-for-manufacturing-ot/images/secure-cloud-nw-reso.png)

 *Secure cloud connected network resources *
