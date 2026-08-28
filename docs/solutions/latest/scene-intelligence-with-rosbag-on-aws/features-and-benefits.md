---
source_url: https://docs.aws.amazon.com/solutions/latest/scene-intelligence-with-rosbag-on-aws/features-and-benefits.html
---

# Features and benefits
<a name="features-and-benefits"></a>

The solution provides the following features:

 **Extract rosbag data**

You can use this solution to store rosbag files in [Amazon Simple Storage Service](https://aws.amazon.com/s3/) (Amazon S3) and invoke [Directed Acyclic Graphs](https://docs.aws.amazon.com/mwaa/latest/userguide/working-dags.html) (DAGs) with [Amazon Managed Workflows for Apache Airflow](https://aws.amazon.com/managed-workflows-for-apache-airflow/) (Amazon MWAA) to extract and process the data. With the data extracted and processed, you can more easily review and analyze your data.

 **Customizable end-to-end**

You can determine which sensors to process, change the machine learning (ML) models used for processing, and bring your own DAGs for processing.

 **Indexable metadata**

Business data output that the solution writes to DynamoDB and is automatically available in OpenSearch Service, ready to be queried without user management.

 **Integration with Service Catalog AppRegistry and Application Manager, a capability of AWS Systems Manager**

This solution includes a [Service Catalog AppRegistry](https://docs.aws.amazon.com/servicecatalog/latest/arguide/intro-app-registry.html) resource to register the solution’s CloudFormation template and its underlying resources as an application in both AppRegistry and [Application Manager](https://docs.aws.amazon.com/systems-manager/latest/userguide/application-manager.html). With this integration, you can centrally manage the solution’s resources and enable application search, reporting, and management actions.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Scene Intelligence with Rosbag on AWS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query solutions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
