---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/migration-sas-grid/licensing.html
---

# Cost and licensing
<a name="licensing"></a>

At a high level, the cost of migrating a SAS workload to AWS assumes establishing a new environment on AWS. The cost includes accounting for personnel time and effort as well as provisioning computing resources and licensing software for the new environment.

## SAS licenses
<a name="sas-licenses"></a>

Selecting the appropriate size instance type for the SAS license is an important consideration. In general, SAS licensing is based on the number of physical CPUs on the host machine(s). In comparison, AWS typically specifies the number of virtual CPUs (vCPUs, or hyperthreading) for its instance types. As a rule, for the target destination, select an Amazon Elastic Compute Cloud (Amazon EC2) instance that has **twice the number of vCPUs** as compared to the physical CPUs in the source environment. See [Optimizing CPU options](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/instance-optimize-cpu.html) in the Amazon EC2 documentation for more information about optimizing vCPU-based licensing costs.

Another consideration is the cost of running two environments (source and target) at the same time, while getting the value of only one environment. SAS offers two policies to help reduce the cost of migration efforts like this, depending on the exact circumstances involved: policy for upgrading SAS software, and policy for testing new hardware.

|
|
| Policy | Description | Duration |
| --- |--- |--- |
| Upgrading SAS software | SAS allows all customers who are upgrading to a new production release to run two parallel copies of the licensed software (the old release and the new release) for 180 days (6 months) at no additional charge.<br />For metered offerings, customers can run two parallel copies of the licensed software, but both will be metered for billing purposes. | 180 days |
| Testing new hardware | The following scenarios are covered by SAS evaluation paperwork and are offered free of charge for a limited test period. The standard test period for each scenario is 30 days.+ Testing new hardware before upgrading production machines and production systems to the new hardware configuration; performing parallel processing.<br />+ Testing new operating systems before converting from one operating system to another in a production environment; performing parallel processing. | 30 days |

**Note**
*Test machines* are defined as hardware the customer is responsible for that is used to run SAS software in an evaluation environment to verify quality and accuracy of data output.

Contact your SAS account representative for more information specific to your site and license.

## Cost estimates for AWS services
<a name="cost"></a>

[AWS Pricing Calculator ](https://calculator.aws/)is an online tool that helps you estimate the monthly cost of AWS services for your use case, based on your expected usage. The Pricing Calculator is continuously updated with the latest pricing for all AWS services in all Regions. The calculator includes support for most AWS services. You can include additional costs such as data ingress/egress charges, data storage charges, and retrieval fees. You can also select Amazon EC2 with various pricing models such as On-Demand, Dedicated, and Reserved Instances. We recommend that you use Pricing Calculator to estimate your monthly AWS bill more efficiently.

**Note**
Evaluate the ratio of vCPU to I/O bandwidth and vCPU to ephemeral storage per AWS instance type. Choose the instance that provides the best ratio of those two factors for your SAS Grid processing computing needs.

### Workload sizing
<a name="workload-sizing.2bfa7e1b-7d1e-5e5e-b7f0-aad2bb1d71f4"></a>
+ [Small ](https://calculator.aws/#/estimate?id=792fd54c3c37fae0acce8bbd6bdd592d474dd984)– SAS Grid without high availability in a single Availability Zone

  2x SAS Grid (i3en.6xlarge instance), 1x Metadata Server, 1x Web Server
+ [Medium ](https://calculator.aws/#/estimate?id=516858af13b47382074ec69b907c13664f18ad1d)– SAS Grid with high availability in a single Availability Zone

  4x SAS Grid (i3en.12xlarge instance), 3x Metadata Server, 2x Web Server
+ [Large ](https://calculator.aws/#/estimate?id=6044f60e4693c472506978f68ac63fba89f5fde2)– SAS Grid with high availability in a single Availability Zone

  8x SAS Grid (i3en.12xlarge instance), 3x Metadata Server, 2x Web Server
