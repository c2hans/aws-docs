---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/strategy-matter-standard/development-with-matter.html
---

# Development with Matter

## Using Alexa
<a name="using-alexa"></a>

Amazon offers tools for Matter development. These tools help you build Matter products that are designed to work with Amazon Alexa and other Matter-compatible smart home systems.

### Program: Works with Alexa
<a name="program--works-with-alexa.0a76c445-02bc-5107-85df-77fd40062145"></a>

This program helps you verify that your Alexa-connected devices meet quality standards for customer experience. The Works with Alexa (WWA) badge can help customers identify your certified devices. For more information, see [Announcing Matter Launch and Introducing Works with Alexa (WWA) for Matter devices](https://developer.amazon.com/en-US/blogs/alexa/device-makers/2022/11/matter-works-with-alexa-introduction-november-2022) (Amazon blog post).

### SDK: Develop Matter with Alexa
<a name="sdk--develop-matter-with-alexa.cc2e1fa5-582c-52ec-b2e1-7ce5cad529e4"></a>

This SDK lets you add local Matter connectivity to your device. It also includes managed cloud connectivity, business intelligence, and over-the-air (OTA) update support. For more information, see [Get the most out of Matter with Alexa](https://developer.amazon.com/en-US/alexa/matter).

### Kit: Alexa Ambient Home Developer Kit
<a name="kit--alexa-ambient-home-developer-kit.1e5796a7-aa68-5cfa-b867-76294b0d949c"></a>

This kit helps you integrate with devices across protocols to build an ambient and unified smart home with Alexa. For more information, see [Amazon Alexa](https://developer.amazon.com/en-US/alexa/alexa-ambient-home-dev-kit).

### Endpoint: Commissionable Endpoint
<a name="endpoint--commissionable-endpoint.21642e4a-d75b-566a-8802-6f96824339dc"></a>

For skill-connected Matter devices, the Commissionable Endpoint API creates a local, Matter-based connection to Alexa devices. With your customer's permission, this connection doesn't require additional setup steps from the customer. For more information, see [Alexa.Commissionable Interface 1.0](https://developer.amazon.com/en-US/docs/alexa/device-apis/alexa-commissionable.html) (Alexa Skills Kit).

## AWS Private CA support for Matter
<a name="pca-support-for-matter"></a>

[AWS Private Certificate Authority](https://docs.aws.amazon.com/privateca/latest/userguide/PcaWelcome.html) (AWS Private CA) provides guidance on using the Matter standard.

### DAC for Matter
<a name="dac-for-matter.96dcedd7-7342-56b3-b9d0-ca94cd894d5b"></a>

Matter requires a device attestation certificate (DAC), which must be issued by a device attestation CA that is compliant with the Matter public key infrastructure (PKI) certificate policy (CP). Device vendors can use AWS Private CA to do the following:
+ Host the Product Attestation Authority (PAA) certificate authority (CA)
+ Host the Product Attestation Intermediate (PAI) CA
+ Issue, sign, and maintain each device's DAC

### Node Operational Certificates (NOC)
<a name="node-operational-certificates--noc-.380d728e-ba74-58d6-957a-e54c595c8223"></a>

In addition to device attestation, AWS Private CA supports issuing Node Operational Certificates (NOCs), which are used to secure communication within a Matter fabric. AWS provides Java samples for activating a root CA and subordinate CA for NOCs and creating a NOC.

For more information, see [Using the AWS Private CA API to implement Matter certificates](https://docs.aws.amazon.com/privateca/latest/userguide/API-CBR-intro.html) in the AWS Private Certificate Authority documentation.

### CRL Revocation Support (Matter version 1.2 and later)
<a name="crl-revocation-support--matter-version-1.2-and-later-.dcf9de54-f8b8-5c1b-990f-ca603279d5de"></a>

Matter version 1.2 introduced DAC revocation using certificate revocation lists (CRLs). When you enable CRL revocation for CAs that issue Matter certificates, set `OmitExtension` to `true` in the `CrlConfiguration` object within the `CrlDistributionPointExtensionConfiguration` structure. In Matter, the CRL distribution point (CDP) URI is not embedded in certificates. Instead, devices fetch it from the Matter Distributed Compliance Ledger (DCL). You must upload the CDP URI to the Matter DCL for discovery during DAC validation.

### Infrastructure for Matter
<a name="infrastructure-for-matter.cd2bd337-d785-591e-bf05-91402dc9b3d1"></a>

Operating Matter-compliant CAs requires supporting infrastructure for audit logging, log retention, access control, and CRL distribution. You can build this infrastructure by using AWS Private CA with [AWS CloudTrail](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/index.html), Amazon CloudWatch Logs, [Amazon S3](https://docs.aws.amazon.com/AmazonS3/latest/userguide/), and [AWS Identity and Access Management](https://docs.aws.amazon.com/IAM/latest/UserGuide/) (IAM). If you publish CRLs to Amazon S3, keep the bucket private by turning on Amazon S3 Block Public Access, and serve the CRLs through [Amazon CloudFront](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/). For the controls that the Matter PKI CP requires, see the Matter PKI Compliance Guide.

### Guide for Matter PKI compliance
<a name="guide-for-matter-pki-compliance.a022e477-03c5-52e5-9dfc-0b7586f7826f"></a>

This [Matter PKI Compliance Guide](https://d1.awsstatic.com/whitepapers/compliance/matter-pki-compliance-guide.pdf) explains how to implement and demonstrate compliance with the CSA Matter PKI CP requirements. It provides information about how you can use AWS Private CA to create and operate Matter-compliant CAs.

## Managed integrations with AWS IoT Device Management
<a name="aws-iot-device-management-managed-integrations"></a>

[AWS IoT Device Management](https://docs.aws.amazon.com/iot/latest/developerguide/iot-thing-management.html) includes the managed integrations feature, which provides a unified interface for onboarding and managing diverse IoT devices regardless of connection type (direct, hub-based, or cloud-to-cloud).

The following are key capabilities relevant to Matter:
+ Device SDKs supporting Zigbee, Z-Wave, Matter, and Wi-Fi protocols
+ More than 80 device data model templates based on the AWS implementation of the Matter data model standard
+ Partner-built cloud-to-cloud (C2C) connectors
+ Unified device control across multiple brands and protocols
+ Available in the Canada (Central), Europe (Ireland), and Middle East (UAE) AWS Regions

For more information, see [What is managed integrations for AWS IoT Device Management?](https://docs.aws.amazon.com/iot-mi/latest/devguide/what-is-managedintegrations.html)
