---
source_url: https://docs.aws.amazon.com/whitepapers/latest/establishing-your-cloud-foundation-on-aws/change-management-categories-priorities.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Change Management categories and priorities
<a name="change-management-categories-priorities"></a>

## Categories
<a name="categories"></a>

Changes can be grouped and categorized based on perceived level of impact and urgency. Changes come in three categories: normal, standard, and emergency.
+ **Standard Change** – This change is an established change that is low-risk and well understood; therefore, it does not need a formal review and approval process. These changes utilize a condensed version of the normal change procedures that simplifies the process in order to quickly satisfy the change requester’s need. For example, when a user requests for an internal storage resource to be created within your environment. This change request has low risk and can frequently be automated with a self-service change management fulfillment service. Standard changes are submitted via a request for change process and reviewed by approving body sometimes know and a Change Advisory Board (CAB).
+ **Normal Change** – This change is unique and has a higher risk of uncertainty of the anticipated outcome. This is typically defined as the default change and warrants a formal review and approval process to initiate the change implementation. For example, when a new service requires a firewall rule to be updated to allow incoming from a non-standard port.
+ **Emergency Change** – This change addresses unforeseen operational issues, such as failures, security threats, and vulnerabilities. This type of change is a rapid change that is required to continue or restore the business operations, to address significant risk, or to solve emergency business needs. Emergency changes should still follow documented procedures and use the organizational emergency change management process; however, the approval process is streamlined by defining a smaller approval body commonly known as the Emergency Change Advisory Board (ECAB). The ECAB is a special group convened to advise on approval/rejection and planning for emergency changes. The membership to the ECAB includes people with experience and authority to assume risk to make rapid decisions.

Depending on the categories you choose, you will need to provide a process for approval. Standard changes require a formal review process and approval from a change approving authority such as a CAB you will setup. Emergencies require a fast reaction; however, they still warrant an approving body. Depending on the risk your organization wants to take, change approval should be documented and have some type of approving authority for anything outside of the day-to-day changes. However, not all changes require a formal review and approval; they merely require some form of request submission and automated approval. As customers move toward automation, change management can be done in a highly automated and scripted manner with minimal manual input.

**Note**
Recurring changes that are tasks with low risk should be categorized as standard and auto-approved. Change management should focus on enablement and not become bureaucratic roadblock to delivering value.

## Priorities
<a name="priority"></a>

Changes should also be defined with a priority level to assist in identifying the impact and urgency of the change. Impact is a measure of the effect of an incident, issue, or change on a business process. Impact is often based on how service levels will be affected. *Urgency* is a measure of how long it will be until an incident, problem, or change has a significant business impact. For example, a high impact incident may have low urgency if the impact will not affect the business until the end of the financial year. Creating a matrix to assist in identifying the priority of change request helps facilitate a standardize process to identify the priority of the change and schedule the execution of the change appropriately.

## Initiating request for change
<a name="initiating-request-for-change"></a>

An essential part of change management is the request for change process, documents, and end-users request for change and triggers the review and approval process. Changes that fall within scope for your change management process will require a *Request for Change* (RFC) to be submitted for review and approval. A change request is a formal communication looking for a modification to one or more configuration items within scope of your change management system. A request for change can include the following:
+ RFC Document
+ Service Desk call
+ Project initiation document
+ Tickets generated from IT Support service

We recommend that you determine the applicable information to support your change control process. Depending on the category of change, a request for change can capture different levels of detail. Basic information that needs to be captured is the service or configuration item that will be change, who is submitting the change, and justification for the change. There needs to be enough information that the approving authority can approve or deny the change. The following table gives an example of basic information which should be captured on all RFCs:

|  RFC data point  |  Description  |
| --- | --- |
|  Submitted By  | Point of contact for change initiation  |
|  Date Requested | Date the request for change was submitted  |
|  Title of Change | Title of the change |
|  Description of Change | Brief description of the change |
|  Justification of Change | Reason change is necessary |
|  Identified Risks | A list of identified risks and their risk mitigation efforts |
|  Impact Scope  | The impact the change will have within the environment |
| Schedule  | Schedule of the maintenance window for the change to be completed in |
| Suggested Implementation | Plan to implement the change |
| Rollback | Plan to rollback change if necessary |

## Change communication
<a name="change-communication"></a>

The change management process fulfills the review, approval, and orchestration of changes. A cohesive communications plan is a critical component for success to help further mitigate risks when making IT changes. When all the right people are involved - the technical manager, the business manager, the people making the change, and the business users – all the right tools are provided, and all the right fallback actions are tested, a communications plan helps ensure a comprehensive and successful change.

An important part of the process is to communicate the intended change and, if necessary, coordinate a maintenance window to implement the change. Change management requires that all stakeholders for the change are notified if the change will impact their service or operations.

## Change management tools
<a name="change-management-tools"></a>

To facilitate configuration and change management, manual or automated tools can be used. Tool selection should be based on the needs of the project stakeholders including organization and environmental considerations and/or requirements.

Change management tools can integrate with the operating environment facilitating workflows that deliver communication, change orchestration, approval processes, and configuration item baseline tracking and monitoring. This type of change management tool more often requires an advanced environment setup that support workflow templates for automation and take considerable amount of planning and setup. They require an understanding of the scope of change you desire to manage and how well-defined scripted steps for change implementation.
