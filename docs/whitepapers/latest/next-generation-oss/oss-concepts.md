---
source_url: https://docs.aws.amazon.com/whitepapers/latest/next-generation-oss/oss-concepts.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# OSS Concepts
<a name="oss-concepts"></a>

 There are two conceptual views to define an OSS solution: a business-centric view and a network-centric view. Before diving into the recommended OSS solution architecture on AWS, the following section deconstructs OSS concepts and associates them with technical requirements that are the foundations of the proposed OSS solution on AWS.

## Business-centric view
<a name="business-centric-view"></a>

The business-centric view of OSS aligns with the enhanced Telecom Operations Map (eTOM), where OSS applications provide capabilities in fulfillment, assurance, and operations support and readiness. This logical representation helps define which outcome an OSS component is aligned with, which helps DSPs to ensure their ability in delivering their services.

 Service fulfillment enables the service provider to plan, build, provision, and activate an end-to-end service. These are OSS applications that help with the creation of an Ultra Reliable Low Latency Communications (URLLC) network slice dedicated to self-driving cars, the activation of a cell site, customer equipment, the provisioning of new optical transport equipment, and more high-level services like voice over 5G.

 Service assurance enables the service provider to optimize the Quality of Service (QoS) associated with its networks and services. These OSS applications ensure that end users are provided with the best quality of experience by enabling the monitoring of Service Level Agreement compliance and providing clear information on existing problems while predicting future problems and enabling preemptive correction.

 Operations support and readiness (OSR) equips service providers with the tools, architecture, and environment to execute fulfillment and assurance processes efficiently. Next-generation OSS is geared towards extreme automation across all business processes by enabling self-planning, self-optimizing, and self-healing capabilities. For example, users can cross-correlate the data to improve customer satisfaction (e.g. by enabling proactive fault notifications), or recommend specific services based on existing service consumption.

## Network-centric view
<a name="network-centric-view"></a>

 The network-centric view of OSS aligns with the Open Systems Interconnection (OSI) network management model where OSS applications are grouped into the following five categories: Fault, Configuration, Accounting, Performance, and Security (FCAPS).
+  **Fault management (FM)** encompasses software that helps a CSP understand whether a network component, network subsystem, and/or network is healthy or in a faulty mode. It helps with detection, correction, isolation, and recovery of faults, and generation, handling, distribution, and clearance of alarms.
+  **Configuration management** includes software that helps a CSP define the characteristics of their network components. It helps with network/system discovery, inventory cataloging, capacity and resource availability, provisioning, rollback, and configuration life cycle management.
+  **Accounting** helps with network/system usage, managing quotas, audits, costing, and applicable fraud management measures. Software within this category supports Business System Support (BSS) systems as well.
+  **Performance Management (PM)** includes software that helps a CSP understand its network performance of its network, network functions, and up to the smallest components of their network functions. It handles the network/system utilization, report generation, metrics that are specific to system performance, and capacity planning.
+ **Security** helps with access management, audits, incident reporting and management, and compliance. It allows CSPs to define who accesses what areas of their network components, security of the software supporting the network operations, encryption of data residing and transiting through their network, etc.

   By tackling both network and business views, the proposed OSS Solution on AWS can help CSPs to reduce the complexity of their operations while helping them in uniformizing their operations.

### Network Characteristics
<a name="network-characteristics"></a>

 For an OSS solution to provide value, it should align with network characteristics while fulfilling DSPs’ business outcomes. At its core, an OSS solution’s intent is to facilitate the management and the enablement of a given network.

 A telecommunication network is comprised of numerous Network Functions (NFx) that are categorized as wireless and wireline network functions. Such functions span physical and software equipment such as routers, firewalls, Mobility Management Entity (MME), Evolved Node B (eNodeB), Access and Mobility management Function (AMF), User Plane Function (UPF), small cells, microwave backhaul, 5G New Radio (5G NR), and many more. Each of these NFx must be provisioned, monitored, analyzed, configured, and secured. An OSS architecture on AWS can help you reduce the complexity inherent to managing a complex network comprised of many NFx, often from many Network Equipment Providers (NEPs).

### Fault Management
<a name="fault-management"></a>

 Telecommunication networks are inherently critical to our lives. For example, their network architecture must align with regulatory constraints that require high availability services (e.g. emergency services numbers like 9-1-1).

**Note**
NFx and General Architectural guidelines are not discussed in this whitepaper. An OSS architecture on AWS can help you identify when a network component is at fault, and provide or act on that information in near real-time.

 Different NFx can have different impacts on a given service provided to a consumer. Based on the impact and the type of information NFx can generate, a CSP may require an alarm/event to be treated on the fly or stored for future analysis. An OSS architecture on AWS can help process an alarm with or without storing it. Similarly, it supports numerous storage options.

