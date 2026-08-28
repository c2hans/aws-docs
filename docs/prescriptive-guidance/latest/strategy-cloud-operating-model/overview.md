---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/strategy-cloud-operating-model/overview.html
---

# Cloud Operating Model overview
<a name="overview"></a>

This document provides a definition of the Cloud Operating Model and core capabilities that organizations should focus on when building their own model.

## What is a Cloud Operating Model, and why do you need one?
<a name="what-is-com"></a>

We use the phrase *Cloud Operating Model* to refer to the operating model within an IT organization that is used to build, mature, and optimize one or more cloud environments. The ability to build maturity across a number of capabilities that move the IT organization in the same direction as the overall transformation strategy is becoming ever more important. We coach customers to use the opportunity of defining their Cloud Operating Model to explore cloud-first ways of working that will provide a solid foundation for the continuous evolution of their whole organization. Our experience shows that if you don't spend time on this aspect of your cloud journey, the initiative will stall and your organization will struggle to realize value from your transformation efforts.

This view is backed up by the report [Predicts 2023: Collaborate, Automate and Orchestrate to Optimize Costs and Value During the Economic Crisis](https://www.gartner.com/en/documents/4020625) on the Gartner website, in which they summarize that infrastructure and operations leaders should use workload orchestration, automation, and collaborative practices to achieve the goal of delivering value while optimizing costs.

However, you cannot just implement these recommendations. They require an understanding of your current capabilities, how these capabilities are organized to meet operational requirements, and a plan to increase maturity across your teams. In effect, you need to understand your Cloud Operating Model so you can position your organization to execute on the cloud strategy. Your Cloud Operating Model must then evolve over time as capabilities continue to mature and your organization gains more value from the transformation.

## Key Concepts
<a name="key-concepts"></a>

To start, let's define the key concepts used in this paper, because the terminology and approach can differ across cloud providers.

## Capabilities
<a name="capabilities"></a>

We use *capabilities* as a collective term that covers people, process, and technology. Because there is an inclination to only focus on the technology aspects of the cloud and deprioritize the people and process angles, the term *capabilities* joins these three aspects to describe *the ability to do something*. This collective term also simplifies the identification of the people, process, and technology changes required at each point in your cloud journey.

## It's a continuous journey
<a name="continuous-journey"></a>

Defining a new operating model is not a one-time exercise. You need to build a model and supporting mechanisms that can serve the needs of the organization today, but, as cloud capability matures, can evolve and continuously improve over time to meet changing needs.

## The AWS Cloud Operating Model Framework
<a name="com-framework"></a>

The AWS Cloud Operating Model (COM) Framework consists of 73 capabilities, grouped into 17 domains and 5 perspectives, as illustrated in the following diagram.

![The AWS Cloud Operating Model Framework](http://docs.aws.amazon.com/prescriptive-guidance/latest/strategy-cloud-operating-model/images/guide-img/9a407f0b-ea38-4662-8d39-755295f71238/images/a2a0b318-a057-4ffa-839d-245b0c38ed2c.png)

|
|
| Perspectives | Operations Leadership | Cloud Operations | Platform Enablement | Service Management | Cost and Governance |
| --- |--- |--- |--- |--- |--- |
| **Domains** | + Operations leadership<br />+ Organization | + Resiliency<br />+ Observability<br />+ Security operations | + Architecture and patterns<br />+ Lifecycle management<br />+ Provisioning and vending | + Capacity management<br />+ Knowledge dissemination<br />+ Operational reporting<br />+ Operations partners<br />+ Process enablement<br />+ Product management<br />+ SME services | + Financial management<br />+ Resource/estate management |

Using a framework like ours supports the development of your Cloud Operating Model by providing consistency as you understand, organize, design, implement, and mature your organization in line with the goals of your transformation journey.

## A Cloud Center of Excellence is not a Cloud Operating Model
<a name="ccoe"></a>

A Cloud Center of Excellence (CCoE) has become a well-known concept when migrating to the cloud or running workloads in the cloud. However, the CCoE is not a Cloud Operating Model. It is a cross-organizational leadership function that supports successful cloud adoption across the enterprise through alignment, enablement, and automation; whereas the Cloud Operating Model is the operating model within an IT organization that is used to build, mature, and optimize one or more cloud environments.

The following table summarizes the differences between the two terms.

|
|
|   | Cloud Operating Model | Cloud Center of Excellence |
| --- |--- |--- |
| **Use case** | When you have significant workloads in the cloud, but you aren't meeting the key performance indicators (KPIs), business outcomes, or values you were expecting to gain from the cloud over traditional on-premises approaches | When progress has stalled or your organization needs to enable the adoption of the cloud and new ways of thinking, deciding, behaving, and innovating by standardizing best practices for autonomous work |
| **Teams included** | IT and business teams | Cross-functional, multi-skilled resources aligned to the Cloud Leadership Team, Cloud Business Office, and Cloud Platform Engineering |
| **Focus** | Supporting, enabling, and optimizing cloud workloads by maturing your organization's existing operating model and capabilities to adopt cloud-first ways of working | Establishing an entity to accelerate and build technical and cultural foundations to enable migration and innovation |
| **Expected outcomes** | Greater operational efficiencies, reduced cost of IT delivery, reduced risk, greater agility, and more innovative technical capabilities and services | Accelerated and sustainable cloud adoption; empower cloud-driven products teams with a self-service environment, minimized disruptions, greater adoption of standardized approaches and patterns, and increased productivity that accelerates delivery; optimized agility and value of cloud; scale through ongoing risk mitigation |

There are similarities in the capabilities required by a Cloud Operating Model and a CCoE. However, because the CCoE focuses on the move to the cloud, it requires more capabilities, such as People Enablement and Organizational Acceleration. To be successful, a CCoE has to fit and work within the existing operating model, but the two are distinct concepts and the two terms aren't interchangeable.

## Managing your workforce
<a name="workforce"></a>

We often work with customers who are transitioning from on premises to cloud environments. This means that at the point of engagement with AWS, the majority of their infrastructure and workloads are still on-premises and still require management, often by the same teams that are part of the migration or transformation program. In the report [25 Amazing Cloud Adoption Statistics [2023]: Cloud Migration, Computing, And More on the Zippia website](https://www.zippia.com/advice/cloud-adoption-statistics/) (Zippia.com, June 22, 2023) the writer notes that 94 percent of enterprises surveyed use some form of cloud services. However, the same report says that by 2026 only 45 percent of enterprise IT budget will be on cloud expenses. This means that despite ubiquitous cloud services, large on-premises estates will continue to exist and will need to be managed. Therefore, many enterprises organize their workforce to deliver both cloud and non-cloud services. Building your Cloud Operating Model incrementally means that you can focus on what's needed now as well as what's coming next, and adapt as you go along to ensure that you are managing your workforce in a way that's sustainable to the teams involved.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
