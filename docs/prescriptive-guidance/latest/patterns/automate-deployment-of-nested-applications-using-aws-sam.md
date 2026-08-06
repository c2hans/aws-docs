---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/automate-deployment-of-nested-applications-using-aws-sam.html
---

# Automate deployment of nested applications using AWS SAM
<a name="automate-deployment-of-nested-applications-using-aws-sam"></a>

*Dr. Rahul Sharad Gaikwad, Ishwar Chauthaiwale, Dmitry Gulin, and Tabby Ward, Amazon Web Services*

## Summary
<a name="automate-deployment-of-nested-applications-using-aws-sam-summary"></a>

On Amazon Web Services (AWS), AWS Serverless Application Model (AWS SAM) is an open-source framework that provides shorthand syntax to express functions, APIs, databases, and event source mappings. With just a few lines for each resource, you can define the application you want and model it by using YAML. During deployment, SAM transforms and expands the SAM syntax into AWS CloudFormation syntax that you can use to build serverless applications faster.

AWS SAM simplifies the development, deployment, and management of serverless applications on the AWS platform. It provides a standardized framework, faster deployment, local testing capabilities, resource management, seamless Integration with Development Tools, and a supportive community. These features make it a valuable tool for building serverless applications efficiently and effectively.

This pattern uses AWS SAM templates to automate the deployment of nested applications. A nested application is an application within another application. Parent applications call their child applications. These are loosely coupled components of a serverless architecture.

