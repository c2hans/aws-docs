---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/modernization-phased-approach/modernization-readiness-factors.html
---

# Modernization readiness factors
<a name="modernization-readiness-factors"></a>

Observe the following standards and best practices when you're modernizing your applications.

## Code
<a name="code.f43fdd57-1bf1-5647-9716-2c4137f66a05"></a>
+ Provide code comments that document the functionality of your software, and use them to generate documentation.
+ Follow code management and deployment processes that support frequent code check-ins and traceability to feature requests.
+ Build test suites that include unit, functional, performance, and critical path tests, with 100 percent code coverage.
+ Encourage code reuse to deliver the same or similar functionality in your code base.
+ Develop prototypes to validate features with users before investing in full code development.

## Build and test
<a name="build-and-test.e20ec89c-1c33-519a-915c-c8418f2b88a6"></a>
+ Redefine feature completeness based on testing, to improve quality and prevent recurring issues.
+ Automate acceptance tests.
+ Monitor all automated tests, and establish a process for handling failures in place.
+ Track performance in both production and non-production environments, define service-level objectives (SLOs) based on realistic traffic and load testing, and provide the ability to scale to meet performance requirements.
+ Abstract sensitive data from configuration files, and provide tools that automate and monitor configurations.

## Release
<a name="release.9c3d1dd5-7800-54d5-aab4-7227479b2c30"></a>
+ Automate deployments with support for dependencies (for example, database releases), regression testing, and tracking.
+ Release code to the production environment incrementally, after every successful build.
+ Manage feature flags (toggles) effectively: support run-time configuration, monitor usage, maintain flags throughout the development cycle, and assign owners by category.
+ Provide traceability in your build pipelines, to track triggers, failure notifications, and successful completion.
+ Run automated deployment processes and tests for "zero touch" code updates in continuous delivery.
+ Use zero-downtime, fully automated blue/green deployment methodologies.
+ Make sure that your database schema changes are implemented consistently across all development and production environments.

## Operate
<a name="operate.0f3de4d6-9f46-5643-8b49-7ba226849d1a"></a>
+ Create a DevOps triage runbook that's integrated with your notification system.
+ Make sure that your monitoring and notification system meets service-level objectives (SLOs) and supports thresholds, health checks, non-standard HTTP responses, and unexpected results.
+ Establish effective risk management and disaster recovery processes.
+ Develop a log rotation and retention strategy that meets your business and legal requirements.
+ Develop dashboards that track product performance, measure the success of new features, and display alerts when metrics don't meet expectations.

## Optimize
<a name="optimize.abccd67a-5f99-5fd2-9031-efe19a41b384"></a>
+ Review and improve processes regularly, based on performance and quality measures.
+ Implement root cause analysis and prevention processes to prevent issues from recurring.
+ Provide data-driven metrics that capture product health, and make sure that all notifications and actions are based on these metrics.

## Readiness
<a name="readiness.59ffebbb-7aa2-5bc6-bdaa-93289a59c4c8"></a>
+ Dedicate a cross-functional team (including business partners, developers, testers, and architects) to your modernization efforts.
