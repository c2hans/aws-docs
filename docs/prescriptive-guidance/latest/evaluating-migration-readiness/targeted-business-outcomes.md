---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/evaluating-migration-readiness/targeted-business-outcomes.html
---

# Targeted business outcomes
<a name="targeted-business-outcomes"></a>

This section discusses the three expected outcomes from a cloud-readiness review: understanding the current state, identifying strengths and weaknesses, and creating an action plan.

## Understanding the current state of the cloud journey
<a name="understanding-current-state"></a>

When organizations contemplate large-scale migration to AWS, they generally fall somewhere along the path of what is called the *stages of adoption*, as illustrated the following diagram. The four stages—project, foundation, migration, and reinvention—are discussed in the blog post [The Journey Toward Cloud-First & the Stages of Adoption](https://aws.amazon.com/blogs/enterprise-strategy/the-journey-toward-cloud-first-the-stages-of-adoption/) on the AWS Cloud Enterprise Strategy blog. The purpose of a readiness assessment is to determine how far along in the stages of adoption the organization is currently at, and which parts of the organization's environment are sufficiently mature to move to the next stage.

![Graph showing cloud adoption journey from project to reinvention, with stages of migration and cloud-native development.](https://docs.aws.amazon.com/prescriptive-guidance/latest/evaluating-migration-readiness/images/guide-img/bde27ed7-c694-4dae-aea7-c2ff62bb249a/images/1536d570-77ef-4d5b-bd03-cd142097df1d.png)

**Example:**

If an organization is planning their first workload to move to the cloud, they're considered to be in the project (or proof of concept) phase. This phase doesn't require a unified account structure or other foundational constructs. However, to prepare a larger migration initiative, foundational aspects such as proper tagging should be in place. Otherwise, there is a risk of having to delay migrations to solve foundational issues.

## Identifying areas of strength and weakness
<a name="identifying-strengths-weaknesses"></a>

Identifying areas of strength and weakness is the second main outcome of a readiness assessment. Strengths determine the teams and practices that are ready for broad adoption across the organization. These are areas that don't require further work to enable successful cloud migrations at scale. Weaknesses are areas where actions need to be taken to improve the practices or capabilities to enable cloud migrations. Solving gaps early ensures a smooth migration process and eliminates the risk of project delays in building out foundational capabilities. The heat map illustrated in the following figure shows areas of strength and weakness across an organization. Action plans will need to be put in place for areas highlighted in yellow or red.

![Project plan diagram showing various stages and components of a customer migration process.](https://docs.aws.amazon.com/prescriptive-guidance/latest/evaluating-migration-readiness/images/guide-img/bde27ed7-c694-4dae-aea7-c2ff62bb249a/images/c43666b7-c74f-4314-8ffe-36288e8f08da.png)

**Example:**

An IT team might build an account structure that is well suited to cover the upcoming needs of the organization, but application developers and owners might not be aware that their application will be migrated to the AWS Cloud, and might not have the skill set to operate that application in the AWS Cloud. This example illustrates a gap in application owner buy-in and development team preparedness, and the organization should plan corrective actions during readiness assessment.

## Creating an action plan to enable scale and speed
<a name="creating-action-plan"></a>

After you identify strengths and weaknesses, you will need to put an action plan in place to close the gaps and scale identified areas of strength within the organization. The plan should have assigned owners and due dates to ensure that the project drives forward. We recommend that you engage your internal process improvement and organizational change teams to help drive the cloud initiative forward. These teams usually have toolkits for baselining current capabilities, establishing communications, handling buy-in planning, and similar processes, which will be useful.

**Note**
The AWS Professional Services team provides a program called Mobilize. This prescriptive model guides your organization to develop foundational capabilities across all areas of AWS CAF to address the areas identified in the Migration Readiness Assessment (MRA). The AWS Partner Network (APN) also provides services that can help you in your migration readiness efforts.