A given NFx can become faulty at any time for numerous reasons: loss of power, faulty software, faulty hardware, faulty operations, natural disasters, etc. These events follow a random pattern. They could be isolated to a unique NFx, generalized to a few NFx, or impacting a large amount of NFx. An OSS architecture on AWS can help you scale up and down based on the flow of alarms coming from the network.

 Given the complexity of the network and the plurality of components in a given service path, a CSP’s OSS solution should help in identifying which faulty component results in network degradation (of any form) while filtering noise. For example, a down S1 interface will result in both eNodeB and MME alarms. An OSS architecture on AWS can help you identify which element is faulty through alarm correlations, configuration knowledge, logical and physical inventory information, learning historical behaviors, and using predictive models.

### Configuration Management
<a name="configuration-management"></a>

 Configuration Management (CM) is a central part of an OSS solution. CM includes applications that help manage NFx configuration and provides an inventory layer to subsequent OSS applications as well as BSS applications. Note that in this document, we purposely didn’t expand on Inventory Management (IM), which is a critical component to CM. At its core, CM is a database (or many databases) that is constantly updated with network CM data and constantly requested by network CM data consumers. It provides a centralized view of the network.

The amount of network changes a CM solution should support varies based on use cases. A DSP may want to optimize an NFx or push a new service to thousands of NFx. Similarly, events can occur on one NFx or many NFx that cause NFx configuration to self-change their behavior and configurations. To efficiently support this behavior, an OSS architecture on AWS can help you scale up and down based on the amount of network changes requested, ingested, or processed, whether programmatically or by users.

 When a change event (or a service state change) occurs on an NFx, a DSP may want to trigger a script that fine tunes the NFx itself or other NFx without negatively impacting the NFx, other NFx, and the overall service delivery. An OSS architecture on AWS can help you be responsive and support the positioning of the CM workload to reduce latency when needed.

 DSPs have to handle a new layer of complexity with the introduction of new architectures and new concepts, such as 5G. Each of these new NFx and new architectures bring more data for the CM solution to handle. With financial pressure, limited knowledgeable engineer availability, and time-to-market requirements, DSPs are looking for a CM solution that incorporates machine learning concepts to gain insight from their network configuration, identify patterns and anomalies, and support automation. An OSS architecture on AWS can help you leverage data lake concepts to enable an intelligent and self-operating network.

### Performance Management
<a name="performance-management"></a>

 PM encompasses applications that help manage NFx performance. PM allows a DSP to enable observability with a specific granularity on a given NFx, multiple NFx, and network wide. An OSS architecture on AWS provides DSPs with the network analytics capabilities that give them insight on their network performance while their network evolves.

 An OSS architecture on AWS can help DSPs to automatically discover their NFx datasets as their network evolves, while having the ability to ingest large amounts of information in a scalable manner. The reference architecture provided in this whitepaper helps your solution to be cost-efficient by reducing data duplication. This is achieved by building a PM solution on top of a data lake to simplify the navigation through a large amount of data, and providing the required data governance.

 Our proposed OSS Architecture on AWS can help DSPs reduce their operational costs by providing programmatic data insights and enabling the development of workflow based on performance data. It provides DSPs with the ability to identify which components have the most negative impact on their overall network performance while learning what series of configuration, changes, faults, and KPIs result in performance degradation.

 The proposed OSS Architecture on AWS enables data enrichment and learning from past events. It supports constant innovation by providing an architecture that allows for quick experimentation and quickly building applications (graphical, programmatic, storage quarriable, etc.).

### Security Management
<a name="security-management"></a>

 Security Management is a critical component to an OSS solution. It can be viewed in two parts:
+  Security of the OSS solution.
+  Security of the network it manages.

 First, as defined in [AWS Well-Architected Framework](https://docs.aws.amazon.com/wellarchitected/latest/framework/welcome.html), our proposed AWS Architecture on AWS is built on the seven design principles for security in the cloud:
+ Implement a strong identity foundation
+ Enable traceability
+ Apply security at all layers
+ Automate security best practices
+ Protect data in transit and at rest,
+ Keep people away from data
+ Prepare for security events

The proposed OSS architecture on AWS helps you identify operational mistakes, identify risk vectors before they appear, predict operational mistakes, and prevent malicious parties from having prime access to a DSP’s network.

 Second, the proposed OSS architecture on AWS simplifies securing the network it manages. This is achieved by providing auditing capabilities to determine if an NFx’s configuration deviates from a secure gold standard, and by providing automation that addresses identified security issues. Similarly, the proposed OSS architecture on AWS can help you simplify the distribution of security updates to both physical and virtual NFx, providing the scalability to adequately upgrade a large portion of the network while minimizing network impact. Finally, the proposed architecture can help you to simplify the encryption of network traffic and Operations, Administration and Maintenance (OAM) traffic while reducing the encryption cost.

 By having an OSS solution that enables securing the network while providing DSPs with the security governance to protect a given network, DSPs can benefit from enhanced security compliance.

 The proposed next-generation OSS architecture on AWS can help you align with the BSS solutions of the future to eliminate traditional business and operational silos. It’s critical to view network data that enables business logics as easily-made-accessible by the OSS stack, while also providing the framework to enrich data based on business logic. This convergence of BSS and OSS stacks is a key enabler to CSPs becoming DSPs. This combination of BSS and OSS capabilities in a unified layer supporting the business and operations of DSPs is also called Digital Support System (DSS).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Whitepapers. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query whitepapers` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
