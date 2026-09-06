---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/strategy-migration-connect/agile-methods.html
---

# Agile methods to accelerate delivery and innovation
<a name="agile-methods"></a>

We recommend that you use an agile methodology in conjunction with DevOps and CI/CD practices as the underpinnings of your migration to Amazon Connect Customer. These practices become the foundation for a dynamic, user-focused, and experiment-driven approach to customer experience.

If you have a compelling business reason to initially migrate your contact center as is to Connect Customer without adding new features, we still highly recommend adapting an agile approach to enable experimentation and the continuous improvement of the customer experience over time.

Borrowing from [Amazon's business approach to transformation](https://aws.amazon.com/executive-insights/content/digital-transformation-lead-with-culture-enable-with-technology/), we recommend a *think big, start small, go fast* approach. You start by clarifying your business goals and focus areas, and brainstorm with key stakeholders to define and align on key opportunities for innovation.  You then work back from the customer to understand who they are, what they need, and how to improve their experience. From there, you define and prioritize key initiatives to create a minimum lovable product (MLP) that drives business outcomes and provides immediate impact within the initial agile sprint. Establishing an Connect Customer technical foundation and the agile delivery framework during the initial sprint builds the foundation of the customer experience (CX) flywheel, which is depicted in the following diagram.

![Agile delivery framework for contact center migrations](http://docs.aws.amazon.com/prescriptive-guidance/latest/strategy-migration-connect/images/guide-img/c8027e22-fcd9-43b3-b8a7-234ec8eb0644/images/972cefc3-01a4-4959-84dc-119c641e5027.png)

Subsequent sprints are prioritized by working back from customer needs, and organized by additional functionality, additional users and business units, or a combination of the two. The following diagram shows a typical agile sprint process. Underpinning the agile sprint process is change management (CM) activities, ensuring the organization is keeping pace with technology delivery.

![Amazon Connect agile delivery with organizational change management](http://docs.aws.amazon.com/prescriptive-guidance/latest/strategy-migration-connect/images/guide-img/c8027e22-fcd9-43b3-b8a7-234ec8eb0644/images/65f3b058-532f-4656-b4e9-a9b5204822ca.png)

After teams and stakeholders agree on a multi-phase migration and transformation plan (as discussed in the following sections), the initial agile sprint establishes the foundation of an Connect Customer contact center**,** which provides a common baseline of capability, prepares the flywheel mechanism for accelerating transformation, and defines the mechanisms for continuous improvement. The key elements of this foundation include:
+ Deploying Connect Customer on a secure, high-performing, resilient, and efficient AWS infrastructure.
+ Configuring contact flows that define the customer experience and establishing design conventions for consistent experiences.
+ Developing representative experiences such as customer identification and lookups.
+ Setting up the business administration console.
+ Integrating critical third-party systems.
+ Configuring the data model and data pipeline, such as how to access Connect Customer data from a data lake or data warehouse.
+ Creating a DevOps operational runbook.

These elements are the building blocks for delivering operational fundamentals with next-generation capabilities to elevate the customer experience and reduce operational costs. They are the first items to be used by a project, so they should be prioritized. The foundation is the catalyst for additional sprints and becomes the enabler for continuous experimentation and improvement.
