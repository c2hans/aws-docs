---
source_url: https://docs.aws.amazon.com/whitepapers/latest/availability-and-beyond-improving-resilience/availability-and-beyond-improving-resilience.html
---

# Availability and Beyond: Understanding and Improving the Resilience of Distributed Systems on AWS
<a name="availability-and-beyond-improving-resilience"></a>

Publication date: **November 12, 2021** ([Document history](document-revisions.md))

 Today, businesses operate complex, distributed systems both in the cloud and on-premises. They want these workloads to be resilient in order to serve their customers and achieve their business outcomes. This paper outlines a common understanding for availability as a measure of resilience, establishes rules for building highly available workloads, and offers guidance on how to improve workload availability.

## Introduction
<a name="introduction"></a>

 What does it mean to build a highly available workload? How do you measure availability? What can I do to increase my workload's availability? This document will help you answer these kinds of questions. It is divided into three major sections. The first section, *Understanding availability* is largely theoretical. It establishes a common understanding of the definition of availability and the factors that impact it. The second section, *Measuring availability*, provides guidance on empirically measuring your workload's availability. The third section, *Designing highly available distributed systems on AWS* is a practical application of the ideas presented in the first section. Additionally, throughout these sections, this paper will identify rules for building resilient workloads. This document is intended to support the guidance and best practices presented in the [AWS Well-Architected Reliability Pillar](https://docs.aws.amazon.com/wellarchitected/latest/reliability-pillar/welcome.html).

 Throughout this paper, you will encounter a lot of algebraic math. The key takeaways are the concepts this math supports, not the math itself. That said, it is also the intent of this paper to present a challenge. When you operate highly available workloads, you need to be able to prove, mathematically, that what you built is achieving what you intended. Even the best designs built on good intentions might not consistently achieve the desired outcome. This means you need mechanisms that measure the effectiveness of the solution, and thus, some level of math is necessary in building and operating resilient, highly available distributed systems.

**Are you Well-Architected?**
 The [AWS Well-Architected Framework](https://aws.amazon.com/architecture/well-architected/) helps you understand the pros and cons of the decisions you make when building systems in the cloud. The Framework's six pillars teach architectural best practices for designing and operating your systems. These practices help you build systems that are reliable, secure, efficient, cost-effective, and sustainable.
 The [AWS Well-Architected Tool](https://aws.amazon.com/well-architected-tool/) is available at no charge in the [AWS Management Console](https://console.aws.amazon.com/wellarchitected). Use it to review your workloads against these best practices by answering a set of questions for each pillar.
 For more expert guidance and best practices for your cloud architecture—reference architecture deployments, diagrams, and whitepapers—refer to the [AWS Architecture Center](https://aws.amazon.com/architecture/).
