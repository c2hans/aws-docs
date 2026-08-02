---
source_url: https://docs.aws.amazon.com/whitepapers/latest/cross-domain-solutions/what-is-a-cross-domain-solution.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# What is a Cross-Domain Solution?
<a name="what-is-a-cross-domain-solution"></a>

 The Committee on National Security Systems (CNSS) defines a CDS as a form of controlled interface that enables manual or automatic access or transfer of information between different security domains. We discuss two CDS types in this whitepaper: a one-way transfer (OWT) device, and a multi-domain data guard.

## One-Way Transfer Device
<a name="one-way-transfer-device"></a>

 An OWT device allows data to flow in a single direction from one security domain to another. A common implementation of an OWT device uses a single strand of fiber-optic cable. To ensure data flows only in one direction, the OWT uses a single optical transmitter. The optical transmitter is placed on only one end of the fiber optic cable (for example, the data producer). The optical receiver is placed on the opposite end (for example, the data consumer). Because they only transfer data in one direction, OWT devices are often referred to as diodes, like the semiconductors of the same name.

## Multidomain Data Guard
<a name="multidomain-data-guard"></a>

 A multidomain data guard is a specialized system that enables bidirectional data flow between security domains. A common implementation of a multidomain data guard is a single server running a trusted, hardened multi-level operating system with multiple network interface cards (NICs). Each NIC provides a physical demarcation for a single security domain. The multidomain data guard inspects all data transmitted between domains to ensure that the data remains in compliance with a unique rule set that is specific to the guard’s deployment.

## Traditional Deployment
<a name="traditional-deployment"></a>

 Figure 1 shows a traditional cross-domain solution deployment between two security domains. Security Domain A is connected to Security Domain B using a CDS. If the CDS is an OWT device, resources deployed in Network A can communicate to resources deployed in Network B by sending data through the CDS. If instead, the CDS is a multidomain data guard, resources in either security domain can communicate with the other security domain by sending data through the CDS. In the following example, the CDS is administrated and physically located within the protections of Security Domain B.

![Traditional cross-domain solution deployment between two security domains](http://docs.aws.amazon.com/whitepapers/latest/cross-domain-solutions/images/traditional-cross-domain-solution-deployment.png)

 *Figure 1: Traditional CDS deployment*
