---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/migration-operations-integration/operations-readiness.html
---

# Operations readiness
<a name="operations-readiness"></a>

Workshops are an eﬀective way to understand your current operating model and to deﬁne an AWS operating model.

Operating models on AWS can be structured across three main paradigms: traditional operations, CloudOps, and DevOps. Each model offers distinct approaches to managing cloud operations,

**Traditional operations model**
+ Maintains conventional processes based on IT Infrastructure Library (ITIL)
+ Operates with clear separation between development and operations teams
+ Uses established change management procedures
+ Relies on existing ITSM tools that are integrated with AWS services
+ Suitable for organizations that are in the early stages of cloud adoption
+ Works well with the [rehost](https://docs.aws.amazon.com/prescriptive-guidance/latest/large-migration-guide/migration-strategies.html#rehost) (lift and shift) and [relocate](https://docs.aws.amazon.com/prescriptive-guidance/latest/large-migration-guide/migration-strategies.html#relocate) migration strategies

**CloudOps model**
+ Represents a hybrid approach that combines traditional and cloud-native practices
+ Takes advantage of AWS-specific operational capabilities
+ Implements automated monitoring and management
+ Maintains some traditional controls while adopting cloud practices
+ Ideal for organizations during cloud transformation
+ Aligns well with the [replatform](https://docs.aws.amazon.com/prescriptive-guidance/latest/large-migration-guide/migration-strategies.html#replatform) and [repurchase](https://docs.aws.amazon.com/prescriptive-guidance/latest/large-migration-guide/migration-strategies.html#repurchase) migration strategies
+ Serves as a transitional model during cloud maturity development

**DevOps model**
+ Represents a fully integrated development and operations approach
+ Emphasizes automation and continuous delivery
+ Implements cloud-native practices and tools
+ Features cross-functional teams and collaborative workflows
+ Focuses on rapid iteration and deployment
+ Best suited for the [refactor](https://docs.aws.amazon.com/prescriptive-guidance/latest/large-migration-guide/migration-strategies.html#refactor) (reimagine) migration strategy
+ Represents the most mature cloud operating model

The following diagram illustrates these three models.

![Traditional, CloudOps, and DevOps operations models.](https://docs.aws.amazon.com/prescriptive-guidance/latest/migration-operations-integration/images/guide-img/6545b5e3-3780-4eb8-a195-e92454bb488e/images/5cdac8a6-21b7-4d26-aa6e-d9878ce83645.png)

The choice of operating model should align with your organization's cloud maturity, migration strategy, and business objectives. Organizations often evolve through these models as they progress in their cloud journey—starting with traditional operations and gradually moving toward DevOps as their cloud capabilities mature.

The following diagram shows suggested operating models based on the [7Rs migration strategies](https://docs.aws.amazon.com/prescriptive-guidance/latest/large-migration-guide/migration-strategies.html) and approach to AWS.

![Operating models mapped to 7 migration strategies.](https://docs.aws.amazon.com/prescriptive-guidance/latest/migration-operations-integration/images/guide-img/6545b5e3-3780-4eb8-a195-e92454bb488e/images/8b0fd0e2-8c2c-4296-b011-8dbda1005e8b.png)
