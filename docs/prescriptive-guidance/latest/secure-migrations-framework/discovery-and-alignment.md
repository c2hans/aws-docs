---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/secure-migrations-framework/discovery-and-alignment.html
---

# Security discovery and alignment
<a name="discovery-and-alignment"></a>

When mobilizing a migration project, the first domain for the security and compliance workstream is *security discovery and alignment*. This domain is intended to help your organization achieve the following goals:
+ Train the security and compliance workstream about the AWS security services, capabilities, and compliance adherence
+ Discover your security and compliance requirements and current practices. Consider these requirements from an infrastructure and operations standpoint, including:
  + Security challenges and drivers for the target end state
  + Cloud security team skillset
  + Security risk and compliance policies, configurations, controls, and guardrails
  + Security risk appetite and baseline
  + Existing and prospective security tooling

## Immersion day workshops
<a name="immersion-day-workshops"></a>

To align on these goals, use security and compliance immersion days. *Immersion days* are workshops that cover a range of security-related topics, such as:
+ [AWS shared responsibility model](https://aws.amazon.com/compliance/shared-responsibility-model/)
+ [AWS security services](https://aws.amazon.com/products/security/)
+ [AWS Security Reference Architecture (AWS SRA)](https://docs.aws.amazon.com/prescriptive-guidance/latest/security-reference-architecture/)
+ [AWS compliance](https://aws.amazon.com/compliance/)
+ [Security Pillar](https://docs.aws.amazon.com/wellarchitected/latest/security-pillar/welcome.html) of the AWS Well-Architected Framework

The immersion day workshops help establish a knowledge baseline for your security team. It trains them about AWS security services and security and compliance best practices. AWS Solution Architects, AWS Professional Services, and AWS Partners can help you perform these interactive workshops. They use standard presentation decks, AWS labs, and whiteboard activities to help prepare your teams.

## Discovery workshops
<a name="discovery-workshops"></a>

After the immersion day workshops, you perform multiple deep-dive security and compliance discovery workshops. These help your teams discover the current security, risk, and compliance (SRC) requirements of the infrastructure, applications, and operations. You analyze these requirements through the following perspectives: people, process, and technology. The following are the areas of discovery for each perspective.

### People perspective
<a name="people-perspective.81504aa1-1aa7-58cd-9b7f-affe28b8356d"></a>
+ **Organizational structure **– Understand the current security and compliance workstream structure and responsibilities.
+ **Capabilities and skillsets **– Have practical knowledge and skillsets for AWS services and for cloud security and compliance capabilities. This includes discovery, planning, implementation, and operations.
+ **Responsible, accountable, consulted, informed (RACI) matrix** – Define the roles and responsibilities for current security and compliance activities within the organization.
+ **Culture **– Understand the current security and compliance culture. Prioritize security and compliance as part of build, design, implementation, and operation phases. Introduce Development Security Operations (DevSecOps) into the cloud security and compliance culture.

### Process perspective
<a name="process-perspective.462d4629-38d4-52ef-a0b5-d164db1ab55a"></a>
+ **Practices** – Define and document the current security and compliance processes to build, design, implement, and operate. Processes include:
  + Identity access and management
  + Incident detection controls and response
  + Infrastructure and network security
  + Data protection
  + Compliance
  + Business continuity and recovery
+ **Implementation documentation **– Document security and compliance policies, control configurations, tooling documentation, and architecture documentation. These documents are required to cover security and compliance from the infrastructure, network, applications, databases, and deployment areas.
+ **Risk documentation** – Create information security risk documentation that outlines the risk appetite and threshold.
+ **Validations **– Create internal and external security validation and audit requirements.
+ **Runbooks** – Develop operational runbooks that cover the current, standard implementation and governance processes for security and compliance.

### Technology perspective
<a name="technology-perspective.2ba9b117-f8d0-56ef-9cf3-505c07f21db0"></a>
+ **Services and tools** – Use tools to validate your security and compliance posture and to enforce and govern the current IT landscape. Establish tooling for the following categories:
  + Identity access and management
  + Incident detection controls and response
  + Infrastructure and network security
  + Data protection
  + Compliance
  + Business continuity and recovery

During the AWS security discovery workshop, you use standardized data collection templates and questionnaires to collect data. In scenarios where you are unable to provide the information due to lack of data clarity or obsolete data, you can use a migration discovery tool to collect application and infrastructure-level security information. For a list of discovery tools that you can use, see [Discovery, planning, and recommendation migration tools](https://aws.amazon.com/prescriptive-guidance/migration-tools/migration-discovery-tools/) on AWS Prescriptive Guidance. The list provides details about each tool's discovery capabilities and usage. It also compares tools to help you choose the best tool to meet your IT landscape requirements and constraints.

During the initial security assessment, we highly recommend that you start with threat modeling. This helps you identify possible threats and existing measures that are in place. There might also be predefined and documented requirements for security, compliance and risk. For more information, see the [Threat modeling for builders workshop](https://explore.skillbuilder.aws/learn/course/external/view/elearning/13274/threat-modeling-the-right-way-for-builders-workshop) (AWS training) and see [How to approach threat modeling](https://aws.amazon.com/blogs/security/how-to-approach-threat-modeling/) (AWS blog post). This This approach helps you reconsider your security and compliance strategies for deployment, implementation, and governance in the AWS Cloud.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
