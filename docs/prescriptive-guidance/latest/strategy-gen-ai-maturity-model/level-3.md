---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/strategy-gen-ai-maturity-model/level-3.html
---

# Generative AI maturity model level 3: Launch
<a name="level-3"></a>

At this level, organizations transition from proof-of-concept initiatives to the methodical deployment of select, proven generative AI solutions into production environments. This level represents a pivotal shift away from experimentation to focus on robust governance protocols, real-time monitoring systems, and dedicated support infrastructures. Companies focus on launching a few production-grade applications that demonstrate clear business impact. This level emphasizes operational rigor - implementing comprehensive launch frameworks, establishing clear governance guidelines, and maintaining strong security standards. Releasing reliable generative AI solutions that deliver quantifiable results prepares the organization for broader adoption.

This section includes the following topics:
+ [Focus and criteria](#level-3-focus)
+ [Key activities](#level-3-activities)
+ [Transformation strategy to reach the next level](#level-3-transformation)

## Focus and criteria
<a name="level-3-focus"></a>

At this level, organizations systematically deploy generative AI solutions into production environments and implement robust governance, monitoring, and support mechanisms. These mechanisms deliver consistent value and operational excellence while maintaining security and compliance standards. The focus shifts from experimental generative AI applications to deploying production-ready solutions that deliver measurable business value through robust launch processes, comprehensive governance frameworks, and systematic performance monitoring. This level focuses on deploying a select number of production-ready generative AI solutions that serve as foundational implementations for launch frameworks and governance mechanisms.

The following are the criteria for being at this level:
+ Production-ready generative AI solutions are delivering measurable business outcomes.
+ The organization has implemented baseline security, governance, and responsible AI frameworks.
+ Operational controls are established and include automated monitoring and alerting systems.
+ The organization has defined a human-in-the-loop process for AI decisions.
+ For cross-functional AI teams, preliminary roles and operational responsibilities have been defined.

## Key activities
<a name="level-3-activities"></a>

The following table shows the key activities for each pillar of adoption.

|
|
| **Pillar of adoption** | **Activities** |
| --- |--- |
| Business | + Sign off on a first version of a RACI matrix for generative AI operations.+ Identify key roles that are needed for platform architecture, development, and support.+ Measure operational efficiency and business value through comprehensive dashboards.+ Track and optimize operational costs and resource utilization. |
| People | + Create generative AI platform teams or squads for architecture, development, and maintenance.+ Implement an always available, tiered support structure and training programs. |
| Governance | + Obtain formal architecture endorsements from an enterprise architecture review board.+ Establish a responsible AI policy framework and secure stakeholder approvals.+ Create a cross-functional oversight committee for AI implementation reviews.+ For generative AI solutions, maintain documentation for governance approvals, risk assessments, standardized design patterns, and technical specifications. |
| Platform | + Implement automated CI/CD pipelines for generative AI solutions.+ Deploy infrastructure as code (IaC) to manage AWS resources.+ Document design patterns and technical specifications for generative AI solutions.+ Maintain CMDB records for generative AI platform components. |
| Security | + Implement robust security controls for generative AI solutions and their data pipelines.+ Implement a preliminary policy for responsible AI.+ Optimize scalable infrastructure to support real-time data ingestion, vector search, and fine-tuning.+ Conduct regular security assessments and audits.+ Deploy Amazon Bedrock Guardrails to standardize safety and privacy controls across generative AI applications. |
| Operations | + Establish SLA frameworks and performance metrics.+ Monitor model performance and guardrail violations. Set up alerts.+ Create operational dashboards that have automated alerting systems.+ Follow ITIL processes for change management and asset management.+ Established a centralized knowledge repository that contains operational runbooks, playbooks, FAQs, and troubleshooting guides.+ Establish data observability practices. Track data lineage, provenance, and quality metrics to identify gaps before scaling.+ Establish tiered support levels that have clear escalation paths.+ Implement regular performance reviews and analyze customer feedback. |

## Transformation strategy
<a name="level-3-transformation"></a>

To scale generative AI initiatives, organizations should:
+ **Formalize the generative AI operating model** –** **Formalize the RACI matrix across the organization.
+ **Enhance the generative AI platform** – Conduct assessment of existing generative AI implementations to identify reusable patterns and components. Evaluate whether the technology stack is ready to scale. Start to envision and design modular architecture that has centralized prompt management, automated evaluation frameworks, and standardized patterns for efficient scaling of generative AI solutions.
+ **Expand use cases** – Integrate AI capabilities across multiple departments and explore new applications.
+ **Improve the developer experience** –** **Transform the existing platform into a self-service internal platform. This platform is a comprehensive environment that provides standardized tools, workflows, and governance for AI development across the enterprise.
+ **Share knowledge** – Establish inner-source practices and create a component marketplace for sharing reusable AI assets across teams. *Inner-source practices* is the strategy of applying an open source development approach within an organization.
+ **Set up operational scaling** – Enhance your support infrastructure with automated incident response and capacity planning. This prepares the infrastructure to scale for enterprise-wide adoption of generative AI.
+ **Invest in advanced analytics** – Use advanced analytics tools in the cloud, such as [Amazon CloudWatch](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/WhatIsCloudWatch.html) for metrics and [Amazon Quick](https://docs.aws.amazon.com/quicksight/latest/user/welcome.html) for visualization, to use data analytics for continuous improvement.
+ **Review the data governance model **–** **Assess whether your data governance model currently supports self-service capabilities while maintaining standardized policies and access controls. An overly restrictive or centralized approach might hinder your ability to scale data initiatives beyond the core team, especially across diverse business units.

By taking these actions, organizations can:
+ Scale generative AI initiatives across the organization for broad impact.
+ Continue to enhance the platform while identifying opportunities to improve productivity and reusability.
+ Improve the developer experience and reduce cognitive loads.
+ Foster a data-driven culture.
+ Attract top talent by positioning the organization as a generative AI leader.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
