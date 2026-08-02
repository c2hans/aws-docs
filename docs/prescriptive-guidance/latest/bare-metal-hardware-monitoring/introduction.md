---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/bare-metal-hardware-monitoring/introduction.html
---

# Bare-metal hardware monitoring on AWS by using Telegraf and Redfish
<a name="introduction"></a>

*Tamilselvan P, Naveen Suthar, and RAJNEESH TYAGI, Amazon Web Services*

Effective hardware monitoring is crucial for ensuring the reliability and performance of mission-critical systems. In a multi-vendor environment, where [bare-metal hardware](https://en.wikipedia.org/wiki/Bare-metal_server) components are sourced from different manufacturers, the challenge lies in implementing a consistent and scalable monitoring solution. Many vendors have adopted the [DMTF Redfish](https://www.dmtf.org/standards/redfish) API, a cross-vendor industry standard for hardware health monitoring. This API offers a RESTful interface that is designed to streamline and enhance hardware management operations.

The adoption of Redfish has brought numerous benefits, including higher concurrent operation volumes, reduced operational time, and improved scalability over traditional protocols, such as Simple Network Management Protocol (SNMP). However, it has also introduced its own set of challenges.

One of the primary challenges is the lack of consistent implementation across different vendors. Despite the standard interface, each vendor has their own interpretation and implementation. For example, one vendor might represent temperature sensor data differently than another vendor, even though they are both using the Redfish API. This leads to inconsistencies in data representation and functionality.

To solve this challenge, you can use [Telegraf](https://docs.influxdata.com/telegraf/v1/), an open source agent for collecting and reporting metrics and data. Its plugin-based architecture supports development of vendor-specific plugins or input plugins. You can use these plugins to resolve the differences in Redfish API implementations across vendors. These plugins encapsulate vendor-specific logic, providing a consistent interface for data collection and monitoring. This mitigates the effect of inconsistent Redfish API implementations across different hardware vendors.

Another critical aspect of Redfish API adoption is the need for robust authentication and authorization mechanisms. Because the Redfish API provides direct access to hardware components, it's critical that you establish proper access control and security measures. Telegraf supports various authentication methods, including basic authentication, token-based authentication, and integration with external identity providers. This helps you secure communication with the Redfish API endpoints and helps you limit access to only authorized personnel, based on defined roles and permissions.

## Intended audience
<a name="intended-audience"></a>

This guide is intended for IT infrastructure managers, systems administrators, DevOps engineers, network administrators, and other IT operations professionals who have a basic understanding of the following:
+ [Amazon Elastic Kubernetes Service (Amazon EKS)](https://docs.aws.amazon.com/eks/latest/userguide/what-is-eks.html) is a managed Kubernetes service for deploying and managing containerized applications.
+ Container services, such as [Docker](https://www.docker.com/resources/what-container/), are lightweight virtualization technologies that you can use to package applications with their dependencies into portable, self-contained units. These units are called *containers*.
