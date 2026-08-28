---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/migration-tools/app-mobility-concierto-cloud.html
---

# Concierto.cloud
<a name="app-mobility-concierto-cloud"></a>

*Last update: November 17, 2025*

**Note**
AWS Partner product descriptions and reported qualifications, including compliance, are provided by the AWS Partner and are not verified by AWS. For more information about these products, contact the AWS Partner. You are encouraged to conduct your own additional due diligence before choosing to use any of the products listed.

## Product overview
<a name="app-mobility-concierto-cloud-overview"></a>

|
|
| Category | Product capabilities |
| --- |--- |
| **Product website** | [Concierto.cloud](https://www.concierto.cloud/) |
| **Product certifications**<br />[AWS Competency Program](https://aws.amazon.com/partners/offerings/) competencies and other certifications | AWS Migration and Modernization – Application Mobility |
| **AWS Marketplace**<br />Link to subscribe or download | [Concierto.cloud on AWS Marketplace](https://aws.amazon.com/marketplace/seller-profile?id=f4eb933a-efc0-4e94-a0da-9a28bc819cc4) |
| **Tool deployment model**<br />Product can be SaaS-based or customer-deployed | + SaaS on AWS (vendor VPC)<br />+ Servers deployed on AWS (customer VPC)<br />+ Servers deployed on premises in customer environment<br />+ SaaS or servers in other cloud provider environment |
| **Compliance** | + General Data Protection Regulation (GDPR)<br />+ System and Organization Controls (SOC)<br />+ International Organization for Standardization (ISO) 27001:2022<br />+ National Institute of Standards and Technology (NIST) 800-53<br />+ CSA Star Level 2 |
| **Service model** | + Full self-service – Deployment, management, and maintenance can be done by the customer or end-user<br />+ Managed service (including partner-enabled service) – Deployment, management, and maintenance require professional services |
| **Pricing model** | Subscription |

## Application mobility capabilities
<a name="app-mobility-concierto-cloud-capabilities"></a>

|
|
| Category | Product capabilities |
| --- |--- |
| **Replication method**<br />The ability to support one or more of the following replication methods:+ Agentless – Uses protocols or interfaces such as SNMP or WMI<br />+ Agent-based – Requires installation of software on the source resources, such as Linux or Windows servers<br />+ Login-based – Uses protocols, such as SSH and RDP, to log in to the source servers | + Agentless<br />+ Login-based |
| **Supported sources**<br />The hosting environments that the product can migrate applications from | + Container platforms, including Docker and Kubernetes-based<br />+ Google Cloud Platform<br />+ Microsoft Azure<br />+ Physical servers<br />+ VMware |
| **Application data collection**<br />The ability to collect data to support application transformation, such as code from .NET legacy to .NET core, monolith-to-microservices code conversions, or server-to-container conversions | + Application anomalies<br />+ Application environment<br />+ Application errors and codes<br />+ Environment<br />+ Frameworks and libraries<br />+ Missing source code attribute<br />+ Number of lines of code<br />+ Number of unique functions or modules at source level or binary level<br />+ Performance data and metrics<br />+ Programming language<br />+ Software versions<br />+ Software vulnerabilities |
| **Supported operating systems**<br />Operating systems that the product can migrate | + Linux<br />+ Windows |
| **Supported targets**<br />Resources that the product can migrate to | + Amazon Elastic Compute Cloud (Amazon EC2)<br />+ AWS Lambda<br />+ Amazon Elastic Container Service (Amazon ECS) or Amazon Elastic Kubernetes Service (Amazon EKS) |
| **Source code repository integration**<br />Repositories that the product can analyze to support application transformation | + Bitbucket<br />+ GitHub<br />+ GitLab |
| **Deployment integration**<br />Services that the product integrates with to support deployment | + AWS CodePipeline<br />+ Bamboo<br />+ Buddy<br />+ GitLab<br />+ Jenkins |
| **Infrastructure as code templates**<br />Templates that the product can generate to support application deployment | + AWS CloudFormation<br />+ HashiCorp Terraform |
| **Notifications**<br />Methods that the product can use to notify you of progress or issues | + Email<br />+ Logs<br />+ Metrics<br />+ SMS |
| **Replication options, continuous asynchronous replication** | Available |
| **Replication options, bandwidth consumption**<br />The ability to manage bandwidth consumption, such as by using throttling or parallel replication streams | Available |
| **Replication options, storage types**<br />The ability to select storage types for both temporary and target replication disk volumes to manage performance and cost | Available |
| **Replication options, reporting progress**<br />The ability to report replication progress, including success, stall, or failure states, and send events or alerts for those states | Available |
| **Conversion options, programming languages**<br />The ability to convert application code to other languages | .NET to .NET Core, Java upgrades, legacy SDK for .NET upgrades |
| **Conversion options, AWS native services**<br />The ability to convert an application for deployment to AWS Cloud native services | Available |
| **Conversion options, AWS managed container services**<br />The ability to convert an application for deployment to AWS managed container services | Available |
| **Conversion options, AWS serverless services**<br />The ability to convert an application to a serverless architecture based on AWS Lambda and Amazon API Gateway | Not available |
| **Conversion options, licensing**<br />The ability to convert licensing mechanisms. For example replace a BYOL license with an AWS license-included option | Not available |
| **Data import**<br />The ability to import data from other telemetry sources and applications in common formats, such as CSV, JSON, YAML, or API | Available |
| **Data export**<br />The ability to export discovered data into a usable format, such as CSV, JSON, YAML, or API | Available |
| **Data sovereignty support**<br />The ability to store data on premises or at a designated location based on the data protection policies or government data sovereignty regulations | Yes |

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
