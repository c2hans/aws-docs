---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/migration-opentext-teamsite/high-level-migration-process-flow.html
---

# High-level migration process flow
<a name="high-level-migration-process-flow"></a>

The migration process occurs in five phases: discovery, design, development, testing and refinement, and implementation. The following table provides an overview of these five phases and the migration process flow.

|
|
|  | **Discovery** | **Design** | **Development** | **Testing and refinement** | **Implementation** |
| --- |--- |--- |--- |--- |--- |
| **Outcomes** | + Existing system architecture<br />+ Migration inventory<br />+ Functional and non-functional requirements<br />+ Future system architecture (High-level) | + Migration strategy for each component (7 Rs)<br />+ Target AWS architecture<br />+ TCO analysis and assessment<br />+ High-level migration plan | + Ready-to-deploy applications<br />+ Automation scripts in CloudFormation<br />+ A step-by-step migration plan, including automated and non-automated tasks<br />+ Detailed test plans | + Testing reports<br />+ Refined automation scripts, migration plans, and testing plans | + An OpenText Customer Experience platform running on the AWS Cloud<br />+ Testing reports |
| **Tasks** | + Discovery workshops<br />+ Documentation analysis | + Multi-disciplinary subject matter expert (SME) meetings<br />+ Cost analysis<br />+ Validation workshops | + Multi-disciplinary SME meetings<br />+ Application refactoring and adaptation<br />+ Adapt and create automation scripts<br />+ Create or provision new services or functionalities | + Automated testing<br />+ Adapt automation and migration plans | + Migration plan implementation<br />+ Automated testing |
| **Customer resources** | + Technical and business documentation<br />+ Business owners and technical architects – Participation in workshops and interviews | + Current TCO data<br />+ Business owners and technical architects – Participation in validation workshops and interviews.<br />+ Access to technical assets (environments, source code, or deployment pipelines) | + Access to technical assets (environments, source code, or deployment pipelines)<br />+ Technical teams – Support about current applications. | + User testing<br />+ Infrastructure teams – Support for migration activities | + User testing<br />+ Infrastructure teams – Support for migration activities |
| **Accelerators** | + OpenText architecture analysis framework<br />+ Diagrams<br />+ Focus points | + Existing knowledge about the most common migration strategies and target AWS products and services for each solution component | Existing automation assets for:+ Provisioning of AWS resources<br />+ Data migration<br />+ Application installation and configuration | Automated testing assets creating during previous migrations, such as:+ System health checks<br />+ Performance and Load testing scripts | Automated testing assets creating during previous migrations, such as:+ System health checks<br />+ Performance and Load testing scripts |

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
