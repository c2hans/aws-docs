---
source_url: https://docs.aws.amazon.com/whitepapers/latest/oracle-database-aws-best-practices/oracle-licensing-considerations.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Oracle licensing considerations
<a name="oracle-licensing-considerations"></a>

 You can run Amazon RDS for Oracle under two different licensing models - "License Included" and "Bring-Your-Own-License (BYOL)". In the "License Included" service model, you do not need separately purchased Oracle licenses.

Oracle Database licensing on AWS is based on the number of virtual CPUs on the EC2 instance on which the database is installed. For information about Oracle Database licensing, refer to your Oracle contract or license terms. You can consult with independent third-party license review firms on specific licensing questions and planning on AWS instances. Reach out to your AWS sales representative for more information. A few key points to consider are:
+  As stated in [Amazon EC2 Instance Types page](https://aws.amazon.com/ec2/instance-types/), each vCPU is a thread of either an Intel Xeon core or an AMD EPYC core, except for A1 instances, T2 instances, and m3.medium.
+  **Number of CPU cores** - You can customize the number of CPU cores for the instance.
+  **Threads per core** - You can disable multithreading by specifying a single thread per CPU core.
+  VMware Cloud on AWS also offers a [custom CPU core count](https://cloud.vmware.com/community/2019/02/13/custom-cpu-core-count-overview/) feature for its host nodes. You have an option of selecting 8, 16, or 32 CPU cores per host for I3, or selecting 8, 16 or 48 CPU cores for R5 host type.
+  Any discussion of Oracle licensing policies and costs in this whitepaper is for informational purposes only and is based on the information available at the time of publication. For more specific information, users should consult their own Oracle license agreements.

## Amazon RDS license included
<a name="amazon-rds-license-included"></a>

 You have the option to include the cost of the Oracle Database license in the hourly price of the Amazon RDS service if you use the License Included service model. In this case, you do not need to purchase Oracle licenses separately; the Oracle Database software has been licensed by AWS. License Included per-hour pricing includes software, underlying hardware resources, and Amazon RDS management capabilities. This service model optimizes license costs, and gives you flexibility when scaling your Amazon RDS instances up or down. You can take advantage of hourly pricing with no upfront fees or long-term commitments. In addition, you can purchase Amazon RDS Reserved Instances under one-year or three-year reservation terms. With Reserved Instances, you can make a low, one-time payment up front for each database instance, and then pay a significantly discounted hourly usage rate.

**Note**
 **Note:** The hourly license for the License Included model in Amazon RDS is available only for Oracle Standard Edition One and Standard Edition Two. For other editions of Oracle Database on Amazon RDS and any edition of Oracle Database on Amazon EC2, you need to use your own license (that is, acquire a license from Oracle), as discussed in the following section.

 Since you are paying for the Oracle license only for the hours in which you use Amazon RDS, the License Included option may help you reduce overall licensing costs for development and testing environments that are active only during business hours. For most businesses, the total business hours per week (10 x 5 = 50 hours) is only about 30% of the total hours in a week (24 x 7 = 168 hours), so this service model could result in considerable savings.

 This service model also gives you the flexibility to resize the instance based on your needs, because the license is included in the instance cost. In cases where your regular capacity requirements are much smaller than periodic, predictable spikes, this service model allows you to scale up to absorb the additional capacity needed, and scale down to save on cost. For example, you might have databases that require the performance of a `db.m3.large` instance for most days of the month except for the last three days. During the last three days of the month, your database might be heavily used due to payroll processing and month-end closing. In this scenario, you can use Oracle Database on Amazon RDS based on the `db.m3.large` instance type throughout the month, scale up to `db.m3.2xlarge` for the last three days, and then scale down again. This could translate to 65% or more cost savings compared to using the `db.m3.2xlarge` instance for the whole month.

## Bring Your Own License (BYOL)
<a name="bring-your-own-license-byol"></a>

 If you already own Oracle Database licenses, you can use the BYOL service model to run your Oracle databases on Amazon RDS. This will result in a lower cost for the Amazon RDS instance because the cost of the Oracle license isn’t included. The BYOL model is designed for customers who prefer to use their existing Oracle Database licenses or purchase new licenses directly from Oracle.

 If you want to use Oracle Database Enterprise Edition with Amazon RDS, or run your own self-managed Oracle Database on Amazon EC2 or VMware Cloud on AWS, BYOL is the only supported option.

### Oracle license portability to AWS
<a name="oracle-license-portability-to-aws"></a>

 Subject to the terms and conditions of the specific license agreement, Oracle licenses may be portable to AWS. In other words, your existing licenses can be transferred for use on AWS. These include:
+  Server-based licenses (based on CPUs used)
+  Enterprise License Agreements (ELA)
+  Unlimited License Agreements (ULA)
+  Business Process Outsourcing (BPO) licenses
+  Oracle PartnerNetwork (OPN) licenses
+  Named User Plus licenses

 Additional conditions or limitations (including possible costs) may be applicable for licenses that are ported to AWS. Check your specific license agreement for additional details and limitations.

 Oracle licensing applies similarly to Oracle Database on Amazon RDS and on Amazon EC2 with the exception that hourly licensing is available only on Amazon RDS.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Whitepapers. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query whitepapers` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
