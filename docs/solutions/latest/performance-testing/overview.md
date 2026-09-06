---
source_url: https://docs.aws.amazon.com/solutions/latest/performance-testing/overview.html
---

# Overview
<a name="overview"></a>

## Journey Overview
<a name="journey-overview"></a>

**Who should read this journey:** Platform Engineers, DevOps Engineers, Cloud Architects, SRE, Application Developers, Technical Leaders

This journey takes you from understanding why performance failures happen in production through running continuous, production-scale load tests integrated into your CI/CD pipeline. Your application works in development, but will it survive 10,000 concurrent users on launch day? Performance testing is the discipline that answers this question before your customers do, and this journey embeds that discipline into every stage of your development lifecycle.

Performance failures share a common root cause: the application was never tested under realistic conditions at realistic scale. Teams assume that passing unit tests and integration tests means the system is production-ready, but performance is an emergent property that only manifests when components interact under load. The cost of discovering these problems in production includes lost revenue, emergency war rooms, and weeks of post-incident remediation.

By the end of this journey, you will have deployed Distributed Load Testing on AWS to simulate realistic traffic patterns, defined success metrics through SLIs and SLOs, established baseline comparisons that catch regressions automatically, and combined load testing with chaos engineering to build truly resilient systems. Performance testing will be a continuous signal in your pipeline rather than a one-time gate before launch.

## How This Journey Works
<a name="how-this-journey-works"></a>

This journey follows a maturity progression from Explorer through Practitioner to Expert. Early stages build foundational understanding of why performance fails in production and establish the "Early, After, Always" testing philosophy. Middle stages provide hands-on implementation guidance for deploying load testing infrastructure, defining success metrics through SLIs and SLOs, and integrating tests into CI/CD pipelines. Later stages address chaos engineering integration, production-scale validation, and continuous performance governance. Each stage builds on what came before, transforming performance testing from a pre-launch gate into a continuous engineering discipline.

### Journey Stages
<a name="journey-stages"></a>

| Stage | Title | Maturity Level | What You'll Accomplish |
| --- | --- | --- | --- |
| 1 | Why Performance Fails in Production | Explorer | Every engineering team has experienced it. The application sailed through functional testing,... |
| 2 | Defining Success: SLIs, SLOs, and Performance Budgets | Explorer | Before running a single test, you need to define what "good" looks like. Without clear success... |
| 3 | Understanding Test Types | Practitioner | The term "load test" is often used as a catch-all, but there are eight distinct test types, each... |
| 4 | Choosing Your Testing Tool | Practitioner | Distributed Load Testing on AWS (DLT) is the recommended solution for performance testing on... |
| 5 | Designing Realistic Test Scenarios | Practitioner | A load test is only as useful as the traffic pattern it simulates. Testing with uniform request... |
| 6 | Interpreting Results and Taking Action | Practitioner | Raw load test data is noise without a framework for interpretation. The goal is not to generate... |
| 7 | Automating Performance in CI/CD | Expert | Performance testing delivers the most value when it runs automatically on every change, not as a... |
| 8 | Chaos Engineering Meets Load Testing | Expert | Load testing tells you how the system performs under expected conditions. Chaos engineering... |
| 9 | Scaling to Production-Grade Testing | Expert | Moving from "my first load test" to "production-grade performance engineering" requires... |
