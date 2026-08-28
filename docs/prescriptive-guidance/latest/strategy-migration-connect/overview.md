---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/strategy-migration-connect/overview.html
---

# Overview
<a name="overview"></a>

## Pillars of successful migration
<a name="pillars"></a>

To carry out a successful contact center migration, you shouldn't view the migration as only a technology delivery project―you should approach it from multiple perspectives. Otherwise, you might overlook vital preparations such as staff training and operating model changes. These non-technology considerations are crucial in ensuring overall success.

The pillars illustrated in the following diagram are perspectives and capabilities described in the [AWS Cloud Adoption Framework (AWS CAF)](https://aws.amazon.com/professional-services/CAF/). This framework provides best practice guidance to help you digitally transform and accelerate your business outcomes through innovative use of AWS. Each perspective covers a set of capabilities that stakeholders own or manage in the contact center transformation and migration process.

![Pillars of successful migration for contact centers](http://docs.aws.amazon.com/prescriptive-guidance/latest/strategy-migration-connect/images/guide-img/c8027e22-fcd9-43b3-b8a7-234ec8eb0644/images/f087d564-526c-40c5-985a-ce346e0d0fce.png)

Moving users (customers, agents, and operators) to a new platform and tool set is a considerable amount of work. Contact center migrations require thorough planning, whether you are taking your existing on-premises contact center journeys to the cloud, or refactoring the whole customer and agent experience.

The following sections discuss approaches and best practices to plan, manage, and complete migrations to Amazon Connect Customer.

## Primary vision
<a name="vision"></a>

A successful contact center migration starts with business requirements and then focuses on people, processes, and technology.

Start planning your Connect Customer migration by first developing a primary vision statement. This should be a general principle that guides the direction of decision-making. You can then define more specific guiding principles for particular decision areas within the bounds of this general principle.

For example, the primary vision statement for your project might answer the question, "What does success look like?" as follows: "*Minimal user disruption* (in order of significance: *customers, agents, system operators*) while migrating service lines at *pace*."

Notice the emphasis on the following phrases:
+ *Minimal user disruption* ‒ Depending on your contact center's opening hours and backend systems, it might not be possible to avoid downtime entirely during the migration. Be realistic and consider whether the expected disruption is tolerable compared with the time and effort required to complete the migration without any downtime. Accepting minimal disruption rather than no disruption might reduce risks in other areas of project delivery or provide significant cost savings. For example, you might decide to circulate a new web address to users for accessing the new Connect Customer desktop page instead of migrating an existing known web address. This helps avoid the effort and expense of signing new domain certificates and having to manage a web address cutover.
+ *User list in order of significance *‒ Customers, agents, and system operators have different priorities during a migration. Generally, the highest priority is to avoid disruption to your customers, even if it means additional disruption to agents and backend system operators.
+ *Pace *‒ It is costly, both financially and resource-wise, to operate more than one contact center platform during the migration. Your objective should be to keep the dual-system period as short as practical. The longer it is, the greater the cost, the burden on operators, and the risk of human errors such as making changes on the wrong platform. Balance rigor and depth with the need to move rapidly. Develop a realistic delivery plan and try to follow it.

## Targeted business outcomes
<a name="business-outcomes"></a>

Keep these business outcomes in mind when you plan your contact center migration:
+ **Increased business agility **‒ Deliver new capabilities into production rapidly and safely. For example, sentiment analysis and big data call transcript crawling help you gather near real-time insight into customer communications and enable you to optimize your products and services based on their needs. After you identify and implement these features, you can deliver them by using DevOps principles, which encourage collaboration among your developers and operators, and use infrastructure as code (IaC) tools and continuous integration and continuous delivery (CI/CD) pipelines to manage builds and automate testing. Avoid repeating steps manually wherever possible to avoid human error, which can introduce bugs into the implementation process.
+ **Improved total cost of ownership (TCO), especially in early stages **‒ Rework costs time and effort. To get key decisions right the first time, allocate sufficient time to the discovery and design phases of migration. Infrastructure decisions are difficult to alter without significant cost, so consult with the appropriate stakeholders. For example, changing the encryption policy for call recordings might require additional infrastructure components, so make sure that your security compliance teams approve the encryption policy before you start implementation. Get sign-off on designs before moving into the build phase.
+ **Agile customer experience **– Use agile methodologies to rapidly and iteratively develop caller journeys. Unlike infrastructure components, contact flows and user journeys are easy to alter, so start early with a basic flow and iterate frequently with stakeholders to reach the desired state. It's easy to add a message prompt or to alter menu options in Connect Customer―no programming knowledge is required. Your objective should be to deliver the right user journey, not to rigidly follow the journey that you originally designed. Iterating frequently gives stakeholders the ability to tweak the journey as it matures and feedback is received.
+ **Smooth and timely service introduction** ‒ User training, process changes, and service desk changes are often overlooked until the project is close to completion. The new contact center has to be accepted into your organization's business as usual (BAU) operations as well as meeting the go-live date. Without a proper handover, the project team will not be able to recede and BAU teams will not be prepared to use the new platform. Make your project's integration into BAU operations a gate for go-live approval. It is vital to agree on platform ownership before you go live. Engage service introduction and operating model stakeholders from the beginning of the project, and keep them engaged throughout.
+ **Introduce new, differentiating capabilities to improve customer satisfaction (CSAT) scores** ‒ Ask yourself whether the user experience can be simplified or improved by Connect Customer. Don't limit yourself to lifting and shifting your current call center to the cloud. Use Connect Customer features to improve the user (customer and agent) experience or to simplify the technical implementation of your platform. With relatively little effort, you can incorporate new Connect Customer capabilities into your call center and see a significant improvement in your CSAT scores.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
