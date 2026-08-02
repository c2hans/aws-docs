---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/structure-a-python-project-in-hexagonal-architecture-using-aws-lambda.html
---

# Structure a Python project in hexagonal architecture using AWS Lambda
<a name="structure-a-python-project-in-hexagonal-architecture-using-aws-lambda"></a>

*Furkan Oruc, Dominik Goby, Darius Kunce, and Michal Ploski, Amazon Web Services*

## Summary
<a name="structure-a-python-project-in-hexagonal-architecture-using-aws-lambda-summary"></a>

This pattern shows how to structure a Python project in hexagonal architecture by using AWS Lambda. The pattern uses the AWS Cloud Development Kit (AWS CDK) as the infrastructure as code (IaC) tool, Amazon API Gateway as the REST API, and Amazon DynamoDB as the persistence layer. Hexagonal architecture follows domain-driven design principles. In hexagonal architecture, software consists of three components: domain, ports, and adapters. For detailed information about hexagonal architectures and their benefits, see the guide [Building hexagonal architectures on AWS](https://docs.aws.amazon.com/prescriptive-guidance/latest/hexagonal-architectures/)*.*

## Prerequisites and limitations
<a name="structure-a-python-project-in-hexagonal-architecture-using-aws-lambda-prereqs"></a>

**Prerequisites **
+ An active AWS account
+ Experience in Python
+ Familiarity with AWS Lambda, AWS CDK, Amazon API Gateway, and DynamoDB
+ A GitHub account (see [instructions for signing up](https://docs.github.com/en/get-started/signing-up-for-github/signing-up-for-a-new-github-account))
+ Git (see [installation instructions](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git))
+ A code editor for making changes and pushing your code to GitHub (for example, [Visual Studio Code](https://code.visualstudio.com/) or [JetBrains PyCharm](https://www.jetbrains.com/pycharm/))
+ Docker installed, and the Docker daemon up and running

**Product versions**
+ Git version 2.24.3 or later
+ Python version 3.7 or later
+ AWS CDK v2
+ Poetry version 1.1.13 or later
+ AWS Lambda Powertools for Python version 1.25.6 or later
+ pytest version 7.1.1 or later
+ Moto version 3.1.9 or later
+ pydantic version 1.9.0 or later
+ Boto3 version 1.22.4 or later
+ mypy-boto3-dynamodb version 1.24.0 or later

## Architecture
<a name="structure-a-python-project-in-hexagonal-architecture-using-aws-lambda-architecture"></a>

**Target technology stack  **

The target technology stack consists of a Python service that uses API Gateway, Lambda, and DynamoDB. The service uses a DynamoDB adapter to persist data. It provides a function that uses Lambda as the entry point. The service uses Amazon API Gateway to expose a REST API. The API uses AWS Identity and Access Management (IAM) for the [authentication of clients](https://docs.aws.amazon.com/apigateway/latest/developerguide/permissions.html).

**Target architecture **

To illustrate the implementation, this pattern deploys a serverless target architecture. Clients can send requests to an API Gateway endpoint. API Gateway forwards the request to the target Lambda function that implements the hexagonal architecture pattern. The Lambda function performs create, read, update, and delete (CRUD) operations on a DynamoDB table.

|
|
| This pattern was tested in a PoC environment. You must conduct a security review to identify the threat model and create a secure code base before you deploy any architecture to a production environment.  |
| --- |

![Target architecture for structuring a Python project in hexagonal architecture](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/images/pattern-img/25bd7169-ea5e-4a21-a865-c91c30a3c0da/images/de0d4f0d-ad19-43ec-bd10-676b25477b64.png)

The API supports five operations on a product entity:
+ `GET /products` returns all products.
+ `POST /products` creates a new product.
+ `GET /products/{id}` returns a specific product.
+ `PUT /products/{id}` updates a specific product.
+ `DELETE /products/{id}` deletes a specific product.

You can use the following folder structure to organize your project to follow the hexagonal architecture pattern:

```
app/  # application code
|--- adapters/  # implementation of the ports defined in the domain
     |--- tests/  # adapter unit tests
|--- entrypoints/  # primary adapters, entry points
     |--- api/  # api entry point
          |--- model/  # api model
          |--- tests/  # end to end api tests
|--- domain/  # domain to implement business logic using hexagonal architecture
     |--- command_handlers/  # handlers used to execute commands on the domain
     |--- commands/  # commands on the domain
     |--- events/  # events triggered via the domain
     |--- exceptions/  # exceptions defined on the domain
     |--- model/  # domain model
     |--- ports/  # abstractions used for external communication
     |--- tests/  # domain tests
|--- libraries/  # List of 3rd party libraries used by the Lambda function
infra/  # infrastructure code
simple-crud-app.py  # AWS CDK v2 app
```

## Tools
<a name="structure-a-python-project-in-hexagonal-architecture-using-aws-lambda-tools"></a>

**AWS services**
+ [Amazon API Gateway](https://aws.amazon.com/api-gateway/) is a fully managed service that makes it easy for developers to create, publish, maintain, monitor, and secure APIs at any scale.
+ [Amazon DynamoDB](https://aws.amazon.com/dynamodb/) is a fully managed, serverless, key-value NoSQL database that is designed to run high-performance applications at any scale.
+ [AWS Lambda](https://aws.amazon.com/lambda/) is a serverless, event-driven compute service that lets you run code for virtually any type of application or backend service without provisioning or managing servers. You can launch Lambda functions from over 200 AWS services and software as a service (SaaS) applications, and only pay for what you use.

**Tools**
+ [Git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)  is used as the version control system for code development in this pattern.
+ [Python](https://www.python.org/) is used as the programming language for this pattern. Python provides high-level data structures and an approach to object-oriented programming. AWS Lambda provides a built-in Python runtime that simplifies the operation of Python services.
+ [Visual Studio Code](https://code.visualstudio.com/) is used as the IDE for development and testing for this pattern. You can use any IDE that supports Python development (for example, [PyCharm](https://www.jetbrains.com/pycharm/)).
+ [AWS Cloud Development Kit (AWS CDK](https://aws.amazon.com/cdk/)) is an open-source software development framework that lets you define your cloud application resources by using familiar programming languages. This pattern uses the CDK to write and deploy cloud infrastructure as code.
+ [Poetry](https://python-poetry.org/) is used to manage dependencies in the pattern.
+ [Docker](https://www.docker.com/) is used by the AWS CDK to build the Lambda package and layer.

**Code **

The code for this pattern is available in the GitHub [Lambda hexagonal architecture sample](https://github.com/aws-samples/lambda-hexagonal-architecture-sample) repository.

## Best practices
<a name="structure-a-python-project-in-hexagonal-architecture-using-aws-lambda-best-practices"></a>

To use this pattern in a production environment, follow these best practices:
+ Use customer managed keys in AWS Key Management Service (AWS KMS) to encrypt [Amazon CloudWatch log groups](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/encrypt-log-data-kms.html) and [Amazon DynamoDB tables](https://docs.aws.amazon.com/kms/latest/developerguide/services-dynamodb.html).
+ Configure [AWS WAF for Amazon API Gateway](https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-control-access-aws-waf.html) to allow access only from your organization's network.
+ Consider other options for API Gateway authorization if IAM doesn’t meet your needs. For example, you can use [Amazon Cognito user pools](https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-integrate-with-cognito.html) or [API Gateway Lambda authorizers](https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-use-lambda-authorizer.html).
+ Use [DynamoDB backups](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/BackupRestore.html).
+ Configure Lambda functions with a [virtual private cloud (VPC) deployment](https://docs.aws.amazon.com/lambda/latest/dg/configuration-vpc.html) to keep network traffic inside the cloud.
+ Update the allowed origin configuration for [cross-origin resource sharing (CORS) preflight](https://developer.mozilla.org/en-US/docs/Web/HTTP/CORS) to restrict access to the requesting origin domain only.
+ Use [cdk-nag](https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/check-aws-cdk-applications-or-cloudformation-templates-for-best-practices-by-using-cdk-nag-rule-packs.html) to check the AWS CDK code for security best practices.
+ Consider using code scanning tools to find common security issues in the code. For example, [Bandit](https://bandit.readthedocs.io/en/latest/) is a tool that’s designed to find common security issues in Python code. [Pip-audit](https://pypi.org/project/pip-audit/) scans Python environments for packages that have known vulnerabilities.

This pattern uses [AWS X-Ray](https://aws.amazon.com/xray/?nc1=h_ls) to trace requests through the application’s entry point, domain, and adapters. AWS X-Ray helps developers identify bottlenecks and determine high latencies to improve application performance.

## Epics
<a name="structure-a-python-project-in-hexagonal-architecture-using-aws-lambda-epics"></a>

### Initialize the project
<a name="initialize-the-project"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Create your own repository. | [See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/structure-a-python-project-in-hexagonal-architecture-using-aws-lambda.html) | App developer |
| Install dependencies. | [See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/structure-a-python-project-in-hexagonal-architecture-using-aws-lambda.html) | App developer |
| Configure your IDE. | We recommend Visual Studio Code, but you can use any IDE of your choice that supports Python. The following steps are for Visual Studio Code.[See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/structure-a-python-project-in-hexagonal-architecture-using-aws-lambda.html) | App developer |
| Run unit tests, option 1: Use Visual Studio Code. | [See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/structure-a-python-project-in-hexagonal-architecture-using-aws-lambda.html) | App developer |
| Run unit tests, option 2: Use shell commands. | [See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/structure-a-python-project-in-hexagonal-architecture-using-aws-lambda.html) | App developer |

### Deploy and test the application
<a name="deploy-and-test-the-application"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Request temporary credentials. | To have AWS credentials on the shell when you run `cdk deploy`, create temporary credentials by using AWS IAM Identity Center (successor to AWS Single Sign-On). For instructions, see the blog post [How to retrieve short-term credentials for CLI use with AWS IAM Identity Center](https://aws.amazon.com/blogs/security/aws-single-sign-on-now-enables-command-line-interface-access-for-aws-accounts-using-corporate-credentials/). | App developer, AWS DevOps |
| Deploy the application. | [See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/structure-a-python-project-in-hexagonal-architecture-using-aws-lambda.html) | App developer, AWS DevOps |
| Test the API, option 1: Use the console. | Use the [API Gateway console](https://docs.aws.amazon.com/apigateway/latest/developerguide/how-to-test-method.html) to test the API. For more information about API operations and request/response messages, see the [API usage section of the readme file](https://github.com/aws-samples/lambda-hexagonal-architecture-sample/blob/main/README.md#api-usage) in the GitHub repository. | App developer, AWS DevOps |
| Test the API, option 2: Use Postman. | If you want to use a tool such as [Postman](https://www.postman.com/):[See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/structure-a-python-project-in-hexagonal-architecture-using-aws-lambda.html) | App developer, AWS DevOps |

### Develop the service
<a name="develop-the-service"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Write unit tests for the business domain. | [See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/structure-a-python-project-in-hexagonal-architecture-using-aws-lambda.html) | App developer |
| Implement commands and command handlers. | [See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/structure-a-python-project-in-hexagonal-architecture-using-aws-lambda.html) | App developer |
| Write integration tests for secondary adapters. | [See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/structure-a-python-project-in-hexagonal-architecture-using-aws-lambda.html) | App developer |
| Implement secondary adapters. | [See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/structure-a-python-project-in-hexagonal-architecture-using-aws-lambda.html) | App developer |
| Write end-to-end tests. | [See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/structure-a-python-project-in-hexagonal-architecture-using-aws-lambda.html) | App developer |
| Implement primary adapters. | [See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/structure-a-python-project-in-hexagonal-architecture-using-aws-lambda.html) | App developer |

## Related resources
<a name="structure-a-python-project-in-hexagonal-architecture-using-aws-lambda-resources"></a>

**APG guide**
+ [Building hexagonal architectures on AWS](https://docs.aws.amazon.com/prescriptive-guidance/latest/hexagonal-architectures/)

**AWS References**
+ [AWS Lambda documentation](https://docs.aws.amazon.com/lambda/)
+ [AWS CDK documentation](https://docs.aws.amazon.com/cdk/)
  + [Your first AWS CDK app](https://docs.aws.amazon.com/cdk/v2/guide/hello_world.html)
+ [API Gateway documentation](https://docs.aws.amazon.com/apigateway/)
  + [Control access to an API with IAM permissions](https://docs.aws.amazon.com/apigateway/latest/developerguide/permissions.html)
  + [Use the API Gateway console to test a REST API method](https://docs.aws.amazon.com/apigateway/latest/developerguide/how-to-test-method.html)
+ [Amazon DynamoDB documentation](https://docs.aws.amazon.com/dynamodb/)

**Tools**
+ [git-scm.com website](https://git-scm.com/)
+ [Installing Git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)
+ [Creating a new GitHub repository](https://docs.github.com/en/repositories/creating-and-managing-repositories/creating-a-new-repository)
+ [Python website](https://www.python.org/)
+ [AWS Lambda Powertools for Python](https://docs.powertools.aws.dev/lambda/python/latest/)
+ [Postman website](https://www.postman.com/)
+ [Python mock object library](https://docs.python.org/3/library/unittest.mock.html)
+ [Poetry website](https://python-poetry.org/)

**IDEs**
+ [Visual Studio Code website](https://code.visualstudio.com/)
+ [PyCharm website](https://www.jetbrains.com/pycharm/)
