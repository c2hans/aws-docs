---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/modernization-aspnet-web-services/types.html
---

# Types of ASP.NET web services
<a name="types"></a>

When you're planning to modernize your legacy [ASP.NET ](https://asp.net/)web services on AWS, you can generally group these services in two categories:
+ REST-based ASP.NET web services. These are built using either ASP.NET Web API (RESTful) or the ASP.NET Model-View-Controller (MVC) pattern.
+ SOAP-based ASP.NET web services. These are implemented by using Windows Communication Foundation (WCF) or ASP.NET Web Service (ASMX) files and ASP.NET WebMethods.

REST is the dominant architectural style in use today for web APIs. Therefore, services that are implemented using this approach are compatible with most modern tooling and frameworks, so they have a more straightforward modernization path. Modernizing these services is facilitated using API gateways and API managers, and primary concerns involve how the services model the resources and business domains they represent, and how the services are secured. However, web services that rely on SOAP generally predate REST-based services, and, therefore, have limited support today. Migration of these services involve the same concerns as REST-based services. They also face the additional challenge of little to no tooling and framework support.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
