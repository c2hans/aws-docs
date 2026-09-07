---
source_url: https://docs.aws.amazon.com/whitepapers/latest/next-generation-oss/data-unification.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Data Unification
<a name="data-unification"></a>

 An OSS Architecture on AWS enables telecommunication providers to consolidate their OSS and BSS stacks, allowing for reduction of the data duplication inherent to legacy architectures. For example, traditional, on-premise architecture required a network inventory to be copied across the entire stack, which often existed in hundreds of systems. Following the best practices and architecture defined in this document, you can consolidate the Inventory Management (IM) solution and have a consumers-based model, allowing you to develop applications without duplicating that data. With each duplication coming at a cost, this reduces your overall solution costs. AWS services provide the flexibility and scale to develop your OSS & BSS applications. The following figure illustrates the idea behind data unification:

![Diagram showing Data Unification – Telco Data Lake](https://docs.aws.amazon.com/whitepapers/latest/next-generation-oss/images/data-unification-telco-data-lake.png)

 In this figure, the concept of Telco Data Lake is introduced. AWS enables you to unify your configuration, performance, and inventory data. This improves your overall operational efficiency, reduces your costs, and enables you to innovate faster. For example, a BSS Analytics solution may require information on the network availability to enable a service request requiring additional QoS at additional costs. That same information may also be used by the Service Assurance solution to build a prediction model supporting network optimization. AWS services allow you to consolidate that information, scale it, and govern its access.

 Moreover, with the advent of 5G networks, the classical division between OSS and BSS is blurred. The mechanisms to monetize and configure the network now need to happen in seconds, dynamically, and automatically. To realize the benefits of 5G, the OSS and BSS architectures should align with data unification concepts.
