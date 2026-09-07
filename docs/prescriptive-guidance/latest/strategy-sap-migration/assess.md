---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/strategy-sap-migration/assess.html
---

# Assess phase
<a name="assess"></a>

![https://1a9zxhkqsj.execute-api.us-west-2.amazonaws.com/v1/contents/2072f727-3a0b-4e29-9a4f-baa84a3343bb/images/e2d1ba8e-a949-489d-86ea-0bf6c6838d91.png](https://docs.aws.amazon.com/prescriptive-guidance/latest/strategy-sap-migration/images/guide-img/2072f727-3a0b-4e29-9a4f-baa84a3343bb/images/0c3ef683-6e2f-49fa-8943-79d191f90d60.png)

The assess phase focuses on the evaluation and discovery of your current infrastructure, processes, organizational structure, and requirements for your SAP workloads. This phase often begins as a part of the cloud provider selection process.

The assess phase consists of these steps:

1. When you have selected AWS as a cloud provider, in the preliminary stages of your project, AWS Professional Services verifies all SAP systems and SAP landscapes that are in scope for migration. The goal is to make sure that all data points are valid and to fill in any gaps.

1. The project team prepares a detailed inventory of integrations, batch jobs, and satellite systems that are part of the SAP system landscape, and determines the versions of operating systems, databases, and SAP and non-SAP applications. This includes all compatibility, support, licensing, and compliance requirements. It also includes technical requirements such as the current and projected size of databases, network capacity, required compute performance, and high availability (HA) and disaster recovery (DR) requirements for each application.

1. Organizational aspects are assessed. These include your SAP Center of Excellence and the technical, organizational, and project management capabilities (both in-house and partner-assisted) that would be needed to support migration efforts and to maintain regular operations in parallel with migration. This assessment also includes the operation calendar of the SAP application estate, regular maintenance procedures, backups, and security checks.

1. Business aspects, such as restricted dates, financial closings, peak trading times, and transaction periods, are taken into account. Business inputs on critical topics, such as business continuity, legal and regulatory compliance, data privacy, data residency, and security, are considered.

|
|
| Objectives:+ Transfer knowledge to your teams on migrating to AWS and operating SAP workloads on AWS<br />+ Assess the current SAP architecture, and create an inventory of the current SAP system landscape and ongoing and planned projects<br />+ Define future migration and architecture objectives<br />+ Define the conceptual future-state architecture<br />+ Assess the potential infrastructure and total cost of ownership (TCO) benefits  | Activities:+ Present and discuss options for migrating SAP workloads to AWS, modernization concepts, and examples<br />+ Create an inventory of the current SAP application estate and architecture, and planned customer projects<br />+ Explore migration and modernization strategies and tactics<br />+ Define the conceptual future-state architecture, and, if required, TCO calculations<br />+ Outline a landing zone (that is, a cloud foundation)  |
| --- |--- |
|             **Inputs:**+ Presentations, workshops, and round tables<br />+ Documentation on the current SAP landscape, SAP applications, databases, operating systems, sizing, and similar technical specifications<br />+ Draft migration and architecture objectives such as recovery point objective (RPO), recovery time objective (RTO), HA and DR requirements<br />+ AWS best practices and examples |             **Outputs:**+ Presentation that focuses on SAP on AWS, including high-level migration and architectural concepts, references, and examples<br />+ Migration objectives, tactics, and strategy document<br />+ Conceptual architecture document<br />+ Draft landing zone |

The following illustration provides a simplified example of an SAP on AWS Discovery Workshop that is delivered as a part of the assess phase. Note the active participation of both your teams and AWS Professional Services, with separate agenda items.

![](https://docs.aws.amazon.com/prescriptive-guidance/latest/strategy-sap-migration/images/guide-img/2072f727-3a0b-4e29-9a4f-baa84a3343bb/images/d59e9060-ddf1-45d6-93b5-68ffae76c828.png)
