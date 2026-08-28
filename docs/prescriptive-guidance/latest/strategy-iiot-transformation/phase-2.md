---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/strategy-iiot-transformation/phase-2.html
---

# Phase 2: Evaluating your current state
<a name="phase-2"></a>

A complete IIoT digital transformation journey encompasses not only the IIoT-specific devices and strategy but also a holistic consideration of how those IIoT assets integrate with your IT and OT infrastructure and operations personas. Your infrastructure might be *on-premises* (local), or it might be *hybrid* of both on-premises and cloud infrastructure. Migrating your infrastructure to the cloud allows you to take full advantage of cloud-native features to improve agility, performance, and scalability.

In this phase, you do the following:

1. [Focus on people and culture](#focus-on-people-and-culture)

1. [Discover your current systems and technology stack](#discovery)

1. [Review other key considerations](#other-considerations)

AWS Professional Services uses a set of prescriptive offerings that are tried-and-tested with other customers. We can help you assess your current state and build a phased roadmap for your target state.

## Focus on people and culture
<a name="focus-on-people-and-culture"></a>

One of the key challenges is not having the proper team skill sets to enable and sustain the IIoT digital transformation. You need to upskill your team, create new roles, and hire new talent to drive success. [Unlocking success in digital transformations](https://www.mckinsey.com/business-functions/people-and-organizational-performance/our-insights/unlocking-success-in-digital-transformations) (McKinsey & Company survey report) states that "The digital transformation success is more than three times likelier when respondents say their organizations have invested the right amount in digital talent." We recommend you consider the following topics to assess the skill sets of your current team and take actions accordingly:
+ Cloud technology stack expertise
+ Primary technical skill sets such as:
  + IIoT
  + Machine learning (ML)
  + Data analytics tools and methods
  + Data lakes
  + Online analytical processing (OLAP) and online transaction processing (OLTP) systems, such as SQL/NoSQL databases and data warehouses
  + Business intelligence tools
  + Real-time monitoring tools
  + Web application development, including frontend and backend
  + Operating systems, such as Linux
  + Programming languages, such as Java, Python, JavaScript
+ The resources to build software products and solutions, including:
  + Business analyst
  + Product owner
  + Project manager
  + UX/UI designer
  + Software architect
  + Data architect
  + IoT architect
  + Software developer
  + Software testing and automation engineer
  + Development Operations (DevOps) engineer
  + Data scientist
  + OT subject matter experts (SMEs), such as processing engineers, production engineers, plant managers, and line managers
+ The team is sized and structured according to agile principle and practices
+ Partners for long-term and short-term acceleration and training

Another important point is having an innovative culture to embrace digital transformation and drive it. Because even if you have the correct strategy, processes, and tools in place, if your organizational culture does not encourage innovation and adoption, the digital transformation is less likely to be successful. Consider some of the following strategies to encourage adoption of the digital transformation in your organization:
+ Having a North Star vision, values, and principles (for more information, see [North Star vision](phase-3.md#north-star-vision))
+ Having senior leadership support
+ Having a roadmap that minimizes disruptions to operations
+ Promoting an entrepreneurial mindset and accepting failures
+ Having data-driven, customer-focused goals
+ Adopting agile process and tools
+ Recognizing individuals who advocate for the digital transformation, and providing them opportunities to lead or participate in the initiative
+ Involving employees in the initiatives
+ Providing more autonomy and flexibility for the teams
+ Promoting teamwork, communication, and transparency
+ Having strong and fast feedback mechanisms

## Discover your current systems and technology stack
<a name="discovery"></a>

The technical capabilities of your existing systems define the scope of the future system architecture. Therefore, you need to discover your IT and OT infrastructure to understand its current technical capabilities.

Consider the following to assess the current edge infrastructure capabilities:
+ Current edge architecture
+ Existing IoT or IIoT systems or solutions and their capabilities
+ Current data analytics and machine learning use cases, such as descriptive analytics, predictive analytics, anomaly detection, predictive and preventive maintenance, near real-time dashboard, and BI reporting
+ Scale of existing solutions and future requirements
+ Data sources and their capabilities for ingesting data, including:

  1. Devices or tools, such as sensors, actuators, programmable logic controllers (PLCs), gateways, and OPC Unified Architecture (OPC UA) servers

  1. Supported protocols for those device and tools, such as Modbus, BACnet, MQTT, and OPC UA

  1. Data specifications, such as telemetry frequency, size of typical message, format, and volume
+ Network infrastructure for clear isolation between OT and IT network
+ Network connectivity, such as Ethernet, Wi-Fi, LoRaWAN, and 5G
+ Existing historians and data storage systems
+ Existing cloud connectivity options

Consider the following to assess the current cloud infrastructure capabilities:
+ Current cloud architecture
+ Data lakes
+ Data analytics
+ Data transformation
+ Data service layer
+ Data monitoring and BI
+ Machine learning
+ Web applications

## Review other key considerations
<a name="other-considerations"></a>

In addition to the infrastructure considerations, there are also security, compliance, risk management, governance, and operational factors that you need to account for when assessing your current state. Assess the following topics in depth to address some of these considerations:
+ Information security strategy that assesses and mitigates threats.
+ High-availability requirements, such as recovery time objectives (RTOs) and recovery point objectives (RPOs) for the system.
+ Data governance and access control.
+ Identity and access management for the system.
+ Data retention policies.
+ Data classification and sensitivity.
+ Data encryption, at-rest and in-transit.
+ Compliance and regulatory requirements for processing and storing sensitive data are critical. This includes regulations such as General Data Protection Regulation (GDPR), personally identifiable information (PII), and Health Insurance Portability and Accountability Act (HIPAA).
+ Service-level agreements (SLAs) for downstream data consumption and applications.
+ Business risk management.
+ Asset and device lifecycle management.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
