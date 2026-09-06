---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/performance-engineering-aws/introduction.html
---

# A phased approach for performance engineering in the AWS Cloud
<a name="introduction"></a>

*Varun Sharma, Archana Bhatnagar, Akash Kumar, and Pratik Sharma, Amazon Web Services*

This guide outlines the best practices for planning, building, and enabling performance engineering for application workloads running on Amazon Web Services (AWS). It lays out four pillars for performance engineering,** **and it suggests different approaches to meet applications' performance requirements. For each pillar, this guide lists tools and solutions for setting up performance tests and the testing environment.

## What is performance engineering?
<a name="what"></a>

Performance Engineering encompasses the techniques applied during a system's development lifecycle to ensure the non-functional performance requirements (such as throughput, latency, or memory usage) are met.

Before performance testing starts, you need to set up the performance environment. A typical performance environment stands on the following pillars:
+ Test-data generation
+ Test observability
+ Test automation
+ Test reporting

## Why use performance engineering?
<a name="why"></a>

Performance engineering is the process of continuously optimizing the application performance from the start of the design phase. It brings great value to the business by avoiding rework and refactoring of code at a later stage in the development cycle. Beginning performance engineering at the design phase results in an application that performs better because performance can be factored into the design. Performance engineering requires the active participation of system architects, developers, DevOps, and Quality Assurance.
