---
source_url: https://docs.aws.amazon.com/whitepapers/latest/next-generation-oss/next-generation-oss.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Next-Generation OSS with AWS
<a name="next-generation-oss"></a>

Publication date: **September 21, 2021** ([Document history](document-revisions.md))

 An Operations Support System (OSS) is key to enabling Communication Service Providers’ digital transformation journey. Building OSS applications on Amazon Web Services (AWS) enables operational efficiency, cost reduction, elasticity, and innovation. This whitepaper outlines the best practices for developing OSS applications on the AWS Cloud platform, and offers reference architectures to guide organizations in the delivery of OSS solutions spanning domain management, service assurance, service fulfillment, service orchestration, and network analytics.

## Introduction
<a name="introduction"></a>

Communication Service Providers (CSPs) are constantly looking for ways to improve the efficiency of their network operations, reduce their time to market and their operating costs, and adapt to technological evolution. CSPs view their network as an array of network components and network services no longer separated by arbitrary functional lines. CSPs require an operational agility that enables forthcoming opportunities such as Mobile Virtual Network Operator (MVNO), business plans for new network slices (for several use cases like IoT), consumers application (such as ultra-low latency gaming), enterprise application (such as private network), and virtual reality (VR) and augmented reality (AR) business-to-consumer applications (which are unlocked by the introduction of 5G technology).

CSPs are looking for OSS to enable operational agility, and want an OSS that informs on what is being serviced and where, what is being provisioned and where, and how their entire operations perform, predict faults, and self-heal. CSPs want an OSS that allows them to programmatically deploy new network services and functions and have them readily available, and to dynamically reconfigure their network while reducing the complexity of their OSS stack.

The traditional view of an OSS stack that is comprised of multiple independent and functionally-separated network management functions doesn’t match the dynamic behavior of Network Function Virtualization (NFV) and doesn’t take advantage of the adaptability that the NFV cloud architecture enables. CSPs OSS solutions need to evolve with the network.

This whitepaper describes the benefits of OSS on AWS. It includes an OSS reference architecture, an overview of OSS functions and requirements based on characterizing the network OSS manages, operational characteristics, use cases, and best practices for architecting OSS on AWS (which includes high-availability, scalability, security, performance, and operational excellence). Information contained in this document will enable you to develop a next-generation OSS solution on AWS, which will provide a cost-efficient and agile path to CSPs in their digital transformation journey to becoming Digital Service Providers (DSPs).
