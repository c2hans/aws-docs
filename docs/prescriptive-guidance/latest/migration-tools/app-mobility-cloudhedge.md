---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/migration-tools/app-mobility-cloudhedge.html
---

# CloudHedge OmniDeq application modernization platform
<a name="app-mobility-cloudhedge"></a>

*Last update: June 3, 2024*

**Note**
AWS Partner product descriptions and reported qualifications, including compliance, are provided by the AWS Partner and are not verified by AWS. For more information about these products, contact the AWS Partner. You are encouraged to conduct your own additional due diligence before choosing to use any of the products listed.

## Product overview
<a name="app-mobility-cloudhedge-overview"></a>

|
|
| Category | Product capabilities |
| --- |--- |
| **Product website** | [CloudHedge](https://cloudhedge.io/) |
| **Product certifications**<br />[AWS Competency Program](https://aws.amazon.com/partners/offerings/) competencies and other certifications | Migration and Modernization ISV Competency |
| **AWS Marketplace**<br />Link to subscribe or download | [CloudHedge on AWS Marketplace](https://aws.amazon.com/marketplace/seller-profile?id=bf734cc2-cc04-4151-9dd8-bffcf14239c1) |
| **Tool deployment model**<br />Product can be SaaS-based or customer-deployed | + SaaS on AWS (vendor VPC)<br />+ Servers deployed on AWS (customer VPC)<br />+ Servers deployed on premises in customer environment<br />+ SaaS or servers in other cloud provider environment |
| **Compliance** | Not available |
| **Service model** | + Full self-service – Deployment, management, and maintenance can be done by the customer or end-user<br />+ Self-service with vendor support – Deployment, management, and maintenance can be done by customer or end-user with the option of vendor support<br />+ Managed service (including partner-enabled service) – Deployment, management, and maintenance require professional services |
| **Pricing model** | Subscription |

## Application mobility capabilities
<a name="app-mobility-cloudhedge-capabilities"></a>

|
|
| Category | Product capabilities |
| --- |--- |
| **Replication method**<br />The ability to support one or more of the following replication methods:+ Agentless – Uses protocols or interfaces such as SNMP or WMI<br />+ Agent-based – Requires installation of software on the source resources, such as Linux or Windows servers<br />+ Login-based – Uses protocols, such as SSH and RDP, to log in to the source servers | + Agentless<br />+ Login-based |
| **Supported sources**<br />The hosting environments that the product can migrate applications from | + Container platforms, including Docker and Kubernetes-based<br />+ Google Cloud Platform<br />+ Hyper-V<br />+ Microsoft Azure<br />+ Physical servers<br />+ VMware |
| **Application data collection**<br />The ability to collect data to support application transformation, such as code from .NET legacy to .NET core, monolith-to-microservices code conversions, or server-to-container conversions | + Programming language<br />+ Software versions<br />+ Environment |
| **Supported operating systems**<br />Operating systems that the product can migrate | + IBM AIX<br />+ HP-UX<br />+ Linux<br />+ Solaris<br />+ Windows |
| **Supported targets**<br />Resources that the product can migrate to | + Amazon Elastic Compute Cloud (Amazon EC2)<br />+ AWS Lambda<br />+ Amazon Elastic Container Service (Amazon ECS) or Amazon Elastic Kubernetes Service (Amazon EKS)<br />+ Other environmental configuration, including security groups |
| **Source code repository integration**<br />Repositories that the product can analyze to support application transformation | + AWS CodeCommit<br />+ Bitbucket<br />+ GitHub<br />+ GitLab<br />+ Microsoft Azure Repos |
| **Deployment integration**<br />Services that the product integrates with to support deployment | Jenkins |
| **Infrastructure as code templates**<br />Templates that the product can generate to support application deployment | + Ansible<br />+ HashiCorp Terraform<br />+ PowerShell scripts |
| **Notifications**<br />Methods that the product can use to notify you of progress or issues | + Email<br />+ Logs |
| **Replication options, continuous asynchronous replication** | Available |
| **Replication options, bandwidth consumption**<br />The ability to manage bandwidth consumption, such as by using throttling or parallel replication streams | Available |
| **Replication options, storage types**<br />The ability to select storage types for both temporary and target replication disk volumes to manage performance and cost | Available |
| **Replication options, reporting progress**<br />The ability to report replication progress, including success, stall, or failure states, and send events or alerts for those states | Available |
| **Conversion options, programming languages**<br />The ability to convert application code to other languages | .NET Framework and .NET Legacy to .NET Core 6 and .NET Core 8 |
| **Conversion options, AWS native services**<br />The ability to convert an application for deployment to AWS Cloud native services | Available |
| **Conversion options, AWS managed container services**<br />The ability to convert an application for deployment to AWS managed container services | Available |
| **Conversion options, AWS serverless services**<br />The ability to convert an application to a serverless architecture based on AWS Lambda and Amazon API Gateway | Not available |
| **Conversion options, licensing**<br />The ability to convert licensing mechanisms. For example replace a BYOL license with an AWS license-included option | Not available |
| **Data import**<br />The ability to import data from other telemetry sources and applications in common formats, such as CSV, JSON, YAML, or API | Available |
| **Data export**<br />The ability to export discovered data into a usable format, such as CSV, JSON, YAML, or API | Available |
| **Data sovereignty support**<br />The ability to store data on premises or at a designated location based on the data protection policies or government data sovereignty regulations | Yes |

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
