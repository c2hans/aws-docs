---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/migration-tools/business-case-concierto-cloud.html
---

# Concierto.cloud
<a name="business-case-concierto-cloud"></a>

*Last update: November 17, 2025*

**Note**
AWS Partner product descriptions and reported qualifications, including compliance, are provided by the AWS Partner and are not verified by AWS. For more information about these products, contact the AWS Partner. You are encouraged to conduct your own additional due diligence before choosing to use any of the products listed.

## Product overview
<a name="business-case-concierto-cloud-overview"></a>

|
|
| Category | Product capabilities |
| --- |--- |
| **Product website** | [Concierto.cloud](https://www.concierto.cloud/) |
| **Product certifications**<br />[AWS Competency Program](https://aws.amazon.com/partners/offerings/) competencies and other certifications | AWS Migration and Modernization – Business Case Analysis |
| **AWS Marketplace**<br />Link to subscribe or download | [Concierto.cloud on AWS Marketplace](https://aws.amazon.com/marketplace/seller-profile?id=f4eb933a-efc0-4e94-a0da-9a28bc819cc4) |
| **Tool deployment model**<br />Product can be SaaS-based or customer-deployed | SaaS on AWS (vendor VPC)Servers deployed on AWS (customer VPC)Servers deployed on premises in customer environmentSaaS or servers in other cloud provider environment |
| **Compliance** | General Data Protection Regulation (GDPR)System and Organization Controls (SOC)International Organization for Standardization (ISO) 27001:2022National Institute of Standards and Technology (NIST) 800-53CSA Star Level 2 |
| **Service model** | Full self-service – Deployment, management, and maintenance can be done by the customer or end-userManaged service (including partner-enabled service) – Deployment, management, and maintenance require professional services |
| **Pricing model** | Subscription |

## Business case analysis capabilities
<a name="business-case-concierto-cloud-capabilities"></a>

|
|
| Category | Product capabilities |
| --- |--- |
| **Data import**<br />The ability to upload IT asset data from discovery tools (such as CMDB extract, VCenter extract, SolarWinds, or Hyper-V) or from software distribution tools (such as Microsoft SCCM) | ManuallyProgrammatically through the API |
| **Right-sizing, Amazon EC2 instance type**<br />The ability to select the Amazon EC2 instance type with the lowest cost based on the source server profile(1) and utilization data(2), application characteristics(3), and Amazon EC2 characteristics(4) | vCPU and CPU core count mapping and RAM mapping between the source server or VM and target Amazon EC2 instanceCPU and RAM utilization data over time, including maximum (peak), average (or median), standard deviation, and percentile statisticsApplication or user process CPU utilization |
| **Exclusion of resource types**<br />The ability to exclude Amazon Elastic Compute Cloud (Amazon EC2) instance types, such as burstable T3, from TCO calculation | Yes |
| **Right-sizing, tenancy**<br />The ability to make optimized recommendations across Amazon EC2 tenancies with Dedicated Hosts or Dedicated Instances | Dedicated Hosts |
| **Right-sizing, attached storage**<br />The ability to use source storage profile data, utilization data, application characteristics, and AWS storage characteristics in order to right-size attached storage, such as Amazon Elastic Block Store (Amazon EBS), with proper types, such as SSD or HDD | Yes |
| **Choice of resource capacity allocation**<br />The ability to select resource capacity allocation schemes (such as low or high resource utilization reservation) or fine-tune the utilization threshold (such as selecting a statistically lowered option 90th or 95th percentile) to reflect your conservative or optimistic resource allocation plan | No |
| **License analysis**<br />The ability to provide default license mapping and options in AWS with cost comparisons of bringing existing licenses versus buying licenses from AWS | Provide Amazon EC2 license options, including BYOL and AWS license-included optionsOptimize server license cost by reducing the licensable number of CPU coresOptimize server license edition (for example, recommend downgrade option from Microsoft SQL Server Enterprise to Microsoft SQL Server Standard)Analyze replatform costs; for example, Microsoft SQL Server to Amazon Relational Database Service (Amazon RDS), Oracle to Amazon Aurora PostgreSQL-Compatible EditionAnalyze database consolidation costs |
| **TCO coverage, on premises**<br />Cost estimates over 1 year and 3 years, respectively | Server and storage costsSoftware, license, and support costsFacility and maintenance costs (rack, infrastructure, power, and real estate)Labor costs |
| **TCO coverage, AWS**<br />Cost estimates over 1 year and 3 years, respectively | Amazon EC2 and Reserved Instance costs |
| **TCO coverage, migration**<br />Cost estimates | Training costsTool costsLabor costs (customer, partner, and AWS resources) |
| **TCO data sovereignty support**<br />The ability to store TCO analysis data on premises or at a designated location based on the data protection policies or government data sovereignty regulations | Yes |

1 Resource profile – CPU family (x86, RISC/PowerPC, ...), number of CPU cores, memory size, number of disks, storage size, IOPS, network interfaces, bandwidth

2 Resource utilizations – Time-series utilization data with peak, average or median, standard deviation, IOPS, throughput, percentile with sampling interval of 5 minutes and minimum sampling duration of 1 month

3 Application characteristics – CPU-intense, CPU-bursty, memory-intense, storage I/O-bound, or network-bound

4 [Amazon EC2 characteristics](https://aws.amazon.com/ec2/instance-types/)
