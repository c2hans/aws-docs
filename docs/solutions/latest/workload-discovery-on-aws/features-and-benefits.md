---
source_url: https://docs.aws.amazon.com/solutions/latest/workload-discovery-on-aws/features-and-benefits.html
---

# Features and benefits
<a name="features-and-benefits"></a>

Workload Discovery on AWS provides the following features:

 **Build architecture diagrams using near real-time data**

Workload Discovery on AWS scans your accounts every 15 minutes to ensure that the diagrams you create are an accurate and current representation of your workloads.

 **View resources from multiple accounts and Regions in one place**

The solution maintains an inventory of the AWS resources across your AWS accounts and Regions in a centralized graph database, allowing you to explore multiple accounts and Regions and their relationships to each other in a single UI.

 **AWS Organizations integration**

When deploying the solution with [AWS Organizations](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_introduction.html), Workload Discovery on AWS will automatically discover all the supported resources in your organization. In this configuration, there is no need to directly manage the deployment of account specific CloudFormation templates to make these accounts available for discovery.

 **Collate cost data across your workloads**

When enabled, the cost feature allows you to search for resources in your account by cost and add the resources you find to a diagram. You can also add cost data to already existing diagrams.

 **Export to diagrams.net (formerly draw.io)**

Workload Discovery on AWS can export your diagrams so that you can further annotate them using this third-party drawing software.

 **Integration with AWS Service Catalog AppRegistry and Application Manager, a capability of AWS Systems Manager**

This solution includes a [Service Catalog AppRegistry](https://docs.aws.amazon.com/servicecatalog/latest/arguide/intro-app-registry.html) resource to register the solution’s CloudFormation template and its underlying resources as an application in both Service Catalog AppRegistry and [Application Manager](https://docs.aws.amazon.com/systems-manager/latest/userguide/application-manager.html). With this integration, you can centrally manage the solution’s resources and enable application search, reporting, and management actions.
