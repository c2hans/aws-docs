---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/sap-greenfield-implementations/planning.html
---

# Best practices for the planning phase
<a name="planning"></a>

During the planning phase of a greenfield SAP implementation, the project typically encounters various challenges and opportunities. This section discusses five key learnings based on SAP on AWS greenfield implementations that the AWS Professional Services team has been involved in.  You can implement some of these recommendations even before your project kicks off or the consulting team gets involved.  Providing drafts of documents such as the roles and responsibilities matrix or team contacts list helps speed up the ramp-up process.

## Build a RACI matrix
<a name="raci"></a>

Building a responsibility assignment matrix for the infrastructure team is critical to any implementation project.  This matrix takes the form of a comprehensive responsible, accountable, consulted, and informed (RACI) chart. The RACI is used to clarify roles, assignments, and tasks in a complex team structure. It should be developed in partnership with the AWS SAP Cloud team, the SAP Basis team, the SAP systems integrator (SI), and the customer.  This can be driven by any of those groups or by a project manager. Building the RACI without the input of these stakeholders creates inconsistencies, gaps, and sometimes even conflicts. It is important to consider all the phases of the project. Having the RACI upfront strengthens the partnership among all involved parties and creates clarity. Ideally, the RACI should be completed before project kick-off.

Here is an excerpt from a sample RACI matrix for a greenfield SAP implementation project. (To download the complete RACI matrix, see attachments.)

