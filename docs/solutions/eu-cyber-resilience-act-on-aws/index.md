---
source_url: https://docs.aws.amazon.com/solutions/eu-cyber-resilience-act-on-aws/index.html
---

---
title: 'Guidance for EU Cyber Resilience Act on AWS'
canonical_url: https://docs.aws.amazon.com/solutions/eu-cyber-resilience-act-on-aws/
source: aws-documentation
generated_on: 2026-10-08
---

# Guidance for EU Cyber Resilience Act on AWS

## Overview

This Guidance demonstrates how to secure IoT device fleets throughout their lifecycle while meeting EU Cyber Resilience Act (CRA) compliance requirements through automated certificate management, threat detection, and incident reporting. IoT devices receive secure x.509 certificates during manufacturing and store them in their Trusted Platform Module, enabling automatic provisioning on first connection. AWS IoT Device Management maintains device security over the required 5-year minimum support period through secure over-the-air firmware updates, while AWS IoT Device Defender continuously monitors for threats and automatically rotates compromised certificates. Security events are consolidated in Amazon CloudWatch with 10+ year retention for EU CRA auditing, and severe cybersecurity incidents are automatically reported to ENISA and national CSIRTs through the EU's designated reporting platform. You can automate IoT security operations from device provisioning through decommissioning while maintaining continuous EU CRA compliance, reducing manual security management overhead and accelerating incident response.

## Benefits

### Achieve EU regulatory compliance efficiently

Deploy a comprehensive IoT security architecture that satisfies EU Cyber Resilience Act requirements including five-year device support, automated incident reporting to ENISA, and hardware backed authentication with minimal operational overhead.

### Automate security across device lifecycles

Streamline device provisioning, certificate management, and firmware updates with automated workflows that reduce manual errors while maintaining continuous security monitoring and threat detection across your entire IoT fleet.

### Accelerate incident response with intelligence

Detect security anomalies in near real-time and trigger automated remediation workflows including certificate rotation and threat investigation, reducing exposure windows while maintaining comprehensive audit trails for regulatory compliance.

## How it works

These technical details feature an architecture diagram to illustrate how to effectively use this solution. The architecture diagram shows the key components and their interactions, providing an overview of the architecture's structure and functionality step-by-step.

[Download the architecture diagram](https://d1.awsstatic.com/onedam/marketing-channels/website/aws/en_US/solutions/approved/documents/architecture-diagrams/eu-cyber-resilience-act-on-aws.pdf)

![Architecture diagram](/images/solutions/eu-cyber-resilience-act-on-aws/images/eu-cyber-resilience-act-on-aws-1.png)

1. **Step 1**: A subordinate CA is created in AWS Private Certificate Authority (PCA) with a certificate issued and signed by the offline Root CA.
1. **Step 2**: IoT devices are provisioned with x.509 operational certificates from AWS PCA during manufacturing, securely storing them in their Trusted Platform Module (TPM).
1. **Step 3**: On first connection with an unregistered certificate, an AWS IoT Core Rule invokes a AWS Lambda function that queries Amazon DynamoDB, validates the certificate via AWS PCA OCSP, creates IoT Thing and Policy resources, activates the certificate, enabling the device to establish MQTT connectivity.
1. **Step 4**: Server-side encryption at rest, managed by AWS Key Management Service (KMS), is enabled across all services.
1. **Step 5**: AWS IoT Device Management can manage the device lifecycle through the required 5-year minimum support period. This includes maintaining device security through secure over-the-air (OTA) updates with signed firmware with AWS IoT Jobs and Fleet Indexing, and tracking software states to maintain version control with AWS IoT Software Package Catalog.
1. **Step 6**: AWS IoT Device Defender publishes findings from both audit checks and anomaly detection (authorization failures, traffic patterns) to Amazon SNS, triggering AWS Step Functions workflows. For certificate findings, the workflow orchestrates rotation via AWS IoT Jobs, where devices generate CSRs, receive AWS PCA-signed certificates, and confirm installation before old certificate revocation.
1. **Step 7**: The findings from AWS IoT Device Defender are also sent to AWS Security Hub which can be consumed from a Security Operations Center (SOC).
1. **Step 8**: AWS Security Hub feeds vulnerability data to Amazon Detective, enabling automated threat investigation and forensic analysis of security incidents.
1. **Step 9**: Amazon CloudWatch alerts propagate to Amazon EventBridge, enabling the triggering of AWS Step Functions workflows for remediation.
1. **Step 10**: Amazon Cloud Watch consolidates all security documentation events, vulnerabilities, incidents, and investigations—into a unified compliance repository with 10+ year retention for EU CRA auditing.
1. **Step 11**: Amazon EventBridge with AWS Lambda functions reports severe cybersecurity incidents and actively exploited vulnerabilities to ENISA/CSIRT through the EU's designated single reporting platform. Cybersecurity partners analyze SBOM files stored in AWS IoT Device Management, identify vulnerabilities, and securely deliver detailed reports to authorized Amazon S3 buckets.
[Read usage guidelines](/solutions/guidance-disclaimers/)
