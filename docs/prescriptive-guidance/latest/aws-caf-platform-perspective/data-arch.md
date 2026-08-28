---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/aws-caf-platform-perspective/data-arch.html
---

# Data architecture
<a name="data-arch"></a>

**Design and evolve a fit-for-purpose data and analytics architecture.**

A [well-designed](https://docs.aws.amazon.com/wellarchitected/latest/analytics-lens/welcome.html) data and analytics [architecture](https://aws.amazon.com/architecture/analytics-big-data/?cards-all.sort-by=item.additionalFields.sortDate&cards-all.sort-order=desc&awsf.content-type=*all&awsf.methodology=*all) is essential to gain actionable insights. By designing and evolving a fit-for-purpose data and analytics architecture, organizations reduce complexity, cost, and technical debt while unlocking valuable insights from their ever-growing data volumes. By aligning with AWS CAF principles, businesses can create a data architecture that seamlessly integrates with their existing platform. This alignment  positions organizations to capitalize on the advantages offered by modern data processing and analytics technologies.

The data and analytics architecture is the blueprint of an organization's capabilities to derive value out of data. It helps the organization gain new business insights and is a catalyst for business growth. To support business needs, a modern data architecture should align with short-term and long-term business goals and be unique to the organization's cultural and contextual requirements. In today's world, the successful implementation and adoption of a data and analytics architecture are based on the principle of enabling the right data at the right time to the right consumer.

This is achieved by planning and organizing how an organization's data assets are modeled, physically or logically, how the data is secured, and how these data models interact with one another to address business problems and to derive unknown patterns and generate insights.

## Start
<a name="data-arch-start"></a>

### Define overarching capability
<a name="define-overarching-capability.e16fb3b6-f490-5242-8eee-e2ab8b014e7f"></a>

In the current business environment, it is critical for the modern data analytics platform to derive value from data to support various domains in the organization. Instead of adopting a single data architecture approach, [modern data architecture](https://aws.amazon.com/big-data/datalakes-and-analytics/modern-data-architecture/) should include toolsets and patterns that are purpose-built and optimized for specific use cases. The architecture should be able to evolve and includes basic building blocks, such as scalable data lakes, purpose-built analytics services, unified data access, and unified governance.

### Organize data zones
<a name="organize-data-zones.040b6686-aab2-5bb9-9242-24c91404a94b"></a>

How the data is organized and stored for quick and easy access is a critical aspect of data architecture. This can be achieved by setting up custom data zones within a data lake. The data zones are categorized as follows:
+ Raw data that's collected from heterogeneous sources
+ Curated and transformed data to support the analytical needs of each domain
+ Use case or product-based data marts for reporting needs
+ Externally exposed data with security and compliance controls

### Plan for agility and democratization of data
<a name="plan-for-agility-and-democratization-of-data.45c787ba-9be1-59c0-b2f5-99ad5f900c26"></a>

The effectiveness of an analytics platform depends on the speed of provisioning data as well as democratizing the provisioned data for consumption. Data provisioning agility is achieved by the ability of the data architecture to procure and process data in a variety of ways―such as real-time, near-real time, batch, micro-batch, or hybrid―based on the use case. Data democratization is achieved by defining data sharing and access control workflows that are monitored by data stewards. Implementing a data marketplace is one of the enablers for democratizing data.

### Define secure data delivery
<a name="define-secure-data-delivery.ac56ab12-4218-5b4d-bf78-23568863a9e6"></a>

A modern data architecture is a fortress to the outside world in security but allows easy access to employees or data users, as defined by their job functions, and adheres to compliance restrictions such as the [Health Insurance Portability and Accountability Act (HIPAA)](https://aws.amazon.com/compliance/hipaa-compliance/), personally identifiable information (PII), [General Data Protection Regulation (GDPR)](https://aws.amazon.com/compliance/gdpr-center/), and so on. This is achieved by role-based access control (RBAC) and tag-based access control (TBAC) methods. On AWS, tags are used to control access to data to simplify access control management. Do this in alignment with the principles that are outlined in the [AWS CAF Security perspective](https://docs.aws.amazon.com/whitepapers/latest/overview-aws-cloud-adoption-framework/security-perspective.html).

### Plan for cost effectiveness
<a name="plan-for-cost-effectiveness.1c52b255-94b6-50e7-a3e9-022872a91c39"></a>

Traditional data warehouses provide tightly coupled computing and storage with a high cost of resource utilization. A modern architecture decouples computing and storage, and implements tiered storage based on the data lifecycle. For example, on AWS, you can use [Amazon Simple Storage Service (Amazon S3)](https://docs.aws.amazon.com/AmazonS3/latest/userguide/Welcome.html) to control costs and decouple data storage from compute. [Amazon S3 storage classes](https://aws.amazon.com/s3/storage-classes/) are purpose-built to provide the lowest cost storage for different access patterns. In addition, AWS compute tools (such as [Amazon Athena](https://docs.aws.amazon.com/athena/latest/ug/what-is.html), [AWS Glue](https://docs.aws.amazon.com/glue/latest/dg/what-is-glue.html), [Amazon Redshift](https://docs.aws.amazon.com/redshift/latest/dg/welcome.html), and [Amazon SageMaker Runtime](https://docs.aws.amazon.com/sagemaker/latest/dg/whatis.html)) are serverless, so you don't have to manage infrastructure, and you pay only for what you use.

## Advance
<a name="data-arch-advance"></a>

Modern data architecture could be further enhanced to increase the breadth of data usage―from standard analytics that supports business and operational functions to more complex capabilities that support predictions and insights―and helps support faster decision-making. To achieve this, the architecture supports the capabilities described in the following sections.

### Understand feature engineering
<a name="understand-feature-engineering.eeab727b-2f31-5c44-93e0-2024e75e6c84"></a>

[Feature engineering](https://docs.aws.amazon.com/wellarchitected/latest/machine-learning-lens/feature-engineering.html) uses machine learning and involves setting up feature stores or feature marts. Data science teams create new features (derived attributes) for both supervised and unsupervised learning models and store them in feature marts for simplified transformation and enhanced data accuracy. Enterprises can reuse the features across multiple analytics models, which improves speed to market.

### Plan to denormalize datasets
<a name="plan-to-denormalize-datasets.274563b4-782b-5c7b-8d37-7194de7ec171"></a>

Constructing denormalized datasets or data marts could significantly simplify the datasets for business users by making the required data readily available at a single location and increasing the speed of analytics. If designed carefully, one record could support multiple usage models and reduce the overall development lifecycle. Effective governance of denormalized datasets is also significant for two reasons. Implementing denormalized data could create a large number of redundant datasets, which could become a challenge to manage at scale. In addition, these datasets could be increasingly difficult to repurpose if they aren't modeled correctly.

### Design portability and scalability
<a name="design-portability-and-scalability.24ae1951-daf2-57bd-9ed1-d6d324755a9f"></a>

Large organizations seldom have all their applications and users on a single data platform. Their applications and data stores are typically distributed across legacy on-premises and cloud platforms, making it difficult for analytics teams to mix and merge data. We recommend that you containerize data based on characteristics such as domain, geography, business use cases, and so on. This containerization increases portability between various platforms and applications and supports more effective consumption. Segmenting data into containers and exposing them through APIs helps you scale your data architecture more easily. It enables hybrid, end-to-end data flow and helps on-premises and cloud-based applications work seamlessly.

## Excel
<a name="data-arch-excel"></a>

As a modern analytics architecture evolves within an organization, it is important to manage that change by introducing reusable concepts. These concepts increase durability and adoption while keeping costs in check. Some of the concepts to consider are discussed in the following sections.

### Design a configurable framework
<a name="design-a-configurable-framework.b1c74fa6-c0fe-5d3a-af70-d4921de58a2a"></a>

Organizations often create multiple, complex models to address their unique business needs. These models require the creation of multiple data pipelines and engineered features. Over time, this creates significant redundancy and increases operating costs. Creating a framework that incorporates a set of parameter-driven, configurable base models reduces the development time and operating costs. The analytical engine can implement these configurable models to provide the desired output.

### Plan to build a unified analytical engine
<a name="plan-to-build-a-unified-analytical-engine.df0afe0a-11e6-574c-adaa-65a83f6a62f1"></a>

Business problems are unique and often require custom technologies to address requirements, resulting in multiple analytical engines in an organization. Designing and developing a unified AI-based analytical engine interface that can support multiple programming paradigms simplifies usage and reduces costs.

### Define DataOps
<a name="define-dataops.af9de4b3-99ac-5145-88e1-5dd7738ca554"></a>

Most data professionals spend a significant amount of time performing data operations such as locating the right data, transforming, modeling, and so on. Having agile data operations (DataOps) can greatly enhance the data architecture by breaking down the silos of data engineers, data scientists, data owners, and analysts. DataOps enables better communication between teams, reduces cycle time, and ensures high data quality. Data and analytics architectures have undergone numerous transformations over time because of changing business needs and technological advancements. An organization must strive to develop, implement, and maintain a data and analytics architecture that evolves over time and supports its business.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
