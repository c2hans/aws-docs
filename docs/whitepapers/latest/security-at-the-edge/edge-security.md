---
source_url: https://docs.aws.amazon.com/whitepapers/latest/security-at-the-edge/edge-security.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Security at the edge
<a name="edge-security"></a>

 AWS provides services and features you can use to help you create secure architectures, workloads, and services to elevate your security from edge to cloud. Security at AWS starts with core infrastructure, which is built for the cloud and designed to meet the most stringent security requirements in the world. For example, all data flowing across the AWS global network that interconnects data centers and [Regions](https://aws.amazon.com/about-aws/global-infrastructure/regions_az/) is automatically encrypted at the physical layer before it leaves AWS secured facilities.

 At the edge, AWS offers services that address the different aspects of edge security, including preventive security mechanisms like encryption and access control, continuous monitoring mechanisms like configuration auditing, and physical security like tamper-evident enclosures. Customers that need to store and process data on premises, or in countries where there is no AWS Region, can do so securely with AWS edge services. This capability can help you comply with data handling or data residency requirements.

 AWS Cloud security principles are fundamental and apply regardless of where an organization operates. These principles are discussed in detail in a later section of this whitepaper. AWS offerings combine a high security bar with agility to adapt rapidly as needed. AWS customers working at the edge have access to over 200 fully featured, integrated cloud and device services, many of which have specific edge capabilities.

 AWS services with Points of Presence (PoP) at edge locations — globally scaled and connected through the AWS network backbone — provide a more secure, performant, and available experience. AWS also offers services that run on the edge, which enable you to deliver content. AWS edge services, which provide infrastructure and software that deliver data processing, analysis, and storage at endpoints comprise a comprehensive set of cloud services that support the secure deployment and management of edge devices.

 Security at the edge has the same principles as cloud security. By extending cloud services to the edge, AWS gives you a way to operate safely, with strong security infrastructure and safeguards. AWS-owned infrastructure is monitored 24/7 to help safeguard the confidentiality, integrity, and availability of our customers’ data. Moving cloud workloads to edge devices or endpoints provides you with more control and visibility, and mitigates risk.

**Media and entertainment at the edge**
 The media and entertainment industry provides natural examples of customers who need to focus on securing their content delivery at the edge. For example, [Amazon CloudFront](https://aws.amazon.com/cloudfront/) provides streaming services with low latency, sustained high throughput, lower rebuffering rates, and integration with other AWS services, while also securely distributing content globally. For more information, see [Amazon CloudFront for Media & Entertainment](https://aws.amazon.com/cloudfront/media/).

 A defense in depth model (for example, using multiple independent layers of specialized security controls) provides layers of protection. In addition to the design principles of the [AWS Well-Architected Framework’s Security Pillar](https://docs.aws.amazon.com/wellarchitected/latest/security-pillar/design-principles.html), this paper highlights three aspects of edge protection whose PoP is at AWS edge locations. The three highlighted edge protections that help secure the connection points between the origin infrastructure, edge services, and customer edge devices or applications are:
+  Secure content delivery
+  Network and application layer protection
+  Distributed Denial of Service (DDoS) mitigation

 The design principles also cover the security of edge devices and applications. A comprehensive defense in depth strategy should include services that account for the security of both AWS edge locations, and edge devices and applications.