![Excerpt from a RACI matrix for an SAP on AWS greenfield project.](http://docs.aws.amazon.com/prescriptive-guidance/latest/sap-greenfield-implementations/images/guide-img/3deae530-9b57-46ef-8dd1-542c426e8365/images/791525fd-71b7-46f4-8a0a-4f464e1b3de5.png)

## Review the SoW
<a name="sow"></a>

Understand all the elements of the statement of work (SoW) for AWS consulting and advisory services, and jointly review the SoW with key stakeholders so that the deliverables are clearly understood by all. If the infrastructure team intends to do more than what the SoW defines, be sure to document that in the risk, assumptions, actions, issues, dependencies, and decisions (RAAIDD) log. In a greenfield SAP implementation project, staying nimble and agile is of utmost importance, so deviating from the SoW is a common scenario.  However, expectations can become obscured if the AWS implementation partner starts to deliver beyond what is documented. When changes occur, you should keep a running list of the new scope of work and the trade-offs that might have to be made.  For a waterfall project approach, a scope change management process must be defined and implemented. For an agile project, a backlog prioritization process is more appropriate for managing scope.

Considerations:
+ As you progress through the project, be sure to capture the new scope and define any new deliverables.  This will help you manage expectations and seek assistance in prioritizing your backlog.
+ Identify and prioritize documentation changes and tasks along with the existing delivery backlog, so documentation can be produced throughout the lifetime of the project instead of being delayed until the end.
+ Conduct a regular SoW walkthrough throughout the project in order to stay aligned on the deliverables and priorities.
+ For production cutover, make sure to have an SoW with read-only access approved at least 12 months in advance to help with hypercare support.

## Create a team organization chart and contact list
<a name="org-chart"></a>

Build a high-level organization chart that depicts the teams and leadership structure.  Go deeper by developing a cross-team contact list that includes the name, title, and role of everyone on the infrastructure team and key points of contact for various functions, such as security, network and firewall operations, Microsoft Active Directory, in-house cloud operations, and server operations.  Everyone should know who is involved and what role they play on the project.  Delays and miscommunications inevitably occur when the team doesn't have this information.  Understanding the titles of the stakeholders is also important.   For example, you wouldn't want to invite director-level stakeholders to working design sessions or daily stand-ups, unless they are key contributors to the discussions. Knowing titles and roles enables you to invite the right people to the relevant meetings. Being able to visualize the teams in an organization chart helps you understand how the teams are structured and work together on the project.

The following diagram provides an example of a typical SAP on AWS infrastructure organization chart.

![Example of an SAP on AWS infrastructure organization chart.](http://docs.aws.amazon.com/prescriptive-guidance/latest/sap-greenfield-implementations/images/guide-img/3deae530-9b57-46ef-8dd1-542c426e8365/images/c187731a-0631-486a-a30d-319e2c8950df.png)

## Establish an engagement model with your in-house cloud team
<a name="engagement-model"></a>

If your IT organization has an in-house AWS Cloud team, you should establish an engagement model with that team and clarify the work that they will perform, compared with what the AWS implementation partner (for example, AWS Professional Services or AWS Partner) is tasked to do. A key responsibility to consider is the support of environments after they are built and handed over.  For example, if there are only two AWS SAP Cloud architects who are building a multi-landscape and multi-environment infrastructure for a dozen SAP applications, they will not have the bandwidth to support the environment they complete building *and* build new environments at the same time.  One option is to ask the in-house cloud team to take over the support of the completed environments.  This gives the in-house team an opportunity to learn and take ownership of the environments. They will eventually become responsible for maintaining and expanding these environments, when the project progresses and a new scope of work is identified.

The in-house cloud infrastructure and cloud DevOps teams should also agree on the type of automation software to be used—for example, whether to use CloudFormation or Terraform as an infrastructure as code (IaC) tool. Similarly, they might decide to use AWS Systems Manager or Ansible for configuration tasks such as bootstrapping volumes and possibly SAP installations. These decisions should be documented. Additionally, if there is a requirement for a third-party monitoring and observability dashboard, but this was not a deliverable in the SoW, consider placing monitoring and logging hooks by using Amazon CloudWatch and Amazon Simple Notification Service (Amazon SNS) in the interim. The in-house cloud team can implement integration with a third-party monitoring solution at a later time.

The engagement model or support agreement should also be part of the RACI matrix and articulated in the SoW.  There is a significant level of automation that can be achieved by using AWS services. The SoW and RACI matrix should identify what needs to be achieved as part of the greenfield SAP implementation project, and what can be delegated to the operations team.

When you establish an engagement model, determine whether a waterfall, agile, or mixed approach will be the key method for moving forward. AWS Professional Services observed a 300 percent increase in task completion and 94 percent reduction in planning time in engagements that implemented an agile or mixed approach compared with a waterfall approach. In the planning phase, you should also select a communication plan and tooling approach with the help of the customer. The following table shows a sample communication plan.

![Sample communication plan for SAP on AWS greenfield projects.](http://docs.aws.amazon.com/prescriptive-guidance/latest/sap-greenfield-implementations/images/guide-img/3deae530-9b57-46ef-8dd1-542c426e8365/images/54c861bf-439b-4a29-ad18-73811c1ef36a.png)

Lastly, make sure to identify the customer and the SAP Basis team that will support the project early. Training them as you implement and migrate new solutions is key to starting knowledge transfer sessions early.

## Document the cloud build and deployment process
<a name="build-deploy"></a>

If your IT organization has an in-house cloud team, that team should document** **the cloud build and deployment process by using process flow diagrams and share these diagrams with the entire team. You want your key stakeholders to easily detect any bottlenecks or inefficiencies in the process, and understand the role that your existing internal processes play in creating inefficiencies or delays. In the following example, you can see how the Active Directory join and Domain Name System (DNS) update processes take the longest time to complete. Having this visual might motivate the teams to collaborate and figure out how to reduce the time involved in that step of the process.

![Example of a process flow diagram for the cloud build and deployment process of an SAP on AWS greenfield implementation](http://docs.aws.amazon.com/prescriptive-guidance/latest/sap-greenfield-implementations/images/guide-img/3deae530-9b57-46ef-8dd1-542c426e8365/images/253f531f-c8ff-49fa-a187-ba3191061867.png)

Considerations:
+ Document the help desk process and workflow separately, share this information with the infrastructure team, and make sure that everyone has access to the help desk tools so there is no reliance on one person.  Oftentimes, there can be a complicated and time-consuming ticket process for doing Active Directory joins, DNS updates, opening up firewalls, and requesting encryption keys.  It's critical to document these processes and to consider the Service Level Agreement (SLA) of each team in the project planning phase.  It also helps explain the reasons for a delay or bottleneck that requires special attention to remove.
+ Assign a named point of contact for Active Directory and firewall or networking tasks.  Those dedicated resources should be part of your project.  If you have to rely on service tickets, you cannot control service SLA.

## Project roadmaps and milestone tracker
<a name="project-roadmap"></a>

The following charts provide an example roadmap for a multi-year SAP on AWS greenfield project.

![Sample roadmap for the first year of an SAP on AWS greenfield project.](http://docs.aws.amazon.com/prescriptive-guidance/latest/sap-greenfield-implementations/images/guide-img/3deae530-9b57-46ef-8dd1-542c426e8365/images/10a1d20a-e9e2-4b0b-9cce-8e1d653f5994.png)

![Sample roadmap for the second year of an SAP on AWS greenfield project.](http://docs.aws.amazon.com/prescriptive-guidance/latest/sap-greenfield-implementations/images/guide-img/3deae530-9b57-46ef-8dd1-542c426e8365/images/87fb7841-778d-48a9-88a5-612d4022db3c.png)

![Sample roadmap for the third year of an SAP on AWS greenfield project.](http://docs.aws.amazon.com/prescriptive-guidance/latest/sap-greenfield-implementations/images/guide-img/3deae530-9b57-46ef-8dd1-542c426e8365/images/ae124f9f-8f50-4a5c-9d19-752bc83329de.png)

![Sample roadmap for the final year of an SAP on AWS greenfield project.](http://docs.aws.amazon.com/prescriptive-guidance/latest/sap-greenfield-implementations/images/guide-img/3deae530-9b57-46ef-8dd1-542c426e8365/images/45509d64-7a3c-49c0-8e21-7e252e18cba3.png)

The following chart shows example engagement timelines with AWS Professional Services for the same project.

![Sample AWS Professional Services engagement timeline for an SAP on AWS greenfield project.](http://docs.aws.amazon.com/prescriptive-guidance/latest/sap-greenfield-implementations/images/guide-img/3deae530-9b57-46ef-8dd1-542c426e8365/images/4df44770-3988-4522-9012-8cc43e2ce7dd.png)

The following chart shows a go-live milestone tracker for this project.

![Sample milestone tracker for an SAP on AWS greenfield project.](http://docs.aws.amazon.com/prescriptive-guidance/latest/sap-greenfield-implementations/images/guide-img/3deae530-9b57-46ef-8dd1-542c426e8365/images/e592217d-0ce2-4a5b-9528-73e3d10a5616.png)
