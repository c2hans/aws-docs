---
source_url: https://docs.aws.amazon.com/solutions/latest/cloud-migration-factory-on-aws/features-and-benefits.html
---

# Features and benefits
<a name="features-and-benefits"></a>

The solution provides the following features:

 **Manage, track and initiate you workload migration to AWS from a single web interface, supporting multiple target AWS accounts and regions.**

Provided with Amazon S3 static web site hosting, or in private deployment from an Amazon EC2 instance running a web server. All activities performed by the solution are initiated from with a single web interface, provided by the solution. See Migration Factory web interface for details.

 **Prepackaged automation tasks to perform many of the tasks required to fully migrate workloads to AWS using AWS Application Migration Service.**

The solution provides all the automation tasks required to migrate thousands of workloads to AWS without requiring scripting and with limited knowledge required to get started. All automations can be initiated from the web interface and behind the scenes use AWS System Manager to initiate and run the automation jobs on the provided automation server(s).

 **Customize the solution with automation packages and attribute schema extensions**

The majority of migrations require custom automation tasks to be run for applications and other environmental specific reasons, Cloud Migration Factory on AWS supports user customization of the provided scripts as well as the ability to load custom script into the solution. The solution also allows for the migration metadata store to be extended in seconds, providing administrators the ability to add and remove attributes to the schema that are needing to be tracked or used during the migration.

 **Integration with Service Catalog AppRegistry and AWS Systems Manager Application Manager**

This solution includes a Service Catalog AppRegistry resource to register the solution’s CloudFormation template and its underlying resources as an application in both [Service Catalog AppRegistry](https://docs.aws.amazon.com/servicecatalog/latest/arguide/intro-app-registry.html) and [AWS Systems Manager Application Manager](https://docs.aws.amazon.com/systems-manager/latest/userguide/application-manager.html). With this integration, you can centrally manage the solution’s resources and enable application search, reporting, and management actions.
