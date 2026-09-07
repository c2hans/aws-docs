---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/strategy-application-portfolio-assessment-migration/methodology-approach.html
---

# Methodology and approach
<a name="methodology-approach"></a>

The strategic approach to application portfolio assessment is to establish a series of stages that will run in parallel to other program workstreams. These stages will progressively collect and analyze application and infrastructure data while pivoting between two main levels: portfolio level and application level.

## Portfolio-level assessment
<a name="portfolio-level-assessment"></a>

The* portfolio-level assessment* focuses on collecting and analyzing general data from applications and infrastructure to obtain a high-level view of the entire portfolio. This view includes high-level technical and business attributes such as application names, environment, product versions, business and technical criticality, and performance and utilization metrics. This is key to understanding priorities and the scope of the program, creating high-confidence plans, managing the portfolio, and informing the business case.

## Application-level assessment
<a name="application-level-assessment"></a>

The *application-level assessment* focuses on the architecture and technology of each application. It includes creating AWS designs and defining migration strategies and patterns that support the move to the cloud and further optimization. This type of assessment is typically time consuming, and it's approached in a sequence of smaller chunks, aligned to migration waves, throughout the project lifecycle.

As the migration date approaches, detailed application information, down to the technology level, is required for informing security, operations, infrastructure deployment, and migration activities. Therefore, detailed application-level discovery is targeted at those applications that are candidates to be migrated in the near-term. Detailed discovery is then performed for the next group of applications, in a slightly overlapped sequence, throughout the program lifecycle and in parallel to ongoing migrations.

The following diagram shows the key activities for each stage of assessment and how they pivot between *portfolio-level* assessment (identification of sources of data, high-level discovery, initial inventory, prioritization, and directional business case) and *application-level* assessment (detailed discovery, AWS design, and migration strategy). Portfolio-level and application-level assessments represent the breadth and depth of information required.

![Timeline for discovery, application assessment, migration planning, and continuous improvement.](https://docs.aws.amazon.com/prescriptive-guidance/latest/strategy-application-portfolio-assessment-migration/images/guide-img/7c9d894c-c8ca-4901-8b62-e1a8c08d1940/images/75c04ac9-0103-4877-af7d-5fcd7fe2a71d.png)
