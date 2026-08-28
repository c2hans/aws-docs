---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/database-decomposition/challenges.html
---

# Common challenges and managing responsibilities for database decomposition
<a name="challenges"></a>

Database decomposition is a complex process that requires careful planning, execution, and management. As organizations seek to modernize their data infrastructure, they often encounter a myriad of challenges that can impact the success of their projects. This section describes the common hurdles and introduces a structured approach to overcoming these obstacles.

## Common challenges
<a name="challenges-common"></a>

A database decomposition project faces several challenges across technical, people, and business dimensions. On the technical front, ensuring data consistency across distributed systems poses a significant hurdle. It can also have potential performance and stability impacts during the transition period, and you must seamlessly integrate with existing systems. People-related challenges include the learning curve associated with the new system, potential resistance to change from employees, and the availability of necessary resources. From a business perspective, the project must contend with the risks of timeline overruns, budget constraints, and the potential for business disruption during the migration process.

## Defining roles and responsibilities
<a name="challenges-raci"></a>

Given these complex challenges that span technical, people, and business dimensions, establishing clear roles and responsibilities becomes critical for project success. A Responsible, Accountable, Consulted, and Informed (RACI) matrix provides the necessary structure to navigate these challenges. It explicitly defines who makes decisions, who performs the work, who provides input, and who needs to stay informed at each stage of the decomposition. This clarity helps prevent delays caused by ambiguous decision-making, encourages appropriate stakeholder engagement, and creates accountability for key deliverables. Without such a framework, teams may struggle with overlapping responsibilities, missed communications, and unclear escalation paths—issues that could exacerbate the existing technical complexities and change management challenges while increasing the risk of timeline and budget overruns.

The following sample RACI matrix is a starting point that can help you clarify potential roles and responsibilities in your organization.

|
|
| **Task or activity** | **Project manager** | **Architect** | **Developer** | **Stakeholder** |
| --- |--- |--- |--- |--- |
| Identify business outcomes and challenges | A/R | R | C | – |
| Define the scope and identify requirements | A | R | C | C/I |
| Identify the project success metrics | A | R | C | I |
| Create and execute the communication plan | A/R | C | C | I |
| Define the target architecture | I | A/R | C | – |
| Control database access | I | A/R | R | – |
| Create and execute the business continuity plan | A/R | C | I | – |
| Analyze cohesion and coupling | I | A/R | R | I |
| Move the business logic (such as stored procedures) from the database to the application layer | I | A | R | – |
| Decouple table relationships, known as *joins* | I | A | R | – |

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
