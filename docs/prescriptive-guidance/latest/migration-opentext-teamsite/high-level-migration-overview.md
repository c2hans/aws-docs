---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/migration-opentext-teamsite/high-level-migration-overview.html
---

# High-level migration overview
<a name="high-level-migration-overview"></a>

The following table shows a high-level overview of an OpenText TeamSite and Media Management migration to the AWS Cloud.

|  |  |
| --- |--- |
| Workload | Source workload | OpenText Customer Experience solutions:+ [OpenText TeamSite](https://www.opentext.com/products-and-solutions/products/customer-experience-management/web-content-management/opentext-teamsite)<br />+ [OpenText LiveSite](https://www.opentext.com/products-and-solutions/products/customer-experience-management/web-content-management/opentext-teamsite)<br />+ [OpenText Media Management](https://www.opentext.com/products-and-solutions/products/customer-experience-management/digital-asset-management/opentext-media-management)<br />+ [OpenText MediaBin](https://www.opentext.com/products-and-solutions/products/customer-experience-management/digital-asset-management/opentext-mediabin) |
| --- |--- |--- |
| Source environment | On premises or on another cloud provider. |
| **Migration** | Migration strategy (7 Rs) | Depending on your source environments, you can use the following migration strategies:+ Refactor<br />+ Rehost<br />+ Replatform |
| Is this an upgrade in workload version? | No |
| Is the source workload different from an independent software vendor (ISV) workload? | No |
| Estimated migration duration | Depending on your source environment, a migration can take between two and three weeks. |
| **Estimated cost** | Estimated cost of running ISV workloads on the AWS Cloud | A sample cost structure for three environments (development, QA-UAT, and production) using<br />[Elastic Load Balancing](https://docs.aws.amazon.com/elasticloadbalancing/latest/userguide/what-is-load-balancing.html) and a DevOps toolset for development and deployment is available in [this estimate](https://calculator.aws/?id=109c6f7bda67e38c02c99d31423b5a72f04561b6#/estimate) from AWS Pricing Calculator. |
| **Assumptions and prerequisites** | Minimum and maximum system requirements | Check the compatibility matrix for your OpenText product version. This matrix is available in the release notes on the [OpenText support portal](https://www.opentext.com/support). |

|  |  |  |
| --- |--- |--- |
|   | Service-level agreements (SLAs) | You can meet SLAs with a basic setup that uses Elastic Load Balancing, AWS Lambda functions, and two Availability Zones. |
| Licensing and operating model in the AWS account | For more information about your OpenText license agreement, contact your<br />OpenText account manager. |
| AWS services used in the AWS account | + [Amazon API Gateway](https://docs.aws.amazon.com/apigateway/latest/developerguide/welcome.html)<br />+ [Amazon Elastic Block Store (Amazon EBS)](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/AmazonEBS.html)<br />+ [Amazon Elastic Compute Cloud (Amazon EC2)](https://docs.aws.amazon.com/ec2/index.html)<br />+ [Amazon Elastic Container Service (Amazon ECS)](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/Welcome.html)<br />+ [Amazon OpenSearch Service](https://docs.aws.amazon.com/elasticsearch-service/latest/developerguide/what-is-amazon-elasticsearch-service.html)<br />+ [Elastic Load Balancing](https://docs.aws.amazon.com/elasticloadbalancing/latest/userguide/what-is-load-balancing.html)<br />+ [Lambda](https://docs.aws.amazon.com/lambda/latest/dg/welcome.html)<br />+ [Amazon Relational Database Service (Amazon RDS)](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Welcome.html)<br />+ [Amazon Simple Storage Service (Amazon S3)](https://docs.aws.amazon.com/AmazonS3/latest/userguide/Welcome.html) |

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
