---
source_url: https://docs.aws.amazon.com/microservice-extractor/latest/userguide/microservice-extractor-apis.html
---

AWS .NET Modernization Tools Porting Assistant (PA) for .NET, AWS App2Container (A2C), AWS Toolkit for .NET Refactoring (TR), and AWS Microservice Extractor (ME) for .NET is no longer open to new customers. If you would like to use the service, sign up prior to November 7, 2025. Alternatively use [AWS Transform](https://aws.amazon.com/transform/), which is an agentic AI service developed to accelerate enterprise modernization of .NET.

# APIs Tab
<a name="microservice-extractor-apis"></a>

 You can view which APIs your application utilizes as well as the classes where they are referenced by navigating to the **APIs** tab after onboarding and analyzing an application. From the search bar in the table, you are able to either include or exclude APIs based on several fields, including their **compatibility** with .NET Core and corresponding Class. From this page you can also select any number of APIs and add them to a group by clicking the **Add to Group** button, just like you would in the Visualization tab.

![All APIs discovered in a solution and their associated classes.](http://docs.aws.amazon.com/microservice-extractor/latest/userguide/images/APIsTable.png)

 **Note:** The groups created will be created using the classes that the corresponding APIs belong to; therefore a class containing multiple APIs will not be able to have its APIs in separate groups.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Microservice Extractor for .NET. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query microservice-extractor` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
