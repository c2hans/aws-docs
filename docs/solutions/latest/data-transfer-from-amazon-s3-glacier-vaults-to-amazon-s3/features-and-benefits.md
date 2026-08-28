---
source_url: https://docs.aws.amazon.com/solutions/latest/data-transfer-from-amazon-s3-glacier-vaults-to-amazon-s3/features-and-benefits.html
---

# Features and benefits
<a name="features-and-benefits"></a>

 The Guidance provides the following features:

 **Automation**

Automate the process of restoring, copying, and transferring archives from a vault in the Amazon Glacier service to a bucket in the Amazon S3 service. After you move your data, you can use the Amazon S3 console. A prebuilt Amazon CloudWatch dashboard helps you monitor metrics and visualize the copy operation progress.

 **Ability to assign storage classes**

 When you use this Guidance to move your data from the Amazon Glacier service into the Amazon S3 service, you choose a storage class to assign to all of your objects. After your data is stored in the Amazon S3 service, you can change the storage classes to fit the use case for each file. We recommend carefully reviewing each storage class and its pricing details before deploying this Guidance. See [Amazon S3 storage class considerations](amazon-s3-storage-class-considerations.md) for more information.

 **Visibility and access to data**

 After the Guidance stores Amazon Glacier archives as objects in the destination S3 bucket, you can add tags to data. Tagging offers benefits such data classification, permissions controls, object lifecycle management, and cost allocation. For more information, see [Categorizing your storage using tags](https://docs.aws.amazon.com/AmazonS3/latest/userguide/object-tagging.html) in the *Amazon Simple Storage Service User Guide*.

 **Flexibility to cancel your transfer and resume later**

 The Guidance tracks the progress of the transfer. You can stop and restart transfers without needing to retransfer existing archives. See [Problem: Transfer workflow must be stopped](troubleshooting.md#problem-transfer-workflow-must-be-stopped) for more information.

 **Cost optimization**

 Copy Amazon Glacier vault archives to an S3 bucket and assign more [cost-effective storage classes](https://aws.amazon.com/s3/pricing/), such as:
+  The low-cost S3 Glacier Deep Archive storage class for data that you rarely access
+  The S3 Glacier Instant Retrieval storage class if you'll need your data quarterly but within milliseconds
+  The S3 Standard storage class for data you'll need daily

 You can also configure and apply [S3 Lifecycles](https://docs.aws.amazon.com/AmazonS3/latest/userguide/object-lifecycle-mgmt.html) to transition your objects automatically into different storage classes, based on rules you set.

 **Integration with Service Catalog AppRegistry and Application Manager, a capability of AWS Systems Manager **

 This Guidance includes a [Service Catalog AppRegistry](https://docs.aws.amazon.com/servicecatalog/latest/arguide/intro-app-registry.html) resource to register the Guidance's CloudFormation template and its underlying resources as an application in both Service Catalog AppRegistry and [Application Manager](https://docs.aws.amazon.com/systems-manager/latest/userguide/application-manager.html). With this integration, centrally manage the Guidance's resources and enable application search, reporting, and management actions.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Data Transfer from Amazon S3 Glacier Vaults to Amazon S3. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query solutions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
