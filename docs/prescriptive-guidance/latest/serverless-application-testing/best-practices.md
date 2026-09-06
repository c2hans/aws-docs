---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/serverless-application-testing/best-practices.html
---

# Best practices for testing serverless applications
<a name="best-practices"></a>

The following sections outline best practices for achieving effective coverage when testing serverless applications.

## Prioritize testing in the cloud
<a name="prioritize-cloud"></a>

For well-designed applications, you can employ a variety of testing techniques to satisfy a range of requirements and conditions. However, based on current tooling, we recommend that you focus on testing in the cloud as much as possible. Although testing in the cloud can create developer latency, increase costs, and sometimes require investments in additional DevOps controls, this technique provides the most reliable, accurate, and complete test coverage.

You should have access to isolated environments in which to perform testing. Ideally, each developer should have a dedicated AWS account to avoid any issues with resource naming that can occur when multiple developers who are working in the same code try to deploy or invoke API calls on resources that have identical names. These environments should be configured with the appropriate alerts and controls to avoid unnecessary spending. For example, you can limit the type, tier, or size of resources that can be created, and set up email alerts when estimated costs exceed a given threshold.

If you must share a single AWS account with other developers, automated test processes should name resources to be unique for each developer. For example, update scripts or TOML configuration files that cause AWS SAM CLI [sam deploy](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/sam-cli-command-reference-sam-deploy.html) or [sam sync](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/sam-cli-command-reference-sam-sync.html) commands can automatically specify a stack name that includes the local developer's user name.

Testing in the cloud is valuable for all phases of testing, including unit tests, integration tests, and end-to-end tests.

## Use mocks if necessary
<a name="use-mocks"></a>

Mock frameworks are a valuable tool for writing fast unit tests. They are especially valuable when tests need to cover complex internal business logic, such as mathematical or financial calculations or simulations. Look for unit tests that have a large number of test cases or input variations, where the inputs do not change the pattern or the content of calls to other cloud services. Creating mock tests for these scenarios can improve developer iteration times.

Code that is covered by unit tests that use mock testing should also be covered by testing in the cloud. This is necessary because the mocks are still running on a developer's laptop or build machine, and the environment might be configured differently than it will be in the cloud. For example, your code might include AWS Lambda functions that use more memory or take more time than Lambda is configured to allocate when it's run with certain input parameters. Or your code might include environment variables that aren't configured in the same way (or at all), and the differences might cause the code to behave differently or to fail.

Don't use mocks of cloud services to validate the proper implementation of those service integrations. Although it might be acceptable to mock a cloud service when you're testing other functionality, you should test cloud service calls in the cloud to validate the correct configuration and functional implementation.

Mocks can add value to unit testing, especially when you're testing a large number of cases frequently. This benefit is reduced for integration tests, because the level of effort to implement the necessary mocks increases with the number of connection points. End-to-end testing should not use mocks, because these tests generally deal with states and complex logic that cannot be easily simulated with mock frameworks.

## Understand the tradeoffs of emulation testing
<a name="avoid-emulators"></a>

Emulators can be a practical choice for specific use cases. For example, a development team with limited, inconsistent, or slow internet access may find that emulation testing is the most reliable way to iterate on code before moving to a cloud environment.

For most other circumstances, use emulators selectively. When you rely heavily on an emulator, it can become difficult to incorporate new AWS service features into your testing until the emulation vendor releases an update to provide feature parity. Emulators also require upfront and ongoing investment for setup and configuration across development systems and build machines. Additionally, many cloud services don't have emulators available; selecting an emulation-first strategy may either preclude the use of those services or produce code and configurations that aren't well tested against real service behavior.

If you use emulation testing, complement it with cloud testing as much as possible to validate that proper cloud configurations are in place and to test interactions with services that can only be simulated or mocked in an emulated environment.

Emulation testing can provide fast feedback for unit tests and, depending on the features and behavioral parity of the emulation software, may support some integration and end-to-end tests as well.

## Scope tests through natural boundaries
<a name="scope-tests"></a>

As serverless applications grow across more architectural components, natural boundaries emerge around subsystems—especially when following best practices like single-purpose functions and event-driven decoupling. These boundaries serve as effective testing edges where you can validate contracts between components.

### Identify architecture boundaries
<a name="identify-architecture-boundaries.579324d8-6a26-5c29-accb-f1cf000835af"></a>

