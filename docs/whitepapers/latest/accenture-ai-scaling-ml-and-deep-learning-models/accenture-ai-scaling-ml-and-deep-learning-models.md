---
source_url: https://docs.aws.amazon.com/whitepapers/latest/accenture-ai-scaling-ml-and-deep-learning-models/accenture-ai-scaling-ml-and-deep-learning-models.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Accenture Enterprise AI – Scaling Machine Learning and Deep Learning Models
<a name="accenture-ai-scaling-ml-and-deep-learning-models"></a>

Publication date: **July 27, 2022** ([Document revisions](document-revisions.md))

## Abstract
<a name="abstract"></a>

 Today, there is a real-time, global, tectonic shift in the workplace caused by digital transformation. Accelerated by the Covid pandemic, this digital transformation has created never-seen-before opportunities and significant workplace disruption. Fully realizing the new market opportunities demands a modernized workforce. A skills gap contributed to by several factors exist in today's labor market. Some of these factors are the increase in the number of people entering the workforce each year, lack of relevant education, and the rise in technology which needs workers to be equipped with new skills to help them keep up with advancements. Addressing this widening gap between the current workforce skills and those needed for tomorrow is front and center in the minds of every C-suite.

 This whitepaper outlines an innovative, scalable and automated solution using [deep learning](https://aws.amazon.com/deep-learning/) (DL) and [machine learning](https://aws.amazon.com/machine-learning/) (ML) on Amazon Web Services (AWS), to help solve the problem of bridging the existing talent and skills gap for both workers and organizations. Combining advanced data science, ML engineering, deep learning, [ethical artificial intelligence](https://c3.ai/glossary/artificial-intelligence/ethical-ai/) (AI), and [MLOps](https://en.wikipedia.org/wiki/MLOps) on AWS, this whitepaper provides a roadmap to enterprises and teams to help build production-ready ML solutions, and derive business value out of the same.

## Are you Well-Architected?
<a name="are-you-well-architected"></a>

 The [AWS Well-Architected Framework](https://aws.amazon.com/architecture/well-architected/) helps you understand the pros and cons of the decisions you make when building systems in the cloud. The six pillars of the Framework allow you to learn architectural best practices for designing and operating reliable, secure, efficient, cost-effective, and sustainable systems. Using the [AWS Well-Architected Tool](https://aws.amazon.com/well-architected-tool/), available at no charge in the [AWS Management Console](https://console.aws.amazon.com/wellarchitected), you can review your workloads against these best practices by answering a set of questions for each pillar.

 In the [Machine Learning Lens](https://docs.aws.amazon.com/wellarchitected/latest/machine-learning-lens/machine-learning-lens.html), we focus on how to design, deploy, and architect your machine learning workloads in the AWS Cloud. This lens adds to the best practices described in the Well-Architected Framework.

 For more expert guidance and best practices for your cloud architecture—reference architecture deployments, diagrams, and whitepapers—refer to the [AWS Architecture Center](https://aws.amazon.com/architecture/).

## Introduction
<a name="introduction"></a>

 Today’s rapidly changing environment demands the ability for organizations to adapt to change to create a sustainable and productive workforce. Thriving in this environment requires rapid adaptation and readiness for upskilling the workforce for tomorrow.

 According to VentureBeat, about 87% of ML models never make it to production. Even though 9 out of 10 business executives believe that AI will be at the center of the next technological revolution, completion, and successful production deployment is [seen as a big challenge](https://towardsdatascience.com/why-90-percent-of-all-machine-learning-models-never-make-it-into-production-ce7e250d5a4a) as it requires specific engineering expertise and collaboration between several teams (ML engineering, IT, Data Science, DevOps, and so on).

 [Accenture](https://www.accenture.com/us-en) has built a scalable, industrialized, AI-powered solution that is a key component in helping solve the talent and skilling problem of today and tomorrow to create a productive workforce. It describes an innovative, cloud-native AWS approach that can be taken to industrialize the ML solution, and help organizations bridge the skills gap.

 This whitepaper describes a technical solution (also referred to as industry solution) for building and scaling ML, and specifically, DL models for these use cases, and how Accenture is industrializing the end-to-end process to achieve the technical goals previously detailed. The technical thought process explained here can be expanded and applied to most problems in other industries. You can also use it to create a stable and sustainable Enterprise AI system.

## Frictionless ideation to production
<a name="frictionless-ideation-to-production"></a>

 The goal of Enterprise AI and MLOps is to reduce friction and get all models from ideation to production in the shortest possible time, with as little risk as possible. Integrating AI technologies into business operations can prove to be a game-changer for organizations, with the benefits of reducing costs, boosting efficiency, generating actionable, precise insights, and creating new revenue streams. This requires not only creating efficient models, but also creating a complete end-to-end stable, resilient, and repeatable Enterprise AI system that can provide sustainable value and be amenable to continuous improvements to adapt to changing environments.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Whitepapers. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query whitepapers` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
