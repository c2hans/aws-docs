---
source_url: https://docs.aws.amazon.com/solutions/latest/scalable-analytics-using-apache-druid-on-aws/features-and-benefits.html
---

# Features and benefits
<a name="features-and-benefits"></a>

The guidance provides the following features:

 **Easily deploy Druid clusters to AWS accounts**

The guidance offers customers flexibility to customize installations, including your choice of AWS compute engine and storage from a variety of instance and serverless options. You can choose different compute types, such as [Amazon Elastic Compute Cloud](https://aws.amazon.com/ec2/) (Amazon EC2), [Amazon Elastic Kubernetes Service](https://aws.amazon.com/eks/) (Amazon EKS) , or [AWS Fargate](https://aws.amazon.com/fargate/), helping you to select the most suitable infrastructure for your specific needs.

 **High degree of customization**

The guidance supports various EC2 instance types, including Graviton instances, and offers flexibility in selecting database services, such as [Aurora PostgreSQL - Compatible Edition](https://aws.amazon.com/rds/aurora/features/), Aurora PostgreSQL Serverless, or bringing your own database. Customers have the freedom to fine-tune Druid configuration parameters to meet their requirements precisely.

 **High Availability and resiliency**

The guidance provides high availability and resiliency through features such as automatic scaling with customizable policies, and distributing Druid nodes across multiple availability zones. It also supports recreating clusters from metadata store and deep storage backups, ensuring data is protected and available even in the face of unexpected failures.

 **Built-in logging and monitoring with Amazon CloudWatch**

The guidance outputs log entries, emitted by Druid, to a centralized Amazon CloudWatch log group to ease debugging and troubleshooting activities, sets up a monitoring dashboard to track the health of the Druid cluster, and configures alarms based on customer preferences.

 **Integration with Service Catalog AppRegistry and Application Manager, a capability of AWS Systems Manager**

This guidance includes a [Service Catalog AppRegistry](https://docs.aws.amazon.com/servicecatalog/latest/arguide/intro-app-registry.html) resource to register the guidance’s CloudFormation template and its underlying resources as an application in both Service Catalog AppRegistry and [Application Manager](https://docs.aws.amazon.com/systems-manager/latest/userguide/application-manager.html). With this integration, you can centrally manage the guidance’s resources and enable application search, reporting, and management actions.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Guidance for Scalable Analytics Using Apache Druid on AWS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query solutions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
