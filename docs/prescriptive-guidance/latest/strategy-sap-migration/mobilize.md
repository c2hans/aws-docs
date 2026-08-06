---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/strategy-sap-migration/mobilize.html
---

# Mobilize phase
<a name="mobilize"></a>

![https://1a9zxhkqsj.execute-api.us-west-2.amazonaws.com/v1/contents/2072f727-3a0b-4e29-9a4f-baa84a3343bb/images/aeafd8e5-5b53-40ee-bff8-7bc4da136ebe.png](http://docs.aws.amazon.com/prescriptive-guidance/latest/strategy-sap-migration/images/guide-img/2072f727-3a0b-4e29-9a4f-baa84a3343bb/images/4265ed75-72cd-4e76-b171-cfcbef961b60.png)

The mobilize phase focuses on refining and blueprinting your target SAP on AWS architecture, supporting the implementation of proof of concept (PoC) projects, and defining migration tooling and planning. This phase builds the foundation for the migration process. It specifies detailed, non-functional requirements, SAP on AWS architecture, landing zone, details of the migration approach, and the refined migration plan. In this phase, the majority of the migration team will be onboarded and briefed for the migration project. The preparation for the migration of SAP workloads will be finalized, to ensure a successful start to the next phase (migration).

The mobilize phase consists of these steps:

1. Plan and implement the PoC based on clearly defined customer criteria.

1. Mobilize and onboard the project team.

1. Refine and completely specify non-functional requirements for SAP on AWS workloads.

1. Map new and existing SAP workloads to a new AWS infrastructure.

1. Design SAP on AWS architecture by following the principles discussed in [SAP Lens - AWS Well-Architected Framework](https://docs.aws.amazon.com/wellarchitected/latest/sap-lens/sap-lens.html).

1. Design and build a new (or refine an existing) landing zone that's compliant with SAP workload requirements.

1. Complete the detailed project plan.

1. Prepare the code required for AWS infrastructure provisioning and SAP initial installations.

1. Prepare and set up the required migration and conversion tools.

|
|
|             Objectives:+ Produce a blueprint for a detailed, future-state architecture of SAP workloads in AWS<br />+ Produce a detailed migration plan<br />+ Finalize the landing zone<br />+ Mobilize and organize migration teams in your organization, at AWS, and at the partner organization) |             Actions:+ Refine detailed customer requirements<br />+ Map existing SAP workloads to AWS services<br />+ Define required tooling and integrations<br />+ Produce a detailed, future state architecture and define transition states<br />+ Produce a detailed migration plan; define roles and responsibilities<br />+ Onboard the project team |
| --- |--- |
| **            Inputs:**+ Outputs from the assessment phase<br />+ Detailed requirements for DR, HA, security, key operational procedures, performance, software versions (operating systems, databases, SAP and non-SAP systems), and integrations<br />+ AWS best practices for migrating and running SAP workloads on AWS |             **Outputs**:+ Detailed migration plan and responsible, accountable, consulted, informed (RACI) matrix<br />+ Detailed requirements for DR, HA, security, separations, DevOps, performance, software versions, and similar considerations<br />+ Detailed technical approach and tooling requirements for migration<br />+ Detailed future-state SAP architecture blueprint<br />+ Landing zone <br />+ Infrastructure as code (IaC) |

To see how Covestro, one of the leading suppliers of premium polymers, chose AWS Professional Services to support their cloud migration and to create a platform architecture that met their needs, see the case study [Covestro uses AWS to Transform Operations and Drive Manufacturing Innovation](https://aws.amazon.com/solutions/case-studies/covestro-case-study/). Covestro moved more than 500 business applications and 1,000 servers from its data centers to an AWS landing zone.

The following illustration provides a simplified example of a typical SAP mobilization project team.

![](http://docs.aws.amazon.com/prescriptive-guidance/latest/strategy-sap-migration/images/guide-img/2072f727-3a0b-4e29-9a4f-baa84a3343bb/images/223ab819-be23-4bc5-8123-14fade6da928.png)
