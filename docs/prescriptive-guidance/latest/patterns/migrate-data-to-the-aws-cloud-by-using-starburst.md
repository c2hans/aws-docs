---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/migrate-data-to-the-aws-cloud-by-using-starburst.html
---

# Migrate data to the AWS Cloud by using Starburst
<a name="migrate-data-to-the-aws-cloud-by-using-starburst"></a>

*Antony Prasad Thevaraj and Suresh Veeragoni, Amazon Web Services*

*Shaun Van Staden, None*

## Summary
<a name="migrate-data-to-the-aws-cloud-by-using-starburst-summary"></a>

Starburst helps accelerate your data migration journey to Amazon Web Services (AWS) by providing an enterprise query engine that brings existing data sources together in a single access point. You can run analytics across multiple data sources to get valuable insights, before finalizing any migration plans. Without disrupting business-as-usual analytics, you can migrate the data by using the Starburst engine or a dedicated extract, transform, and load (ETL) application.

## Prerequisites and limitations
<a name="migrate-data-to-the-aws-cloud-by-using-starburst-prereqs"></a>

**Prerequisites**
+ An active AWS account
+ A virtual private cloud (VPC)
+ An Amazon Elastic Kubernetes Service (Amazon EKS) cluster
+ An Amazon Elastic Compute Cloud (Amazon EC2) Auto Scaling group
+ A list of current system workloads that need to be migrated
+ Network connectivity from AWS to your on-premises environment

## Architecture
<a name="migrate-data-to-the-aws-cloud-by-using-starburst-architecture"></a>

**Reference architecture**

The following high-level architecture diagram shows the typical deployment of Starburst Enterprise in the AWS Cloud:

1. The Starburst Enterprise cluster runs inside your AWS account.

1. A user authenticates by using Lightweight Directory Access Protocol (LDAP) or Open Authorization (OAuth) and interacts directly with the Starburst cluster.

1. Starburst can connect to several AWS data sources, such as AWS Glue, Amazon Simple Storage Service (Amazon S3), Amazon Relational Database Service (Amazon RDS), and Amazon Redshift. Starburst provides federated query capabilities across data sources in the AWS Cloud, on premises, or in other cloud environments.

1. You launch Starburst Enterprise in an Amazon EKS cluster by using Helm charts.

1. Starburst Enterprise uses Amazon EC2 Auto Scaling groups and Amazon EC2 Spot Instances to optimize infrastructure.

1. Starburst Enterprise connects directly to your existing on-premises data sources to read data real-time. In addition, if you have an existing Starburst Enterprise deployment in this environment, you can directly connect your new Starburst cluster in the AWS Cloud to this existing cluster.

![High-level architecture diagram of Starburst Enterprise deployment in the AWS Cloud](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/images/pattern-img/12ae0463-9029-4a32-9d7b-70cdb5406fb0/images/e9975d3a-f75b-41a2-8c08-5b82539adf8c.png)

