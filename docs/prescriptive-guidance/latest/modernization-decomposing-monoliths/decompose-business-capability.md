---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/modernization-decomposing-monoliths/decompose-business-capability.html
---

# Decompose by business capability
<a name="decompose-business-capability"></a>

You can use your organization's business process or capabilities to decompose a monolith. A *business capability *is what a business does to generate value (for example, sales, customer service, or marketing). Typically, an organization has multiple business capabilities and these vary by sector or industry. Use this pattern if your team has enough insight into your organization's business units and you have subject matter experts (SMEs) for each business unit. The following table explains the advantages and disadvantages of using this pattern.

|
|
| Advantages | Disadvantages |
| --- |--- |
| Generates a stable microservices architecture if the business capabilities are relatively stable.Development teams are cross-functional and organized around delivering business value instead of technical features.Services are loosely coupled. | Application design is tightly coupled with the business model.Requires an in-depth understanding of the overall business, because it can be difficult to identify business capabilities and services. |

In the following diagram, an insurance monolith is decomposed into four microservices based on business capabilities.

![Decompose by business capability pattern](http://docs.aws.amazon.com/prescriptive-guidance/latest/modernization-decomposing-monoliths/images/guide-img/8e9fa68d-7532-4c4b-8c7b-74bc6afdb7b9/images/52518157-f36e-4cfc-bd31-b669586c3ecb.png)
