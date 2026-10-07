---
source_url: https://docs.aws.amazon.com/solutions/securing-operational-technology-assets-with-dragos-on-aws/index.html
---

---
title: 'Guidance for Securing Operational Technology (OT) Assets with Dragos on AWS'
canonical_url: https://docs.aws.amazon.com/solutions/securing-operational-technology-assets-with-dragos-on-aws/
source: aws-documentation
generated_on: 2026-10-06
---

# Guidance for Securing Operational Technology (OT) Assets with Dragos on AWS

Reduce attack surface and vulnerabilities with a cybersecurity solution to protect your critical infrastructure

## Overview

This Guidance demonstrates how to monitor the connectivity between operational technology (OT), IT, or external networks to ensure the security and integrity of critical industrial systems. It provides centralized monitoring and threat management for connected assets, enabling you to identify and prioritize risks to your OT environment with a holistic view of your assets and threat detection capabilities. This Guidance also supports auditing and compliance regulations, with its comprehensive monitoring and reporting capabilities. It generates detailed reports on asset inventory, vulnerabilities, security events, and timeline-based auditing of network communications, reducing your security risk while helping you meet compliance requirements.

## Benefits

### Protect critical manufacturing operations

Detect and respond to cybersecurity threats across industrial control systems and manufacturing networks. Gain comprehensive visibility into operational technology environments while maintaining production continuity and safety.

### Unify security across facilities

Consolidate threat detection and incident response across multiple manufacturing sites from a single console. Enable your security teams to monitor and protect distributed operations with consistent policies and centralized analytics.

### Accelerate threat detection and response

Identify security anomalies in near real-time using automated monitoring and machine learning-powered analysis. Reduce investigation time by correlating operational technology and enterprise security events in one unified view.

## How it works

This architecture diagram shows how to use the cybersecurity platform Dragos to secure operational technology (OT) assets at various manufacturing sites.

[Download the architecture diagram](https://d1.awsstatic.com/solutions/guidance/architecture-diagrams/securing-operational-technology-assets-with-dragos-on-aws.pdf)

![Architecture diagram](/images/solutions/securing-operational-technology-assets-with-dragos-on-aws/images/securing-operational-technology-assets-with-dragos-on-aws-1.png)

1. **Step 1**: In the Purdue model for industrial control system (ICS) security, Level 0 refers to the physical process: sensors and actuators, field devices, solenoid valves, and motors. For basic control, Level 1 consists of programmable logic controllers (PLC), distributed control systems (DCS), and safety instrumented systems (SIS) that interface with the electromechanical devices in Level 0.
1. **Step 2**: At Level 2, DCS, Supervisory Control and Data Acquisition (SCADA), and human-machine interfaces (HMIs) provide control and monitoring of the manufacturing process. One or more Dragos sensors collect data from the control system network through a mirror port on an existing network switch on a network traffic access point (TAP).
1. **Step 3**: Level 3 consists of historians, engineering workstations, and other systems that manage manufacturing operations. One or more Dragos sensors collect data from the supervisory network through a mirror port on an existing network switch or network TAP. Level 3.5 denotes the demilitarized zone (DMZ) that separates the corporate network from the industrial control systems (ICS) environment.
1. **Step 4**: The Dragos sensor converts network traffic into lightweight metadata, which is then forwarded to Dragos SiteStore for correlation and processing through an encrypted connection that supports TLS and Internet Protocol Security (IPSec) protocols.
1. **Step 5**: Dragos SiteStore, hosted on Amazon Elastic Kubernetes Service (Amazon EKS), serves as the management and reporting console for the Dragos sensor data. To enable multi-site operational technology (OT) access, this can reside in a separate virtual private cloud (VPC). Dragos SiteStore can also be deployed on-premises depending on your needs.
1. **Step 6**: Dragos CentralStore, residing on Amazon EKS, provides enterprise-scale, multi-site OT visibility, detection, and response. Dragos CentralStore can also be deployed on-premises depending on your needs.
1. **Step 7**: The OT security event data from SiteStore and CentralStore is sent to a security incident and event management system (SIEM) or a security operations center (SOC) that features AWS Security Hub, Amazon GuardDuty, Amazon Macie, and AWS CloudTrail, among other services. Considerations for the security operations center in the cloud provides more context for a SOC function when you operate in the cloud.
1. **Step 8**: Syslog data associated with OT security events can be stored in an Amazon Simple Storage Service (Amazon S3) data lake. The data can be analyzed using Amazon Athena, Amazon OpenSearch Service, and Amazon SageMaker. This data can also be combined with IT security data to provide a centralized view of all OT and IT security events to enable alerting and automatic remediation.
[Read usage guidelines](/solutions/guidance-disclaimers/)
