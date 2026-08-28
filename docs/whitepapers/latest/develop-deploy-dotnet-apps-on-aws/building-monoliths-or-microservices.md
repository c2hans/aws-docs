---
source_url: https://docs.aws.amazon.com/whitepapers/latest/develop-deploy-dotnet-apps-on-aws/building-monoliths-or-microservices.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Building Monoliths or Microservices
<a name="building-monoliths-or-microservices"></a>

One of the most common ways to build enterprise applications is as a single, unified application, in which all components are tightly coupled, and working from a shared database. When the .NET Framework was released, such monolithic applications were widespread. Even today it’s not uncommon to see ASP.NET applications with over 100,000 lines of code that have to be deployed to a single internet information service (IIS) instance.

As enterprise applications grew bigger, new challenges emerge out of this approach. The first problem is managing the resources available to an application. As monolithic applications grow bigger, they invariably require more resources, from compute and memory requirements to storage and network bandwidth. Although these issues can be solved by scaling the application servers vertically up or horizontally out, this approach naturally scales the whole application, even if a single module needs the additional resources.

The second problem is complexity. Monolithic applications with tightly coupled modules grow increasingly complex over time, which can make maintenance so complicated that even the smallest changes require significant effort for development, testing, and deployment. The increasing complexity adds friction to the business need for agility.

Because of the challenges inherent in monolithic applications, many modern applications have shifted to a new paradigm, commonly known as a *microservices architecture*. Microservices are small services providing a bounded context of functionality, each using their own data store, and predominantly integrating with other services by using event-driven communication.

Although microservices introduce their own complexities, such as how to separate data or how to distribute services, breaking monolithic applications into loosely coupled microservices can help overcome many of the problems with monolithic applications. Aside from the architectural benefits of microservices, the loose coupling in microservices means each service can be deployed and scaled independently. By ensuring each microservice has its own development lifecycle, DevOps teams are no longer tied to other team’s release cycles, and can therefore increase their deployment frequency, improving their agility, and increasing the business’s ability to respond to change.

Although .NET 5 can be used for a variety of application architectures, its lighter footprint and cross-platform nature makes it ideal for microservices. .NET 5 is also highly suitable for deploying to modern execution environments, including containers and serverless functions.

The following sections of this paper include several ways you can deploy both monolithic and distributed applications in the AWS Cloud. Monolithic deployment patterns are mostly applicable for legacy enterprise applications, or for developing new applications with limited complexity or scaling requirements, whereas microservices are commonly chosen for building optimized modern applications.

For more information on how to design and develop microservices, see the *[Implementing Microservices on AWS](https://docs.aws.amazon.com/whitepapers/latest/microservices-on-aws/microservices-on-aws.html)* whitepaper.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Whitepapers. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query whitepapers` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
