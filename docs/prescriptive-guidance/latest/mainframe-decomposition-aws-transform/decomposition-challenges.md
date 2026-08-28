---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/mainframe-decomposition-aws-transform/decomposition-challenges.html
---

# The critical role of decomposition in mainframe modernization
<a name="decomposition-challenges"></a>

Mapping technical components to business domains and modules introduces significant challenges in mainframe transformation projects. These challenges include:
+ **Legacy complexity**. Mainframe systems often contain decades-old code, tightly coupled components, and undocumented dependencies, which complicate business functionality isolation.
+ **Poor business-IT alignment**. Misalignment often occurs when technical teams don't fully grasp business processes, and business stakeholders struggle to understand technical intricacies.
+ **Data dependency**. In mainframe systems, multiple business functions often share centralized databases, which complicates data ownership separation.
+ **Size**. The high volume of mainframe components—thousands of programs, transactions, and jobs—makes manual decomposition time-consuming and error-prone.

Decomposition addresses these challenges by breaking down monolithic systems into smaller, more manageable, business-aligned modules and creating meaningful categories of business and technical functionalities that align with desired business and technical outcomes. Decomposition provides significant benefits:
+ It creates clear business alignment by organizing technical components into logical business domains, which simplifies system modernization and maintenance.
+ It accelerates transformation by reducing complexity and enabling faster, more efficient modernization. The smaller modular components also support incremental changes.
+ It enhances agility because teams can update, scale, and integrate modularized systems with modern technologies more easily.
+ It reduces risk because teams can test, migrate, modernize, and maintain smaller, well-defined modules more easily.

When organizations focus on decomposition and align technical components with business domains, they can overcome one of the biggest hurdles in mainframe transformation. This approach creates the foundation for successful modernization and leads to more agile and responsive systems.

You typically start the decomposition process after you complete the analysis phase. The decomposition process requires multiple iterations for grouping programs and components correctly within domains or modules.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
