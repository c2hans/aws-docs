---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/migration-factory-cloudendure/how-to-get-started-with-cloud-migration-factory.html
---

# How to get started with Cloud Migration Factory
<a name="how-to-get-started-with-cloud-migration-factory"></a>

The Cloud Migration Factory solution is available to all AWS customers and partners, and it can be deployed to your AWS account in just a few minutes. To deploy Cloud Migration Factory, see the [AWS Cloud Migration Factory Solution](https://aws.amazon.com/solutions/implementations/cloud-migration-factory-on-aws/) on the AWS Solutions website. The source code is available in a [GitHub repository](https://github.com/awslabs/aws-cloudendure-migration-factory-solution). If you have any questions, email AWS Professional Services at *migration-factory-support@amazon.com*.

## Prerequisites
<a name="prereqs"></a>

Cloud Migration Factory requires the following:
+ [Set up your AWS infrastructure](https://docs.aws.amazon.com/prescriptive-guidance/latest/migration-aws-environment/).
+ Complete the initial [portfolio discovery](https://docs.aws.amazon.com/prescriptive-guidance/latest/migration-portfolio-discovery/) and wave planning.
+ Follow the instructions in the [AWS Transform MGN user guide](https://docs.aws.amazon.com/mgn/latest/ug/mandatory-setup.html) to initialize and configure permissions for this service in the target AWS accounts.
+ Follow the instructions in the [AWS Cloud Migration Factory Solution implementation guide](https://docs.aws.amazon.com/solutions/latest/cloud-migration-factory-on-aws/solution-overview.html) to deploy Cloud Migration Factory.

After you complete these prerequisites, we can help you complete the steps described in the following sections to perform the migration. If you have multiple waves, you must repeat the steps for each wave. The recommended wave size is 25–35 servers. If you are planning to cut over more (for example, 100 servers) in the same cutover window, we recommend that you split the 100 servers into multiple waves and run the automation multiple times, because smaller waves are easier to troubleshoot from our experience.
