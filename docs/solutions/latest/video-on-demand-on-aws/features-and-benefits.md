---
source_url: https://docs.aws.amazon.com/solutions/latest/video-on-demand-on-aws/features-and-benefits.html
---

# Features and benefits
<a name="features-and-benefits"></a>

The solution provides the following features:

 **Reference implementation**

Leverage the Video on Demand on AWS solution as a reference implementation to automatically provision the AWS services necessary to build a scalable, distributed video-on-demand workflow.

 **Customization**

The Video on Demand on AWS solution leverages AWS Step Functions, which breaks the workflow into individual steps (ingest, processing, and publishing), making it easier to customize or extend the architecture for your specific video-on-demand needs.

 **Digital Rights Management**

With this solution, you can also choose to use AWS Elemental MediaPackage for packaging content into different formats and to apply digital rights management (DRM). MediaPackage can reduce storage costs for the outputs; however, there is a trade-off between packaging costs and storage costs.

 **Integration with Service Catalog AppRegistry and AWS Systems Manager Application Manager**

This solution includes a Service Catalog AppRegistry resource to register the solution’s CloudFormation template and its underlying resources as an application in both [Service Catalog AppRegistry](https://docs.aws.amazon.com/servicecatalog/latest/arguide/intro-app-registry.html) and [AWS Systems Manager Application Manager](https://docs.aws.amazon.com/systems-manager/latest/userguide/application-manager.html). With this integration, you can centrally manage the solution’s resources and enable application search, reporting, and management actions.
