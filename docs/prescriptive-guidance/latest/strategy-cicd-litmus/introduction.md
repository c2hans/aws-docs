---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/strategy-cicd-litmus/introduction.html
---

# The CI/CD litmus test: Is your pipeline fully CI/CD?
<a name="introduction"></a>

*Steven Guggenheimer and Ananya koduri, Amazon Web Services*

Is your pipeline automated? It's a simple question, but many organizations approach the answer too simply. The answer is much more complicated than a *yes* or *no*.

Innovations in technology are happening constantly, and sometimes it can be hard for organizations to keep up. Is this new thing a fad, or is it the next big thing? Should I overhaul my current practices, or should I wait? Often, by the time it becomes clear that something is indeed the next big thing, you can find yourself playing catchup. *Continuous integration and continuous delivery* (CI/CD) is here to stay, but it wasn't always that way. Many people took a long time to be convinced, and some people still need more convincing.

CI/CD is the process of automating the source, build, test, staging, and production stages of the software release process, and it is commonly described as a pipeline. Today, the cost savings and speed of CI/CD automations have convinced most organizations of its value. But transitioning to this new approach is not an easy task. You need to make sure your staff has the right training, you need to upgrade some resources, and then you need to test, test, test. There's a lot to do. In most cases, you want to make these changes gradually to help your organization adapt.

The purpose of this document is to define what it means to have a fully CI/CD process. It provides a tool to evaluate your own processes and presents a path forward for processes that aren't there yet. This path forward is rarely an overnight conversion. These processes are complex and depend upon many factors, including current employee skill sets and current infrastructure demands. We recommend you prioritize and make small, incremental changes.

## Objectives
<a name="objectives"></a>

The following are the potential benefits of implementing the recommendations in this guide:
+ **Efficiency** – A fully CI/CD deployment process can reduce complexity, workloads, and countless hours spent debugging, performing manual processes, and maintaining. For more information, see [Benefits of continuous delivery](https://docs.aws.amazon.com/whitepapers/latest/practicing-continuous-integration-continuous-delivery/benefits-of-continuous-delivery.html). According to a [TechAhead blog post](https://www.techaheadcorp.com/blog/how-ci-cd-save-app-development-time/), the implementation of the CI/CD process can lead to an estimated 20% savings in time, effort, and resources.
+ **Cost reduction** – According to a [Forbes Insight report](https://www.forbes.com/sites/forbesinsights/2017/03/16/how-it-service-management-delivers-value-to-the-digital-enterprise/), "Three out of four executives agree that the amount of time, money, and resources spent on ongoing maintenance and management—versus new project development or new initiatives—is affecting the overall competitiveness of their organization." The shorter the development cycle, the higher the chances are that your organization can meet ambitious time-to-market goals and grab the right opportunities at the right time.
+ **Speed** – Typically, a fully CI/CD pipeline is able to release software changes to customers within a few hours. Especially in cases with quick fault isolations and small patch pushes, the CI/CD pipeline helps improve the mean time to recovery (MTTR). For more information, see [Reducing MTTR](https://docs.aws.amazon.com/whitepapers/latest/availability-and-beyond-improving-resilience/reducing-mttr.html).
+ **Security** – Fully CI/CD pipelines also secure the release process by reducing the possible entry points for attacks and reducing the risk of human error. The security gains that come with fully automated CI/CD pipelines help avoid the costly consequences of data breaches, service outages, and more.
+ **Reduced attrition** – Developers are more satisfied when they can spend more time creating great features and less time mired in an endless cycle of maintenance and debugging. For organizations, this means acquiring and retaining top talent for longer periods of time.
+ **Superior quality code** – Developers release code into a shared repository in small batches, which enables them to conduct [parallel testing](https://www.browserstack.com/guide/what-is-parallel-testing#:~:text=Parallel%20Testing%20is%20a%20process,reduce%20time%20and%20resource%20constraints.) (BrowserStack blog post). Rather than working in isolation, they share their builds with the team frequently, and they collaborate to identify critical bugs. This provides support for developers, which helps prevent bad code from making it to production. Support from developer peers contributes to high-quality releases and drives organizational growth.
+ **Maintenance** – Maintenance and updates are a crucial part of making a great product. However, don't take the system down during peak traffic times. You can use a CI/CD pipeline to perform maintenance during low-usage hours that minimize downtime and performance impacts.

## Attachments
<a name="attachments-de5d2132-0072-4b65-b7ac-e1e4c4852e08"></a>

To access additional content that is associated with this document, download and unzip the following file:

[attachment.zip](samples/attachment.zip)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
