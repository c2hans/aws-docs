---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/migration-tools/app-mobility-ams.html
---

# AWS Transform MGN
<a name="app-mobility-ams"></a>

*Last update: June 3, 2024*

## Product overview
<a name="app-mobility-ams-overview"></a>

|
|
| Category | Product capabilities |
| --- |--- |
| **Product website** | [AWS Transform MGN](https://aws.amazon.com/application-migration-service/) |
| **Tool deployment model**<br />Product can be SaaS-based or customer-deployed | Servers deployed on AWS (customer VPC) |
| **Compliance** | Federal Risk and Authorization Management Program (FedRAMP)General Data Protection Regulation (GDPR)Health Insurance Portability and Accountability Act (HIPAA)Payment card industry (PCI)System and Organization Controls (SOC) |
| **Service model** | Full self-service – Deployment, management, and maintenance can be done by the customer or end-userSelf-service with vendor support – Deployment, management, and maintenance can be done by customer or end-user with the option of vendor support |
| **Pricing model** | No charge for service; resource charges apply |

## Application mobility capabilities
<a name="app-mobility-ams-capabilities"></a>

|
|
| Category | Product capabilities |
| --- |--- |
| **Replication method**<br />The ability to support one or more of the following replication methods:Agentless – Uses protocols or interfaces such as SNMP or WMIAgent-based – Requires installation of software on the source resources, such as Linux or Windows serversLogin-based – Uses protocols, such as SSH and RDP, to log in to the source servers | AgentlessAgent-based |
| **Supported sources**<br />The hosting environments that the product can migrate applications from | Google Cloud PlatformHyper-VMicrosoft AzurePhysical serversVMware |
| **Application data collection**<br />The ability to collect data to support application transformation, such as code from .NET legacy to .NET core, monolith-to-microservices code conversions, or server-to-container conversions | Not available |
| **Supported operating systems**<br />Operating systems that the product can migrate | LinuxWindows |
| **Supported targets**<br />Resources that the product can migrate to | Amazon Elastic Compute Cloud (Amazon EC2) |
| **Source code repository integration**<br />Repositories that the product can analyze to support application transformation | Not available |
| **Deployment integration**<br />Services that the product integrates with to support deployment | Not available |
| **Infrastructure as code templates**<br />Templates that the product can generate to support application deployment | Not available |
| **Notifications**<br />Methods that the product can use to notify you of progress or issues | LogsMetrics |
| **Replication options, continuous asynchronous replication** | Available |
| **Replication options, bandwidth consumption**<br />The ability to manage bandwidth consumption, such as by using throttling or parallel replication streams | Not available |
| **Replication options, storage types**<br />The ability to select storage types for both temporary and target replication disk volumes to manage performance and cost | Available |
| **Replication options, reporting progress**<br />The ability to report replication progress, including success, stall, or failure states, and send events or alerts for those states | Available |
| **Conversion options, programming languages**<br />The ability to convert application code to other languages | Not available |
| **Conversion options, AWS native services**<br />The ability to convert an application for deployment to AWS Cloud native services | Not available |
| **Conversion options, AWS managed container services**<br />The ability to convert an application for deployment to AWS managed container services | Not available |
| **Conversion options, AWS serverless services**<br />The ability to convert an application to a serverless architecture based on AWS Lambda and Amazon API Gateway | Not available |
| **Conversion options, licensing**<br />The ability to convert licensing mechanisms. For example replace a BYOL license with an AWS license-included option | Available |
| **Data import**<br />The ability to import data from other telemetry sources and applications in common formats, such as CSV, JSON, YAML, or API | Available |
| **Data export**<br />The ability to export discovered data into a usable format, such as CSV, JSON, YAML, or API | Available |
| **Data sovereignty support**<br />The ability to store data on premises or at a designated location based on the data protection policies or government data sovereignty regulations | Yes |
