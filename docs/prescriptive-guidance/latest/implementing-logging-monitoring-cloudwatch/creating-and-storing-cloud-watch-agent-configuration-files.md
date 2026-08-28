---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/implementing-logging-monitoring-cloudwatch/creating-and-storing-cloud-watch-agent-configuration-files.html
---

# Managing CloudWatch agent configuration files
<a name="creating-and-storing-cloud-watch-agent-configuration-files"></a>

We recommend that you create a standard Amazon CloudWatch agent configuration that includes the system logs and metrics that you want to capture across all your Amazon Elastic Compute Cloud (Amazon EC2) instances and on-premises servers. You can use the CloudWatch agent [configuration file wizard](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/create-cloudwatch-agent-configuration-file-wizard.html) to help you create the configuration file. You can run the configuration wizard multiple times to generate unique configurations for different systems and environments. You can also modify the configuration file or create variations by [using the configuration file schema](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-Agent-Configuration-File-Details.html). The CloudWatch agent configuration file can be stored in [AWS Systems Manager Parameter Store](https://docs.aws.amazon.com/systems-manager/latest/userguide/systems-manager-parameter-store.html) parameters.  You can create separate Parameter Store parameters if you have [multiple CloudWatch agent configuration files](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-Agent-common-scenarios.html#CloudWatch-Agent-multiple-config-files). If you are using multiple AWS accounts or AWS Regions, you must manage and update the Parameter Store parameters in each account and Region. Alternatively, you can centrally manage your CloudWatch configurations as files in Amazon S3 or a version-control tool of your choice.

The `amazon-cloudwatch-agent-ctl` script included with the CloudWatch agent allows you to specify a configuration file, Parameter Store parameter, or the agent's default configuration. The default configuration aligns to the basic, predefined metric set and configures the agent to report memory and disk space metrics to CloudWatch. However, it doesn't include any log file configurations. The default configuration is also applied if you use [Systems Manager Quick Setup](https://docs.aws.amazon.com/systems-manager/latest/userguide/systems-manager-quick-setup.html) for the CloudWatch agent.

Because the default configuration doesn't include logging and isn't customized for your requirements, we recommend that you create and apply your own CloudWatch configurations, customized to your requirements.

## Managing CloudWatch configurations
<a name="store-cloudwatch-configuration-s3"></a>

By default, CloudWatch configurations can be stored and applied as Parameter Store parameters or as CloudWatch configuration files.  The best choice will depend on your requirements.  In this section, we discuss the pros and cons for these two options.  A representative solution is also detailed for managing CloudWatch configuration files for multiple AWS accounts and AWS Regions.

### Systems Manager Parameter Store parameters
<a name="systems-manager-parameter-store-parameters.e6ecee03-c5d7-520b-87a3-45fc9a0ef88b"></a>

Using Parameter Store parameters to manage CloudWatch configurations works well if you have a single, standard CloudWatch agent configuration file that you want to apply and manage in a small set of AWS accounts and Regions. When you store your CloudWatch configurations as Parameter Store parameters, you can use the CloudWatch agent configuration tool (`amazon-cloudwatch-agent-ctl` on Linux) to read and apply the configuration from Parameter Store without requiring you to copy the configuration file to your instance. You can use the **AmazonCloudWatch-ManageAgent **Systems Manager Command document to update the CloudWatch configuration on multiple EC2 instances in a single run. Because Parameter Store parameters are regional, you must update and maintain your CloudWatch Parameter Store parameters in each AWS Region and AWS account. If you have multiple CloudWatch configurations that you want to apply to each instance, you must customize the **AmazonCloudWatch-ManageAgent** Command document** **to include these parameters.

### CloudWatch configuration files
<a name="cloudwatch-configuration-files.4fd3f461-8d32-5a03-beb8-cc47f78aa295"></a>

Managing your CloudWatch configurations as files might work well if you have many AWS accounts and Regions and you are managing multiple CloudWatch configuration files. Using this approach, you can browse, organize, and manage them in a folder structure.  You can apply security rules to individual folders or files to limit and grant access such as update and read permissions. You can share and transfer them outside of AWS for collaboration.  You can version control the files to track and manage changes.  You can apply CloudWatch configurations collectively by copying the configuration files to the CloudWatch agent configuration directory without applying each configuration file individually. For Linux, the CloudWatch configuration directory is found at `/opt/aws/amazon-cloudwatch-agent/etc/amazon-cloudwatch-agent.d`. For Windows, the configuration directory is found at `C:\ProgramData\Amazon\AmazonCloudWatchAgent\Configs`.

When you start the CloudWatch agent, the agent automatically appends each file found in these directories to create a CloudWatch composite configuration file. The configuration files should be stored in a central location (for example, an S3 bucket) that can be accessed by your required accounts and Regions.  An example solution using this approach is provided.

### Organizing CloudWatch configurations
<a name="organizing-cloudwatch-configurations.892230c4-fe37-55ff-8f4d-b5216a070cbc"></a>

Regardless of the approach used to manage your CloudWatch configurations, organize your CloudWatch configurations. You can organize your configurations into file or Parameter Store paths using an approach such as the following.

|  |  |
| --- |--- |
| */config/standard/windows/ec2* | Store standard Windows-specific CloudWatch configuration files for Amazon EC2. You can further categorize your standard operating system (OS) configurations for different Windows versions, EC2 instance types, and environments under this folder. |
| */config/standard/windows/onpremises* | Store standard Windows-specific CloudWatch configuration files for on-premises servers. You also further categorize your standard OS configurations for different Windows versions, server types, and environments under this folder. |
| */config/standard/linux/ec2* | Store your standard Linux-specific CloudWatch configuration files for Amazon EC2. You can further categorize your standard OS configuration for different Linux distributions, EC2 instance types, and environments under this folder. |
| */config/standard/linux/onpremises* | Store your standard Linux-specific CloudWatch configuration files for on-premises servers. You can further categorize your standard OS configuration for different Linux distributions, server types, and environments under this folder. |
| */config/ecs* | Store CloudWatch configuration files that are specific to Amazon Elastic Container Service (Amazon ECS) if you use Amazon ECS container instances. These configurations can be appended to the standard Amazon EC2 configurations for Amazon ECS specific systems-level logging and monitoring. |
| */config/<application\_name>* | Store your application-specific CloudWatch configuration files. You can further categorize your applications with additional folders and prefixes for environments and versions. |

## Example: Storing CloudWatch configuration files in an S3 bucket
<a name="example"></a>

This section provides an example using Amazon S3 to store CloudWatch configuration files and a custom Systems Manager runbook to retrieve and apply the CloudWatch configuration files. This approach can address some of the challenges of using Systems Manager Parameter Store parameters for CloudWatch configuration at scale:
+ If you use multiple Regions, you must synchronize CloudWatch configuration updates in each Region's Parameter Store. Parameter Store is a Regional service and the same parameter must be updated in each Region that uses the CloudWatch agent.
+ If you have multiple CloudWatch configurations, you must initiate the retrieval and application of each Parameter Store configuration. You must individually retrieve each CloudWatch configuration from the Parameter Store and also update the retrieval method whenever you add a new configuration. In contrast, CloudWatch provides a configuration directory for storing configuration files and applies each configuration in the directory, without requiring them to be individually specified.
+ If you use multiple accounts, you must ensure that each new account has the required CloudWatch configurations in its Parameter Store. You also need to make sure that any configuration changes are applied to these accounts and their Regions in the future.

You can store CloudWatch configurations in an S3 bucket that is accessible from all your accounts and Regions. You can then copy these configurations from the S3 bucket to the CloudWatch configuration directory by using Systems Manager Automation runbooks and Systems Manager State Manager. You can use the [cloudwatch-config-s3-bucket.yaml](https://github.com/aws-samples/logging-monitoring-apg-guide-examples/blob/main/cloudwatch-config-s3-bucket.yaml) AWS CloudFormation template to create an S3 bucket that is accessible from multiple accounts within an organization in AWS Organizations. The template includes an `OrganizationID` parameter that grants read access to all accounts within your [organization](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_getting-started_concepts.html).

The augmented sample Systems Manager runbook, provided in the [Set up State Manager and Distributor for CloudWatch agent deployment and configuration](https://docs.aws.amazon.com/prescriptive-guidance/latest/implementing-logging-monitoring-cloudwatch/install-cloudwatch-systems-manager.html#set-up-systems-manager-distributor) section of this guide, is configured to retrieve files using the S3 bucket created by the [cloudwatch-config-s3-bucket.yaml](https://github.com/aws-samples/logging-monitoring-apg-guide-examples/blob/main/cloudwatch-config-s3-bucket.yaml) AWS CloudFormation template.

Alternatively, you can use a version control system (for example, GitHub) to store your configuration files. If you want to automatically retrieve configuration files stored in a version control system, you have to manage or centralize the credential storage and update the Systems Manager Automation runbook that is used to retrieve the credentials across your accounts and Regions.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
