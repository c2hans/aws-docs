---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/modernization-aspnet-web-services/whats-next.html
---

# Next steps and resources
<a name="whats-next"></a>

To begin the migration and modernization process for your legacy ASP.NET applications:

1. Determine the type of ASP.NET web services you will be migrating to AWS. From a modernization perspective, ASP.NET web services can be classified in three categories. The first two categories, discussed in this guide, are SOAP-based ASP.NET web services written either with ASMX files or by using Windows Communication Foundation (WCF), and REST-based ASP.NET services written by using RESTful ASP.NET Web APIs or the ASP.NET Model-View-Controller (MVC) pattern. The third type of ASP.NET web services are written using ASP.NET MVC and .NET Core or .NET 5. This is the current, recommended way to write ASP.NET REST APIs and should not require significant modernization to migrate to AWS.

1. Determine how these services are secured for authentication and authorization, establish your approach, and prioritize this aspect of the modernization effort.

1. Familiarize yourself with Windows containers, Amazon ECS, and Amazon API Gateway.

1. Read up on [domain-driven design](https://martinfowler.com/bliki/DomainDrivenDesign.html). This will help you make the most of your modernization efforts by ensuring that the modernized services are modeled around cohesive functional domains instead of the design of the legacy system.

1. Establish your target state architecture, and then work backward to determine the interim-state architectures needed to achieve that outcome.

For more information about the patterns discussed in this guide, see the following articles by Martin Fowler:
+ [Strangler fig application](https://martinfowler.com/bliki/StranglerFigApplication.html)
+ [Branch by abstraction](https://martinfowler.com/bliki/BranchByAbstraction.html)
+ [Domain-driven design](https://martinfowler.com/bliki/DomainDrivenDesign.html)

For more information about the AWS services discussed in this guide, see the following references:
+ [Amazon Elastic Container Service (Amazon ECS)](https://aws.amazon.com/ecs/)
+ [Amazon API Gateway](https://aws.amazon.com/api-gateway/)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
