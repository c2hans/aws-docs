---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/azure-to-aws-platform-migration/introduction.html
---

# AI-Enabled Data Platform Migration Assessment: Microsoft Azure to AWS
<a name="introduction"></a>

*Nabarun Bandyopadhyay, Breck Manwaring, and Colby Wentlandt, Amazon Web Services*

Developing an effective migration strategy requires a thorough assessment phase that captures the customer's current environment in detail and builds the inventories needed to accurately estimate migration effort. In practice, this is rarely straightforward. Documenting processes and assets in an unfamiliar environment is time-intensive, teams often have fragmented knowledge, and new unknowns surface quickly during implementation, leading to schedule delays and budget overruns.

This guide presents a methodology to streamline the assessment phase using AI as an accelerator. Developed and validated during a multi-month engagement to migrate a large-scale data platform from Microsoft Azure to AWS, the methodology provides a structured approach to gathering current-state documentation and asset inventories. While focused on data platform migration, the approach can be adapted for other migration types, including infrastructure, application, and DevOps.

## Intended Audience
<a name="intended-audience"></a>

This guide is intended for technical leads, cloud architects, account executives, and other stakeholders involved in planning and executing data platform migrations. It is also relevant for anyone interested in evaluating how to incorporate generative AI into professional services delivery.

## Scope
<a name="scope"></a>

This guide walks through how to plan the assessment phase of a migration, develop a phased migration strategy, and leverage AI-based tooling to accelerate the assessment timeline. It covers how to structure deliverables, validate AI-generated content against source data, and manage a document lifecycle that supports both AI-assisted editing and traditional stakeholder collaboration. The guide also includes reusable templates for key deliverables, adaptable for use on other assessment projects.

**Objectives:**
+ Structure a repository-driven assessment project with epics, user stories, and acceptance criteria
+ Automate source environment discovery using AI-generated extraction scripts
+ Build a layered context model (inventory data, relationships, stakeholder knowledge) that grounds AI-generated documentation
+ Use deterministic validation pipelines to verify AI output against source data
+ Produce current-state and target-state migration deliverables with full traceability to source data
+ Convert and manage deliverables across markdown, Word, and Excel formats for stakeholder collaboration

**Note**
Some AWS services aren't available in all AWS Regions. For Region availability, see the [Service endpoints and quotas](https://docs.aws.amazon.com/general/latest/gr/aws-service-information.html) page in the AWS documentation, and choose the link for the service.
