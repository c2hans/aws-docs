---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/migration-tools/business-case-turbonomic.html
---

# Turbonomic
<a name="business-case-turbonomic"></a>

*Last update: May 15, 2023*

**Note**
AWS Partner product descriptions and reported qualifications, including compliance, are provided by the AWS Partner and are not verified by AWS. For more information about these products, contact the AWS Partner. You are encouraged to conduct your own additional due diligence before choosing to use any of the products listed.

## Product overview
<a name="business-case-turbonomic-overview"></a>

|
|
| Category | Product capabilities |
| --- |--- |
| **Product website** | [IBM Turbonomic](https://www.ibm.com/products/turbonomic) |
| **Product certifications**<br />[AWS Competency Program](https://aws.amazon.com/partners/offerings/) competencies and other certifications | AWS Migration and Modernization – Business Case AnalysisAWS Cloud Management Tools CompetencyAWS Microsoft Workloads CompetencyAWS Cloud Migration Competency |
| **AWS Marketplace**<br />Link to subscribe or download | [Turbonomic on AWS Marketplace](https://aws.amazon.com/marketplace/seller-profile?id=3493e57b-6545-412e-a1d4-f1edf709d9ce) |
| **Tool deployment model**<br />Product can be SaaS-based or customer-deployed | Servers deployed on AWS (customer VPC)Servers deployed on premises in customer environmentSaaS or servers in other cloud provider environment |
| **Compliance** | Not available |
| **Service model** | Full self-service – Deployment, management, and maintenance can be done by the customer or end-userSelf-service with vendor support – Deployment, management, and maintenance can be done by customer or end-user with the option of vendor support |
| **Pricing model** | Subscription |

## Business case analysis capabilities
<a name="business-case-turbonomic-capabilities"></a>

|
|
| Category | Product capabilities |
| --- |--- |
| **Data import**<br />The ability to upload IT asset data from discovery tools (such as CMDB extract, VCenter extract, SolarWinds, or Hyper-V) or from software distribution tools (such as Microsoft SCCM) | ManuallyProgrammatically through the API |
| **Right-sizing, Amazon EC2 instance type**<br />The ability to select the Amazon EC2 instance type with the lowest cost based on the source server profile(1) and utilization data(2), application characteristics(3), and Amazon EC2 characteristics(4) | vCPU and CPU core count mapping and RAM mapping between the source server or VM and target Amazon EC2 instanceCPU and RAM utilization data over time, including maximum (peak), average (or median), standard deviation, and percentile statisticsCPU speed (GHz) per generationApplication or user process CPU utilizationSynthetic workload test against processor benchmarkingIntel x86 Hyper-Threading Technology for symmetric multiprocessing (SMP) applications |
| **Exclusion of resource types**<br />The ability to exclude Amazon Elastic Compute Cloud (Amazon EC2) instance types, such as burstable T3, from TCO calculation | Yes |
| **VMware Cloud on AWS analysis**<br />The ability to analyze the cost of VMware Cloud on AWS by modeling VMware Cloud workload configurations, such as using Amazon Simple Storage Service (Amazon S3) for storage | Not available |
| **Right-sizing, tenancy**<br />The ability to make optimized recommendations across Amazon EC2 tenancies with Dedicated Hosts or Dedicated Instances | Not available |
| **Right-sizing, attached storage**<br />The ability to use source storage profile data, utilization data, application characteristics, and AWS storage characteristics in order to right-size attached storage, such as Amazon Elastic Block Store (Amazon EBS), with proper types, such as SSD or HDD | Yes |
| **Choice of resource capacity allocation**<br />The ability to select resource capacity allocation schemes (such as low or high resource utilization reservation) or fine-tune the utilization threshold (such as selecting a statistically lowered option 90th or 95th percentile) to reflect your conservative or optimistic resource allocation plan | Yes |
| **License analysis**<br />The ability to provide default license mapping and options in AWS with cost comparisons of bringing existing licenses versus buying licenses from AWS | Provide Amazon EC2 license options, including BYOL and AWS license-included options |
| **TCO coverage, on premises**<br />Cost estimates over 1 year and 3 years, respectively | Server and storage costsSoftware, license, and support costs |
| **TCO coverage, AWS**<br />Cost estimates over 1 year and 3 years, respectively | Amazon EC2 and Reserved Instance costsStorage costsLicense costs |
| **TCO coverage, migration**<br />Cost estimates | Not available |
| **TCO data sovereignty support**<br />The ability to store TCO analysis data on premises or at a designated location based on the data protection policies or government data sovereignty regulations | Yes |

1 Resource profile – CPU family (x86, RISC/PowerPC, ...), number of CPU cores, memory size, number of disks, storage size, IOPS, network interfaces, bandwidth

2 Resource utilizations – Time-series utilization data with peak, average or median, standard deviation, IOPS, throughput, percentile with sampling interval of 5 minutes and minimum sampling duration of 1 month

3 Application characteristics – CPU-intense, CPU-bursty, memory-intense, storage I/O-bound, or network-bound

4 [Amazon EC2 characteristics](https://aws.amazon.com/ec2/instance-types/)
