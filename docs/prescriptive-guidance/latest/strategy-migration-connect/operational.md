---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/strategy-migration-connect/operational.html
---

# Operational workstream
<a name="operational"></a>

The operational workstream supports the technical foundation and user journey workstreams. The majority of non-technical activities that are crucial to overall migration success are part of this workstream.

This workstream involves decisions that can be changed or reversed with little effort or impact. Product specifications that are based on how people work and engage are rarely right the first time―there are many stakeholders and voices to consider. It is important to engage early and consult widely and often, so an agile and iterative approach makes sense for this workstream. You start with an early draft of an operating model or training materials and iterate frequently and rapidly to get to the final product.

The operational workstream consists of five phases: project governance, alignment, operating model definition, service introduction, and training.

![Operational workstream in contact center migrations](https://docs.aws.amazon.com/prescriptive-guidance/latest/strategy-migration-connect/images/guide-img/c8027e22-fcd9-43b3-b8a7-234ec8eb0644/images/bb84baf2-a2e1-490d-9f81-2cf4ba31a333.png)

## Program governance
<a name="program-governance.7c597b72-eeca-508a-95aa-2abd384c2066"></a>

Program governance activities run throughout the entire timeline of a migration project. Regardless of the stage the project is in, activities should be regular (scheduled recurring meetings), transparent (project team is given the opportunity to raise risks and issues frankly), and with engaged governance (leaders are empowered and willing to make decisions or escalate accordingly). These are vital for highlighting and resolving issues promptly and effectively.

## Alignment
<a name="alignment.299115aa-e6b2-5335-b21a-4c62baf4badf"></a>

This is the first formal activity of the project and focuses on aligning the project scope to business outcomes. Alignment provides an opportunity to validate and adjust earlier plans and estimates based on discussions with stakeholders.

Key actions during this activity include:
+ Discover high-level customer use cases, current technical and business pain points, and opportunities for improvement.
+ Discuss and agree on desired business outcomes, determine their relative priorities, and identify success criteria.
+ Develop a high-level solution design, which is used to define scope and technology choices in this early phase. This high-level design provides direction to accelerate low-level design activities in later phases.
+ Validate timelines and implementation costs.

## Operating model definition
<a name="operating-model-definition.23f8664a-90b6-5113-82c4-9bd42b137ae1"></a>

The activities in this phase define *who* will use the contact center solution and *how* the solution will be managed. The operating model is not a procedural document, a runbook, or a configuration file. For example, it shouldn't explain how to pull logs and attach them to a support ticket, or provide screenshots of this procedure. Instead, it should identify who should pull the logs and which queue or vendor they should be sent to.

The operating model definition should include:
+ A responsible, accountable, supported, consulted, and informed (RASCI) matrix, so each team understands its roles and responsibilities, and how they will interact with other teams. The following provides an excerpt from a RASCI matrix.

![Example RASCI matrix for contact center migrations](https://docs.aws.amazon.com/prescriptive-guidance/latest/strategy-migration-connect/images/guide-img/c8027e22-fcd9-43b3-b8a7-234ec8eb0644/images/669b2f51-8045-4c16-9288-32d8c9343c6a.png)

+ Process flow swimlanes that define the end-to-end activities and who is responsible for each activity. For example, there should be a process flow for engaging out-of-hours support so it's clear who gets paged, what happens if they can't be reached, who logs the support ticket, and how the business criticality is judged. Another example is the emergency queuing message. The process flow should show who decides that it needs to be initiated, and what data they should use to make that decision.

The operating model is typically defined in the second half of a project, because you have to finalize the solution design and user journeys before you can define the processes to manage them accurately. However, we recommend that you line up stakeholders early in the process and reserve their time for the later phases of the project.

Gather examples of similar documents from your organization that you can use as templates. This will facilitate review and sign-off by stakeholders because the document structure will be familiar to them.

Make sure that your stakeholders sign off on the operating model *before *your new contact center moves into production, and make it a requirement for your decision to go live. Each team member needs to understand their role and the process for operating the contact center in the production environment.

## Service introduction (SI)
<a name="service-introduction--si-.273bf53d-5cb0-52dd-ad19-271703077d65"></a>

SI activities implement the changes defined in the operating model. Think of the operating model definition as the design and build phases for the new model, and SI as the deploy phase of the operating model.

The SI team is often a dedicated team in your organization, and works independently from the project team. The project must pass the SI team's criteria and checklists before it receives approval to go live. For example, checklists include user acceptance testing (UAT) results and confirmation that a clashing event (such as a change freeze or, another scheduled go-live event) isn't taking place on the same day that the project goes live, that users have the necessary training, and that operations teams are ready to proceed.

Do not leave SI activities to the end of the project. Engage the SI team early in the project and include them in your distribution list for design documentation. Early involvement ensures that the SI team can assist in the preparation to go live, such as helping to select the most suitable [AWS support plan](https://aws.amazon.com/premiumsupport/plans/), providing impact statements for change requests (CRs), and supporting change approval board (CAB) discussions.

## Training
<a name="training.82009cf0-6850-59e4-a879-bea98719774c"></a>

Creating training materials and conducting well-attended training sessions are vital to successful migrations. Technology can work perfectly, but if users don't know how to answer calls and perform their daily tasks, the migration will be considered a failure.

Training activities might include direct user training, training the trainers, training for supervisors, training for support staff, and training for system administrators or product owners. Each organization is unique, so some options might be a better cultural fit than others.

We recommend a *train the trainer* approach that involves your organization's in-house training staff. Your staff knows your organization's culture, and the training format and techniques that best suit your users. Project team members can take on subject matter expert (SME) roles to provide technical materials (such as user manuals, administrator console manuals, and screen guides) that can be used as source material for the train the trainer sessions. If your organization doesn't have a training team, project SMEs should train supervisors and lead support staff, who can then train the users of the contact center.

We also recommend that system administrators and product owners take formal, instructor-led product training courses to gain a deeper understanding of the AWS environment and Connect Customer console, so they can use product features and troubleshoot effectively.
