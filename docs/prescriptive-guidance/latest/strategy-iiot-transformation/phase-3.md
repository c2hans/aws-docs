---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/strategy-iiot-transformation/phase-3.html
---

# Phase 3: Defining a blueprint
<a name="phase-3"></a>

Based on the evaluation of your current state in the previous phase, you can start building your blueprint. A *blueprint* is an end-to-end IIoT system reference architecture you adopt on your digital transformation journey. It serves as the foundation of your IIoT digitalization journey and helps you realize your business objectives. A blueprint:
+ Is guided by your [North Star vision](#north-star-vision)
+ Adheres to the [core tenets of a successful solution framework](#core-tenets)
+ Consists of [repeatable and reusable building blocks](#building-blocks)

Sometimes, you might need a quick proof of concept to demonstrate value and feasibility for certain parts of the blueprint.

## North Star vision
<a name="north-star-vision"></a>

Your blueprint should be guided by your *North Star vision*, which is a clear, concise, and long-term goal that provides direction for making business decisions. If you don't have a North Star vision, think big when creating one. This vision generally takes 3–5 years to realize. To achieve this vision, starting small and scaling fast are the keys to success.

## Core tenets of a successful solution framework
<a name="core-tenets"></a>

To create a unified IT and OT data backbone in your blueprint, you need a functional architecture. Based on our experiences, we've identified the following three core tenets of the solution framework:
+ Maximize insights
  + Democratizing access to data provides diverse insights and drives business value, such as SKU margin optimization.
  + Performing descriptive analytics on real-time or historical operational data helps you monitor KPIs, identify trends, identify potential areas of improvement, and take actions.
  + Performing diagnostic analytics on data helps you identify the root cause of operational events.
  + Performing predictive analytics on data helps you forecast future events in your business and operations.
  + Performing prescriptive analytics on data suggests multiple solutions for solving a given problem, based on descriptive and predictive analytics results.
+ Minimize technical debt
  + Integrating seamlessly with the key existing IT/OT systems eliminates temporary solutions.
  + Automating the deployment pipeline removes manual process from your operations.
  + Standardizing tools prevents proliferation of tools and bespoke applications.
  + Using centralized management services to deploy standardized configurations across the environment, preventing the use of non-standard and potentially problematic configurations at the local site.
  + Creating patterns for updating and deploying infrastructure automatically or with minimal intervention for repeatable tasks. Examples include updating operating systems, periodically rotating device certificates, installing patches, or scaling data storage.
  + Designing and implementing repeatable and reusable patterns for rapid production deployment across sites at scale.
+ Modular and future-proof blueprint
  + Designing for interoperability with existing IT/OT systems and infrastructures.
  + Designing for modularity, which helps you start small and scale fast, iteratively add new components, and select the best option for your use case.
  + Designing for flexibility with existing (*brownfield*) and new (*greenfield*) infrastructures.

## Repeatable and reusable building blocks
<a name="building-blocks"></a>

The *building blocks* of an IIoT digital transformation journey are the various functional layers, considerations, and use cases that comprise the blueprint. The following image shows the high-level repeatable and reusable functional building blocks of a blueprint.

![The high-level building blocks of the conceptual architecture in a blueprint.](https://docs.aws.amazon.com/prescriptive-guidance/latest/strategy-iiot-transformation/images/guide-img/2cc5efa2-2b32-4bb7-bd9d-d0a92a28e1ac/images/58b88f26-7653-4e44-a8a4-d95b0f220a6b.png)

The following are the layers of a blueprint:
+ **Data ingestion** – This edge layer collects data from various sources in your on-premises infrastructure or cloud environment. Typical IT/OT data sources might include telemetry data from supervisory control and data acquisition (SCADA) systems, distributed control systems (DCS), PLCs, secondary sensors, manufacturing execution systems (MES), software as a service (SaaS) and legacy applications, enterprise resource planning (ERP) systems, customer relationship management (CRM) systems, various supply chain systems, and data historians.
+ **Edge insights and applications** – Depending on your use cases, you might want to deploy this edge layer. This layer is used to address any low latency and data residency requirements for your architecture, support production continuation when disconnected from the cloud, and enable innovation at the edge.
+ **Data management** – This layer is responsible for various aspects of typical data management functions, such as:
  + Building and managing semantic data models (SDMs) for IT/OT resources for governance. Adding contexts to the machine data by using a semantic data model helps with downstream analytics for process and machine modeling.
  + Storing the data collected in the data ingestion layer. Use the data stored in this layer for processing and providing local insights, and for providing store-and-forward functionality when disconnected from the cloud.
  + Processing the data in the cloud to meet various consumption needs for end users, such as data integration, data normalization, data enrichment, data quality, data discovery, data catalog, and search.
  + Enabling a flexible data consumption service for external consumers to provide business insights.
+ **Data insights** – This cloud layer is used for business insights that range from simple, such as near real-time KPI dashboards, to advanced, such as predictive maintenance, demand forecasting, and inventory management that uses the flexible data consumption service from the data management layer.
+ **Data serving** – This cloud layer is used to democratize access to the data for various end users, such as various OT personas, data scientists, data engineers, and data analysts. This layer seamlessly serves data to other enterprise systems and third-party solutions to enable use cases and business applications.
+ **Use cases and business applications** – This is the top layer of the architecture. This cloud layer contains the business applications and tools that address your business use cases. As needed, the applications and tools in this layer access the data and insights in the supporting layers.
+ **Cross-cutting considerations** – This layer contains key non-functional requirements that apply to the data sources, edge, and cloud. This layer includes must-have elements, such as end-to-end security, configuration management, logging, compliance, and regulatory requirements. This layer helps you securely and efficiently operate your architecture, providing opportunities to enhance performance, reduce costs, or use automations that enable rapid deployment at scale across sites.

To create this unified data solution, we recommend using a unified functional architecture similar to the one presented. This holistic approach helps you think big, start small, and scale fast. Rather than taking on the entire digital transformation journey at once and making the journey impossibly difficult, you keep iterating on smaller deliverables that help you achieve your business outcomes. You might already have some of these building blocks in place today, and if so, you can reuse them.

## AWS IDP solution offering
<a name="aws-idp"></a>

AWS Professional Services uses a tried-and-tested approach, AWS Industrial Data Platform (IDP), to discover, design, and implement a flexible and extensible unified data solution for Industry 4.0 (also known as *smart manufacturing*,* smart factory*, or* smart industrial*) success. The AWS IDP addresses a catalog of common use cases, such as:
+ Operational and actionable KPIs for production and asset optimization, including overall equipment effectiveness (OEE), throughput, yield, and cycle time
+ Automated quality and defect management solutions for predictive quality
+ Predictive maintenance that reduces downtime and catastrophic equipment failures
+ Energy optimization and carbon footprint reduction for sustainable manufacturing
+ Supply chain optimization, including inventory management, demand forecasting, and track and trace

Your blueprint architecture might vary based on your use cases, your current state assessment, and the identified gaps. For more information about the relevant AWS services that you can use in your blueprint, see the [AWS Industrial Data Platform (IDP) reference architecture](https://d1.awsstatic.com/architecture-diagrams/ArchitectureDiagrams/industrial-data-platform-ra.pdf).
