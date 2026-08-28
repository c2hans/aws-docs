---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/strategy-transform-adm-operating-model-gen-ai/adm-op-model.html
---

# Overview of an ADM operating model
<a name="adm-op-model"></a>

Transitioning from typical IT operating model concepts to the specific context of ADM requires understanding how these principles apply to software development and maintenance processes. The ADM operating model provides a comprehensive framework to manage the entire application lifecycle from planning to development to maintenance. It helps achieve successful alignment between business goals and IT execution.

Creating an ADM operating model is typically a shared responsibility between the *customer *(business and in-house IT) and/or *partners* (application managed services (AMS) delivered by consulting and technology partners). This collaborative approach makes use of diverse expertise and aligns with the organization's specific needs and technological landscape.

As shown in the following diagram, an ADM model consists of interconnected layers that play critical roles:
+ [Business layer](#adm-business-elements) – This top layer aligns ADM activities with the organization's strategic goals. Here, leaders define business strategy, shape enterprise architecture, and establish governance mechanisms. As generative AI integration becomes more prevalent, this layer becomes increasingly dynamic. It facilitates rapid and continuous alignment between business objectives and development activities.
+ [Service integration layer](#adm-service-int-elements) – This operational nexus bridges the gap between business needs and technical implementation. As organizations introduce generative AI, this layer orchestrates complex interactions between human teams and AI systems to deliver seamless services.
+ [Organization structure layer](#adm-org-structure-elements) – This layer focuses on people, process, and technology, and it experiences significant changes during AI integration. Roles will evolve, teams will reimagine processes, and the technology stack will expand to include AI tools. This layer drives the practical implementation of an organization's generative AI transformation.
+ [Organization capability layer](#adm-org-capability-elements) – This foundational layer involves the strategic distribution of resources globally and the cultivation of essential skills and expertise needed for AI-augmented ADM. As AI integration progresses, this layer plays a crucial role in developing new competencies, establishing Centers of Excellence (COE), and fostering a culture of continuous learning.

![The four layers of an ADM model are business, service integration, organization structure, and organization capability.](http://docs.aws.amazon.com/prescriptive-guidance/latest/strategy-transform-adm-operating-model-gen-ai/images/guide-img/b9a9e359-a4e7-4079-8cd0-44ed873cc2c3/images/fc6c64ad-8e32-4a19-98c7-c4995162a06b.png)

As organizations prepare to integrate generative AI into their ADM practices, they can reshape each layer of this model as necessary. Organizations can reimagine SDLC processes, redefine roles, and recalibrate technology stacks to benefit fully from generative AI.

The true power of an ADM operating model lies in its ability to transform and manage change. This transformation requires close collaboration among all stakeholders to help ensure a cohesive and effective implementation of AI-augmented ADM practices.

For more details about each layer, see the following sections:
+ [Business layer elements in an ADM operating model](#adm-business-elements)
+ [Service integration layer elements in an ADM operating model](#adm-service-int-elements)
+ [Organization structure layer elements in an ADM operating model](#adm-org-structure-elements)
+ [Organization capability layer elements in an ADM operating model](#adm-org-capability-elements)

## Business layer elements in an ADM operating model
<a name="adm-business-elements"></a>

The customer is responsible for activities related to the following elements:
+ Business strategy
  + Improve the customer experience and drive key business outcomes
  + Modernize core systems for high business impact
  + Enhance agility and innovation capabilities
+ Business line and support functions (Geographic areas and country)
  + LOBs
  + Marketing
  + Human resources
  + Procurement
  + Legal
  + Information technology (IT)
+ Dashboards, KPIs, and reporting
  + Service performance reporting
  + Service level agreement (SLA) and operating level agreement (OLA) monitoring and reporting
  + Business performance reporting
+ Governance, risk, and compliance
  + Steering committee and quarterly review
  + Risk assessment and management
  + Audits, compliance, and regulatory reporting
+ Enterprise and IT architecture
  + Business-aligned IT strategy
  + Architecture and design principles
  + Technology standards and policies
+ Budgeting and forecasting
  + Budget planning and control
  + Financial performance management
  + Demand forecasting and planning
+ Business value
  + Improve resiliency
  + Improve productivity
  + Improve business agility
  + New feature release

## Service integration layer elements in an ADM operating model
<a name="adm-service-int-elements"></a>

This layer includes the following key areas of service management (responsibility of the consulting and technology partners) and service governance (responsibility of the customer):
+ **Service management** encompasses delivery of IT services including service desk, incident and problem management, change management, and service level management. AI-powered automation and intelligent support capabilities enhance service quality and efficiency.
+ **Service governance** focuses on oversight and control mechanisms including service validation, availability management, capacity planning, and configuration management. With effective service governance, services align with business objectives while maintaining compliance and performance standards.

## Organization structure layer elements in an ADM operating model
<a name="adm-org-structure-elements"></a>

The organization layer focuses on people, process, and technology.

Partners are responsible for activities related to *people* elements. In some cases, customers have a co-sourced engagement model resulting in shared responsibility for the following:
+ Organization structure and people roles
  + Product management – Project owner and business analyst
  + Project management – Project manager, Scrum Master, and Agile Coach
  + Architecture and design – Solution architect, technical lead, and user experience (UX) designer
  + Development – Software developer and user interface (UI) designer
  + Quality assurance – Testing lead, quality assurance (QA) tester, and performance engineer
  + Operations – DevOps engineer and release manager
  + Support and maintenance – Support engineer and technical writer
  + Subject matter experts (SME) – Security subject matter experts (SMEs), integration SME, and domain-specific SMEs

Partners are responsible for activities related to the following *process* elements:
+ Application functional management services
  + Business process management
  + Information and data management
  + Functional management
+ Application development services
  + Project and requirement management
  + Architecture
  + Design and development
  + Testing and quality assurance (QA)
+ Application maintenance services (Operations)
  + Services support management (ITSM)
  + Service request management
  + Updates and patch management
  + Service improvements
+ Application technical management services
  + Application basics support (Level 1)
  + Middleware management
  + Database management
  + Service improvements
+ Platform management services
  + Managed landing zone
  + Managed operating system (OS)
  + Database
  + Observability
  + Security
  + Network
  + Backup
  + Integration
  + Cloud financial
  + Other services

Partners are responsible for activities related to implementation and management of the following *technology* elements:
+ Technology and tools
  + Includes cloud, virtualization, containers, operating systems, databases, and other management tools
  + Developer tools and integrated development environments (IDEs)
  + Continuous integration and continuous development (CI/CD) tools
  + Bug fix and IT service management (ITSM) tools
+ Technology and consulting partnerships
  + Hyperscaler (AWS and others)
  + Technology ISVs
  + IT/Service desk supplier
  + Infrastructure outsourcing (Network, data center, security, and workplace services)

## Organization capability layer elements in an ADM operating model
<a name="adm-org-capability-elements"></a>

Generally, customers hold accountability for making the key decisions about the following activities:
+ Program and change management capabilities
  + Portfolio management
  + Feature and backlog management
  + Organization change management
+ Collaboration and communication capabilities
  + Productivity tools
  + Collaboration tools
  + Communication tools
+ Knowledge base management
  + Market research
  + Customer feedback and issues resolutions
  + Business and domain knowledge
+ Onshore locations, such as corporate office, regional office, or remote sites
+ Captive centers

One or more consulting partners are responsible for implementing and managing activities related to the following elements:
+ Nearshore delivery locations
+ Offshore delivery locations
+ Talent acquisition, training and certification, and resource management
+ Centers of Excellence
  + Innovation
  + Technology evaluation and proof of concept (POC)
  + POVs, best practices, standards, and policies

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
