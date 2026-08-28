---
source_url: https://docs.aws.amazon.com/whitepapers/latest/optimizing-enterprise-economics-with-serverless/optimizing-enterprise-economics-with-serverless.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Optimizing Enterprise Economics with Serverless Architectures
<a name="optimizing-enterprise-economics-with-serverless"></a>

Publication date: **September 15, 2021** ([Document history](document-revisions.md))

This whitepaper is intended to help Chief Information Officers (CIOs), Chief Technology Officers (CTOs), and senior architects gain insight into serverless architectures and their impact on time to market, team agility, and IT economics. By eliminating idle, underutilized servers at the design level and dramatically simplifying cloud-based software designs, serverless approaches rapidly change the IT landscape.

This whitepaper covers the basics of serverless approaches and the AWS serverless portfolio. It includes several case studies illustrating how existing companies are gaining significant agility and economic benefits from adopting serverless strategies. In addition, it describes how organizations of all sizes can use serverless architectures to architect reactive, event-based systems and quickly deliver cloud-native microservices at a fraction of conventional costs.

## Are you Well-Architected?
<a name="are-you-well-architected"></a>

 The [AWS Well-Architected Framework](https://aws.amazon.com/architecture/well-architected/) helps you understand the pros and cons of the decisions you make when building systems in the cloud. The six pillars of the Framework allow you to learn architectural best practices for designing and operating reliable, secure, efficient, cost-effective, and sustainable systems. Using the [AWS Well-Architected Tool](https://aws.amazon.com/well-architected-tool/), available at no charge in the [AWS Management Console](https://console.aws.amazon.com/wellarchitected), you can review your workloads against these best practices by answering a set of questions for each pillar.

 In the [Serverless Application Lens](https://docs.aws.amazon.com/wellarchitected/latest/serverless-applications-lens/welcome.html), we focus on best practices for architecting your serverless applications on AWS.

 In the [HPC Lens](https://docs.aws.amazon.com/wellarchitected/latest/high-performance-computing-lens/welcome.html), we focus on best practices for architecting your High Performance Computing (HPC) workloads on AWS.

 In the [Machine Learning Lens](https://docs.aws.amazon.com/wellarchitected/latest/machine-learning-lens/machine-learning-lens.html), we focus on how to design, deploy, and architect your machine learning workloads in the AWS Cloud.

 For more expert guidance and best practices for your cloud architecture—reference architecture deployments, diagrams, and whitepapers—refer to the [AWS Architecture Center](https://aws.amazon.com/architecture/).

## Introduction
<a name="introduction"></a>

 Many companies are already gaining benefits from running applications in the public cloud, including cost savings from pay-as-you-go billing and improved agility through the use of on-demand IT resources. [Multiple studies](https://www.perle.com/articles/the-cost-savings-of-cloud-computing-40191237.shtml) across application types and industries have demonstrated that migrating existing application architectures to the cloud lowers the Total Cost of Ownership (TCO) and improves time to market.

 Relative to on-premises and private cloud solutions, the public cloud makes it significantly simpler to build, deploy, and manage fleets of servers and the applications that run on them. The public cloud has established itself as the new normal, with [double-digit year-over-year growth since its inception](https://www.gartner.com/en/newsroom/press-releases/2021-06-28-gartner-says-worldwide-iaas-public-cloud-services-market-grew-40-7-percent-in-2020).

 However, companies today have options beyond classic server or virtual machine (VM) based architectures to take advantage of the public cloud. Although the cloud eliminates the need for companies to purchase and maintain their hardware, *any* server-based architecture still requires them to architect for scalability and reliability. Plus, companies need to own the challenges of patching and deploying to those server fleets as their applications evolve.

 Moreover, they must scale their server fleets to account for peak load and then attempt to scale them down when and where possible to lower costs—all while protecting the experience of end-users and the integrity of internal systems. Idle, underutilized servers prove to be costly and wasteful. Researchers calculated the average server utilization to be around [only 18 percent for enterprises](https://d39w7f4ix9f5s9.cloudfront.net/e3/79/42bf75c94c279c67d777f002051f/carbon-reduction-opportunity-of-moving-to-aws.pdf).

 Using serverless services, developers and architects can design and develop complex application architectures, focusing just on business logic without dealing with the complexity of servers.

 As a result, product owners can achieve faster time to market with shorter development, deployment, and testing cycles. In addition, the reduction of server management overheads reduces the TCO, which ultimately results in competitive advantages for the companies.

 With significantly reduced infrastructure costs, more agile and focused teams, and faster time to market, companies that have already adopted serverless approaches are gaining a key advantage over their competitors.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Whitepapers. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query whitepapers` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
