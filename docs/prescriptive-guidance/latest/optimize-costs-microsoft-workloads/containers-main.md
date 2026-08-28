---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/optimize-costs-microsoft-workloads/containers-main.html
---

# Containers
<a name="containers-main"></a>

Modernization is a transformational journey that offers many options, including decomposing monoliths to microservices, re-architecting applications to be event-driven by using serverless functions (AWS Lambda), and repurposing databases from SQL Server to Amazon Aurora or purpose-built managed databases. The modernization pathways to replatform .NET Framework applications to Linux and Windows containers require less effort than other modernization options. Containers offer the following benefits:
+ **Accelerate innovation** – Moving to containers makes it easier to automate stages of the development lifecycle that include building, testing, and deploying applications. By automating these processes, development and operations teams have more time to focus on innovating.
+ **Reduce total cost of ownership (TCO)** – Moving to containers can also reduce your reliance on license management and endpoint protection tools. Because containers are ephemeral units of compute, you can automate and simplify management tasks such as patching, scaling, and backup and restore. This reduces the TCO of administering and operating container-based workloads. Finally, containers are more efficient in comparison to virtual machines because you can use containers to maximize the placement of your applications by providing better isolation. This increases the utilization of your application's infrastructure resources.
+ **Improve resource utilization** – Containers are more efficient in comparison to virtual machines because you can use containers to maximize the placement of your applications. This increases the utilization of your application's infrastructure resources by providing better isolation.
+ **Close the skills gap** – AWS offers immersion days to upskill your development teams on container technology and DevOps practices.

This section covers the following topics:
+ [Move Windows applications to containers](windows-containers-main.md)
+ [Optimize costs for AWS Fargate tasks on Amazon ECS](optimizer-ecs-fargate.md)
+ [Use Kubecost to gain visibility into your Amazon Elastic Kubernetes Service (Amazon EKS) costs](kubecost-main.md)
+ [Replatform Windows applications with App2Container](app2container-main.md)

For licensing information, see the *Licensing *section of [Amazon Web Services and Microsoft: Frequently Asked Questions](https://aws.amazon.com/windows/faq/#licensing-q) or email your questions to microsoft@amazon.com.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
