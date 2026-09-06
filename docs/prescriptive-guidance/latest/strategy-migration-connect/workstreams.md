---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/strategy-migration-connect/workstreams.html
---

# Project phases and workstreams
<a name="workstreams"></a>

In the context of a contact center migration project, *sprint*, *workstream*, and* phase* have the following meanings:
+ A *sprint*** **is a time-bound collection of activities that are delivered by different workstreams. For example, each sprint could be two weeks long.
+ A *workstream *is a team-bound collection of activities associated with a set of technology components or scope. Sprints include workstream activities. For example, AWS account and landing zone creation can be included in a technical foundation workstream, which involves architect and developer team resources. Mapping customer experiences and recording call prompts should be handled by a different, user journey-related workstream, because these tasks involve business stakeholders and service line owners.
+ A *phase *is a goal-oriented collection of activities across workstreams. Phases usually end at milestones, and reaching these milestones means that the project progresses to the next phase. For example, the design phase involves creating documents that are appropriate to each workstream, such as architectural diagrams, build specifications, and high-level design documents. The design phase is completed when these documents are approved by the necessary stakeholders.

Well-defined and autonomous workstreams improve overall project agility. Basing workstreams on specific teams and roles gives team members autonomy in prioritizing sprint backlog items. It also creates boundaries between workstreams, so you can identify and track dependencies, and provides clear accountability.

The high-level plan in the following diagram shows the parallel workstreams and sequence of typical activities in an example contact center migration project.

![Sprints, workstreams, and activities in a contact center migration project](http://docs.aws.amazon.com/prescriptive-guidance/latest/strategy-migration-connect/images/guide-img/c8027e22-fcd9-43b3-b8a7-234ec8eb0644/images/ba528d35-95ed-4079-aee7-a0a275839862.png)

We recommend that you run at least three parallel workstreams: *operational***, ***technical foundation***, **and *user journeys. *The phasing and approach to project activities differ, depending on the nature of the workstream. Each workstream requires a different delivery approach, as explained in the following sections. As the diagram illustrates:
+ Tasks within each workstream are bundled into agile sprints.
+ Sprint 0 is a collection of early tasks focused on project kick-off, discovery, planning, and design.
+ Sprint MLP is a collection of activities for creating a minimum lovable product (MLP) that future sprints can iterate on to provide end-state target capabilities. For example, the MLP could deliver a relatively straightforward caller journey to a small group of agents. After the platform is live and proven stable for the MLP use cases, future sprints (sprints 2, 3, and so on in the diagram) can iterate rapidly to deliver innovative capabilities.
+ Each project and environment is different, so the diagram doesn't provide specific timelines. Use this plan as a starting point for discussions with stakeholders during the initial project planning phase. Determine which activities are relevant, identify any activities that should be added, and determine their estimated duration.
