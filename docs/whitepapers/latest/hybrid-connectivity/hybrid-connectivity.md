---
source_url: https://docs.aws.amazon.com/whitepapers/latest/hybrid-connectivity/hybrid-connectivity.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Hybrid Connectivity
<a name="hybrid-connectivity"></a>

Publication date: **July 6, 2023** ([Document revisions](document-revisions.md))

 Many organizations need to connect their on-premises data centers, remote sites, and the cloud. A hybrid network connects these different environments. This whitepaper describes AWS building blocks and the key requirements to consider when deciding which hybrid connectivity model is right for you. To help you determine the best solution for your business and technical requirements, we provide decision trees to guide you through the logical selection process.

## Introduction
<a name="introduction"></a>

 A modern organization uses an extensive array of IT resources. In the past, it was common to host these resources in an on-premises data center or a colocation facility. With the increased adoption of cloud computing, organizations deliver and consume IT resources from cloud service providers over a network connection. Organizations can opt to migrate some, or all, of their existing IT resources to the cloud. In either case, a common network is required to connect on-premises and cloud resources. Coexistence of on-premises and cloud resources is called *hybrid cloud,* and the common network connecting them is referred to as a *hybrid network*. Even if your organization keeps all its IT resources in the cloud, it may still require hybrid connectivity to remote sites.

 There are several connectivity models to choose from. While having options adds flexibility, selecting the optimal option requires analysis of the business and technical requirements, and elimination of options that are not suitable. You can group requirements together across considerations such as security, time to deploy, performance, reliability, communication model, scalability, and more. Once they have carefully collected, analyzed, and considered the requirements, network and cloud architects can identify the applicable AWS hybrid network building blocks and solutions. To identify and select the optimal model or models, architects must understand advantages and disadvantages of each model. There are also technical limitations that might cause an otherwise suitable model to be excluded.

 To simplify the selection process, this whitepaper guides you through each key consideration in a logical order. Under each consideration, there are questions used to collect requirements. Each design decision’s impact is identified, along with potential solutions. The whitepaper presents decision trees for some of the considerations as a method to aid decision-making process, eliminate options, and understand consequences of each decision. It concludes with a scenario covering a hybrid use case, applying the end-to-end connectivity model selection and design. You can use this example to see how to execute the processes laid out in this whitepaper in a practical example.

 This whitepaper is intended to help you select and design an optimal hybrid connectivity model. This whitepaper is structured as follows:
+  **Hybrid connectivity building blocks** – An overview of AWS services used for hybrid connectivity.
+  **Connectivity selection and design considerations** – A definition of each connectivity model, how each affects the design decision, requirement identification questions, solutions, and decision trees.
+  **A customer use case** - An example of how to apply the considerations and decision trees in practice.

## Are you Well-Architected?
<a name="are-you-well-architected"></a>

 The [AWS Well-Architected Framework](https://aws.amazon.com/architecture/well-architected/) helps you understand the pros and cons of the decisions you make when building systems in the cloud. The six pillars of the Framework allow you to learn architectural best practices for designing and operating reliable, secure, efficient, cost-effective, and sustainable systems. Using the [AWS Well-Architected Tool](https://aws.amazon.com/well-architected-tool/), available at no charge in the [AWS Management Console](https://console.aws.amazon.com/wellarchitected), you can review your workloads against these best practices by answering a set of questions for each pillar.

 For more expert guidance and best practices for your cloud architecture—reference architecture deployments, diagrams, and whitepapers—refer to the [AWS Architecture Center](https://aws.amazon.com/architecture/).
