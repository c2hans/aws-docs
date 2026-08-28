---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/serverless-application-testing/introduction.html
---

# Testing serverless applications on AWS
<a name="introduction"></a>

*Dan Fox, Rob Hill (AWS), Rohan Mehta, and Leslie Raj, Amazon Web Services*

This guide discusses methodologies for testing serverless applications, describes the challenges that you might encounter during testing, and introduces best practices. These testing techniques are intended to help you iterate more quickly and release your code more confidently.

This guide is for developers who are looking to establish testing strategies for their serverless applications. You can use the guide as a starting point to learn about testing strategies, and then visit the [Serverless Test Samples repository](https://github.com/aws-samples/serverless-test-samples) to see examples of tests that follow the patterns and best practices described in this guide. This guide describes serverless testing methodologies, describes the challenges customers encounter when testing serverless applications, and introduces best practices for testing serverless applications. These techniques are intended to help developers iterate more quickly and release more confidently.

## Overview
<a name="overview"></a>

Automated tests are critical investments that help ensure application quality and development speed. Testing also accelerates developer feedback. As a developer, you want to be able to iterate rapidly on your application and get feedback on the quality of your code. Many developers are used to writing applications that they deploy to an environment on their desktop, either directly to their operating system or within a container-based environment. When you work in desktop or container-based environments, you typically write tests against code that is hosted entirely on your desktop. However, in serverless applications, architecture components might not be deployable to a desktop environment but might instead exist only in the cloud. A cloud-based architecture might include persistence layers, messaging systems, security constructs, APIs, and other components. When you write application code that relies on these components, it might be difficult to determine the best way to design and run tests.

This guide helps you align to a testing strategy that reduces friction and confusion, and increases code quality.

## Prerequisites
<a name="prerequisites"></a>

This guide assumes that you are familiar with the basics of automated tests, including how automated software tests are used to ensure software quality. The guide provides a high-level introduction to a serverless application testing strategy, and doesn't require any hands-on experience writing tests.

## Definitions
<a name="definitions"></a>

This guide uses the following terms:
+ *Unit tests* are tests that are run against code for a single architectural component in isolation.
+ *Integration tests*** **are run against two or more architectural components, typically in a cloud environment.
+ *End-to-end tests* verify behaviors across entire applications or workflows.
+ *Emulators* are applications (often provided by a third party) that are designed to mimic a cloud service without provisioning or invoking any cloud resources.
+ *Mocks* (also called *fakes*) are implementations in a testing application that replace a dependency with a simulation of that dependency.

## Objectives
<a name="business-outcomes"></a>

The best practices in this guide are intended to help you achieve two main objectives:
+ Increase quality of serverless applications
  + Testing at architecture boundaries
  + Testing at code boundaries
+ Decrease time to implement or change features

### Increase software quality
<a name="increase-software-quality.d4a50cdc-e0f4-57f1-b7c5-3b2b565571ad"></a>

An application's quality depends to a large extent on the ability of developers to test a variety of scenarios to verify functionality. When you don't implement automated tests, or, more typically, if your tests don't cover the required scenarios adequately, the quality of your application can't be determined or guaranteed.

In a server-based architecture, teams are able to easily define a scope for testing: Any code that runs on the application server has to be tested. Other components that call in to the server, or dependencies that the server calls, are often considered external and out of scope for testing by the team responsible for the application on the server.

Serverless applications often consist of smaller units of work, such as AWS Lambda functions, that run in their own environment. Teams will likely be responsible for multiples of these smaller units within a single application. Some application functionality can be delegated entirely to managed services such as Amazon Simple Storage Service (Amazon S3) or Amazon Simple Queue Service (Amazon SQS) without using any internally developed code. Traditional server-based models for software testing might exclude managed services by considering them external to the application. This can lead to inadequate coverage, where critical scenarios might be limited to manual exploratory testing or to a few integration test cases where the outcome varies by environment. Therefore, adopting testing strategies that encompass managed service behaviors and cloud configurations can improve software quality.

#### Testing at architecture boundaries
<a name="testing-at-architecture-boundaries.e9e95510-ba76-59f4-bba5-c82affa72c43"></a>

As serverless applications grow, they naturally spread across multiple architectural components. While this uses AWS distributed capabilities, it can make end-to-end behavior difficult to understand.

##### Identifying natural boundaries
<a name="identifying-natural-boundaries.6d572dc0-6620-574a-8a0b-39eb772b72a8"></a>

When designing your architecture following serverless best practices (one function = one job, decoupling), you'll notice natural boundaries around subsystems. These boundaries represent logical separation points in your application.

##### Boundaries as testing contracts
<a name="boundaries-as-testing-contracts.d8aa4ff6-dd54-5aec-82db-653535092773"></a>

These architectural boundaries are excellent candidates for testing edges. Treat each boundary as a contract and validate that it behaves according to its defined specification. Think of these boundaries as *seams* in your application where you can insert test validation.

##### Key benefits
<a name="key-benefits.774ee01d-fbc6-5472-98ea-ecba053b2e74"></a>

The following are key benefits of testing at architecture boundaries:
+ **Focused testing scope** – Test subsystems independently without needing to understand the entire application.
+ **Contract validation** – Ensure each boundary maintains its expected behavior as the system evolves
+ **Dual-purpose instrumentation** – These same boundaries make excellent observability hooks in production
+ **Test harness **– Allows you to test asynchronous serverless systems. It helps you test event-driven architectures by capturing and validating events as they flow through your subsystem.

#### Testing at code boundaries
<a name="testing-at-code-boundaries.88d5bb1b-73ff-56fb-9e70-fbba4df73ba8"></a>

Define clear code boundaries by separating infrastructure code, such as Lambda code, from your core business logic. This separation creates distinct testing scopes that simplify your test strategy.

##### The boundary pattern
<a name="the-boundary-pattern.d51ee30a-a24b-507b-b496-c0850077e30f"></a>

Establish two clear code boundaries in your Lambda functions:
+ **Outer boundary (Lambda handler)** – A slim adapter layer that handles concerns specific to AWS Lambda
+ **Inner boundary (business logic)** – Pure business logic methods independent of Lambda runtime

##### Handler as adapter (outer scope)
<a name="handler-as-adapter--outer-scope-.2ba4a2eb-35a6-5a0e-b2ae-66157e8b8aaf"></a>

Your Lambda function handler should be a thin layer that:
+ Extracts data from the incoming `event` and `context` objects
+ Validates the extracted data
+ Passes only relevant details to business logic methods
+ Returns results in the expected format for Lambda

##### Business logic (inner scope)
<a name="business-logic--inner-scope-.f1c27508-7499-59c0-b75f-a4fa907fd4e9"></a>

Your core business logic should:
+ Operate independently of details specific to Lambda
+ Accept simple, validated inputs
+ Return predictable outputs
+ Require minimal dependencies for initialization

##### Testing benefits by scope
<a name="testing-benefits-by-scope.a1e0548b-980b-51a8-b088-94478c4f6993"></a>
+ **Inner boundary tests** – Comprehensive unit tests around business logic without Lambda complexity or environment setup
+ **Outer boundary tests** – Focused integration tests validating the adapter layer's event handling and data extraction
+ **Minimal test overhead** – No complex environments or extensive dependencies needed for the majority of your tests

This boundary-based approach allows you to test most of your code as pure functions while keeping Lambda tests minimal and targeted.

### Decrease time to implement or change features
<a name="decrease-time-to-implement-or-change-features.c8d76fb5-d98b-5ddb-b0e4-7ede7b73b629"></a>

You can minimize the effect of software bugs and configuration problems on costs and schedules by catching these issues during an iterative development cycle. When a developer fails to detect these issues, more people must invest additional effort to identify the problems.

A serverless architecture might include managed services that provide critical application functionality through API calls. For this reason, your development cycle should include tests that validate both the *happy path* (where interactions with these services behave as expected) and the *sad path* (where calls fail, return unexpected responses, or behave differently across environments). Without these tests in place, you may encounter issues that stem from differences between your local environment and the deployed environment. When that happens, you must spend additional time attempting to reproduce and verify a fix, because each iteration now requires validating changes against an environment that differs from your preferred setup.

A proper serverless testing strategy improves your iteration time by providing accurate results for tests that include calls to other services.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
