---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/strategy-devops-value-stream-mapping/create-value-stream-map.html
---

# Creating a development value stream map
<a name="create-value-stream-map"></a>

The following are the steps to create a development value stream map (DVSM):
+ [Step 1: Identify the value stream](#step-1)
+ [Step 2: Define the start and end points](#step-2)
+ [Step 3: Identify the teams involved](#step-3)
+ [Step 4: Train the participants](#step-4)
+ [Step 5: Map the value stream steps](#step-5)
+ [Step 6: Evaluate speed and quality for each step](#step-6)
+ [Step 7: Identify the constraints](#step-7)
+ [Step 8: Continuously improve](#step-8)

## Step 1: Identify the value stream
<a name="step-1"></a>

Value stream mapping focuses on delivering value to a customer. This value stream should be defined as narrowly as possible. Ideally, it encompasses the scope of what a single, [two-pizza team](https://docs.aws.amazon.com/whitepapers/latest/introduction-devops-aws/two-pizza-teams.html) would deliver to the customer if that team included all the individuals from Business through IT, including Development and Operations. If the organization is already structured into value streams and product teams, the development value stream is a single value stream and its associated product team. If not, the development value stream might pass through dozens of teams and hundreds of people—that's OK.

For example, an appropriate value stream might be the customer-facing claims entry interface for an insurance organization. The interface requires collaboration from teams across every department, from Business through IT. The scope of evaluating the entire Claims department would be too broad because it focuses on the organization and not on the value delivered to the customer.

## Step 2: Define the start and end points
<a name="step-2"></a>

The start point of a value stream map is when the business has defined and prioritized the deliverable, and it is ready to be started. Each team has their own definition of *ready*. For more information about defining this term in your organization, see [Walking Through a Definition of Ready](https://www.scrum.org/resources/blog/walking-through-definition-ready) (Scrum blog post). In many cases, *ready* means that the deliverable has moved out of the general backlog and is available in the sprint backlog or added to a Kanban board. The DVSM should not include the backlog, refinement, prioritization, or any other steps required to meet your team's definition of *ready*.

|
|
| Note: Although the time spent in backlog and the prioritization and refinement processes are out of scope for development value stream map, these tasks might cause significant delays in your organization. You can use the same lean process to create separate value stream maps for these activities. |
| --- |

The end point of a value stream map is your team's definition of *done*. For more information about defining this term in your organization, see [Definition of Done](https://www.leadingagile.com/2017/02/definition-of-done/) (Leading Agile blog post). *Done* means that you have successfully instrumented and validated the deliverable. Ideally, it includes delivery to the end customer in production and monitoring that demonstrates the product is successfully implemented, functioning, and adopted.

## Step 3: Identify the teams involved
<a name="step-3"></a>

The DVSM extends across all of the people, processes, and technology required to deliver specific value to the customer. Include a team in the DVSM process if there is a dependency on this team to deliver value to the customer. A team is considered *dependent* if they interact with the deliverable on its way to the customer, take a ticket related to the process or deliverable, or affect the ability to complete the deliverable. New dependencies often emerge during the mapping process, so don't worry about identifying all of the teams upfront. Start with a high-level list of the expected teams.

The following teams are commonly included when creating a development value stream map:
+ Product
+ Business
+ Development
+ Quality
+ Infrastructure
+ CI/CD platform
+ Operations
+ Architecture
+ Site reliability engineering (SRE)
+ Change and release
+ Security

Target a group size of no more than 5–8 participants who can represent these teams. If you find that you need more than eight participants to adequately represent each team, break down the map into sections that you can complete with smaller groups in separate mapping exercises. You can then assemble the sections to build a complete map of the development value stream, from start to end.

## Step 4: Train the participants
<a name="step-4"></a>

Select a tool that the team will use to create the DVSM. You could use a whiteboard with sticky notes, an online whiteboard application, Microsoft Visio, or even Microsoft Excel. You might choose one tool for the collaborative stage and then move the map into a different tool for formal presentation purposes. When you choose a tool for the collaborative stage, consider whether all participants will be attending in person or if the session will have remote attendees. If some attendees are remote, you might choose an application that provides all participants with an equal opportunity to contribute.

Guide participants through the tools and process. Prepare participants and set the expectation that all participants will engage and independently add steps and data to the value stream map. Accountability is critical to the success and speed of the development value stream mapping process, and collaboration helps ensure the DVSM is not single-threaded. If necessary, provide training for the tool you've selected.

Train the participants about the basic process and confirm that they have access to the selected tools prior to the scheduled mapping session. This can prevent delays during the mapping session and allow the team representatives to start contributing and engaging as quickly as possible.

## Step 5: Map the value stream steps
<a name="step-5"></a>

With the participants, identify all of the steps that occur between the start and end points of the value stream. You can start the process by identifying the start and end points and work collaboratively the define the first couple of steps. As the DVSM begins to grow and the participants become more comfortable, ask participants to independently add boxes and data to the board. To make sure all of the steps are accounted for, use your knowledge of the SDLC to question "then what?"

Ask participants to break larger tasks down into manageable steps, especially if those tasks involve multiple owners. However, make sure that the step units don't become too small. Too many steps can make it difficult to complete the map and identify the most significant constraints in the value stream.

The following are steps that are commonly included when creating a development value stream map:
+ Development
+ Unit testing
+ Integration testing
+ Functional testing
+ Regression testing
+ Security validation
+ Performance testing
+ User acceptance testing
+ Defect workflows
+ Change advisory board (CAB) approval
+ Change tickets
+ Request tickets and SLAs
+ Documentation
+ Architecture reviews
+ Data reviews and approval
+ Infrastructure provisioning
+ Network and firewall changes
+ Production deployment
+ Logging and observability orchestration
+ Smoke testing
+ Production incident workflows

Put the steps in sequential order, and connect them with process flow arrows. Identify the *happy path*, which is the process flow if no exceptions or errors are encountered during development. Also identify the *failure path*, which is the flow that occurs when the product fails any step in the development process.

## Step 6: Evaluate speed and quality for each step
<a name="step-6"></a>

In this stage, you determine who own each step and evaluate the speed of that step and how often it produces high-quality results. Ask who performs that work, who it's delivered to, and how often it's sent back because of issues.

Start by identifying the owner of each step. The *owner* is the team that's responsible for performing the work in the step. To make it easier to identify ownership in the map, you can assign each team a different color. If a step has multiple owners, divide that step into multiple, smaller steps so that each team can provide autonomous data and handoffs are properly accounted for.

For every step in the value stream map, ask the step owner to provide the following information. Data should come from anecdotal average scenarios and not pulled from systems or data sources. Often, pulling and normalizing this data is too much effort for the scope of the DVSM. Additionally, the data is often incorrect or doesn't include elements that are difficult to trace or measure. Because the goal is to improve the system they use, trust the people who own the work to have a confident grasp of the following metrics:
+ **Lead time (LT)** –This is the duration of the step from start to end, from when the owner accepts the work to when they hand it off. It includes all time spent working on the deliverable and all downtime, such as time spent waiting. Make sure to track SLAs and hand-off processes between teams as a part of lead time.
+ **Process time (PT)** – This is the amount of time it would take a single person to perform the work, assuming no interruptions or downtime. This is sometimes referred to as the *value-added* time, which is a measure of the time spent adding value to the deliverable.
+ **Percent complete and accurate (%CA)** – This is the percentage of time that the step delivers work or data that is accurate, doesn't require any rework, and doesn't need to be sent back. Examples of inaccurate deliverables include bad data, wrong forms, bugs, defects, flaws, or incidents, as reported by the downstream steps.

It's important that all teams participate and that one team does not speak on behalf of another. Each team should have the autonomy to provide data for the steps they own and discuss handoffs that can significantly affect both speed and quality. This might result in talking to a significant number of people to gather the data.

## Step 7: Identify the constraints
<a name="step-7"></a>

Identify that constraints that significantly affect speed and quality:
+ Speed-related constraints occur in the steps that have the largest gap between the lead time and process time. This indicates there is a significant amount of time wasted in the step, such as time lost to waiting.
+ Quality-related constraints occurs in steps that have low percent complete and accurate scores. This indicates that there is a significant amount of effort and time lost in repeating work to fix defects.

These steps provide the greatest opportunity for speed and quality improvements in your software development process.

Across the value stream, you can add lead times or process times for all steps to obtain a cumulative lead time or process time for the entire value stream. You can also multiply the percent complete and accurate scores for all steps to determine an average. This can help you understand how long work takes across the system and the likelihood of it being correct at any given step.

## Step 8: Continuously improve
<a name="step-8"></a>

After you have identified and prioritized the constraints in the development value stream map, you can use them to drive improvement in your software development process. With the stakeholders and step owners, work to improve speed and quality by eliminating handoffs, wasted time, and excessive processing.

After you implement changes, revisit the DVSM with the step owners and assess whether the changes have been successful. Update the DVSM based on the changes, and then identify and prioritize new constraints in order to drive continuous improvement. It's common for new constraints to appear in a different part of the map or for constraints to escalate from low to high priority.
