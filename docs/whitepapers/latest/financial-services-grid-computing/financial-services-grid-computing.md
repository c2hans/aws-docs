---
source_url: https://docs.aws.amazon.com/whitepapers/latest/financial-services-grid-computing/financial-services-grid-computing.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Financial Services Grid Computing on AWS
<a name="financial-services-grid-computing"></a>

Publication date: **August 9, 2024** ([Document history](document-revisions.md))

 Financial services organizations rely on high performance computing (HPC) infrastructure grids to calculate risk, value portfolios, and provide reports to their internal control functions and external regulators. The scale, cost, and complexity of this infrastructure is an increasing challenge. Amazon Web Services (AWS) provides a number of services that enable these customers to surpass their current capabilities by delivering results more quickly and at a lower cost than with on-premises resources.

 The intended audience for this paper includes grid computing managers, architects, and engineers within financial services organizations who want to improve their service. It describes the key AWS services to consider, some best practices, and includes relevant reference architecture diagrams.

## Overview
<a name="overview"></a>

 High performance computing (HPC) in the financial services industry is an ongoing challenge because of the pressures from ever-increasing computational demand across retail, commercial, and investment groups, combined with growing cost and capital constraints. The traditional, on-premises approaches to solving these problems have evolved from centralized, monolithic solutions, to business-aligned clusters of commodity hardware, to modern, multi-tenant grid architectures with centralized schedulers that manage disparate compute capacity.

 Cloud concepts such as *capacity on demand* and *pay as you go* pricing models offer new opportunities to teams who run HPC platforms to leverage previously unheard-of flexibility and scale to their businesses. This might take the form of a bursting model, where existing capacity is augmented by the cloud, or it might be through a *lift and shift* approach with new elastic clusters deployed into the cloud.

 Historically, the challenge has been to manage a fixed set of on-premises resources, while maximizing utilization and minimizing queuing times. In a cloud-based model with capacity that is effectively unconstrained, the focus shifts away from managing and throttling demand, and towards optimizing supply. With this model, decisions become more granular and tailored to each customer, and focus on *how fast* and at *what cost*, with the ability to make adjustments as required by the business. With this relatively unconstrained capacity, concepts such as queuing and prioritization become irrelevant, as clients are able to submit calculation requests and have them serviced immediately. This also results in upstream consumers increasingly expecting and demanding near instantaneous processing of their workloads at any scale.

 Initial cloud migrations of HPC platforms are often seen as extensions or evolutions of on-premises grid implementations. However, forward-looking institutions are experimenting with the ever-expanding ecosystem of capabilities enabled by AWS. Some emerging themes include refreshing financial models to run on open-source Linux based operating systems, and exploring the performance benefits of the latest Arm-based central processing units (CPUs) through [AWS Graviton](https://aws.amazon.com/ec2/graviton/). [Amazon SageMaker AI](https://aws.amazon.com/sagemaker/) increasingly democratizes the use of artificial intelligence/machine learning (AI/ML) techniques, and customers are looking to these tools to enable accelerated development of predictive risk models. Serverless approaches to both scheduling and orchestration are emerging trends with customers looking at solutions including the open-source [HTC-Grid project](https://aws.amazon.com/blogs/hpc/cloud-native-high-throughput-computing-with-aws-htc-grid/).

 For data-heavy calculations, [Amazon EMR](https://aws.amazon.com/emr) offers a fully managed, industry-leading cloud big data platform based on standard tooling using [directed acyclic graph](https://en.wikipedia.org/wiki/Directed_acyclic_graph) structures. This topic is explored further in the blog post [How to improve FRTB’s Internal Model Approach implementation using Apache Spark and Amazon EMR](https://aws.amazon.com/blogs/industries/how-to-improve-frtbs-internal-model-approach-implementation-using-apache-spark-and-amazon-emr/).

 As HPC environments move to the cloud, the applications that are associated with them start to migrate too. Risk management systems which drive compute grids quickly become a bottleneck when the downstream HPC platform is unconstrained. By migrating these applications alongside the compute grid, the applications benefit from the elasticity that the cloud provides. In turn, data sources such as market and static data are sourced natively from within the cloud, from the same providers that customers work with today through services such as [AWS Data Exchange](https://aws.amazon.com/data-exchange/).

 Many of the building blocks required for fully serverless risk management and reporting solutions already exist today within AWS, with services like [AWS Lambda](https://aws.amazon.com/lambda/) for serverless compute and [AWS Step Functions](https://aws.amazon.com/step-functions/) to coordinate them. As financial institutions become increasingly familiar and comfortable with these services, it’s likely that serverless patterns will become the predominant HPC architectures of the future.

## Are you Well-Architected?
<a name="are-you-well-architected"></a>

 The [AWS Well-Architected Framework](https://aws.amazon.com/architecture/well-architected/) helps you understand the pros and cons of the decisions you make when building systems in the cloud. The six pillars of the Framework allow you to learn architectural best practices for designing and operating reliable, secure, efficient, cost-effective, and sustainable systems. Using the [AWS Well-Architected Tool](https://aws.amazon.com/well-architected-tool/), available at no charge in the [AWS Management Console](https://console.aws.amazon.com/wellarchitected), you can review your workloads against these best practices by answering a set of questions for each pillar.

 In the [Financial Services Industry Lens](https://docs.aws.amazon.com/wellarchitected/latest/financial-services-industry-lens/welcome.html), we focus on best practices for architecting your Financial Services Industry workloads on AWS.

 In the [HPC Lens](https://docs.aws.amazon.com/wellarchitected/latest/high-performance-computing-lens/welcome.html), we focus on best practices for architecting your High Performance Computing (HPC) workloads on AWS.

 For more expert guidance and best practices for your cloud architecture—reference architecture deployments, diagrams, and whitepapers—refer to the [AWS Architecture Center](https://aws.amazon.com/architecture/).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Whitepapers. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query whitepapers` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
