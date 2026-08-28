---
source_url: https://docs.aws.amazon.com/whitepapers/latest/designing-next-generation-vehicle-communication-aws-iot/designing-next-generation-vehicle-communication-aws-iot.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Designing Next Generation Vehicle Communication with AWS IoT Core and MQTT
<a name="designing-next-generation-vehicle-communication-aws-iot"></a>

**Utilizing MQTT and AWS IoT Core to Implement a Connected Vehicle Architecture**

Publication date: **January 12, 2024** ([Document history](document-revisions.md))

 This whitepaper outlines the best practices for implementing an extensible, scalable and resilient communication architecture for the next generation of vehicles on AWS. Utilizing AWS IoT Core with its managed MQTT broker as the centralized communication platform for vehicle telemetry, provides OEMs this global platform to build their connected vehicle platforms upon and enables differentiated customer experiences and brand-new mobility use cases the industry has begun to demand. This paper reviews why MQTT and publish/subscribe pattern work best for connected vehicle platforms and reviews, in detail, the building blocks the AWS IoT Core can provide to enable OEMs and other connected mobility provides to build a managed platform with those tools.

 This whitepaper is intended for vehicle manufacturer cloud architects and engineers or decision makers determining if AWS IoT Core is the proper solution for next-generation vehicle workloads to the cloud.

## Introduction
<a name="introduction"></a>

 The automotive industry is seeing a transformational change in the way consumers interact with their vehicles. This change is driving the size of the connected car global market, which is projected to reach [$225 billion by 2027](https://www.alliedmarketresearch.com/connected-car-market). We are seeing shifts in available use cases as automotive manufacturers (OEMs) and tier 1 suppliers begin to adopt these technologies in the vehicle, and these are enabling the following vehicle capabilities:
+  The consumer’s connected experience, in and out of the vehicle
+  Car-sharing and ride sharing services, enabling a new mobility vertical
+  Autonomous enhancements
+  Fleet management

 In the industry today, we see OEMs pushing both for newer revenue streams and the aggregation and monetization of vehicular data by connecting all vehicles to these platforms. Primarily, OEMs are looking to capture signal information off the vehicle allowing for more efficient identification of fleet-wide issues, predictive maintenance and reduction of warranty claims, one of the larger expenses for OEMs. In addition, streamlining the operationalization of the vehicle’s lifecycle, OEMs are introducing more customer-centric use cases via a connected vehicle functions which allow for convenient monitoring of the vehicle from your smart phone, remote commands, roadside assistance and emergency calling.

 On most legacy connected vehicle platforms, many of these connected services were built using technologies not designed for the connected vehicle use cases, but understandably were the more prominent technologies available to implement. Additionally, when designing these platforms, cloud technologies were still in their infancy and OEMs that did switch their connected vehicle platforms to the cloud, used a lift and shift mechanism for many of their workloads, not optimizing the platform for cloud native architectures. This led to higher operational overheads, inefficiencies with capacity planning and, in turn, much higher variable costs to manage and run these platforms.

 We are now starting to see a shift away from these architectures and OEMs have begun a movement to managed platforms and cloud native implementations, letting companies like AWS manage the security, extensibility and scalability of their connected vehicle platforms.

 The next generation of vehicles will demand a better user experience, on a scalable, durable, extensible platform. This document will cover the implementation of AWS IoT Core as the next generation connected vehicle communication platform.

## Are you Well-Architected?
<a name="are-you-well-architected"></a>

 The [AWS Well-Architected Framework](https://aws.amazon.com/architecture/well-architected/) helps you understand the pros and cons of the decisions you make when building systems in the cloud. The six pillars of the Framework allow you to learn architectural best practices for designing and operating reliable, secure, efficient, cost-effective, and sustainable systems. Using the [AWS Well-Architected Tool](https://aws.amazon.com/well-architected-tool/), available at no charge in the [AWS Management Console](https://console.aws.amazon.com/wellarchitected), you can review your workloads against these best practices by answering a set of questions for each pillar.

 In the [IoT Lens](https://docs.aws.amazon.com/wellarchitected/latest/iot-lens/welcome.html) and [IoT Lens Checklist](https://docs.aws.amazon.com/wellarchitected/latest/iot-lens-checklist/overview.html), we focus on best practices for architecting your IoT applications on AWS.

 In the [Connected Mobility Lens](https://docs.aws.amazon.com/wellarchitected/latest/connected-mobility-lens/connected-mobility-lens.html), we focus on best practices for integrating technology into transportation systems and enhancing the overall mobility experience.

 For more expert guidance and best practices for your cloud architecture—reference architecture deployments, diagrams, and whitepapers—refer to the [AWS Architecture Center](https://aws.amazon.com/architecture/).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Whitepapers. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query whitepapers` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
