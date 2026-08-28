---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/resilience-lifecycle-framework/introduction.html
---

# Resilience lifecycle framework: A continuous approach to resilience improvement
<a name="introduction"></a>

*Lisi Lewis, Jason Barto, Wangechi Doble, Bruno Emer, John Formento, Mike Haken, Neeraj Kumar, and Clark Richey, Amazon Web Services*

Modern organizations today face an ever-growing number of resilience-related challenges, especially as expectations from customers shift toward an *always on, always available* mindset. Remote teams and complex, distributed applications are coupled with an increasing need for frequent releases. As a result, an organization and its applications need to be more resilient than ever.

AWS defines resilience as the ability of an application to resist or recover from disruptions, including those related to infrastructure, dependent services, misconfigurations, and transient network issues. (See [Resiliency, and the components of reliability](https://docs.aws.amazon.com/wellarchitected/latest/reliability-pillar/resiliency-and-the-components-of-reliability.html) in the AWS Well-Architected Framework Reliability Pillar documentation.) However, to achieve the desired level of resilience, trade-offs are often required. Operational complexity, engineering complexity, and cost will need to be assessed and adjusted accordingly.

Based on years of working with customers and internal teams, AWS has developed a resilience lifecycle framework that captures resilience learnings and best practices. The framework outlines five key stages that are illustrated in the following diagram. At each stage you can use strategies, services, and mechanisms  to improve your resilience posture.

![Resilience lifecycle framework](http://docs.aws.amazon.com/prescriptive-guidance/latest/resilience-lifecycle-framework/images/guide-img/3fbf10f7-8a26-4fb7-b9c0-58902dbfe93c/images/f9b747e4-5196-48c9-832c-06fed270be40.png)

These stages are discussed in the following sections of this guide:
+ [Stage 1: Set objectives](stage-1.md)
+ [Stage 2: Design and implement](stage-2.md)
+ [Stage 3: Evaluate and test](stage-3.md)
+ [Stage 4: Operate](stage-4.md)
+ [Stage 5: Respond and learn](stage-5.md)

## Terms and definitions
<a name="definitions"></a>

The resilience concepts of each stage are applied at different levels, ranging from individual components to entire systems. Implementing these concepts requires a clear definition of several terms:
+ A *component* is an element that performs a function, and consists of software and technology resources. Examples of components include code configuration, infrastructure such as networking, or even servers, data stores, and external dependencies such as multi-factor authentication (MFA) devices.
+ An *application* is a collection of components that delivers business value, such as a customer-facing web storefront or the backend process that improves machine learning models. An application might consist of a subset of components in a single AWS account, or it might be a collection of multiple components that span multiple AWS accounts and Regions.
+ A *system* is a collection of applications, people, and processes that are required to manage a given business function. It encompasses the application required to run a function; operational processes such as continuous integration and continuous delivery (CI/CD), observability, configuration management, incident response, and disaster recovery; and the operators who manage such tasks.
+ A *disruption* is an event that prevents your application from delivering its business function properly.
+ *Impairment* is the effect that a disruption has on an application if it isn't mitigated. Applications can be impaired if they suffer a set of disruptions.

## Continuous resilience
<a name="continuous-resilience"></a>

The resilience lifecycle is an ongoing process. Even within the same organization, your application teams might perform at different levels of completeness within each stage, depending on the requirements of your application. However, the more complete each stage is, the higher level of resilience your application will have.

You should think of the resilience lifecycle as a standard process that your organization can operationalize. AWS has intentionally modeled the resilience lifecycle to be similar to the software development lifecycle (SDLC), with the goal of incorporating planning, testing, and learning throughout the operating processes while you develop and operate your applications. As with many agile development processes, the resilience lifecycle can be repeated with every iteration of the development process.  We recommend that you deepen the practices within each stage of the lifecycle progressively over time.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
