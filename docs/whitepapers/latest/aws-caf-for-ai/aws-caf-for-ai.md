---
source_url: https://docs.aws.amazon.com/whitepapers/latest/aws-caf-for-ai/aws-caf-for-ai.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# AWS Cloud Adoption Framework for Artificial Intelligence, Machine Learning, and Generative AI
<a name="aws-caf-for-ai"></a>

**Accelerating Your Cloud-Powered AI Transformation**

Publication date: **February 13, 2024** ([Document history](document-revisions.md))

In this document, we outline the AWS Cloud Adoption Framework for Artificial Intelligence (AI), Machine Learning (ML), and generative AI, a framework that describes a mental model for organizations that strive to generate business value from Artificial Intelligence. In this framework, we describe the Artificial Intelligence journey that customers go through as their organizational capabilities on AI and ML mature. We structure this journey by carving out foundational capabilities that assist an organization to grow its maturity in AI. Finally, we provide prescriptive guidance by providing an overview of the target state of these foundational capabilities and explaining how to evolve them step by step to generate business value along the way.

## Introduction to Artificial Intelligence
<a name="introduction-to-ai"></a>

Artificial Intelligence (AI) is a broad field that aims to create or at least imitate intelligent machines capable of performing tasks that traditionally require human intelligence. These tasks can include anything from understanding natural language and visual perception to decision-making and problem-solving. One commonality among many AI systems is the pursuit of probabilistic outcomes—essentially, generating predictions or decisions with a high degree of certainty, often mirroring the complexity of human judgment. Such systems can then be used to automate or augment knowledge work.

A significant portion of AI today is built upon machine learning (ML), a branch of AI that focuses on developing techniques that enable computers to learn from and make decisions based on data. Rather than relying on explicit programming, machine learning models generalize from examples, making them highly versatile for a myriad of applications. Among the various techniques within machine learning is deep learning, a specialized subset that uses neural networks with multiple layers to analyze complex factors in data. Deep learning is especially adept at handling unstructured data like images and text, and has led to breakthroughs in numerous complex tasks such as image and speech recognition.

An emerging capability within deep learning is generative AI, which makes AI generate or create new, potentially original content. This innovative sub-discipline is increasingly being recognized for its ability to produce outputs that mimic aspects of human-like thought and reasoning capabilities. Advances in computing power, data availability, and algorithmic innovation have made generative AI possible, paving the way for a wide range of applications, from entertainment and art to scientific research.

Together, these sub-disciplines and techniques represent the layered and interrelated landscape of Artificial Intelligence, each contributing to the development of systems that can autonomously perform an increasingly broad array of tasks. The applications and capabilities of AI are likely to continue to expand quickly, making it an integral part of our daily lives and a crucial tool for solving complex problems.

| *"Generative AI has captured people's imagination in a way few innovations have. As it evolves beyond the realm of researchers and developers, it's proving to have broad applications that range from enhancing consumer experiences to solving complex enterprise problems. Whether it's producing human-like text, assisting coders with AI-driven code snippets, or automating customer interactions via intelligent chatbots, the possibilities seem endless. Beyond these applications, generative AI serves as a catalyst for reimagining how technology can augment human abilities and extend our reach, doing so with an unprecedented blend of scalability, customization, and intelligence. As we stand on the precipice of mass adoption, the technology's promise isn't just in accomplishing tasks more efficiently, but in fundamentally redefining what is possible across various sectors."* – Andy Jassy, CEO Amazon |
| --- |
|   |

**Note**
Moving forward, the term *Artificial Intelligence (AI)* is used as an umbrella term encompassing all its various sub-disciplines. When referring to specialized areas within AI, they are specified by name, such as *generative AI* or *Machine Learning*, to distinguish them from the broader field of AI.

![Diagram showing the taxonomy of artificial intelligence, machine learning, deep learning, and generative AI](https://docs.aws.amazon.com/whitepapers/latest/aws-caf-for-ai/images/taxonomy-of-ai-ml-deeplearning-and-genai.png)

## Introduction to AWS CAF-AI
<a name="introduction-to-caf-ai"></a>

The AWS Cloud Adoption Framework for Artificial Intelligence, Machine Learning, and generative AI (CAF-AI) serves as both a starting point and a guide for your ongoing journey in AI, ML, and generative AI. This framework aims to inspire and inform your mid-term planning and strategy in these specialized fields. Use it as a resource for discussions about your AI strategy, not only within your team but also when collaborating with coworkers and AWS Partners.

Depending on where you are in your journey, you might focus on a specific section and hone your skills there, or you might use the whole document to judge maturity and help direct near-term improvement areas. CAF-AI is a constantly growing and updated summary and index of all the things that you need to consider when adopting AI at an enterprise level and help you to go beyond a single proof of concept (POC). Our goal is to give our customers the same prescriptive guidance they know and expect from the [AWS Cloud Adoption Framework](https://aws.amazon.com/cloud-adoption-framework/) (AWS CAF) for AI, so they can successfully implement it. AWS CAF is underpinned by a set of foundational organizational capabilities and provides prescriptive guidance that thousands of organizations around the world have successfully used to accelerate their cloud transformation journeys.

In AWS CAF-AI, we remain reliant on these foundational capabilities but we enrich many of them so they include the changes that AI demands. In addition, we identify and add new foundational capabilities that organizations should consider as part of their AI journey.

## AWS CAF: The Cloud Adoption Framework
<a name="aws-caf-the-cloud-adoption-framework"></a>

 At AWS over the last 10 years, we have built the [AWS Cloud Adoption Framework](https://aws.amazon.com/professional-services/CAF/) (AWS CAF) as a cornerstone for our customers’ cloud adoption strategy. While evolving this framework, we have kept it largely unbound to specific technologies beyond the cloud to make sure that its insights and mental model can be used by many of our diverse customers. However, Artificial Intelligence is an entirely new breed of technologies that has a large impact on all verticals and most of our customers. We have built CAF-AI to help our customers along their journey of AI adoption accelerated through cloud technology.

## Are you Well-Architected?
<a name="are-you-well-architected"></a>

 The [AWS Well-Architected Framework](https://aws.amazon.com/architecture/well-architected/) helps you understand the pros and cons of the decisions you make when building systems in the cloud. The six pillars of the Framework allow you to learn architectural best practices for designing and operating reliable, secure, efficient, cost-effective, and sustainable systems. Using the [AWS Well-Architected Tool](https://aws.amazon.com/well-architected-tool/), available at no charge in the [AWS Management Console](https://console.aws.amazon.com/wellarchitected), you can review your workloads against these best practices by answering a set of questions for each pillar.

 In the [Machine Learning Lens](https://docs.aws.amazon.com/wellarchitected/latest/machine-learning-lens/machine-learning-lens.html), we focus on how to design, deploy, and architect your machine learning workloads in the AWS Cloud. This lens adds to the best practices described in the Well-Architected Framework.

 For more expert guidance and best practices for your cloud architecture—reference architecture deployments, diagrams, and whitepapers—refer to the [AWS Architecture Center](https://aws.amazon.com/architecture/).