Look for natural seams in your application design:
+ Between services, such as an Amazon EventBridge rule connecting a publisher to a consumer
+ At API edges, such as Amazon API Gateway endpoints that front Lambda functions
+ Around workflows, such as AWS Step Functions orchestrating multiple services
+ At storage layers, such as Amazon DynamoDB streams triggering downstream processing

### Separate Lambda code from business logic
<a name="separate-9999999999999999lam--code-from-business-logic.400b5c80-0b44-5f98-9bcd-7bee9baa921d"></a>

Simplify your tests by isolating Lambda code from core business logic. Your Lambda handler should act as a thin adapter between the AWS runtime and your application logic. It should extract and validate event data and then delegate to a testable function that has no Lambda dependencies. This makes your business logic portable, easier to reason about, and straightforward to test without mocking Lambda objects or setting up complex environments.

### Treat boundaries as contracts
<a name="treat-boundaries-as-contracts.2f48075c-8e72-5953-9115-1c3ff51459b0"></a>

Test at the boundary, not through it. Validate what crosses the edge without requiring the entire downstream system. These same boundaries also serve as observability hooks in production. The architectural seams where you test can be instrumented for monitoring using Amazon CloudWatch Logs, AWS X-Ray traces, and EventBridge events.

## Use test harnesses for asynchronous workflows
<a name="test-harnesses"></a>

Serverless applications often rely on asynchronous patterns, where events trigger processing, messages flow through queues, and workflows span multiple services without immediate responses. You can't simply invoke a function and inspect a return value. The result may appear later in a database, a log stream, or another service.

A *test harness* is testing infrastructure you deploy alongside your application to observe and validate this asynchronous behavior. Test harnesses typically include:
+ Event listeners that subscribe to the same events your application produces
+ Storage mechanisms (such as DynamoDB tables or Amazon S3 buckets) where test results can be captured
+ Polling logic in your test code that waits for expected outcomes to appear

Your test code initiates an event, waits for the workflow to complete, then queries the test harness to verify the expected outcome occurred.

The following are best practices:
+ **Define clear SLAs for asynchronous operations** – Establish how long workflows should take and use these as polling timeouts in your tests
+ **Use unique identifiers for test isolation** – Generate unique filenames, message IDs, or correlation tokens per test run to prevent interference between tests
+ **Deploy test infrastructure alongside your application** – Include test harness resources in your infrastructure-as-code templates so they stay in sync as your application evolves
+ **Clean up test data after test runs** – This prevents accumulating test artifacts in your cloud environment

Test harnesses are most valuable for integration tests that validate workflows across multiple services, end-to-end tests that verify complete user journeys, and event-driven architectures where services communicate through EventBridge, Amazon SNS, Amazon SQS, or Amazon Kinesis.

## Organize cloud environments for developer isolation
<a name="organize-cloud-environments"></a>

Testing in the cloud requires environments that are isolated from one another. When developers share a single AWS account, such as a team development account, consider creating a separate application stack for each developer or feature branch. This isolates resources, prevents naming collisions, and avoids quota contention or noisy neighbor issues during testing.

Use AWS Systems Manager Parameter Store or similar tooling to manage stack-specific configurations, such as API endpoints and queue names. For cost efficiency, share expensive resources like Amazon Relational Database Service (Amazon RDS) clusters across developer stacks while keeping lightweight serverless resources (such as Lambda functions, API Gateway stages, and DynamoDB tables) isolated per stack.

In regulated industries, enterprise security policies may restrict developer access to cloud environments, making it difficult to run cloud tests as part of a local development workflow. In these cases, emulation testing can fill the gap between local mock testing and full cloud validation, though it should be complemented with cloud testing whenever access permits.

## Accelerate feedback loops
<a name="feedback-loops"></a>

When you test in the cloud, use tools and techniques to accelerate development feedback loops. For example, use [AWS SAM Accelerate](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/accelerate.html) and AWS CDK watch mode to decrease the time it takes to push code modifications to a cloud environment. The samples in the GitHub [Serverless Test Samples repository](https://github.com/aws-samples/serverless-test-samples) explore some of these techniques.

We also recommend that you create and test cloud resources from your local machine as early as possible during development―not only after a check-in to source control. This practice enables quicker exploration and experimentation when developing solutions. In addition, the ability to automate deployment from a development machine helps you discover cloud configuration problems more quickly and reduces wasted effort from updating and approving modifications to source control.
