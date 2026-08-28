---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/migration-tools/app-mobility-stromasys.html
---

# Stromasys Charon family of emulators
<a name="app-mobility-stromasys"></a>

*Last update: June 3, 2024*

**Note**
AWS Partner product descriptions and reported qualifications, including compliance, are provided by the AWS Partner and are not verified by AWS. For more information about these products, contact the AWS Partner. You are encouraged to conduct your own additional due diligence before choosing to use any of the products listed.

## Product overview
<a name="app-mobility-stromasys-overview"></a>

|
|
| Category | Product capabilities |
| --- |--- |
| **Product website** | [Stromasys Charon](https://www.stromasys.com/emulation-software-solutions/) |
| **Product certifications**<br />[AWS Competency Program](https://aws.amazon.com/partners/offerings/) competencies and other certifications | Migration and Modernization ISV Competency |
| **AWS Marketplace**<br />Link to subscribe or download | [Virtualization for SPARC on AWS Marketplace](https://aws.amazon.com/marketplace/pp/prodview-2zg63j6ykjodw) |
| **Tool deployment model**<br />Product can be SaaS-based or customer-deployed | + Servers deployed on AWS (customer VPC)<br />+ Servers deployed on premises in customer environment |
| **Compliance** | General Data Protection Regulation (GDPR) |
| **Service model** | + Self-service with vendor support – Deployment, management, and maintenance can be done by customer or end-user with the option of vendor support<br />+ Managed service (including partner-enabled service) – Deployment, management, and maintenance require professional services |
| **Pricing model** | Subscription |

## Application mobility capabilities
<a name="app-mobility-stromasys-capabilities"></a>

|
|
| Category | Product capabilities |
| --- |--- |
| **Replication method**<br />The ability to support one or more of the following replication methods:+ Agentless – Uses protocols or interfaces such as SNMP or WMI<br />+ Agent-based – Requires installation of software on the source resources, such as Linux or Windows servers<br />+ Login-based – Uses protocols, such as SSH and RDP, to log in to the source servers | Login-based |
| **Supported sources**<br />The hosting environments that the product can migrate applications from | Physical servers with Sun SPARC, HP PA-RISC, DEC Alpha, VAX, and PDP-11 hardware |
| **Application data collection**<br />The ability to collect data to support application transformation, such as code from .NET legacy to .NET core, monolith-to-microservices code conversions, or server-to-container conversions | Not available |
| **Supported operating systems**<br />Operating systems that the product can migrate | + HP-UX<br />+ Solaris<br />+ Other – OpenVMS, Tru64 UNIX, MPE |
| **Supported targets**<br />Resources that the product can migrate to | Amazon Elastic Compute Cloud (Amazon EC2) |
| **Source code repository integration**<br />Repositories that the product can analyze to support application transformation | Not available |
| **Deployment integration**<br />Services that the product integrates with to support deployment | Jenkins |
| **Infrastructure as code templates**<br />Templates that the product can generate to support application deployment | Not available |
| **Notifications**<br />Methods that the product can use to notify you of progress or issues | + Email<br />+ Logs |
| **Replication options, continuous asynchronous replication** | Not available |
| **Replication options, bandwidth consumption**<br />The ability to manage bandwidth consumption, such as by using throttling or parallel replication streams | Not available |
| **Replication options, storage types**<br />The ability to select storage types for both temporary and target replication disk volumes to manage performance and cost | Not available |
| **Replication options, reporting progress**<br />The ability to report replication progress, including success, stall, or failure states, and send events or alerts for those states | Available |
| **Conversion options, programming languages**<br />The ability to convert application code to other languages | Converts binary code from Sun SPARC, HP PA-RISC, DEC Alpha, VAX, and PDP-11 to x86 binary code |
| **Conversion options, AWS native services**<br />The ability to convert an application for deployment to AWS Cloud native services | Not available |
| **Conversion options, AWS managed container services**<br />The ability to convert an application for deployment to AWS managed container services | Not available |
| **Conversion options, AWS serverless services**<br />The ability to convert an application to a serverless architecture based on AWS Lambda and Amazon API Gateway | Not available |
| **Conversion options, licensing**<br />The ability to convert licensing mechanisms. For example replace a BYOL license with an AWS license-included option | Not available |
| **Data import**<br />The ability to import data from other telemetry sources and applications in common formats, such as CSV, JSON, YAML, or API | Not available |
| **Data export**<br />The ability to export discovered data into a usable format, such as CSV, JSON, YAML, or API | Not available |
| **Data sovereignty support**<br />The ability to store data on premises or at a designated location based on the data protection policies or government data sovereignty regulations | Yes |

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
