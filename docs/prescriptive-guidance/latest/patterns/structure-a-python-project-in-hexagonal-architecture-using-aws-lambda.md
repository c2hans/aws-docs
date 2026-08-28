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
| Create your own repository. | 1. Log in to GitHub.<br />2. Create a new repository. For instructions, see the [GitHub documentation](https://docs.github.com/en/repositories/creating-and-managing-repositories/creating-a-new-repository).<br />3. Clone and push the [sample repository](https://github.com/aws-samples/lambda-hexagonal-architecture-sample) for this pattern into the new repository in your account. | App developer |
| Install dependencies. | 1. Install Poetry.<pre>pip install poetry</pre><br />2. Install packages from the root directory. The following command installs the application and AWS CDK packages. It also installs development packages that are required for running unit tests. All installed packages are placed in a new virtual environment.<pre>poetry install</pre><br />3. To see a graphical representation of the installed packages, run the following command.<pre>poetry show --tree</pre><br />4. Update all dependencies.<pre>poetry update</pre><br />5. Open a new shell within the newly created virtual environment. It contains all installed dependencies.<pre>poetry shell</pre> | App developer |
| Configure your IDE. | We recommend Visual Studio Code, but you can use any IDE of your choice that supports Python. The following steps are for Visual Studio Code.1. Update the `.vscode/settings` file.<pre>{<br />    "python.testing.pytestArgs": [<br />        "app/adapters/tests",<br />        "app/entrypoints/api/tests",<br />        "app/domain/tests"<br />    ],<br />    "python.testing.unittestEnabled": false,<br />    "python.testing.pytestEnabled": true,<br />    "python.envFile": "${workspaceFolder}/.env",<br />} </pre><br />2. Create an `.env` file in the root directory of the project. This ensures that the root directory of the project is included in the `PYTHONPATH` so that `pytest` can find it and properly discover all packages.<pre>PYTHONPATH=. </pre> | App developer |
| Run unit tests, option 1: Use Visual Studio Code. | 1. Choose the Python interpreter of the virtual environment that’s managed by Poetry.<br />2. Run tests from Test Explorer. | App developer |
| Run unit tests, option 2: Use shell commands. | 1. Start a new shell within the virtual environment.<pre>poetry shell</pre><br />2. Run the `pytest` command from the root directory.<pre>python -m pytest</pre><br />Alternatively you can run the command directly from Poetry.<pre>poetry run python -m pytest</pre> | App developer |

### Deploy and test the application
<a name="deploy-and-test-the-application"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Request temporary credentials. | To have AWS credentials on the shell when you run `cdk deploy`, create temporary credentials by using AWS IAM Identity Center (successor to AWS Single Sign-On). For instructions, see the blog post [How to retrieve short-term credentials for CLI use with AWS IAM Identity Center](https://aws.amazon.com/blogs/security/aws-single-sign-on-now-enables-command-line-interface-access-for-aws-accounts-using-corporate-credentials/). | App developer, AWS DevOps |
| Deploy the application. | 1. Install the AWS CDK v2.<pre>npm install -g aws-cdk</pre><br />For more information, see the [AWS CDK documentation](https://docs.aws.amazon.com/cdk/v2/guide/hello_world.html).<br />2. Bootstrap the AWS CDK into your account and Region.<pre>cdk bootstrap aws://12345678900/us-east-1 --profile aws-profile-name</pre><br />3. Deploy the application as an AWS CloudFormation stack by using an AWS profile.<pre>cdk deploy --profile aws-profile-name</pre> | App developer, AWS DevOps |
| Test the API, option 1: Use the console. | Use the [API Gateway console](https://docs.aws.amazon.com/apigateway/latest/developerguide/how-to-test-method.html) to test the API. For more information about API operations and request/response messages, see the [API usage section of the readme file](https://github.com/aws-samples/lambda-hexagonal-architecture-sample/blob/main/README.md#api-usage) in the GitHub repository. | App developer, AWS DevOps |
| Test the API, option 2: Use Postman. | If you want to use a tool such as [Postman](https://www.postman.com/):1. [Install Postman](https://learning.postman.com/docs/getting-started/installation-and-updates/) as a standalone application or browser extension.<br />2. Copy the endpoint URL for the API Gateway. It will be in the following format.<pre>https://{api-id}.execute-api.{region}.amazonaws.com/{stage}/{path}</pre><br />3. Configure the AWS signature in the authorization tab. For instructions, see the AWS re:Post article on [activating IAM authentication for API Gateway REST APIs](https://aws.amazon.com/premiumsupport/knowledge-center/iam-authentication-api-gateway/#:~:text=Send%20a%20request%20to%20test%20the%20authentication%20settings).<br />4. Use Postman to send requests to your API endpoint. | App developer, AWS DevOps |

### Develop the service
<a name="develop-the-service"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Write unit tests for the business domain. | 1. Create a Python file in the `app/domain/tests` folder by using the `test_` file name prefix.<br />2. Create a new test method to test the new business logic by using the following example.<pre>def test_create_product_should_store_in_repository():<br />    # Arrange<br />    command = create_product_command.CreateProductCommand(<br />        name="Test Product",<br />        description="Test Description",<br />    )<br />    # Act<br />    create_product_command_handler.handle_create_product_command(<br />        command=command, unit_of_work=mock_unit_of_work<br />    )<br /> # Assert</pre><br />3. Create a command class in the `app/domain/commands` folder. <br />4. If the functionality is new, create a stub for the command handler in the `app/domain/command_handlers` folder.<br />5. Run the unit test to see it fail, because there is still no business logic.<pre>python -m pytest</pre> | App developer |
| Implement commands and command handlers. | 1. Implement business logic in the newly created command handler file. <br />2. For every dependency that interacts with external systems, declare an abstract class in the `app/domain/ports` folder.<pre>class ProductsRepository(ABC):<br />    @abstractmethod<br />    def add(self, product: product.Product) -> None:<br />        ...<br /> <br />class UnitOfWork(ABC):<br />    products: ProductsRepository<br /><br />    @abstractmethod<br />    def commit(self) -> None:<br />        ...<br /><br />    @abstractmethod<br />    def __enter__(self) -> typing.Any:<br />        ...<br /><br />    @abstractmethod<br />    def __exit__(self, *args) -> None:<br />        ...</pre><br />3. Update the command handler signature to accept the newly declared dependencies by using the abstract port class as type annotation.<pre>def handle_create_product_command(<br />    command: create_product_command.CreateProductCommand,<br />    unit_of_work: unit_of_work.UnitOfWork,<br />) -> str:<br />    ...</pre><br />4. Update the unit test to simulate the behavior of all declared dependencies for the command handler.<pre>    # Arrange<br />    mock_unit_of_work = unittest.mock.create_autospec(<br />        spec=unit_of_work.UnitOfWork, instance=True<br />    )<br />    mock_unit_of_work.products = unittest.mock.create_autospec(<br />        spec=unit_of_work.ProductsRepository, instance=True<br />    )</pre><br />5. Update the assertion logic in the test to check for the expected dependency invocations.<pre>  # Assert<br />    mock_unit_of_work.commit.assert_called_once()<br />    product = mock_unit_of_work.products.add.call_args.args[0]<br /><br />    assertpy.assert_that(product.name).is_equal_to("Test Product")<br />    assertpy.assert_that(product.description).is_equal_to("Test Description")</pre><br />6. Run the unit test to see it succeed.<pre>python -m pytest</pre> | App developer |
| Write integration tests for secondary adapters. | 1. Create a test file in the `app/adapters/tests` folder by using `test_` as a file name prefix.<br />2. Use the Moto library to mock AWS services.<pre>@pytest.fixture <br />def mock_dynamodb(): <br />   with moto.mock_dynamodb(): <br />    yield boto3.resource("dynamodb", region_name="eu-central-1")</pre><br />3. Create a new test method for an integration test of the adapter.<pre>def test_add_and_commit_should_store_product(mock_dynamodb):<br />    # Arrange<br />    unit_of_work = dynamodb_unit_of_work.DynamoDBUnitOfWork(<br />        table_name=TEST_TABLE_NAME, dynamodb_client=mock_dynamodb.meta.client<br />    )<br />    current_time = datetime.datetime.now(datetime.timezone.utc).isoformat()<br /><br />    new_product_id = str(uuid.uuid4())<br />    new_product = product.Product(<br />        id=new_product_id,<br />        name="test-name",<br />        description="test-description",<br />        createDate=current_time,<br />        lastUpdateDate=current_time,<br />    )<br /><br />    # Act<br />    with unit_of_work:<br />        unit_of_work.products.add(new_product)<br />        unit_of_work.commit()<br /> <br />    # Assert</pre><br />4. Create an adapter class in the `app/adapters` folder. Use the abstract class from the ports folder as a base class.<br />5. Run the unit test to see it fail, because there is still no logic.<pre>python -m pytest</pre> | App developer |
| Implement secondary adapters. | 1. Implement logic in the newly created adapter file.<br />2. Update test assertions.<pre># Assert<br />    with unit_of_work_readonly:<br />        product_from_db = unit_of_work_readonly.products.get(new_product_id)<br /><br />    assertpy.assert_that(product_from_db).is_not_none()<br />    assertpy.assert_that(product_from_db.dict()).is_equal_to(<br />        {<br />            "id": new_product_id,<br />            "name": "test-name",<br />            "description": "test-description",<br />            "createDate": current_time,<br />            "lastUpdateDate": current_time,<br />        }<br />    )</pre><br />3. Run the unit test to see it succeed.<pre>python -m pytest</pre> | App developer |
| Write end-to-end tests. | 1. Create a test file in the `app/entrypoints/api/tests` folder by using `test_` as a file name prefix. <br />2. Create a Lambda context fixture that will be used by the test to call Lambda.<pre>@pytest.fixture<br />def lambda_context():<br />    @dataclass<br />    class LambdaContext:<br />        function_name: str = "test"<br />        memory_limit_in_mb: int = 128<br />        invoked_function_arn: str = "arn:aws:lambda:eu-west-1:809313241:function:test"<br />        aws_request_id: str = "52fdfc07-2182-154f-163f-5f0f9a621d72"<br /><br /> return LambdaContext()</pre><br />3. Create a test method for the API invocation.<pre>def test_create_product(lambda_context):<br />    # Arrange<br />    name = "TestName"<br />    description = "Test description"<br />    request = api_model.CreateProductRequest(name=name, description=description)<br /><br />    minimal_event = api_gateway_proxy_event.APIGatewayProxyEvent(<br />        {<br />            "path": "/products",<br />            "httpMethod": "POST",<br />            "requestContext": {  # correlation ID<br />                "requestId": "c6af9ac6-7b61-11e6-9a41-93e8deadbeef"<br />            },<br />            "body": json.dumps(request.dict()),<br />        }<br />    )<br /><br />    create_product_func_mock = unittest.mock.create_autospec(<br />        spec=create_product_command_handler.handle_create_product_command<br />    )<br />    handler.create_product_command_handler.handle_create_product_command = (<br />        create_product_func_mock<br />    )<br /><br />    # Act<br />    handler.handler(minimal_event, lambda_context)</pre><br />4. Run the unit test to see it fail, because there is still no logic.<pre>python -m pytest</pre> | App developer |
| Implement primary adapters. | 1. Create a function for API business logic and declare it as an API resource.<pre>@tracer.capture_method<br />@app.post("/products")<br />@utils.parse_event(model=api_model.CreateProductRequest, app_context=app)<br />def create_product(<br />    request: api_model.CreateProductRequest,<br />) -> api_model.CreateProductResponse:<br />    """Creates a product."""<br />...<br /></pre>All decorators you see are features of the AWS Lambda Powertools for Python library. For details, see the [AWS Lambda Powertools for Python website](https://docs.powertools.aws.dev/lambda/python/latest/).<br />2. Implement the API logic.<pre>id=create_product_command_handler.handle_create_product_command(<br />        command=create_product_command.CreateProductCommand(<br />            name=request.name,<br />            description=request.description,<br />        ),<br />        unit_of_work=unit_of_work,<br />    )<br />    response = api_model.CreateProductResponse(id=id)<br />    return response.dict()</pre><br />3. Run the unit test to see it succeed.<pre>python -m pytest</pre> | App developer |

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

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
