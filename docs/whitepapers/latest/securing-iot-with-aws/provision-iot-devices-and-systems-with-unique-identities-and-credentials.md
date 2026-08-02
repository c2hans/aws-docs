---
source_url: https://docs.aws.amazon.com/whitepapers/latest/securing-iot-with-aws/provision-iot-devices-and-systems-with-unique-identities-and-credentials.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# 3. Provision IoT devices and systems with unique identities and credentials
<a name="provision-iot-devices-and-systems-with-unique-identities-and-credentials"></a>

Provision IoT devices and systems with unique identities and credentials. Apply authentication and access control mechanisms at each system interface.

 Strong identity controls are key to operational excellence. However, IoT implementation considerations around physical control of devices range widely. Therefore, not only is it important to ensure devices receive unique identities and credentials, but also that those credentials are appropriately protected on the device, and monitoring and automated remediation plans are put in place when there’s deviation from expected standards.
+  Assign unique identities to IoT devices such as X.509 certificates to each device. Monitor that the identity does not change on devices or that certificates are not reused.
+  Create mechanisms to facilitate the generation, distribution, rotation, and revocation of credentials.
+  When appropriate, use hardware-protected modules such as TPMs for storing credentials and performing authentication operations.
+  Avoid hardcoding credentials or storing secrets that are not unique to the device on IoT devices.

## Supporting AWS resources
<a name="resources-3"></a>

 AWS provides the following assets, services, and capabilities to help you identify, sort, and secure your IoT assets:
+  [Security and identity for AWS IoT](https://docs.aws.amazon.com/iot/latest/developerguide/security.html)
+  [Device manufacturing and provisioning with X.509 certificates in AWS IoT Core](https://d1.awsstatic.com/whitepapers/device-manufacturing-provisioning.pdf) – Goes over various mechanisms to securely provision identities to your IoT devices.
+  [AWS Certificate Manager](https://aws.amazon.com/certificate-manager/) Private Certificate Authority – For provisioning your own certificates.
+  [Amazon Cognito](https://docs.aws.amazon.com/cognito/latest/developerguide/what-is-amazon-cognito.html) – A service that provides authentication, authorization, and user management for your web and mobile apps.
+  [AWS Identity and Access Management](https://aws.amazon.com/iam/) (IAM) – A service that enables you to manage access to AWS services and resources securely.
+  [Device authentication and authorization for AWS IoT Greengrass](https://docs.aws.amazon.com/greengrass/v1/developerguide/device-auth.html)
+  [AWS Secrets Manager](https://aws.amazon.com/secrets-manager/) – A service that can be used to securely store and manage secrets in the cloud and encrypts the secrets using AWS Key Management Service (AWS KMS).
+  [AWS KMS](https://aws.amazon.com/kms/) – Allows you to easily create and control the keys used for cryptographic operations in the cloud.
+  [Security Pillar of AWS Well-Architected](https://docs.aws.amazon.com/wellarchitected/latest/security-pillar/welcome.html) and [IoT Lens](https://docs.aws.amazon.com/wellarchitected/latest/iot-lens/welcome.html)
