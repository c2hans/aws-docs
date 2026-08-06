---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/migration-tools/business-case-migration-evaluator.html
---

# Migration Evaluator
<a name="business-case-migration-evaluator"></a>

*Last update: May 15, 2023*

## Product overview
<a name="business-case-migration-evaluator-overview"></a>

|
|
| Category | Product capabilities |
| --- |--- |
| **Product website** | [Migration Evaluator](https://aws.amazon.com/migration-evaluator/) |
| **Request for TCO assessment**<br />The ability to provide a business case to make sound AWS planning and migration decisions | [Submit request](https://pages.awscloud.com/Migration-Evaluator-request.html) |
| **Tool deployment model**<br />Product can be SaaS-based or customer-deployed | SaaS on AWS (vendor VPC) |
| **Compliance** | General Data Protection Regulation (GDPR) |
| **Service model** | Managed service (including partner-enabled service) – Deployment, management, and maintenance require professional services |
| **Pricing model** | No charge |

## Business case analysis capabilities
<a name="business-case-migration-evaluator-capabilities"></a>

|
|
| Category | Product capabilities |
| --- |--- |
| **Data import**<br />The ability to upload IT asset data from discovery tools (such as CMDB extract, VCenter extract, SolarWinds, or Hyper-V) or from software distribution tools (such as Microsoft SCCM) | Manually |
| **Right-sizing, Amazon EC2 instance type**<br />The ability to select the Amazon EC2 instance type with the lowest cost based on the source server profile(1) and utilization data(2), application characteristics(3), and Amazon EC2 characteristics(4) | + vCPU and CPU core count mapping and RAM mapping between the source server or VM and target Amazon EC2 instance<br />+ CPU and RAM utilization data over time, including maximum (peak), average (or median), standard deviation, and percentile statistics<br />+ CPU speed (GHz) per generation<br />+ Synthetic workload test against processor benchmarking |
| **Right-sizing, Amazon EC2 manufacturer** | + Intel-based Amazon EC2 instances<br />+ AMD-based Amazon EC2 instances |
| **Exclusion of resource types**<br />The ability to exclude Amazon Elastic Compute Cloud (Amazon EC2) instance types, such as burstable T3, from TCO calculation | Yes |
| **VMware Cloud on AWS analysis**<br />The ability to analyze the cost of VMware Cloud on AWS by modeling VMware Cloud workload configurations, such as using Amazon Simple Storage Service (Amazon S3) for storage | Yes |
| **Right-sizing, tenancy**<br />The ability to make optimized recommendations across Amazon EC2 tenancies with Dedicated Hosts or Dedicated Instances | + Dedicated Hosts<br />+ Dedicated Instances |
| **Right-sizing, attached storage**<br />The ability to use source storage profile data, utilization data, application characteristics, and AWS storage characteristics in order to right-size attached storage, such as Amazon Elastic Block Store (Amazon EBS), with proper types, such as SSD or HDD | No |
| **Choice of resource capacity allocation**<br />The ability to select resource capacity allocation schemes (such as low or high resource utilization reservation) or fine-tune the utilization threshold (such as selecting a statistically lowered option 90th or 95th percentile) to reflect your conservative or optimistic resource allocation plan | Yes |
| **License analysis**<br />The ability to provide default license mapping and options in AWS with cost comparisons of bringing existing licenses versus buying licenses from AWS | + Provide Amazon EC2 license options, including BYOL and AWS license-included options<br />+ Optimize server license cost by reducing the licensable number of CPU cores<br />+ Analyze database consolidation costs |
| **TCO coverage, on premises**<br />Cost estimates over 1 year and 3 years, respectively | + Server and storage costs<br />+ Software, license, and support costs<br />+ Facility and maintenance costs (rack, infrastructure, power, and real estate) |
| **TCO coverage, AWS**<br />Cost estimates over 1 year and 3 years, respectively | + Amazon EC2 and Reserved Instance costs<br />+ Storage costs<br />+ Database costs<br />+ VMware Cloud on AWS costs<br />+ License costs |
| **TCO coverage, migration**<br />Cost estimates | Not available |
| **TCO data sovereignty support**<br />The ability to store TCO analysis data on premises or at a designated location based on the data protection policies or government data sovereignty regulations | No |

1 Resource profile – CPU family (x86, RISC/PowerPC, ...), number of CPU cores, memory size, number of disks, storage size, IOPS, network interfaces, bandwidth

2 Resource utilizations – Time-series utilization data with peak, average or median, standard deviation, IOPS, throughput, percentile with sampling interval of 5 minutes and minimum sampling duration of 1 month

3 Application characteristics – CPU-intense, CPU-bursty, memory-intense, storage I/O-bound, or network-bound

4 [Amazon EC2 characteristics](https://aws.amazon.com/ec2/instance-types/)
