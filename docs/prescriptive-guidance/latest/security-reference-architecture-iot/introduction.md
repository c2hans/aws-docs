---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/security-reference-architecture-iot/introduction.html
---

# AWS Security Reference Architecture (AWS SRA) – Internet of Things (IoT)
<a name="introduction"></a>

*Avik Mukherjee, Amazon Web Services*

|  |
| --- |
| Influence the future of the AWS Security Reference Architecture (AWS SRA) by taking a [short survey](https://amazonmr.au1.qualtrics.com/jfe/form/SV_e3XI1t37KMHU2ua). |

[Internet of Things (IoT)](https://aws.amazon.com/what-is/iot/) refers to the collective network of connected devices and the technology that facilitates communication among devices and between devices and the cloud. IoT implementations pose unique considerations that don't apply to traditional IT deployments. There are three types of IoT implementations: consumer IoT deployments, industrial IoT (IIoT) deployments, and operational technology (OT) deployments. Each of these implementations has a distinct set of security requirements.
+ Consumer IoT solution deployments, such as robotic vacuums and other consumer IoT devices, use AWS to handle scale and spikes. These implementations can introduce a new classification of security considerations to address. These security considerations and challenges include, but aren't limited to:
  + Difficulty in managing and securing a wide range of device types at scale
  + Constrained resources such as compute, storage, and network, which limit the availability of robust security features
  + The possible lack of automated update and patching mechanisms
+ IIoT solution deployments include implementations by automotive, pharmaceutical, and other manufacturing companies that use [AWS IoT SiteWise](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/what-is-sitewise.html). These implementations can optimize production processes, reduce costs, and provide a better experience for your customers. However, there are unique security considerations that stem from integration with OT systems, real-time operations, and physical processes.
+ IoT deployments that are based on OT or supervisory control and data acquisition (SCADA), such as those adopted by mining, energy, and utilities companies, use various AWS IoT services to improve operational efficiencies and reduce operational cost. These implementations pose additional challenges associated with secure OT and IT convergence. These involve safety-critical systems, proprietary and often legacy industrial protocols, and diverse operating environments.

**Note**
This guidance focuses on security best practices that are relevant to the growing list of use cases that involve IoT, IIoT, and OT-based solutions on AWS. Future updates will iteratively expand the scope and add guidance to include the full array of relevant AWS services and features for this domain.

In this guide:
+ [About the AWS SRA library](about-sra-library.md)
+ [IoT for the AWS SRA](iot-sra.md)
+ [IoT security capabilities](iot-capabilities.md)
+ [Contributors](contributors.md)
+ [Document history](doc-history.md)

## Attachments
<a name="attachments-11475282-b3b8-4c97-8919-9954329a1c00"></a>

To access additional content that is associated with this document, download and unzip the following file:

[attachment.zip](samples/attachment.zip)
