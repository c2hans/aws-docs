---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/hexagonal-architectures/improve-dev-cycle.html
---

# Improving the development cycle
<a name="improve-dev-cycle"></a>

Developing software for the cloud introduces new challenges for software engineers, because it is very hard to replicate the runtime environment locally on the development machine. A straightforward way to validate the software is to deploy it to the cloud and test it there. However, this approach involves a lengthy feedback cycle, especially when the software architecture contains multiple serverless deployments. Improving this feedback cycle shortens the time to develop features, which reduces the time to market significantly.

## Testing in the cloud
<a name="testing-cloud"></a>

Testing directly in the cloud is the only way to make sure that your architectural components, such as gateways in Amazon API Gateway, AWS Lambda functions, Amazon DynamoDB tables, and AWS Identity and Access Management (IAM) permissions, are configured correctly. It might also be the only reliable way to test component integrations. Although some AWS services (such as [DynamoDB](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/DynamoDBLocal.html)) can be deployed locally, most of them cannot be replicated in a local setup. At the same time, third-party tools such as [Moto](https://docs.getmoto.org/en/latest/) and [LocalStack](https://localstack.cloud) that mock AWS services for testing purposes might not reflect real service API contracts accurately, or the number of features might be limited.

 However, the most complex part of the enterprise software is in the business logic, not in the cloud architecture. The architecture changes less often than the domain, which must accommodate new business requirements. Thus, testing business logic in the cloud becomes an intense process of making a change in the code, initiating a deployment, waiting for the environment to be ready, and validating the change. If a deployment takes as little as 5 minutes, making and testing 10 changes in the business logic will take an hour or more. If business logic is more complex, testing might require days of just waiting for deployments to complete. If you have multiple features and engineers on the team, the extended period quickly becomes noticeable to the business.

## Testing locally
<a name="testing-local"></a>

A hexagonal architecture helps developers focus on the domain instead of infrastructure technicalities. This approach uses local tests (the unit testing tools in your chosen development framework) to cover domain logic requirements. You won't have to spend time solving technical integration problems or deploy your software to the cloud to test the business logic. You can run unit tests locally and reduce the feedback loop from minutes to seconds. If a deployment takes 5 minutes but unit tests complete in 5 seconds, that's a significant reduction in the time it takes to detect mistakes. The [*Testing business logic*](improve-software-quality.md#logic)* first* section later in this guide covers this approach in more detail.

## Parallelization of development
<a name="parallel"></a>

The hexagonal architecture approach enables development teams to parallelize development efforts. Developers can design and implement different components of the service individually. This parallelization is possible through the isolation of each component and the defined interfaces between each component.

## Product time to market
<a name="time-to-market"></a>

Local unit testing improves the development feedback cycle and reduces the time to market for new products or features, especially when these contain complex business logic, as explained previously. Furthermore, increased code coverage by unit tests significantly reduces the risk of introducing regression bugs when you update or refactor the code base. Unit test coverage also enables you to continuously refactor the code base to keep it well organized, which speeds the onboarding process for new engineers. This is discussed further in the [*Quality by design*](improve-software-quality.md) section. Lastly, if the business logic is well isolated and tested, it enables developers to adapt quickly to changing functional and non-functional requirements. This is explained further in the [*Adapting to change*](adapt-to-change.md) section.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
