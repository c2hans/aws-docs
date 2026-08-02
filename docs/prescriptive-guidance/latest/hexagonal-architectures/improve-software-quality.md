---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/hexagonal-architectures/improve-software-quality.html
---

# Quality by design
<a name="improve-software-quality"></a>

Adopting a hexagonal architecture helps promote the quality of your code base from the start of your project. It is important to build a process that helps you meet expected quality requirements from the beginning, without slowing down the development process.

## Localized changes and increased readability
<a name="readability"></a>

Using the hexagonal architecture approach enables developers to change code in one class or component without affecting other classes or components. This design promotes the cohesion of developed components. By decoupling the domain from adapters and using well-known interfaces, you can increase the readability of the code. It becomes easier to identify issues and corner cases.

This approach also facilitates code review during development and limits the introduction of undetected changes or technical debt.

## Testing business logic first
<a name="logic"></a>

Local testing can be accomplished by introducing end-to-end, integration, and unit tests to the project. End-to-end tests cover the whole incoming request lifecycle. They typically invoke an application entry point and test to see if it has accomplished the business requirement. Each software project should have at least one test scenario that uses known inputs and produces expected outputs. However, adding more corner-case scenarios can get complex, because each test must be configured to send a request through an entry point (for example, through a REST API or queues), go through all the integration points that the business action requires, and then assert the result. Setting up the environment for the test scenario and asserting results can take a lot of developers' time.

In hexagonal architecture, you test business logic in isolation, and use integration tests to test secondary adapters. You can use mock or fake adapters in your business logic tests. You can also combine the tests for business use cases with unit tests for your domain model to maintain high coverage with low coupling. As a good practice, integration tests should not validate business logic. Instead, they should verify that the secondary adapter calls the external services correctly.

Ideally, you can use test-driven development (TDD) and start defining domain entities or business use cases with proper tests at the very beginning of development. Writing the tests first helps you create mock implementations of the interfaces required by the domain. When the tests are successful and domain logic rules are satisfied, you can implement the actual adapters and deploy software to the test environment. At this point, your implementation of domain logic might not be ideal. You can then work on refactoring the existing architecture to evolve it by introducing design patterns or rearranging code in general. By using this approach, you can avoid introducing regression bugs and you can improve the architecture as the project grows. By combining this approach with the automatic tests you run in your continuous integration process, you can decrease the number of potential bugs before they get to production.

If you use serverless deployments, you can quickly provision an instance of the application in your AWS account for manual integration and end-to-end testing. After these implementation steps, we recommend that you automate testing with every new change pushed to the repository.

## Maintainability
<a name="maintainability"></a>

Maintainability refers to operating and monitoring an application to ensure that it meets all requirements and minimizing the probability of a system failure. To make the system operable, you must adapt it to future traffic or operational requirements. You must also ensure that it's available and easy to deploy with minimum or no impact on clients.

To understand the current and historical state of your system, you must make it *observable*. You can do this by providing specific metrics, logs, and traces that operators can use to ensure that the system works as expected and to track bugs. These mechanisms should also allow operators to conduct root cause analysis without having to log in to the machine and read the code.

A hexagonal architecture aims to increase the maintainability of your web applications so that your code requires less work overall. By separating modules, localizing changes, and decoupling application business logic from adapter implementation, you can produce metrics and logs that help operators gain a deep understanding of the system and understand the scope of specific changes made to the primary or secondary adapters.
