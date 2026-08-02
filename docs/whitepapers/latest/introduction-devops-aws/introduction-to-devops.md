---
source_url: https://docs.aws.amazon.com/whitepapers/latest/introduction-devops-aws/introduction-to-devops.html
---

# Introduction to DevOps on AWS
<a name="introduction-to-devops"></a>

Publication date: **April 7, 2023** ([Document Revisions](document-revisions.md))

Today more than ever, enterprises are embarking on their digital transformation journey to build deeper connections with their customers, to achieve sustainable and enduring business value. Organizations of all shapes and sizes are disrupting their competitors and entering new markets by innovating more quickly than ever before. For these organizations, it is important to focus on innovation and software disruption, making it critical to streamline their software delivery. Organizations that shorten their time from idea to production making speed and agility a priority could be tomorrow's disruptors.

While there are several factors to consider in becoming the next digital disruptor, this whitepaper focuses on DevOps, and the services and features in the Amazon Web Services (AWS) platform that will help increase an organization's ability to deliver applications and services at a high velocity.

## Introduction
<a name="introduction"></a>

DevOps is the combination of cultural philosophies, engineering practices, and tools which increase an organization's ability to deliver applications and services at high velocity and better quality. Over time, several essential practices have emerged when adopting DevOps: continuous integration (CI), continuous delivery (CD), Infrastructure as Code (IaC), and monitoring and logging.

This paper highlights AWS capabilities that help you accelerate your DevOps journey, and how AWS services can help remove the undifferentiated heavy lifting associated with DevOps adaptation. It also describes how to build a continuous integration and delivery capability without managing servers or build nodes, and how to use IaC to provision and manage your cloud resources in a consistent and repeatable manner.
+ **Continuous integration:** A software development practice where developers regularly merge their code changes into a central repository, after which automated builds and tests are run.
+ **Continuous delivery:** A software development practice where code changes are automatically built, tested, and prepared for a release to production.
+ **Infrastructure as Code:** A practice in which infrastructure is provisioned and managed using code and software development techniques, such as version control, and continuous integration.
+ **Monitoring and logging:** Enables organizations to see how application and infrastructure performance impacts the experience of their product’s end user.
+ **Communication and collaboration:** Practices are established to bring the teams closer and by building workflows and distributing the responsibilities for DevOps.
+ **Security:** Should be a cross cutting concern. Your continuous integration and continuous delivery (CI/CD) pipelines and related services should be safeguarded and proper access control permissions should be set up.

An examination of each of these principles reveals a close connection to the offerings available from AWS.

## Are you Well-Architected?
<a name="are-you-well-architected"></a>

The [AWS Well-Architected Framework](https://aws.amazon.com/architecture/well-architected/) helps you understand the pros and cons of the decisions you make when building systems in the cloud. The six pillars of the Framework allow you to learn architectural best practices for designing and operating reliable, secure, efficient, cost-effective, and sustainable systems. Using the [AWS Well-Architected Tool](https://aws.amazon.com/well-architected-tool/), available at no charge in the [AWS Management Console](https://console.aws.amazon.com/wellarchitected), you can review your workloads against these best practices by answering a set of questions for each pillar.
