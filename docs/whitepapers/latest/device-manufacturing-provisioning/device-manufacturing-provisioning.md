---
source_url: https://docs.aws.amazon.com/whitepapers/latest/device-manufacturing-provisioning/device-manufacturing-provisioning.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Device Manufacturing and Provisioning with X.509 Certificates in AWS IoT Core
<a name="device-manufacturing-provisioning"></a>

Publication date: **November 17, 2022** ([Document revisions](document-revisions.md))

## Abstract
<a name="abstract"></a>

 This whitepaper focuses on onboarding Internet of Things (IoT) devices in [AWS IoT Core](https://aws.amazon.com/iot-core/) using unique identities. It covers the different options, challenges, and considerations for manufacturing and provisioning unique [X.509 certificates](https://docs.oracle.com/javase/8/docs/technotes/guides/security/cert3.html) and private keys into devices for certificate-based mutual authentication.

 The whitepaper provides device makers with guidance on the appropriate AWS IoT provisioning options, based on the capabilities of their device and manufacturing process. It is not intended to cover Sigv4 and Custom Authorizer authentication methods.

 This whitepaper is intended for technical architects, IoT cloud engineers, IoT security architects, and embedded engineers. This whitepaper assumes that the reader understands fundamental [Public Key Infrastructure](https://en.wikipedia.org/wiki/Public_key_infrastructure) (PKI) and [Transport Layer Security](https://en.wikipedia.org/wiki/Transport_Layer_Security) (TLS) concepts and terminology.

## Are you Well-Architected?
<a name="well-architected"></a>

The [AWS Well-Architected Framework](https://aws.amazon.com/architecture/well-architected/) helps you understand the pros and cons of the decisions you make when building systems in the cloud. The six pillars of the Framework allow you to learn architectural best practices for designing and operating reliable, secure, efficient, cost-effective, and sustainable systems. Using the [AWS Well-Architected Tool](https://aws.amazon.com/well-architected-tool/), available at no charge in the [AWS Management Console](https://console.aws.amazon.com/wellarchitected), you can review your workloads against these best practices by answering a set of questions for each pillar.

For more expert guidance and best practices for your cloud architecture—reference architecture deployments, diagrams, and whitepapers, refer to the [AWS Architecture Center](https://aws.amazon.com/architecture/).

## Introduction
<a name="introduction"></a>

 During the different phases of IoT device development and manufacturing, the way that these unique identities are provisioned and onboarded to AWS IoT Core can differ. Device makers are faced with a number of considerations during the lifecycle of an IoT device, including:
+  Using a customer-owned Certificate Authority (CA), a third-party CA, or an AWS IoT created CA
+  Using a hardware security module, such as a secure element or trusted platform module (TPM)
+  Cloud resources needed to support the device provisioning process
+  Device-level logic to implement onboarding procedures

 This whitepaper explains the complexities of the device manufacturing supply chain, and assists device makers with recommendations based on the capabilities of their device, limitations of their manufacturing process, and device onboarding requirements of a service operator.
