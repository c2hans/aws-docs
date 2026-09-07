---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/mainframe-decomposition-aws-transform/decomposition-overview.html
---

# Understanding application decomposition
<a name="decomposition-overview"></a>

To modernize your legacy applications, you must first understand how to break them down effectively. This process is known as *decomposition* and uses *seeds*. Seeds are essential components that domain experts identify to help group related application elements logically. For example, seeds such as job names or program names serve as reference points to organize a monolithic system into meaningful categories based on your chosen decomposition strategy. Decomposition is closely connected to migration wave planning, which is discussed [later in this guide](migration-waves.md).

The following diagram shows the high-level process of generative AI-assisted decomposition and migration wave planning provided by AWS Transform.

![Generative AI-assisted decomposition and migration planning with AWS Transform.](https://docs.aws.amazon.com/prescriptive-guidance/latest/mainframe-decomposition-aws-transform/images/guide-img/b2468f31-0c9f-4fc4-9a0f-816b3ed5739c/images/aec68162-b847-4797-a2ed-827fba04b6a9.png)

In this workflow:

1. AWS Transform uses application artifacts and user-provided seeds to analyze and decompose existing applications.

1. Through this analysis, AWS Transform breaks down applications into smaller components.

1. It also identifies elements that are shared across multiple applications.

1. The outcome of this process delivers decomposed application components along with recommended wave plans, which enable organizations to structure their cloud migration project effectively.

Before we explore seed identification, let's examine the main approaches to application decomposition. There are seven key strategies:
+ **Microservices architectures** have become increasingly popular in modern application design. This approach breaks down applications into smaller, independent services that communicate through APIs. For example, consider a credit card processing system. Instead of creating a single monolithic application, you implement separate services for payment authorization, fraud detection, transaction history, card management, and rewards processing. Each service operates independently, which simplifies updates and scaling efforts.
+ **Domain-driven design (DDD)** takes a business-first approach. Using the previous credit card system example, you organize the application into logical business domains such as customer management (user profiles and preferences), billing (statements and payments), risk management (credit scoring and fraud detection), and a rewards domain (points calculations and redemptions).
+ The **strangler fig pattern** offers a more gradual approach to modernization. Instead of attempting a complete overhaul, you methodically replace pieces of the legacy system. In a credit card system, you might start by moving customer management, then migrate fraud detection to a new service, and finally move the transaction processing system. During this gradual modernization, you keep the original system running until you complete the migration.
+ **Service-layer separation** focuses on creating clear boundaries between different application layers. For example, you might separate a credit card application into three layers: the presentation layer (customer portal and mobile interfaces), the business logic layer (payment processing rules and credit calculations), and the data layer (transactions and customer information storage).
+ **Feature-based decomposition** organizes the system around distinct feature sets. In a credit card example, this might include card application processing, payment processing, dispute resolution, rewards management, and statement generation. Each feature would have its own module with clear boundaries.
+ **Database decomposition** addresses the data layer specifically. Instead of using one massive database for the entire system, you split it based on function. A credit card system might have separate databases for customer profiles, transaction records, fraud detection patterns, and rewards data. Each database would be owned by its respective service.
+ **Event-driven architectures** structure the application around business events and their flows. In a credit card system, this creates a chain of events: A card swipe triggers an authorization event, which triggers a fraud check, which might trigger rewards calculations, and so on.
