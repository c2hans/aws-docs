---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/strategy-application-portfolio-assessment-migration/introduction.html
---

# Application portfolio assessment strategy for AWS Cloud migration
<a name="introduction"></a>

*German Goncalves and Mark Berner, Amazon Web Services*

Migrating applications and associated infrastructure to the cloud, requires a strategic and methodical approach to progressively discover and analyze IT assets. These analyses are then used to create high-confidence migration wave plans for implementing migration programs and business transformation. This Amazon Web Services (AWS) Prescriptive Guidance strategy will help you understand the key stages to successfully assess your application portfolio, including the following:
+ Identifying key stakeholders and existing sources of data
+ Implementing automated discovery tooling
+ Progressively enriching the application portfolio dataset
+ Prioritizing applications
+ Establishing a migration wave plan
+ Continuously assessing the portfolio

This strategy is complemented by an [Application portfolio assessment guide for AWS Cloud migration](https://docs.aws.amazon.com/prescriptive-guidance/latest/application-portfolio-assessment-guide/introduction.html) that contains detailed how-to guidance.

## Overview
<a name="overview"></a>

When planning to migrate and modernize a portfolio of applications, organizations of any size must progressively rediscover and analyze their current IT estate. The proactive and progressive approach of this strategy recognizes that not all data about applications and infrastructure (compute, storage, networks) are required upfront in order to move forward. What at first seems to be a complex endeavor can be separated into smaller steps, with specific outcomes, by applying a defined approach.

At a high-level, *application portfolio assessment*** **is the process of gathering application, infrastructure, and business context data to discover, analyze, and plan** **for moving the portfolio to the cloud. Assessment activities are critical for any business embarking on long-running cloud programs because the nature of that journey involves risk and cost. It is not only  applications that are moving to the cloud, it is the business itself being transformed. Therefore, from deciding to move ahead, to enabling actual migrations, a data-backed analysis is key. The analysis informs the process, reduces risk and cost, aligns business and IT priorities, and accelerates business outcomes.

Application portfolio assessment is typically associated with early stages of migration. This is when there is a strong need for data and analysis to inform the business case and produce initial plans. However, after the early stages, application and infrastructure assessment becomes a continuous and interactive set of activities across the entire lifecycle of long-running programs. The progressive and continuous assessment approach, with varying levels of data quantity and fidelity, enhances the understanding of the portfolio until it is migrated. Then the approach focuses on assessment for further optimization and modernization.

Other migration program activities, such as governance, people and skills, landing zone, security, and operations, have dependencies on the data and analysis resulting from application portfolio assessment. For example, mobilizing a migration program, estimating cost, and producing a business case requires a clear understanding of the application portfolio. Also, platform teams shaping the AWS foundations or extending the current AWS environment require portfolio data to create and implement designs. Migration teams use that same data to develop patterns, establish cutover runbooks, and define migration tooling.

The following diagram shows how the stages of portfolio assessment correspond to the AWS phases of migration. The discovery acceleration and initial planning stage begins in the assess phase, typically during the first five weeks. Prioritized applications assessment, in the sixth and seventh weeks, spans the assess and mobilize phases. The portfolio analysis and migration planning stage happens in weeks 8–14, in the mobilize phase. The continuous assessment and improvement stage happens in the migrate and modernize phase, from week 15 until the end of the migration program. This timeline is indicative. The actual duration of the stages will depend on the overall program organization.

![Activities during the assess, mobilize, and migrate and modernize phases.](http://docs.aws.amazon.com/prescriptive-guidance/latest/strategy-application-portfolio-assessment-migration/images/guide-img/7c9d894c-c8ca-4901-8b62-e1a8c08d1940/images/14259955-53b8-46df-a2ce-30996fbd0c15.png)

Long-term portfolio assessment outcomes, such as maintaining an up-to-date inventory of IT assets and dependencies, remain constant throughout the journey. However, data requirements, specific objectives, and key stakeholders vary at each stage. In this strategy, the portfolio journey is represented as four main stages aligned to data requirements for the portfolio job at hand:

1. **Discovery acceleration and initial planning** – Updating the current understanding of the portfolio, creating a directional business case, establishing base rationalization models for migration, and identifying initial migration candidates

1. **Prioritized applications assessment** – Performing a detailed assessment, initial design, and migration strategy of prioritized applications that can be moved in the short-term to reduce time-to-value by providing migration experience and establishing cloud foundations

1. **Portfolio analysis and migration planning** – Building a complete and up-to-date view of the application portfolio by iteratively enriching the dataset, closing data gaps, evolving the business case, and creating high-confidence migration wave plans

1. **Continuous assessment and improvement** – Enabling migrations at scale by producing detailed application and technology assessments for each migration wave, iterating the migration wave plan, and further assessing migrated workloads for optimization and modernization