Please note the following:
+ Starburst is not a data virtualization platform. It is a SQL-based massively parallel processing (MPP) query engine that forms the basis of an overall data mesh strategy for analytics.
+ When Starburst is deployed as part of a migration, it has direct connectivity to the existing on-premises infrastructure.
+ Starburst provides several built-in enterprise and open-source connectors that facilitate connectivity to a variety of legacy systems. For a full list of connectors and their capabilities, see [Connectors](https://docs.starburst.io/latest/connector.html) in the *Starburst Enterprise user guide*.
+ Starburst can query data in real-time from on-premises data sources. This prevents interruptions of regular business operations while data is being migrated.
+ If you are migrating from an existing on-premises Starburst Enterprise deployment, you can use a special connector, *Starburst Stargate*, to connect your Starburst Enterprise cluster in AWS directly to your on-premises cluster. This provides additional performance benefits when business users and data analysts are federating queries from the AWS Cloud to your on-premises environment.

**High-level process overview**

You can accelerate data migration projects by using Starburst because Starburst enables insights across all of your data, prior to migrating it. The following image shows the typical process for migrating data by using Starburst.

![Process flow for migrating data to the AWS Cloud by using Starburst](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/images/pattern-img/12ae0463-9029-4a32-9d7b-70cdb5406fb0/images/e79b0084-7275-4824-8854-646236ec23dc.png)

**Roles**

The following roles are typically required to complete a migration using Starburst:
+ **Cloud administrator **– Responsible for making cloud resources available to run the Starburst Enterprise application
+ **Starburst administrator** – Responsible for installing, configuring, managing, and supporting the Starburst application
+ **Data engineer**– Responsible for:
  + Migrating the legacy data to the cloud
  + Building semantic views to support analytics
+ **Solution or system owner** – Responsible for the overall solution implementation

## Tools
<a name="migrate-data-to-the-aws-cloud-by-using-starburst-tools"></a>

**AWS services**
+ [Amazon Elastic Compute Cloud (Amazon EC2)](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/concepts.html) provides scalable computing capacity in the AWS Cloud. You can launch as many virtual servers as you need and quickly scale them up or down.
+ [Amazon Elastic Kubernetes Service (Amazon EKS)](https://docs.aws.amazon.com/eks/latest/userguide/what-is-eks.html) helps you run Kubernetes on AWS without needing to install or maintain your own Kubernetes control plane or nodes.

**Other tools**
+ [Helm](https://helm.sh/docs/) – Helm is a package manager for Kubernetes that helps you install and manage applications on your Kubernetes cluster.
+ [Starburst Enterprise](https://docs.starburst.io/latest/index.html) – Starburst Enterprise is a SQL-based massively parallel processing (MPP) query engine that forms the basis of an overall data mesh strategy for analytics.
+ [Starburst Stargate](https://docs.starburst.io/latest/connector/starburst-stargate.html) – Starburst Stargate links catalogs and data sources in one Starburst Enterprise environment, such as a cluster in an on-premises data center, to the catalogs and data sources in another Starburst Enterprise environment, such as a cluster in the AWS Cloud.

## Epics
<a name="migrate-data-to-the-aws-cloud-by-using-starburst-epics"></a>

### Assess the data
<a name="assess-the-data"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Identify and prioritize your data. | Identify the data you want to move. Large, on-premises legacy systems can include core data that you want to migrate alongside data that you don’t want to move or can’t be moved because of compliance reasons. Starting with a data inventory helps you prioritize which data you should target first. For more information, see [Get started with automated portfolio discovery](https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/get-started-with-automated-portfolio-discovery.html). | Data engineer, DBA |
| Explore, inventory, and back up your data. | Validate the quality, quantity, and relevance of the data for your use case. Back up or create a snapshot of the data as needed, and finalize the target environment for the data. | Data engineer, DBA |

### Set up the Starburst Enterprise environment
<a name="set-up-the-starburst-enterprise-environment"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Configure Starburst Enterprise in the AWS Cloud. | While data is being catalogued, set up Starburst Enterprise in a managed Amazon EKS cluster. For more information see, [Deploying with Kubernetes](https://docs.starburst.io/latest/k8s.html) in the *Starburst Enterprise reference documentation*. This allows business-as-usual analytics while data migration is in process. | AWS administrator, App developer |
| Connect Starburst to the data sources. | After you have identified the data and set up Starburst Enterprise, connect Starburst to the data sources. Starburst reads data directly from the data source as a SQL query. For more information, see the [Starburst Enterprise reference documentation](https://docs.starburst.io/latest/overview.html). | AWS administrator, App developer |

### Migrate the data
<a name="migrate-the-data"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Build and run the ETL pipelines. | Begin the data migration process. This activity can occur at the same time as business-as-usual analytics. For the migration, you can use a third-party product or Starburst. Starburst has the capability to both read and write data across different sources. For more information, see the [Starburst Enterprise reference documentation](https://docs.starburst.io/latest/overview.html). | Data engineer |
| Validate the data. | After the data has been migrated, validate the data to ensure all required data has been moved and is intact. | Data engineer, DevOps engineer |

### Cut over
<a name="cut-over"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Cut over the data. | After data migration and validation is complete, you can cut over the data. This involves changing the data connection links in Starburst. Instead of pointing at the on-premises sources, you point to the new cloud sources and update the semantic views. For more information, see [Connectors](https://docs.starburst.io/latest/connector.html) in the *Starburst Enterprise reference documentation*. | Data engineer, Cutover lead |
| Roll out to users. | Data consumers begin working off the migrated data sources. This process is invisible to the analytics end users. | Cutover lead, Data engineer |

## Related resources
<a name="migrate-data-to-the-aws-cloud-by-using-starburst-resources"></a>

**AWS Marketplace**
+ [Starburst Galaxy](https://aws.amazon.com/marketplace/pp/prodview-yugyv4gbgn5ss?ref_=srh_res_product_title)
+ [Starburst Enterprise](https://aws.amazon.com/marketplace/pp/prodview-pwnl3c6p2jycg?ref_=srh_res_product_title)
+ [Starburst Data JumpStart](https://aws.amazon.com/marketplace/pp/prodview-ou6drb23gch2u?ref_=srh_res_product_title)
+ [Starburst Enterprise with Graviton](https://aws.amazon.com/marketplace/pp/prodview-2bpppdqlesn6w?ref_=srh_res_product_title)

**Starburst documentation**
+ [Starburst Enterprise user guide](https://docs.starburst.io/index.html)
+ [Starburst Enterprise reference documentation](https://docs.starburst.io/latest/index.html)

**Other AWS documentation**
+ [Get started with automated portfolio discovery](https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/get-started-with-automated-portfolio-discovery.html) (AWS Prescriptive Guidance)
+ [Optimizing Cloud Infrastructure Cost and Performance with Starburst on AWS](https://aws.amazon.com/blogs/architecture/optimizing-cloud-infrastructure-cost-and-performance-with-starburst-on-aws/) (AWS blog post)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
