---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/serverless-cell-router-architecture.html
---

# Set up a serverless cell router for a cell-based architecture
<a name="serverless-cell-router-architecture"></a>

*Mian Tariq and Ioannis Lioupras, Amazon Web Services*

## Summary
<a name="serverless-cell-router-architecture-summary"></a>

As the entry point to a global cell-based application's system, the cell router is responsible for efficiently assigning users to the appropriate cells and providing the endpoints to the users. The cell router handles functions such as storing user-to-cell mappings, monitoring cell capacity, and requesting new cells when needed. It's important to maintain cell-router functionality during potential disruptions.

The cell-router design framework in this pattern focuses on resilience, scalability, and overall performance optimization. The pattern uses static routing, where clients cache endpoints upon initial login and communicate directly with cells. This decoupling enhances system resilience by helping to ensure uninterrupted functionality of the cell-based application during a cell-router impairment.

This pattern uses an AWS CloudFormation template to deploy the architecture. For details about what the template deploys, or to deploy the same configuration by using the AWS Management Console, see the [Additional information](#serverless-cell-router-architecture-additional) section.

**Important**
The demonstration, the code, and the CloudFormation template presented in this pattern are intended for explanatory purposes only. The material provided is solely for the purpose of illustrating the design pattern and aiding in comprehension. The demo and code are not production-ready and should not be used for any live production activities. Any attempt to use the code or demo in a production environment is strongly discouraged and is at your own risk. We recommend consulting with appropriate professionals and performing thorough testing before implementing this pattern or any of its components in a production setting.

## Prerequisites and limitations
<a name="serverless-cell-router-architecture-prereqs"></a>

**Prerequisites**
+ An active Amazon Web Services (AWS) account
+ The latest version of [AWS Command Line Interface (AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-welcome.html))
+ [AWS credentials](https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-files.html) with the necessary permissions to create the CloudFormation stack, AWS Lambda functions, and related resources

**Product versions**
+ Python 3.12

## Architecture
<a name="serverless-cell-router-architecture-architecture"></a>

The following diagram shows a high-level design of the cell router.

![The five-step process of the cell router.](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/images/pattern-img/fd2fbf9d-9ae4-4c27-bc32-cf117350137a/images/feb90b51-dd91-483b-b5a3-b0a5359686e3.png)

The diagram steps through the following workflow:

1. The user contacts Amazon API Gateway, which serves as the front for the cell-router API endpoints.

1. Amazon Cognito handles the authentication and authorization.

1. The AWS Step Functions workflow consists of the following components:
   + **Orchestrator** ‒ The `Orchestrator` uses AWS Step Functions to create a workflow, or state machine. The workflow is triggered by the cell router API. The `Orchestrator` executes Lambda functions based on the resource path.
   + **Dispatcher** ‒ The `Dispatcher` Lambda function identifies and assigns one static cell per registered new user. The function searches for the cell with the least number of users, assigns it to the user, and returns the endpoints.
   + **Mapper** ‒ The `Mapper` operation handles the user-to-cell mappings within the `RoutingDB` Amazon DynamoDB database that was created by the CloudFormation template. When triggered, the `Mapper` function provides the already assigned users with their endpoints.
   + **Scaler** ‒ The `Scaler` function keeps track of the cell occupancy and available capacity. When needed, the `Scaler` function can send a request through Amazon Simple Queue Service (Amazon SQS) to the Provision and Deploy layer to request new cells.
   + **Validator** ‒ The `Validator` function validates the cell endpoints and detects any potential issues.

1. The `RoutingDB` stores cell information and attributes (API endpoints, AWS Region, state, metrics).

1. When the available capacity of cells exceeds a threshold, the cell router requests provisioning and deployment services through Amazon SQS to create new cells.

When new cells are created, `RoutingDB` gets updated from the Provision and Deploy layer. However, that process is beyond the scope of this pattern. For an overview of cell-based architecture design premises and details about the cell-router design used in this pattern, see the [Additional information](#serverless-cell-router-architecture-additional) section.

## Tools
<a name="serverless-cell-router-architecture-tools"></a>

**AWS services**
+ [Amazon API Gateway](https://docs.aws.amazon.com/apigateway/latest/developerguide/welcome.html) helps you create, publish, maintain, monitor, and secure REST, HTTP, and WebSocket APIs at any scale.
+ [AWS CloudFormation](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html) helps you set up AWS resources, provision them quickly and consistently, and manage them throughout their lifecycle across AWS accounts and AWS Regions.
+ [Amazon Cognito](https://docs.aws.amazon.com/cognito/latest/developerguide/what-is-amazon-cognito.html) provides authentication, authorization, and user management for web and mobile apps.
+ [Amazon DynamoDB](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/Introduction.html) is a fully managed NoSQL database service that provides fast, predictable, and scalable performance.
+ [AWS Lambda](https://docs.aws.amazon.com/lambda/latest/dg/welcome.html) is a compute service that helps you run code without needing to provision or manage servers. It runs your code only when needed and scales automatically, so you pay only for the compute time that you use.
+ [Amazon Simple Storage Service (Amazon S3)](https://docs.aws.amazon.com/AmazonS3/latest/userguide/Welcome.html) is a cloud-based object storage service that helps you store, protect, and retrieve any amount of data.
+ [Amazon Simple Queue Service (Amazon SQS)](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/welcome.html) provides a secure, durable, and available hosted queue that helps you integrate and decouple distributed software systems and components.
+ [AWS Step Functions](https://docs.aws.amazon.com/step-functions/latest/dg/welcome.html) is a serverless orchestration service that helps you combine Lambda functions and other AWS services to build business-critical applications.

**Other tools**
+ [Python](https://www.python.org/) is a general-purpose computer programming language.

**Code repository**

The code for this pattern is available in the GitHub [Serverless-Cell-Router](https://github.com/aws-samples/Serverless-Cell-Router/) repository.

## Best practices
<a name="serverless-cell-router-architecture-best-practices"></a>

For best practices when building cell-based architectures, see the following AWS Well-Architected guidance:
+ [Reducing the Scope of Impact with Cell-Based Architecture](https://docs.aws.amazon.com/wellarchitected/latest/reducing-scope-of-impact-with-cell-based-architecture/reducing-scope-of-impact-with-cell-based-architecture.html)
+ [AWS Well-Architected Framework Reliability Pillar: REL10-BP04 Use bulkhead architectures to limit scope of impact](https://docs.aws.amazon.com/wellarchitected/latest/reliability-pillar/rel_fault_isolation_use_bulkhead.html)

## Epics
<a name="serverless-cell-router-architecture-epics"></a>

### Prepare source files
<a name="prepare-source-files"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Clone the example code repository. | To clone the Serverless-Cell-Router GitHub repository to your computer, use the following command:<pre>git clone https://github.com/aws-samples/Serverless-Cell-Router/</pre> | Developer |
| Set up AWS CLI temporary credentials. | Configure the AWS CLI with credentials for your AWS account. This walkthrough uses temporary credentials provided by the AWS IAM Identity Center **Command line or programmatic access** option. This sets the `AWS_ACCESS_KEY_ID`, `AWS_SECRET_ACCESS_KEY`, and `AWS_SESSION_TOKEN` AWS environment variables with the appropriate credentials for use with the AWS CLI. | Developer |
| Create an S3 bucket. | Create an S3 bucket that will be used to store and access the Serverless-Cell-Router Lambda functions for deployment by the CloudFormation template. To create the S3 bucket, use following command: <pre>aws s3api create-bucket --bucket <bucket name> --region eu-central-1 --create-bucket-configuration LocationConstraint=eu-central-1</pre> | Developer |
| Create .zip files. | Create one .zip file for each Lambda function located in the [Functions](https://github.com/aws-samples/Serverless-Cell-Router/tree/main/Functions) directory. These .zip files will be used to deploy the Lambda functions. On a Mac, use the following `zip` commands:<pre>zip -j mapper-scr.zip Functions/Mapper.py<br />zip -j dispatcher-scr.zip Functions/Dispatcher.py<br />zip -j scaler-scr.zip Functions/Scaler.py<br />zip -j cp validator-scr.zip Functions/Validator.py<br />zip -j dynamodbDummyData-scr.zip Functions/DynamodbDummyData.py</pre> | Developer |
| Copy the .zip files to the S3 bucket. | To copy all the Lambda function .zip files to the S3 bucket, use the following commands:<pre>aws s3 cp mapper-scr.zip s3://<bucket name><br />aws s3 cp dispatcher-scr.zip s3://<bucket name><br />aws s3 cp scaler-scr.zip s3://<bucket name><br />aws s3 cp validator-scr.zip s3://<bucket name><br />aws s3 cp dynamodbDummyData-scr.zip s3://<bucket name></pre> | Developer |

### Create the CloudFormation stack
<a name="create-the-cfn-stack"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Deploy the CloudFormation template. | To deploy the CloudFormation template, run the following AWS CLI command:<pre>aws cloudformation create-stack --stack-name serverless.cell-router \<br />--template-body file://Serverless-Cell-Router-Stack-v10.yaml \<br />--capabilities CAPABILITY_IAM \<br />--parameters ParameterKey=LambdaFunctionMapperS3KeyParameterSCR,ParameterValue=mapper-scr.zip \<br />ParameterKey=LambdaFunctionDispatcherS3KeyParameterSCR,ParameterValue=dispatcher-scr.zip \<br />ParameterKey=LambdaFunctionScalerS3KeyParameterSCR,ParameterValue=scaler-scr.zip \<br />ParameterKey=LambdaFunctionAddDynamoDBDummyItemsS3KeyParameterSCR,ParameterValue=dynamodbDummyData-scr.zip \<br />ParameterKey=LambdaFunctionsS3BucketParameterSCR,ParameterValue=<S3 bucket storing lambda zip files> \<br />ParameterKey=CognitoDomain,ParameterValue=<Cognito Domain Name> \<br />--region <enter your aws region id, e.g. "eu-central-1"></pre> | Developer |
| Check progress. | Sign in to the AWS Management Console, open the CloudFormation console at  [https://console.aws.amazon.com/cloudformation/](), and check the progress of stack development. When the status is `CREATE_COMPLETE`, the stack has been deployed successfully. | Developer |

### Assess and verify
<a name="assess-and-verify"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Assign cells to the user. | To initiate the `Orchestrator`, run the following curl command:<pre>curl -X POST \<br />-H "Authorization: Bearer {User id_token}" \<br />https://xxxxxx.execute-api.eu-central-1.amazonaws.com/Cell_Router_Development/cells</pre><br />The `Orchestrator` triggers the execution of the `Dispatcher` function. The `Dispatcher`, in turn, verifies the existence of the user. If the user is found, the `Dispatcher` returns the associated cell ID and endpoint URLs. If the user isn't found, the `Dispatcher` allocates a cell to the user and sends the cell ID to the `Scaler` function for assessment of the assigned cell's residual capacity.<br />The `Scaler` function's response is the following:<br />`"cellID : cell-0002 , endPoint_1 : https://xxxxx.execute-api.eu-north-1.amazonaws.com/ , endPoint_2 : https://xxxxxxx.execute-api.eu-central-1.amazonaws.com/"` | Developer |
| Retrieve user cells. | To use the `Orchestrator` to execute the `Mapper` function, run the following command:<pre>curl -X POST \<br />-H "Authorization: Bearer {User id_token}" \<br />https://xxxxxxxxx.execute-api.eu-central-1.amazonaws.com/Cell_Router_Development/mapper</pre><br />The `Orchestrator` searches for the cell assigned to the user and returns the cell ID and URLs in the following response:<br />`"cellID : cell-0002 , endPoint_1 : https://xxxxx.execute-api.eu-north-1.amazonaws.com/ , endPoint_2 : https://xxxxxxx.execute-api.eu-central-1.amazonaws.com/"` | Developer |

### Clean up
<a name="clean-up"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Clean up the resources. | To avoid incurring additional charges in your account, do the following:1. [Empty the S3 bucket](https://docs.aws.amazon.com/AmazonS3/latest/userguide/empty-bucket.html) that you created for the Lambda functions.<br />2. Delete the bucket.<br />3. Delete the CloudFormation stack. | App developer |

## Related resources
<a name="serverless-cell-router-architecture-resources"></a>

**References**
+ [Static stability using Availability Zones](https://aws.amazon.com/builders-library/static-stability-using-availability-zones/)
+ [AWS Fault Isolation Boundaries: Static stability](https://docs.aws.amazon.com/whitepapers/latest/aws-fault-isolation-boundaries/static-stability.html)

**Video**

[Physalia: Cell-based Architecture to Provide Higher Availability on Amazon EBS](https://www.youtube.com/watch?v=6IknqRZMFic)

[https://www.youtube-nocookie.com/embed/6IknqRZMFic?controls=0](https://www.youtube-nocookie.com/embed/6IknqRZMFic?controls=0)

## Additional information
<a name="serverless-cell-router-architecture-additional"></a>

**Cell-based architecture design premises**

Although this pattern focuses on the cell router, it's important to understand the whole environment. The environment is structured into three discrete layers:
+ The Routing layer, or Thin layer, which contains the cell router
+ The Cell layer, comprising various cells
+ The Provision and Deploy Layer, which provisions cells and deploys the application

Each layer sustains functionality even in the event of impairments affecting other layers. AWS accounts serve as a fault isolation boundary.

The following diagram shows the layers at a high level. The Cell layer and the Provision and Deploy layer are outside the scope of this pattern.

![The Routing layer, the Cell layer with multiple cell accounts, and the Provision and Deploy layer.](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/images/pattern-img/fd2fbf9d-9ae4-4c27-bc32-cf117350137a/images/137ac34d-43c3-42b6-95de-a365ff611ce8.png)

For more information about cell-based architecture, see [Reducing the Scope of Impact with Cell-Based Architecture: Cell routing](https://docs.aws.amazon.com/wellarchitected/latest/reducing-scope-of-impact-with-cell-based-architecture/cell-routing.html).

**Cell-router design pattern**

The cell router is a shared component across cells. To mitigate potential impacts, it's important for the Routing layer to use a simplistic and horizontally scalable design that's as thin as possible. Serving as the system’s entry point, the Routing layer consists of only the components that are required to efficiently assign users to the appropriate cells. Components within this layer don't engage in the management or creation of cells.

This pattern uses static routing, which means that the client caches the endpoints at the initial login and subsequently establishes direct communication with the cell. Periodic interactions between the client and the cell router are initiated to confirm the current status or retrieve any updates. This intentional decoupling enables uninterrupted operations for existing users in the event of cell-router downtime, and it provides continued functionality and resilience within the system.

In this pattern, the cell router supports the following functionalities:
+ Retrieving cell data from the cell database in the Provision and Deploy layer and storing or updating the local database.
+ Assigning a cell to each new registered user of the application by using the cell assignment algorithm.
+ Storing the user-to-cells mapping in the local database.
+ Checking the capacity of the cells during user assignment and raising an event for the vending machine to the Provision and Deploy layer to create cells.
+ Using the cell creation criteria algorithm to provide this functionality.
+ Responding to the newly registered user requests by providing the URLs of the static cells. These URLs will be cached on the client with a time to live (TTL).
+ Responding to the existing user requests of an invalid URL by providing a new or updated URL.

To further understand the demonstration cell router that is set up by the CloudFormation template, review the following components and steps:

1. Set up and configure the Amazon Cognito user pool.

1. Set up and configure the API Gateway API for the cell router.

1. Create a DynamoDB table.

1. Create and configure an SQS queue.

1. Implement the `Orchestrator`.

1. Implement the Lambda functions: `Dispatcher`, `Scaler`, `Mapper`, `Validator`.

1. Asses and verify.

The presupposition is that the Provision and Deploy layer is already established. Its implementation details fall beyond the scope of this artifact.

Because these components are set up and configured by an CloudFormation template, the following steps are presented at a descriptive and high level. The assumption is that you have the required AWS skills to complete the setup and configuration.

*1. Setup and configure the Amazon Cognito user pool*

Sign in to the AWS Management Console, and open the Amazon Cognito console at [https://console.aws.amazon.com/cognito/](). Set up and configure an Amazon Cognito user pool named `CellRouterPool`, with app integration, hosted UI, and the necessary permissions.

*2. Set up and configure the API Gateway API for the cell router*

Open the API Gateway console at [https://console.aws.amazon.com/apigateway/](). Set up and configure an API named `CellRouter`, using an Amazon Cognito authorizer integrated with the Amazon Cognito user pool `CellRouterPool`. Implement the following elements:
+ `CellRouter` API resources, including `POST` methods
+ Integration with the Step Functions workflow implemented in step 5
+ Authorization through the Amazon Cognito authorizer
+ Integration request and response mappings
+ Allocation of necessary permissions

*3. Create a DynamoDB table*

Open the DynamoDB console at [https://console.aws.amazon.com/dynamodb/](), and create a standard DynamoDB table called `tbl_router` with the following configuration:
+ **Partition key** ‒ `marketId`
+ **Sort key** ‒ `cellId`
+ **Capacity mode** ‒ Provisioned
+ **Point-in-time recovery (PITR)** ‒ Off

On the **Indexes** tab, create a global secondary index called `marketId-currentCapacity-index`. The `Scaler` Lambda function will use the index to conduct efficient searches for the cell with the lowest number of assigned users.

Create the table structure with the following attributes:
+ `marketId` ‒ Europe
+ `cellId` ‒ cell-0002
+ `currentCapacity` ‒ 2
+ `endPoint_1` ‒ <your endpoint for the first Region>
+ `endPoint_2` ‒ <your endpoint for the second Region>
+ `IsHealthy` ‒ True
+ `maxCapacity` ‒ 10
+ `regionCode_1` ‒ `eu-north-1`
+ `regionCode_2` ‒ `eu-central-1`
+ `userIds` ‒ <your email address>

*4. Create and configure an SQS queue*

Open the Amazon SQS console at [https://console.aws.amazon.com/sqs/](), and create a standard SQS queue called `CellProvisioning` configured with **Amazon SQS key** encryption.

*5. Implement the Orchestrator*

Develop a Step Functions workflow to serve as the `Orchestrator` for the router. The workflow is callable through the cell router API. The workflow executes the designated Lambda functions based on the resource path. Integrate the step function with the API Gateway API for the cell router `CellRouter`, and configure the necessary permissions to invoke the Lambda functions.

The following diagram shows the workflow. The choice state invokes one of the Lambda functions. If the Lambda function is successful, the workflow ends. If the Lambda function fails, fail state is called.

![A diagram of the workflow with the four functions and ending in a fail state.](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/images/pattern-img/fd2fbf9d-9ae4-4c27-bc32-cf117350137a/images/cfe8d029-6f30-49a1-aaad-cad503bdcbae.png)

*6. Implement the Lambda functions*

Implement the `Dispatcher`, `Mapper`, `Scaler`, and `Validator` functions. When you set up and configure each function in the demonstration, define a role for the function and assign the necessary permissions for performing required operations on the DynamoDB table `tbl_router`. Additionally, integrate each function into the workflow `Orchestrator`.

*Dispatcher function*

The `Dispatcher` function is responsible for identifying and assigning a single static cell for each new registered user. When a new user registers with the global application, the request goes to the `Dispatcher` function. The function processes the request by using predefined evaluation criteria such as the following:

1. **Region** ‒ Select the cell in the market where the user is located. For example, if the user is accessing the global application from Europe, select a cell that uses AWS Regions in Europe.

1. **Proximity or latency** ‒ Select the cell closest to the user For example, if the user is accessing the application from Holland, the function considers a cell that uses Frankfurt and Ireland. The decision regarding which cell is closest is based on metrics such as latency between the user's location and the cell Regions. For this example pattern, the information is statically fed from the Provision and Deploy layer.

1. **Health** ‒ The `Dispatcher` function checks whether the selected cell is healthy based on the provided cell state (Healthy = true or false).

1. **Capacity** ‒ The user distribution is based on *least number of users in a cell* logic, so the user is assigned to the cell that has least number of users.

**Note**
These criteria are presented to explain this example pattern only. For a real-life cell-router implementation, you can define more refined and use case‒based criteria.

The `Orchestrator` invokes the Dispatcher function to assign users to cells. In this demo function, the market value is a static parameter defined as `europe`.

The `Dispatcher` function assesses whether a cell is already assigned to the user. If the cell is already assigned, the `Dispatcher` function returns the cell's endpoints. If no cell is assigned to the user, the function searches for the cell with the least number of users, assigns it to the user, and returns the endpoints. The efficiency of the cell search query is optimized by using the global secondary index.

*Mapper function*

The `Mapper` function oversees the storage and maintenance of user-to-cell mappings in the database. A singular cell is allocated to each registered user. Each cell has two distinct URLs—one for each AWS Region. Serving as API endpoints hosted on API Gateway, these URLs function as inbound points to the global application.

When the `Mapper` function receives a request from the client application, it runs a query on the DynamoDB table `tbl_router` to retrieve the user-to-cell mapping that is associated with the provided email ID. If it finds an assigned cell, the `Mapper` function promptly provides the cell's two URLs. The `Mapper` function also actively monitors alterations to the cell URLs, and it initiates notifications or updates to user settings.

*Scaler function*

The `Scaler` function manages the residual capacity of the cell. For each new user-registration request, the `Scaler` function assesses the available capacity of the cell that the `Dispatcher` function assigned to the user. If the cell has reached its predetermined limit according to the specified evaluation criteria, the function initiates a request through an Amazon SQS queue to the Provision and Deploy layer, soliciting the provisioning and deployment of new cells. The scaling of cells can be executed based on a set of evaluation criteria such as the following:

1. **Maximum users** ‒ Each cell can have 500 maximum number of users.

1. **Buffer capacity** ‒ The buffer capacity of each cell is 20 percent, which  means that each cell can be assigned to 400 users at any time. The remaining 20 percent buffer capacity is reserved for future use cases and handling of unexpected scenarios (for example, when cell creation and provisioning services are unavailable).

1. **Cell creation** ‒ As soon as an existing cell reaches 70 percent of capacity, a request is triggered to create an additional cell.

**Note**
These criteria are presented to explain this example pattern only. For a real-life cell-router implementation, you can define more refined and use case‒based criteria.

The demonstration `Scaler` code is executed by the `Orchestrator` after the `Dispatcher` successfully assigns a cell to the newly registered user. The `Scaler`, upon receipt of the cell ID from the `Dispatcher`, evaluates whether the designated cell has adequate capacity to accommodate additional users, based on predefined evaluation criteria. If the cell's capacity is insufficient, the `Scaler` function dispatches a message to the Amazon SQS service. This message is retrieved by the service within the Provision and Deploy layer, initiating the provisioning of a new cell.

**Validator function**

The `Validator` function identifies and resolves issues pertaining to cell access. When a user signs in to the global application, the application retrieves the cell's URLs from the user profile settings and routes user requests to one of the two assigned Regions within the cell. If the URLs are inaccessible, the application can dispatch a validate URL request to the cell router. The cell-router `Orchestrator` invokes the `Validator`. The `Validator` initiates the validation process. Validation might include, among other checks, the following:
+ Cross-referencing cell URLs in the request with URLs stored in database to identify and process potential updates
+ Running a deep health check (for example, an `HTTP GET` request to the cell's endpoint)

In conclusion, the `Validator` function delivers responses to client application requests, furnishing validation status along with any required remediation steps.

The `Validator` is designed to enhance user experience. Consider a scenario where certain users encounter difficulty accessing the global application because an incident causes cells to be temporarily unavailable. Instead of presenting generic errors, the `Validator` function can provide instructive remediation steps. These steps might include the following actions:
+ Inform users about the incident.
+ Provide an approximate wait time before service availability.
+ Provide a support contact number for obtaining additional information.

The demo code for the `Validator` function verifies that the user-supplied cell URLs in the request match the records stored in the `tbl_router` table. The `Validator` function also checks whether the cells are healthy.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
