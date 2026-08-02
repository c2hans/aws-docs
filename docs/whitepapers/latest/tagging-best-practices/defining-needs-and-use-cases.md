---
source_url: https://docs.aws.amazon.com/whitepapers/latest/tagging-best-practices/defining-needs-and-use-cases.html
---

# Defining needs and use cases
<a name="defining-needs-and-use-cases"></a>

Start building your strategy by engaging with stakeholders who have a fundamental underlying need to consume metadata. These teams define the metadata that resources need to be tagged with to support their activities, such as reporting, automation, and data classification. They outline how the resources need to be organized and which policies they need to be mapped to. Examples of roles and functions that these stakeholders can have in organizations include:
+ **Finance** and **Line of Business** need to understand the value of investment by mapping it to costs to prioritize actions that need to be taken when addressing ineﬃciency. Understanding *cost vs value generated* helps to identify unsuccessful lines of business or product offerings. This leads to informed decisions about continuing support, adopting an alternative (for example, using a SaaS offering or managed service), or retiring an unprofitable business offering.
+ **Governance** and **Compliance** need to understand the categorization of data (for example, public, sensitive, or confidential), whether a specific workload is in or out of scope for audit against a specific standard or regulation, and the criticality of the service (whether the service or application is business-critical) to apply appropriate controls and oversight, such as permissions, policies, and monitoring.
+ **Operations** and **Development** need to understand the workload lifecycle, implemented stages of their supported products, and management of release stages (for example, Development, Test, Production split) and their associated support prioritizations and stakeholder management requirements. Duties such as Backups, Patching, Observability and Deprecation also need to be defined and understood.
+ **Information Security (InfoSec)** and **Security Operations (SecOps)** outline what controls must be applied and which are recommended. InfoSec normally defines the implementation of the controls, and SecOps is generally responsible for managing those controls.

Depending on your use case, priorities, size of your organization, and operational practices, you might need representation from various teams within the organization, such as Finance (including Procurement), Information Security, Cloud Enablement, and Cloud Operations. You also need representation from application and process owners for functions such as patching, backup and restore, monitoring, job scheduling, and disaster recovery. These representatives help drive the definition, implementation, and measure the effectiveness of the tagging strategy. They should [https://www.youtube.com/watch?v=aFdpBqmDpzM](https://www.youtube.com/watch?v=aFdpBqmDpzM) from stakeholders and their use cases, and conduct a cross-functional workshop. In the workshop, they get a chance to share their perspectives and needs, and help drive an overall strategy. Examples of participants and their involvement in various use cases are described later in this whitepaper.

The stakeholders also define and validate the keys for mandatory tags, and can recommend the scope for optional tags. For example, Finance Teams might need to relate a resource to an internal cost center, business unit, or both. Thus, they might require that certain tag keys, such as `CostCenter` and `BusinessUnit`, be made mandatory. Individual development teams might decide to use additional tags for automation purposes, such as `EnvironmentName`, `OptIn`, or `OptOut`.

Key stakeholders need to agree on the tagging strategy approach, and document the answers for compliance- and governance-related questions, such as:
+  What use cases need to be addressed?
+  Who is responsible for tagging resources (implementation)?
+  How are tags enforced and what methods and automation will be used (proactive or reactive)?
+  How are tagging effectiveness and goals measured?
+  How often should the tagging strategy be reviewed?
+  Who drives improvements? How is this done?

 Business functions, such as Cloud Enablement, Cloud Business Oﬃce, and Cloud Platform Engineering, can then play a role of facilitators for the process of building the tagging strategy, help drive its adoption, and ensure consistency of its application by measuring progress, removing roadblocks, and reducing duplicated effort.
