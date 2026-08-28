---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/strategy-matter-standard/development-with-matter.html
---

# Development with Matter
<a name="development-with-matter"></a>

## Using Alexa
<a name="using-alexa"></a>

Amazon offers a comprehensive suite of tools for Matter development. These tools provide an expedited path to build Matter products that are compatible with all major ecosystems and that work seamlessly with Amazon Alexa.

### Program: Works with Alexa
<a name="program--works-with-alexa.e8447c4d-3070-5744-967a-1423a733d703"></a>

This program ensures your Alexa-connected devices provide a great customer experience. The Works with Alexa (WWA) badge increases customer confidence, which helps drive preference for your certified devices. For more information, see [Announcing Matter Launch and Introducing Works with Alexa (WWA) for Matter devices](https://developer.amazon.com/en-US/blogs/alexa/device-makers/2022/11/matter-works-with-alexa-introduction-november-2022) (Amazon blog post).

### SDK: Develop Matter with Alexa
<a name="sdk--develop-matter-with-alexa.97bfebca-b715-556d-9a69-ed9b7f01ecdc"></a>

This SDK lets you add local Matter connectivity to your device while also including managed cloud connectivity, business intelligence, and OTA support. For more information, see [Get the most out of Matter with Alexa](https://developer.amazon.com/en-US/alexa/matter).

### Kit: Alexa Ambient Home Developer Kit
<a name="kit--alexa-ambient-home-developer-kit.605759ea-38cf-5bf1-8261-315b6a072ad6"></a>

This kit helps you integrate with devices across protocols in order to build an ambient and unified smart home with Alexa. For more information, see [Amazon Alexa](https://developer.amazon.com/en-US/alexa/alexa-ambient-home-dev-kit).

### Endpoint: Commissionable Endpoint
<a name="endpoint--commissionable-endpoint.a4f0b331-1332-5e2d-9a39-3334cfa49046"></a>

For skill-connected Matter devices, the Commissionable Endpoint API creates a local, Matter-based connection to Alexa devices without any steps required by your customer with their permission. For more information, see [Alexa.Commissionable Interface 1.0](https://developer.amazon.com/en-US/docs/alexa/device-apis/alexa-commissionable.html) (Alexa Skills Kit).

## AWS Private CA support for Matter
<a name="pca-support-for-matter"></a>

AWS Private Certificate Authority (AWS Private CA) provides guidance on using the Matter standard.

### DAC for Matter
<a name="dac-for-matter.07349b2c-b195-5416-b5ea-277cbe3d5426"></a>

Matter requires a device attestation certificate (DAC), which must be issued by a device attestation CA that is compliant with the Matter public key infrastructure (PKI) certificate policy (CP). Device vendors can use AWS Private CA to do the following:
+ Host the Product Attestation Authority (PAA) certificate authority (CA)
+ Host the Product Attestation Intermediate (PAI) CA
+ Issue, sign and maintain each device's DAC

For more information, see [Use AWS Private Certificate Authority to issue device attestation certificates for Matter](https://aws.amazon.com/blogs/security/use-aws-private-certificate-authority-to-issue-device-attestation-certificates-for-matter/) in the AWS Security Blog.

### Node Operational Certificates (NOC)
<a name="node-operational-certificates--noc-.380d728e-ba74-58d6-957a-e54c595c8223"></a>

In addition to device attestation, AWS Private CA supports issuing Node Operational Certificates (NOCs), which are used to secure communication within a Matter fabric. AWS provides Java samples for activating a root CA and subordinate CA for NOCs and creating a NOC.

For more information, see [Using the AWS Private CA API to implement Matter certificates](https://docs.aws.amazon.com/privateca/latest/userguide/API-CBR-intro.html) in the AWS Private Certificate Authority documentation.

### CRL Revocation Support (Matter version 1.2 and later)
<a name="crl-revocation-support--matter-version-1.2-and-later-.f55c3ebb-67c2-5109-8aea-78e2e261f831"></a>

Matter version 1.2 introduced Device Attestation Certificate (DAC) revocation using Certificate Revocation Lists (CRLs). When enabling CRL revocation for CAs that issue Matter certificates, set `OmitExtension` to `true` in the `CrlConfiguration` object within the `CrlDistributionPointExtensionConfiguration` structure. In Matter, the CRL Distribution Point (CDP) URI is not embedded in certificates but is instead fetched from the Matter Distributed Compliance Ledger (DCL). You must upload the CDP URI to the Matter DCL for discovery during DAC validation.

### Infrastructure for Matter
<a name="infrastructure-for-matter.3642cc2c-4103-5d01-9653-80093622d00e"></a>

AWS provides an example that demonstrates the use of [AWS Cloud Development Kit (AWS CDK)](https://docs.aws.amazon.com/cdk/v2/guide/home.html) to set up PKI infrastructure for Matter. You use AWS Private CA to meet the requirements of the Matter PKI CP. For more information, see [Matter PKI CDK project](https://github.com/aws-samples/aws-private-ca-matter-infrastructure/) on GitHub.

### Java samples
<a name="java-samples.0b9b547a-f185-5439-8360-dc2949d3707b"></a>

AWS Private CA provides Java samples for creating Matter-compliant Product Attestation Authority (PAA) certificates, Product Attestation Intermediate (PAI) certificates, and Device Attestation Certificates (DACs). For more information, see [Using the AWS Private CA API to implement the Matter standard (Java examples)](https://docs.aws.amazon.com/privateca/latest/userguide/API-CBR-intro.html) in the AWS Private Certificate Authority documentation.

### Guide for Matter PKI compliance
<a name="guide-for-matter-pki-compliance.36678f4b-715a-5e1d-acd4-0f1dbfec6b50"></a>

This [Matter PKI Compliance Guide](https://d1.awsstatic.com/whitepapers/compliance/matter-pki-compliance-guide.pdf) explains how to implement and demonstrate compliance with the CSA Matter PKI CP requirements. It provides information about how you can use to AWS Private CA to create and operate Matter-compliant Certificate Authorities (CAs).

## Managed integrations with AWS IoT Device Management
<a name="aws-iot-device-management-managed-integrations"></a>

[AWS IoT Device Management](https://docs.aws.amazon.com/iot/latest/developerguide/iot-thing-management.html) includes the managed integrations feature, which provides a unified interface for onboarding and managing diverse IoT devices regardless of connection type (direct, hub-based, or cloud-to-cloud).

The following are key capabilities relevant to Matter:
+ Device SDKs supporting ZigBee, Z-Wave, Matter, and Wi-Fi protocols
+ More than 80 device data model templates based on the AWS implementation of the Matter data model standard
+ Partner-built cloud-to-cloud (C2C) connectors
+ Unified device control across multiple brands and protocols
+ Available in Canada (Central), Europe (Ireland), and Middle East (UAE) regions

For more information, see [What is managed integrations for AWS IoT Device Management?](https://docs.aws.amazon.com/iot-mi/latest/devguide/what-is-managedintegrations.html)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
