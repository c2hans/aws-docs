---
source_url: https://docs.aws.amazon.com/whitepapers/latest/public-sector-cloud-transformation/selecting-the-right-cloud-for-workloads-differences-between-public-private-and-hybrid.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Selecting the right cloud for workloads – differences between public, private, and hybrid
<a name="selecting-the-right-cloud-for-workloads-differences-between-public-private-and-hybrid"></a>

With the adoption of cloud computing at scale globally, three main cloud models appear: [*private*, *public*, and *hybrid*](https://www.thinksys.com/cloud/private-vs-public-vs-hybrid-cloud/) clouds. The following sections explore which models are the most suitable for which workloads.

## The AWS public cloud
<a name="the-aws-public-cloud"></a>

In the public cloud space, AWS provides services such as the [Amazon Elastic Compute Cloud](https://aws.amazon.com/ec2/) (Amazon EC2), which provides infrastructure and services over the public internet and are hosted at an identified AWS Region (for example, [Canada Central](https://aws.amazon.com/about-aws/whats-new/2020/03/aws-canada-central-region-adds-third-availability-zone/)). Although the infrastructure and services are provisioned from a remote location, the customer has no control and limited visibility over where the service is hosted. But they can use those services anytime anywhere as needed. The AWS public cloud offers advantages such as low cost of ownership, automated deployments, scalability, security, recovery and reliability. AWS public cloud is well-suited for the following:
+  Data storage
+  Data Archival
+  Application Hosting
+  Latency intolerant or mission critical web tiers
+  On-demand hosting for microsite and application
+  Auto-scaling environment for large applications

## The private cloud
<a name="the-private-cloud"></a>

A private cloud, as the name suggests, is cloud infrastructure for use exclusively by a single organization. The cloud is owned, managed and operated exclusively by the organization, by a third-party vendor, or both. In this cloud model, the infrastructure is provisioned on premises using a virtualization layer (for example, VMware). Private cloud environments offer greater configurability support to any application, and support those legacy applications that suffer from performance issues in the public cloud.

While the private cloud offers the greatest level of control and security, it demands that the organization purchase and maintain the entire infrastructure and acquire and retain the skill to do so. This makes the private cloud significantly more expensive. Choosing a private cloud makes sense for:
+  Strict security, latency, regulatory and data privacy levels not met by the public cloud.
+  Organizations that are highly regulated and need data hosted privately and securely.
+  Organizations that are large enough to support the costs.
+  Organizations that need high-performance access to a file system, such as media companies.
+  Hosting applications that have predictable usage patterns and demand low storage costs.
+  Organizations that demand greater adaptability, configurability, and flexibility.
+  Hosting business-critical data and applications.

In the private cloud space, AWS provides the [Amazon Virtual Private Cloud](https://aws.amazon.com/vpc/) (Amazon VPC).

## The hybrid cloud
<a name="the-hybrid-cloud"></a>

When an organization wants to leverage the cloud both for its efficiency and cost saving but also wants on-site security, privacy, and control, it looks to the hybrid cloud, which almost serves as a midway point between the public and private clouds. The hybrid cloud uses a combination of at least one private and one public cloud. A hybrid cloud can also consist of multiple private and public clouds and may use many active servers, physical or virtualized, which are not a part of the private cloud. With the hybrid cloud, organizations can keep each business aspect in the most efficient cloud format possible. However, with the hybrid cloud, organizations have to manage multiple security platforms and aspects and also ensure that all the cloud properties can communicate seamlessly with one another.

 A hybrid cloud is best suited for:
+  Large organizations that want the flexibility and scalability as offered by the public cloud.
+  Organizations that offer services for vertical markets- customer interactions can be hosted in the public cloud while company data can be hosted in the private cloud.
+  Organizations that demand greater operational flexibility and scalability. For them, mission critical data can be hosted on the private cloud and application development and testing can take place in the public cloud.

Given today’s dynamic and increasingly complex business environment, organizations have to constantly reevaluate their cloud infrastructure, whether public, private, or hybrid, to ensure that the cloud delivers results. Because there are different security and management demands for each of these cloud models, organizations must ensure that they select their application candidates for the cloud wisely so that they can foster innovation and improve agility by leveraging their IT resources optimally.
