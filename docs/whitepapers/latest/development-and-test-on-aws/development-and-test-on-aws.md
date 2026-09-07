---
source_url: https://docs.aws.amazon.com/whitepapers/latest/development-and-test-on-aws/development-and-test-on-aws.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Development and Test on Amazon Web Services
<a name="development-and-test-on-aws"></a>

Publication date: **June 29, 2021** ([Document revisions](document-revisions.md))

## Abstract
<a name="abstract"></a>

 This whitepaper describes how Amazon Web Services (AWS) adds value in the various phases of the software development cycle, with specific focus on development and test. For the development phase, this whitepaper:
+  Shows you how to use AWS for managing version control
+  Describes project management tools, the build process, and environments hosted on AWS
+  Illustrates best practices

 For the test phase, this whitepaper describes how to manage test environments and run various kinds of tests, including load testing, acceptance testing, fault tolerance testing, and so on.

 AWS provides unique advantages in each of these scenarios and phases, enabling you to choose the ones most appropriate for your software development project. The intended audiences for this paper are project managers, developers, testers, systems architects, or anyone involved in software production activities.

## Are you Well-Architected?
<a name="are-you-well-architected"></a>

 The [AWS Well-Architected Framework](https://aws.amazon.com/architecture/well-architected/) helps you understand the pros and cons of the decisions you make when building systems in the cloud. The six pillars of the Framework allow you to learn architectural best practices for designing and operating reliable, secure, efficient, cost-effective, and sustainable systems. Using the [AWS Well-Architected Tool](https://aws.amazon.com/well-architected-tool/), available at no charge in the [AWS Management Console](https://console.aws.amazon.com/wellarchitected), you can review your workloads against these best practices by answering a set of questions for each pillar.

 For more expert guidance and best practices for your cloud architecture—reference architecture deployments, diagrams, and whitepapers—refer to the [AWS Architecture Center](https://aws.amazon.com/architecture/).

## Introduction
<a name="introduction"></a>

 Organizations write software for various reasons, ranging from core business needs (when the organization is a software vendor) to customizing or integrating software. Organizations also create different types of software: web applications, standalone applications, automated agents, and so on. In all such cases, development teams are pushed to deliver software of high quality as quickly as possible to reduce the time to market or time to production.

 In this document, “development and test” refers to the various tools and practices applied when producing software. Regardless of the type of software to be developed, a proper set of development and test practices is key to success. However, producing applications not only requires software engineers, but also IT resources, which are subject to constraints like time, money, and expertise.

 The software lifecycle typically consists of the following main elements:

![A diagram showing the elements of the software lifecycle.](https://docs.aws.amazon.com/whitepapers/latest/development-and-test-on-aws/images/software-lifecycle.png)

 This whitepaper covers aspects of the development, build, and test phases. For each of these phases, you need different types of IT infrastructure. AWS provides multiple benefits to software development teams. AWS offers on-demand access to a wide range of cloud infrastructure services, charging only for the resources that are used.

 AWS helps eliminate both the need for costly hardware and the administrative pain that goes with owning and operating it.

 Owning hardware and IT infrastructure usually involves a capital expenditure for a three-five year period, where most development and test teams need compute or storage for hours, days, weeks, or months. This difference in timescales can cause friction due to the difficulty for IT operations to satisfy simultaneous requests from project teams, even as they are constrained by a fixed set of resources. The result is that project teams spend a lot of time justifying, sourcing, and holding on to resources. This time could be spent focusing on the main job.

 By provisioning only the resources needed for the duration of development phases, test runs, or complete test campaigns, your company can achieve important savings compared to investing up front in traditional hardware. With the right level of granularity, you can allocate resources depending on each project’s needs and budget. In addition to those economic benefits, AWS also offers significant operational advantages, such as the ability to set up a development and test infrastructure in a matter of minutes rather than weeks or months, and to scale capacity up and down to provide the IT resources needed, only when they are needed.

 This document highlights some of the best practices and recommendations around development and test on AWS. For example, for the development phase, this document discusses how to securely and durably set up tools and processes such as version control, collaboration environments, and automated build processes. For the testing phase, this document discusses how to set up test environments in an automated fashion, and how to run various types of tests, including side-by-side tests, load tests, stress tests, resilience tests, and more.
