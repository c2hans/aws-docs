---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/automated-patching-for-mutable-instances-in-the-hybrid-cloud-using-aws-systems-manager/stakeholders.html
---

# Key stakeholders, roles, and responsibilities in patch management
<a name="stakeholders"></a>

Successful OS patch management requires having well-defined roles and responsibilities for supporting your automated patching solution and optimizing it continually. This section describes suggested roles and responsibilities that you can modify according to your needs and organizational structure.

## User personas
<a name="user-personas"></a>

The following table describes the user personas involved with the automated patching solution.

|
|
| User persona | Description |
| --- |--- |
| Consumers (C) | The patch management solution for long-running instances is used by different teams involved in OS management, including:+ Development teams that manage full-stack application environments.<br />+ Operations teams that manage the application server OS. |
| Cloud engineering (CE) | The team that's responsible for:+ Continuously optimizing the patch management solution.<br />+ Building cloud services automation.<br />+ Supporting the automation. |
| Cloud business office (CBO) | The team that's involved in:+ Managing the consumer experience for the solution.<br />+ Enablement and user engagement.<br />+ Making sure that the patch solution meets consumers' needs. |
| Cloud service/product owner (CPO) | The person who is responsible for:+ Providing cloud services to consumers.<br />+ Working closely with the leadership team to align the services delivery with expectations and guidelines.<br />+ Managing all customer expectations and escalations related to the platform.<br />+ Owning the platform roadmap. |
| Security operations (SO) | The team that manages patch baselines and approvals. |
| Security operations manager (SOM) | The manager who is responsible for patch compliance. |

## RACI matrix
<a name="raci"></a>

The following responsible, accountable, consulted, informed (RACI) matrix specifies the activities involved with the patch management solution. For each step in the process, it lists the stakeholders and their involvement:
+ **R** – responsible for completing the step
+ **A** – accountable for approving and signing off on the work
+ **C** – consulted to provide input for a task
+ **I** – informed of progress, but not directly involved in the task

|
|
| Patch management solution | CPO | CBO | CE | SO | SOM | C |
| --- |--- |--- |--- |--- |--- |--- |
| Patch management product roadmap execution | A | C | R | C | C | I |
| Patch management architecture and design | A | I | R | C | I |  |
| Patch management development and configuration | A |  | R | C |  |  |
| Patch management validation and testing | A | I | R | I | I |  |
| New AWS account, application, and server onboarding for patching | A | C | R | I |  |  |
| User engagement and enablement | A | R | I | I | I |  |
| User feedback and escalation management | A | R |  | I | I |  |
| Product change management | A | R | C | I |  |  |
| Issue management and resolution | A |  | R | C |  |  |
| Server patching and patch compliance |  |  | C | C |  | AR |
| Patch baseline configuration |  |  | C | R | A | C |
| Patch reporting and compliance |  |  | C | R | AR | I |
