---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/migration-databases-postgresql-ec2/app-migration-service-considerations.html
---

# Application Migration Service
<a name="app-migration-service-considerations"></a>

You can use AWS Application Migration Service to quickly migrate your applications to the cloud with minimal downtime. Application Migration Service minimizes time-intensive, error-prone manual processes by automatically converting your source servers from physical, virtual, and cloud infrastructure to run natively on AWS. Application Migration Service replicates source servers into your AWS account. When you're ready, Application Migration Services automatically converts and launches your servers on AWS so that you can quickly benefit from the cost savings, productivity, resilience, and agility of the AWS Cloud. There are some use cases where Application Migration Service can be the fastest route to the cloud (for example, when you want to migrate a database and operating system to the cloud). To determine if using Application Migration Service is the best option for you, see [When to Choose AWS Application Migration Service](https://aws.amazon.com/application-migration-service/when-to-choose-aws-mgn/) in the Application Migration Service documentation.

## Architecture
<a name="architecture-app-migration-service"></a>

The following diagram shows the architecture for migrating an on-premises PostgreSQL database to the AWS Cloud by using Application Migration Service.

![Application Migration Service architecture](https://docs.aws.amazon.com/prescriptive-guidance/latest/migration-databases-postgresql-ec2/images/guide-img/d9d57133-1a8b-4b7f-bbe9-e908969d06b9/images/5e7fd64d-8a80-45dc-92a9-07d23a0d4426.png)

The diagram shows the following workflow:
+ Install the AWS replication agents on source database servers.
+ Configure the launch settings in the Application Migration Service console.
+ Launch the test instances.
+ Launch the cutover instances.
+ Finalize the cutover.

For more information on using Application Migration Service, see the [How to migrate on-premises workloads with AWS Application Migration Service](https://aws.amazon.com/blogs/publicsector/how-migrate-on-premises-workloads-aws-application-migration-service/) post in the AWS Public Sector Blog. For more information on how to identify potential bottlenecks for replication, see the [Identification of replication bottlenecks when using AWS Application Migration Service](https://aws.amazon.com/blogs/architecture/identification-of-replication-bottlenecks-when-using-aws-application-migration-service/) post in the AWS Architecture Blog.

## Limitations
<a name="limitations-app-migration-service"></a>

We recommend that you consider the following limitations of using Application Migration Service before starting your migration:
+ The maximum number of servers that can be actively replicating at any time is 20 in each supported AWS Region. You can increase this value to 60.
+ You can use a maximum of 200 source servers in a single job.

For more information on limitations, see [What are the MGN service quota limits?](https://docs.aws.amazon.com/mgn/latest/ug/General-Questions-FAQ.html#MGN-service-limits-faq) in the Application Migration Service documentation.
