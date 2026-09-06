---
source_url: https://docs.aws.amazon.com/whitepapers/latest/security-at-the-edge/security-at-the-edge.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Security at the Edge: Core Principles
<a name="security-at-the-edge"></a>

Publication date: **September 24, 2021** ([Document history](document-revisions.md))

 Today’s business leaders know that it is critical to ensure the security of their environments, and the security present in traditional cloud networks is extended to workloads at the edge. This whitepaper provides security executives the foundations for implementing a defense in depth security strategy at the edge by addressing three areas of security at the edge:
+  AWS services at AWS edge locations
+  How those services and others can be used to implement the best practices outlined in the design principles of the AWS Well-Architected Framework Security Pillar
+  The security aspects of additional AWS edge services, which customers can use to help secure their edge environments or expand operations into new, previously unsupported environments

 Together, these elements offer core principles for designing a security strategy at the edge, and demonstrate how AWS services can provide a secure environment extending from the core cloud to the edge of the AWS network and out to customer edge devices and endpoints.

## Introduction to edge computing
<a name="introduction-to-edge-computing"></a>

 Security is the top priority at AWS. The high security bar set by AWS services covers customers as they expand their use of AWS services to bring workloads out to the edge to use its growing number of capabilities and applications.

 Edge computing comprises elements of geography and networking, and brings computing closer to the user. Edge takes place at or near the physical location of either the user or the source of the data. By placing computing services close to these locations, the user benefits from faster, more reliable services.

 This paper discusses AWS services that are available to provide a secure environment, from the core cloud to the edge of the AWS network, and out to customer edge devices and endpoints. Many of the AWS services that provide security capabilities to the edge reside at AWS edge locations, or as close to customers’ edge devices and endpoints as necessary. AWS edge locations are a worldwide network of data centers that run with AWS at physical locations directly connected to the expanding AWS global infrastructure.

 AWS edge services provide infrastructure and software that deliver data processing, analysis, and storage as close to the endpoint as necessary. This includes deploying AWS Managed Services, APIs, and tools to locations outside AWS data centers, and even onto customer-owned infrastructure and devices. AWS enables customers to build high-performance applications that rely on the cloud for data processing and storage, but also need to process or store some data close to where it is generated to deliver ultra-low latency, intelligent, real-time responsiveness, and reduce the amount of data transfer.

 Every AWS customer is unique, and “edge” can mean something different to different customers. Edge use cases and technology can range from autonomous vehicles, medical devices, oil rig sensors, industrial robots, nautical GPS, and meteorological devices. Mobile phones and robot vacuums are also examples of edge devices.

 The objective of AWS edge services is to provide consistent capabilities and customer experience from the edge to the cloud. AWS uses the same programming model for the cloud, on-premises infrastructure, and local devices. This gives you the choice of centralized control or de-centralized control, with decentralized implementation. You have access to the same environment to develop, connect, deploy, manage, and secure with the same tools, regardless of where your workloads are located.