Using nested applications, you can rapidly build highly sophisticated serverless architectures by reusing services or components that are independently authored and maintained but are composed using AWS SAM and the Serverless Application Repository. Nested applications help you to build applications that are more powerful, avoid duplicated work, and ensure consistency and best practices across your teams and organizations. To demonstrate nested applications, the pattern deploys an [example AWS serverless shopping cart application](https://github.com/aws-samples/aws-sam-nested-stack-sample).

## Prerequisites and limitations
<a name="automate-deployment-of-nested-applications-using-aws-sam-prereqs"></a>

**Prerequisites **
+ An active AWS account
+ An existing virtual private cloud (VPC) and subnets
+ An integrated development environment such as Visual Studio Code (for more information, see [Tools to Build on AWS](https://aws.amazon.com/getting-started/tools-sdks/#IDE_and_IDE_Toolkits))
+ Python wheel library installed using pip install wheel, if it’s not already installed

**Limitations **
+ The maximum number of applications that can be nested in a serverless application is 200.
+ The maximum number of parameters for a nested application can have 60.

**Product versions**
+ This solution is built on AWS SAM command line interface (AWS SAM CLI) version 1.21.1, but this architecture should work with later AWS SAM CLI versions.

## Architecture
<a name="automate-deployment-of-nested-applications-using-aws-sam-architecture"></a>

**Target technology stack  **
+ Amazon API Gateway
+ AWS SAM
+ Amazon Cognito
+ Amazon DynamoDB
+ AWS Lambda
+ Amazon Simple Queue Service (Amazon SQS) queue

**Target architecture**

The following diagram shows how user requests are made to the shopping services by calling APIs. The user's request, including all necessary information, is sent to Amazon API Gateway and the Amazon Cognito authorizer, which performs authentication and authorization mechanisms for the APIs.

When an item is added, deleted, or updated in DynamoDB, an event is put onto DynamoDB Streams, which in turn initiates a Lambda function. To avoid immediate deletion of old items as part of a synchronous workflow, messages are put onto an SQS queue, which initiates a worker function to delete the messages.

![POST and PUT operations from API Gateway to Lambda functions to DynamoDB and Product Service.](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/images/pattern-img/218adecc-b5b8-4193-9012-b5d584e2e128/images/5b454bae-5fd4-405d-a37d-6bafc3fcf889.png)

In this solution setup, AWS SAM CLI serves as the interface for AWS CloudFormation stacks. AWS SAM templates automatically deploy nested applications. The parent SAM template calls the child templates, and the parent CloudFormation stack deploys the child stacks. Each child stack builds the AWS resources that are defined in the AWS SAM CloudFormation templates.

![Four-step process using AWS SAM CLI with a parent and three child CloudFormation stacks.](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/images/pattern-img/218adecc-b5b8-4193-9012-b5d584e2e128/images/5828026e-72ad-4a3f-a5f2-bffac0f13e42.png)

1. Build and deploy the stacks.

1. The Auth CloudFormation stack contains Amazon Cognito.

1. The Product CloudFormation stack contains an Lambda function and Amazon API Gateway

1. The Shopping CloudFormation stack contains a Lambda function, Amazon API Gateway, the SQS queue, and the Amazon DynamoDB database.

## Tools
<a name="automate-deployment-of-nested-applications-using-aws-sam-tools"></a>

**Tools**
+ [Amazon API Gateway](https://docs.aws.amazon.com/apigateway/latest/developerguide/welcome.html) helps you create, publish, maintain, monitor, and secure REST, HTTP, and WebSocket APIs at any scale.
+ [AWS CloudFormation](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html) helps you set up AWS resources, provision them quickly and consistently, and manage them throughout their lifecycle across AWS accounts and Regions.
+ [Amazon Cognito](https://docs.aws.amazon.com/cognito/latest/developerguide/what-is-amazon-cognito.html) provides authentication, authorization, and user management for web and mobile apps.
+ [Amazon DynamoDB](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/Introduction.html) is a fully managed NoSQL database service that provides fast, predictable, and scalable performance.
+ [AWS Lambda](https://docs.aws.amazon.com/lambda/latest/dg/welcome.html) is a compute service that helps you run code without needing to provision or manage servers. It runs your code only when needed and scales automatically, so you pay only for the compute time that you use.
+ [AWS Serverless Application Model (AWS SAM)](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/what-is-sam.html) is an open-source framework that helps you build serverless applications in the AWS Cloud.
+ [Amazon Simple Queue Service (Amazon SQS)](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/welcome.html) provides a secure, durable, and available hosted queue that helps you integrate and decouple distributed software systems and components.

**Code **

The code for this pattern is available in the GitHub [AWS SAM Nested Stack Sample](https://github.com/aws-samples/aws-sam-nested-stack-sample) repository.

## Epics
<a name="automate-deployment-of-nested-applications-using-aws-sam-epics"></a>

### Install AWS SAM CLI
<a name="install-aws-sam-cli"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Install AWS SAM CLI. | To install AWS SAM CLI, see the instructions in the [AWS SAM documentation](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-sam-cli-install.html). | DevOps engineer |
| Set up AWS credentials. | To set AWS credentials so that the AWS SAM CLI can make calls to AWS services on your behalf, run the `aws configure` command and follow the prompts.<pre>$aws configure<br />AWS Access Key ID [None]: <your_access_key_id><br />AWS Secret Access Key [None]: your_secret_access_key<br />Default region name [None]:<br />Default output format [None]:</pre><br />For more information on setting up your credentials, see [Authentication and access credentials](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-authentication.html).  | DevOps engineer |

### Initialize the AWS SAM project
<a name="initialize-the-aws-sam-project"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Clone the AWS SAM code repository. | 1. Clone the [aws sam nested stack sample ](https://github.com/aws-samples/aws-sam-nested-stack-sample)repository for this pattern by entering the following command.<pre>git clone https://github.com/aws-samples/aws-sam-nested-stack-sample.git</pre><br />2. Navigate into the cloned directory by entering the following command.<pre>cd aws-sam-nested-stack-sample</pre> | DevOps engineer |
| Deploy templates to initialize the project. | To initialize the project, run the `SAM init` command. When prompted to choose a template source, choose `Custom Template Location`. | DevOps engineer |

### Compile and build the SAM template code
<a name="compile-and-build-the-sam-template-code"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Review the AWS SAM application templates. | Review the templates for the nested applications. This example uses the following nested application templates:+ `auth.yaml` – This template sets up authentication-related resources, such as Amazon Cognito and AWS Systems Manager Parameter Store.<br />+ `product-mock.yaml` – This template deploys product-related resources, such as Lambda functions and Amazon API Gateway.<br />+ `shoppingcart-service.yaml` – This template sets up shopping cart–related resources, such as AWS Identity and Access Management (IAM), DynamoDB tables, and Lambda functions. | DevOps engineer |
| Review the parent template. | Review the template that will invoke the nested application templates. In this example, the parent template is `template.yml`. All separate applications are nested in the single parent template `template.yml`. | DevOps engineer |
| Compile and build the AWS SAM template code.  | Using the AWS SAM CLI, run the following command.<pre>sam build</pre> | DevOps engineer |

### Deploy the AWS SAM template
<a name="deploy-the-aws-sam-template"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Deploy the applications. | To launch the SAM template code that creates the nested application CloudFormation stacks and deploys code in the AWS environment, run the following command.<pre>sam deploy --guided --stack-name shopping-cart-nested-stack --capabilities CAPABILITY_IAM CAPABILITY_AUTO_EXPAND</pre><br />The command will prompt with a few questions. Answer all questions with `y`. | DevOps engineer |

### Verify the deployment
<a name="verify-the-deployment"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Verify the stacks. | To review the AWS CloudFormation stacks and AWS resources that were defined in the AWS SAM templates, do the following:1. Log in to the AWS Management Console, and navigate to the **CloudFormation** console.<br />2. Verify that the parent and child stacks are listed.<br />In this example, `sam-shopping-cart` is the parent stack that calls the nested Auth, Product and Shopping stacks.<br />The product stack gives the Product API Gateway URL link as an output. | DevOps engineer |

## Related resources
<a name="automate-deployment-of-nested-applications-using-aws-sam-resources"></a>

**References**
+ [AWS Serverless Application Model (AWS SAM)](https://aws.amazon.com/serverless/sam/#:~:text=The%20AWS%20Serverless%20Application%20Model,and%20model%20it%20using%20YAML.)
+ [AWS SAM on GitHub](https://github.com/aws/serverless-application-model)
+ [Serverless Shopping Cart Microservice](https://github.com/aws-samples/aws-serverless-shopping-cart) (AWS example application)

**Tutorials and videos **
+ [Build a Serverless App](https://youtu.be/Hv3YrP8G4ag)
+ [AWS Online Tech Talks: Serverless Application Building and Deployments with AWS SAM](https://youtu.be/1NU7vyJw9LU)

## Additional information
<a name="automate-deployment-of-nested-applications-using-aws-sam-additional"></a>

After all the code is in place, the example has the following directory structure:
+ [sam\_stacks](https://docs.aws.amazon.com/lambda/latest/dg/chapter-layers.html) – This folder contains the `shared.py` layer. A layer is a file archive that contains libraries, a custom runtime, or other dependencies. With layers, you can use libraries in your function without needing to include them in a deployment package.
+ *product-mock-service* – This folder contains all product-related Lambda functions and files.
+ *shopping-cart-service* – This folder contains all shopping-related Lambda functions and files.
