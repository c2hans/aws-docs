---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/iap-on-aws/defining-and-managing-service-catalog-product-resources-as-applications.html
---

# Defining and managing Service Catalog product resources as applications
<a name="defining-and-managing-service-catalog-product-resources-as-applications"></a>

Service Catalog AppRegistry provides centralized application search, reporting, and management capabilities. An AppRegistry application can include one or more provisioned product stacks as well as CloudFormation stacks that are independent of Service Catalog.  You can group and view all your application resource collections across the AWS accounts that you define as deployment targets. These accounts could be your development, test, and production lifecycle accounts.

You can also use AppRegistry to associate metadata attributes with an application. You can assign reusable attribute groups that contain sets of attributes. You can then search and act on application resources that have the given attributes by using AppRegistry or integrated services. These integrated services include:
+ [Application Manager](https://docs.aws.amazon.com/systems-manager/latest/userguide/application-manager.html), a capability of AWS Systems Manager, to investigate and remediate issues with AWS resources in the context of your applications and clusters
+ [AWS Resource Access Manager](https://docs.aws.amazon.com/ram/latest/userguide/what-is.html), to share applications and attribute groups with AWS organization principals
+ [AWS services that work with AWS Resource Groups](https://docs.aws.amazon.com/ARG/latest/userguide/integrated-services-list.html)
+ [AWS Resilience Hub](https://docs.aws.amazon.com/resilience-hub/latest/userguide/discover-structure-step1.html) for product structure discovery and resilience assessment
+ [AWS Service Management Connector](https://docs.aws.amazon.com/servicecatalog/latest/smcguide/overview.html) to declare and set up connections to ServiceNow, JIRA, and other popular tools

For more information about AppRegistry, see the following:
+ [AppRegistry Administrator Guide](https://docs.aws.amazon.com/servicecatalog/latest/arguide/intro-app-registry.html).
+ [Increase application visibility and governance using AWS Service Catalog AppRegistry](https://aws.amazon.com/blogs/mt/increase-application-visibility-governance-using-aws-service-catalog-appregistry/) blog post. This article provides an overview of how to use AppRegistry in infrastructure governance, with command-line examples of registering your infrastructure as applications in AppRegistry.
+ [Govern your applications centrally using AppRegistry and Application Manager](https://aws.amazon.com/blogs/mt/govern-your-applications-centrally-using-appregistry-and-application-manager/) blog post. This article provides an overview with a tutorial of how to apply AppRegistry to register a LAMP web application on the AWS Management Console and manage it by using Application Manager.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
