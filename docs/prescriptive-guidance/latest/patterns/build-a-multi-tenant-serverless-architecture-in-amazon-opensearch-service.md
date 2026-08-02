---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/build-a-multi-tenant-serverless-architecture-in-amazon-opensearch-service.html
---

# Build a multi-tenant serverless architecture in Amazon OpenSearch Service
<a name="build-a-multi-tenant-serverless-architecture-in-amazon-opensearch-service"></a>

*Tabby Ward and Nisha Gambhir, Amazon Web Services*

## Summary
<a name="build-a-multi-tenant-serverless-architecture-in-amazon-opensearch-service-summary"></a>

Amazon OpenSearch Service is a managed service that makes it easy to deploy, operate, and scale Elasticsearch, which is a popular open-source search and analytics engine. OpenSearch Service provides free-text search as well as near real-time ingestion and dashboarding for streaming data such as logs and metrics.

Software as a service (SaaS) providers frequently use OpenSearch Service to address a broad range of use cases, such as gaining customer insights in a scalable and secure way while reducing complexity and downtime.

Using OpenSearch Service in a multi-tenant environment introduces a series of considerations that affect partitioning, isolation, deployment, and management of your SaaS solution. SaaS providers have to consider how to effectively scale their Elasticsearch clusters with continually shifting workloads. They also need to consider how tiering and noisy neighbor conditions could impact their partitioning model.

This pattern reviews the models that are used to represent and isolate tenant data with Elasticsearch constructs. In addition, the pattern focuses on a simple serverless reference architecture as an example to demonstrate indexing and searching using OpenSearch Service in a multi-tenant environment. It implements the pool data partitioning model, which shares the same index among all tenants while maintaining a tenant's data isolation. This pattern uses the following AWS services: Amazon API Gateway, AWS Lambda, Amazon Simple Storage Service (Amazon S3), and OpenSearch Service.

For more information about the pool model and other data partitioning models, see the [Additional information](#build-a-multi-tenant-serverless-architecture-in-amazon-opensearch-service-additional) section.

## Prerequisites and limitations
<a name="build-a-multi-tenant-serverless-architecture-in-amazon-opensearch-service-prereqs"></a>

**Prerequisites**
+ An active AWS account
+ [AWS Command Line Interface (AWS CLI) version 2.x](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html), installed and configured on macOS, Linux, or Windows
+ [Python version 3.9](https://www.python.org/downloads/release/python-3921/)
+ [pip3](https://pip.pypa.io/en/stable/) – The Python source code is provided as a .zip file to be deployed in a Lambda function. If you want to use the code locally or customize it, follow these steps to develop and recompile the source code:

  1. Generate the `requirements.txt` file by running the the following command in the same directory as the Python scripts: `pip3 freeze > requirements.txt`

  1. Install the dependencies: `pip3 install -r requirements.txt`

**Limitations**
+ This code runs in Python, and doesn’t currently support other programming languages.
+ The sample application doesn’t include AWS cross-Region or disaster recovery (DR) support.
+ This pattern is intended for demonstration purposes only. It is not intended to be used in a production environment.

## Architecture
<a name="build-a-multi-tenant-serverless-architecture-in-amazon-opensearch-service-architecture"></a>

The following diagram illustrates the high-level architecture of this pattern. The architecture includes the following:
+ Lambda to index and query the content
+ OpenSearch Service to perform search
+ API Gateway to provide an API interaction with the user
+ Amazon S3 to store raw (non-indexed) data
+ Amazon CloudWatch to monitor logs
+ AWS Identity and Access Management (IAM) to create tenant roles and policies

![High-level multi-tenant serverless architecture.](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/images/pattern-img/750196bb-03f6-4b6e-92cd-eb7141602547/images/1a8501e7-0776-4aca-aed3-28e3ada1d15d.png)

**Automation and scale**

For simplicity, the pattern uses AWS CLI to provision the infrastructure and to deploy the sample code. You can create an CloudFormation template or AWS Cloud Development Kit (AWS CDK) scripts to automate the pattern.

## Tools
<a name="build-a-multi-tenant-serverless-architecture-in-amazon-opensearch-service-tools"></a>

**AWS services**
+ [AWS CLI](https://aws.amazon.com/cli/) is a unified tool for managing AWS services and resources by using commands in your command-line shell.
+ [Lambda](https://aws.amazon.com/lambda/) is a compute service that lets you run code without provisioning or managing servers. Lambda runs your code only when needed and scales automatically, from a few requests per day to thousands per second.
+ [API Gateway](https://aws.amazon.com/api-gateway/) is an AWS service for creating, publishing, maintaining, monitoring, and securing REST, HTTP, and WebSocket APIs at any scale.
+ [Amazon S3](https://aws.amazon.com/s3/) is an object storage service that lets you store and retrieve any amount of information at any time, from anywhere on the web.
+ [OpenSearch Service](https://aws.amazon.com/opensearch-service/) is a fully managed service that makes it easy for you to deploy, secure, and run Elasticsearch cost-effectively at scale.

**Code**

The attachment provides sample files for this pattern. These include:
+ `index_lambda_package.zip` – The Lambda function for indexing data in OpenSearch Service by using the pool model.
+ `search_lambda_package.zip` – The Lambda function for searching for data in OpenSearch Service.
+ `Tenant-1-data` – Sample raw (non-indexed) data for Tenant-1.
+ `Tenant-2-data` – Sample raw (non-indexed) data for Tenant-2.

**Important**
The stories in this pattern include AWS CLI command examples that are formatted for Unix, Linux, and macOS. For Windows, replace the backslash (\\) Unix continuation character at the end of each line with a caret (^).

**Note**
In AWS CLI commands, replace all values within the angle brackets (<>) with correct values.

## Epics
<a name="build-a-multi-tenant-serverless-architecture-in-amazon-opensearch-service-epics"></a>

### Create and configure an S3 bucket
<a name="create-and-configure-an-s3-bucket"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Create an S3 bucket. | Create an S3 bucket in your AWS Region. This bucket will hold the non-indexed tenant data for the sample application. Make sure that the S3 bucket's name is globally unique, because the namespace is shared by all AWS accounts.<br />To create an S3 bucket, you can use the AWS CLI [create-bucket](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3api/create-bucket.html) command as follows:<pre>aws s3api create-bucket \<br />  --bucket <tenantrawdata> \<br />  --region <your-AWS-Region></pre><br />where `tenantrawdata` is the S3 bucket name. (You can use any unique name that follows [the bucket naming guidelines](https://docs.aws.amazon.com/AmazonS3/latest/userguide/bucketnamingrules.html).) | Cloud architect, Cloud administrator |

### Create and configure an Elasticsearch cluster
<a name="create-and-configure-an-elasticsearch-cluster"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Create an OpenSearch Service domain. | Run the AWS CLI [create-elasticsearch-domain](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/es/create-elasticsearch-domain.html) command to create an OpenSearch Service domain:<pre>aws es create-elasticsearch-domain \<br />  --domain-name vpc-cli-example \<br />  --elasticsearch-version 7.10 \<br />  --elasticsearch-cluster-config InstanceType=t3.medium.elasticsearch,InstanceCount=1 \<br />  --ebs-options EBSEnabled=true,VolumeType=gp2,VolumeSize=10 \<br />  --domain-endpoint-options "{\"EnforceHTTPS\": true}" \<br />  --encryption-at-rest-options "{\"Enabled\": true}" \<br />  --node-to-node-encryption-options "{\"Enabled\": true}" \<br />  --advanced-security-options "{\"Enabled\": true, \"InternalUserDatabaseEnabled\": true, \<br />    \"MasterUserOptions\": {\"MasterUserName\": \"KibanaUser\", \<br />    \"MasterUserPassword\": \"NewKibanaPassword@123\"}}" \<br />  --vpc-options "{\"SubnetIds\": [\"<subnet-id>\"], \"SecurityGroupIds\": [\"<sg-id>\"]}" \<br />  --access-policies "{\"Version\": \"2012-10-17\", \"Statement\": [ { \"Effect\": \"Allow\", \ <br />    \"Principal\": {\"AWS\": \"*\" }, \"Action\":\"es:*\", \<br />    \"Resource\": \"arn:aws:es:<region>:<account-id>:domain\/vpc-cli-example\/*\" } ] }"</pre><br />The instance count is set to 1 because the domain is for testing purposes. You need to enable fine-grained access control by using the `advanced-security-options` parameter, because the details cannot be changed after the domain has been created. <br />This command creates a master user name (`KibanaUser`) and a password that you can use to log in to the Kibana console.<br />Because the domain is part of a virtual private cloud (VPC), you have to make sure that you can reach the Elasticsearch instance by specifying the access policy to use.<br />For more information, see [Launching your Amazon OpenSearch Service domains within a VPC](https://docs.aws.amazon.com/elasticsearch-service/latest/developerguide/es-vpc.html) in the AWS documentation. | Cloud architect, Cloud administrator |
| Set up a bastion host. | Set up a Amazon Elastic Compute Cloud (Amazon EC2) Windows instance as a bastion host to access the Kibana console. The Elasticsearch security group must allow traffic from the Amazon EC2 security group. For instructions, see the blog post [Controlling Network Access to EC2 Instances Using a Bastion Server](https://aws.amazon.com/blogs/security/controlling-network-access-to-ec2-instances-using-a-bastion-server/).<br />When the bastion host has been set up, and you have the security group that is associated with the instance available, use the AWS CLI [authorize-security-group-ingress](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/authorize-security-group-ingress.html) command to add permission to the Elasticsearch security group to allow port 443 from the Amazon EC2 (bastion host) security group.<pre>aws ec2 authorize-security-group-ingress \<br />  --group-id <SecurityGroupIdfElasticSearch> \ <br />  --protocol tcp \<br />  --port 443 \<br />  --source-group <SecurityGroupIdfBashionHostEC2></pre> | Cloud architect, Cloud administrator |

### Create and configure the Lambda index function
<a name="create-and-configure-the-lam-index-function"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Create the Lambda execution role. | Run the AWS CLI [create-role](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/create-role.html) command to grant the Lambda index function access to AWS services and resources:<pre>aws iam create-role \<br />  --role-name index-lambda-role \<br />  --assume-role-policy-document file://lambda_assume_role.json</pre><br />where `lambda_assume_role.json` is a JSON document that grants `AssumeRole` permissions to the Lambda function, as follows:<pre>{<br />     "Version": "2012-10-17",		 	 	 <br />     "Statement": [<br />         {<br />             "Effect": "Allow",<br />             "Principal": {<br />                 "Service": "lambda.amazonaws.com"<br />               },<br />             "Action": "sts:AssumeRole"<br />         }<br />     ]<br /> }</pre> | Cloud architect, Cloud administrator |
| Attach managed policies to the Lambda role. | Run the AWS CLI [attach-role-policy](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/attach-role-policy.html) command to attach managed policies to the role created in the previous step. These two policies give the role permissions to create an elastic network interface and to write logs to CloudWatch Logs.<pre>aws iam attach-role-policy \<br />  --role-name index-lambda-role \<br />  --policy-arn arn:aws:iam::aws:policy/service-role/AWSLambdaBasicExecutionRole<br /><br />aws iam attach-role-policy \<br />  --role-name index-lambda-role \<br />  --policy-arn arn:aws:iam::aws:policy/service-role/AWSLambdaVPCAccessExecutionRole </pre> | Cloud architect, Cloud administrator |
| Create a policy to give the Lambda index function permission to read the S3 objects. | Run the AWS CLI [create-policy](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/create-policy.html) command to to give the Lambda index function `s3:GetObject` permission to read the objects in the S3 bucket:<pre>aws iam create-policy \<br />  --policy-name s3-permission-policy \<br />  --policy-document file://s3-policy.json</pre><br />The file `s3-policy.json` is a JSON document shown below that grants `s3:GetObject` permissions to allow read access to S3 objects. If you used a different name when you created the S3 bucket, provide the correct bucket name in the `Resource `section:<pre>{<br />    "Version": "2012-10-17",		 	 	 <br />    "Statement": [<br />        {<br />           "Effect": "Allow",<br />           "Action": "s3:GetObject",<br />           "Resource": "arn:aws:s3:::<tenantrawdata>/*"<br />        }<br />    ]<br />}</pre> | Cloud architect, Cloud administrator |
| Attach the Amazon S3 permission policy to the Lambda execution role. | Run the AWS CLI [attach-role-policy](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/attach-role-policy.html) command to attach the Amazon S3 permission policy you created in the previous step to the Lambda execution role:<pre>aws iam attach-role-policy \<br />  --role-name index-lambda-role \<br />  --policy-arn <PolicyARN></pre><br />where `PolicyARN` is the Amazon Resource Name (ARN) of the Amazon S3 permission policy. You can get this value from the output of the previous command. | Cloud architect, Cloud administrator |
| Create the Lambda index function. | Run the AWS CLI [create-function](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lambda/create-function.html) command to create the Lambda index function, which will access OpenSearch Service:<pre>aws lambda create-function \<br />  --function-name index-lambda-function \<br />  --zip-file fileb://index_lambda_package.zip \<br />  --handler lambda_index.lambda_handler \<br />  --runtime python3.9 \<br />  --role "arn:aws:iam::account-id:role/index-lambda-role" \<br />  --timeout 30 \<br />  --vpc-config "{\"SubnetIds\": [\"<subnet-id1\>", \"<subnet-id2>\"], \<br />    \"SecurityGroupIds\": [\"<sg-1>\"]}"</pre> | Cloud architect, Cloud administrator |
| Allow Amazon S3 to call the Lambda index function. | Run the AWS CLI [add-permission](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lambda/add-permission.html) command to give Amazon S3 the permission to call the Lambda index function:<pre>aws lambda add-permission \<br />  --function-name index-lambda-function \<br />  --statement-id s3-permissions \<br />  --action lambda:InvokeFunction \<br />  --principal s3.amazonaws.com \<br />  --source-arn "arn:aws:s3:::<tenantrawdata>" \<br />  --source-account "<account-id>" </pre> | Cloud architect, Cloud administrator |
| Add a Lambda trigger for the Amazon S3 event. | Run the AWS CLI [put-bucket-notification-configuration](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3api/put-bucket-notification-configuration.html) command to send  notifications to the Lambda index function when the Amazon S3 `ObjectCreated` event is detected. The index function runs whenever an object is uploaded to the S3 bucket. <pre>aws s3api put-bucket-notification-configuration \<br />  --bucket <tenantrawdata> \<br />  --notification-configuration file://s3-trigger.json</pre><br />The file `s3-trigger.json` is a JSON document in the current folder that adds the resource policy to the Lambda function when the Amazon S3 `ObjectCreated` event occurs. | Cloud architect, Cloud administrator |

### Create and configure the Lambda search function
<a name="create-and-configure-the-lam-search-function"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Create the Lambda execution role. | Run the AWS CLI [create-role](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/create-role.html) command to grant the Lambda search function access to AWS services and resources:<pre>aws iam create-role \<br />  --role-name search-lambda-role \<br />  --assume-role-policy-document file://lambda_assume_role.json</pre><br />where `lambda_assume_role.json` is a JSON document in the current folder that grants `AssumeRole` permissions to the Lambda function, as follows:<pre>{<br />     "Version": "2012-10-17",		 	 	 <br />     "Statement": [<br />         {<br />             "Effect": "Allow",<br />             "Principal": {<br />                 "Service": "lambda.amazonaws.com"<br />               },<br />             "Action": "sts:AssumeRole"<br />         }<br />     ]<br /> }</pre> | Cloud architect, Cloud administrator |
| Attach managed policies to the Lambda role. | Run the AWS CLI [attach-role-policy](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/attach-role-policy.html) command to attach managed policies to the role created in the previous step. These two policies give the role permissions to create an elastic network interface and to write logs to CloudWatch Logs.<pre>aws iam attach-role-policy \<br />  --role-name search-lambda-role \<br />  --policy-arn arn:aws:iam::aws:policy/service-role/AWSLambdaBasicExecutionRole<br /><br />aws iam attach-role-policy \<br />  --role-name search-lambda-role \<br />  --policy-arn arn:aws:iam::aws:policy/service-role/AWSLambdaVPCAccessExecutionRole </pre> | Cloud architect, Cloud administrator |
| Create the Lambda search function. | Run the AWS CLI [create-function](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lambda/create-function.html) command to create the Lambda search function, which will access OpenSearch Service:<pre>aws lambda create-function \<br />  --function-name search-lambda-function \<br />  --zip-file fileb://search_lambda_package.zip \<br />  --handler lambda_search.lambda_handler \<br />  --runtime python3.9 \<br />  --role "arn:aws:iam::account-id:role/search-lambda-role" \<br />  --timeout 30 \<br />  --vpc-config "{\"SubnetIds\": [\"<subnet-id1\>", \"<subnet-id2>\"], \<br />    \"SecurityGroupIds\": [\"<sg-1>\"]}"</pre> | Cloud architect, Cloud administrator |

### Create and configure tenant roles
<a name="create-and-configure-tenant-roles"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Create tenant IAM roles. | Run the AWS CLI [create-role](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/create-role.html) command to create two tenant roles that will be used to test the search functionality:<pre>aws iam create-role \<br />  --role-name Tenant-1-role \<br />  --assume-role-policy-document file://assume-role-policy.json</pre><pre>aws iam create-role \<br />  --role-name Tenant-2-role \<br />  --assume-role-policy-document file://assume-role-policy.json</pre><br />The file `assume-role-policy.json` is a JSON document in the current folder that grants `AssumeRole` permissions to the Lambda execution role:<pre>{<br />    "Version": "2012-10-17",		 	 	 <br />    "Statement": [<br />        {<br />            "Effect": "Allow",<br />            "Principal": {<br />                 "AWS": "<Lambda execution role for index function>",<br />                 "AWS": "<Lambda execution role for search function>"<br />             },<br />            "Action": "sts:AssumeRole"<br />        }<br />    ]<br />}</pre> | Cloud architect, Cloud administrator |
| Create a tenant IAM policy. | Run the AWS CLI [create-policy](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/create-policy.html) command to create a tenant policy that grants access to Elasticsearch operations:<pre>aws iam create-policy \<br />  --policy-name tenant-policy \<br />  --policy-document file://policy.json</pre><br />The file `policy.json` is a JSON document in the current folder that grants permissions on Elasticsearch:<pre>{<br />    "Version": "2012-10-17",		 	 	 <br />    "Statement": [<br />        {<br />            "Effect": "Allow",<br />            "Action": [<br />                "es:ESHttpDelete",<br />                "es:ESHttpGet",<br />                "es:ESHttpHead",<br />                "es:ESHttpPost",<br />                "es:ESHttpPut",<br />                "es:ESHttpPatch"<br />            ],<br />            "Resource": [<br />                "<ARN of Elasticsearch domain created earlier>"<br />            ]<br />        }<br />    ]<br />}</pre> | Cloud architect, Cloud administrator |
| Attach the tenant IAM policy to the tenant roles. | Run the AWS CLI [attach-role-policy](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/attach-role-policy.html) command to attach the tenant IAM policy to the two tenant roles you created in the earlier step:<pre>aws iam attach-role-policy \<br />  --policy-arn arn:aws:iam::account-id:policy/tenant-policy \<br />  --role-name Tenant-1-role<br /><br />aws iam attach-role-policy \<br />  --policy-arn arn:aws:iam::account-id:policy/tenant-policy \<br />  --role-name Tenant-2-role</pre><br />The policy ARN is from the output of the previous step. | Cloud architect, Cloud administrator |
| Create an IAM policy to give Lambda permissions to assume role. | Run the AWS CLI [create-policy](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/create-policy.html) command to create a policy for Lambda to assume the tenant role:<pre>aws iam create-policy \<br />  --policy-name assume-tenant-role-policy \<br />  --policy-document file://lambda_policy.json</pre><br />The file `lambda_policy.json` is a JSON document in the current folder that grants permissions to `AssumeRole`:<pre>{<br />    "Version": "2012-10-17",		 	 	 <br />    "Statement": [<br />       {<br />            "Effect": "Allow",<br />            "Action":  "sts:AssumeRole",<br />            "Resource": "<ARN of tenant role created earlier>"<br />       }<br />    ]<br />}</pre><br />For `Resource`, you can use a wildcard character to avoid creating a new policy for each tenant. | Cloud architect, Cloud administrator |
| Create an IAM policy to give the Lambda index role permission to access Amazon S3. | Run the AWS CLI [create-policy](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/create-policy.html) command to give the Lambda index role permission to access the objects in the S3 bucket:<pre>aws iam create-policy \<br />  --policy-name s3-permission-policy \<br />  --policy-document file://s3_lambda_policy.json</pre><br />The file `s3_lambda_policy.json` is the following JSON policy document in the current folder:<pre>{<br />    "Version": "2012-10-17",		 	 	 <br />    "Statement": [<br />        {<br />            "Effect": "Allow",<br />            "Action": "s3:GetObject",<br />            "Resource": "arn:aws:s3:::tenantrawdata/*"<br />        }<br />    ]<br />}</pre> | Cloud architect, Cloud administrator |
| Attach the policy to the Lambda execution role. | Run the AWS CLI [attach-role-policy](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/attach-role-policy.html) command to attach the policy created in the previous step to the Lambda index and search execution roles you created earlier:<pre>aws iam attach-role-policy \<br />  --policy-arn arn:aws:iam::account-id:policy/assume-tenant-role-policy \<br />  --role-name index-lambda-role<br /><br />aws iam attach-role-policy \<br />  --policy-arn arn:aws:iam::account-id:policy/assume-tenant-role-policy \<br />  --role-name search-lambda-role<br /><br />aws iam attach-role-policy \<br />  --policy-arn arn:aws:iam::account-id:policy/s3-permission-policy \<br />  --role-name index-lambda-role</pre><br />The policy ARN is from the output of the previous step. | Cloud architect, Cloud administrator |

### Create and configure a search API
<a name="create-and-configure-a-search-api"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Create a REST API in API Gateway. | Run the AWS CLI [create-rest-api](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/apigateway/create-rest-api.html) command to create a REST API resource:<pre>aws apigateway create-rest-api \<br />  --name Test-Api \<br />  --endpoint-configuration "{ \"types\": [\"REGIONAL\"] }"</pre><br />For the endpoint configuration type, you can specify `EDGE` instead of `REGIONAL` to use edge locations instead of a particular AWS Region.<br />Note the value of the `id` field from the command output. This is the API ID that you will use in subsequent commands. | Cloud architect, Cloud administrator |
| Create a resource for the search API. | The search API resource starts the Lambda search function with the resource name `search`. (You don’t have to create an API for the Lambda index function, because it runs automatically when objects are uploaded to the S3 bucket.)[See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/build-a-multi-tenant-serverless-architecture-in-amazon-opensearch-service.html) | Cloud architect, Cloud administrator |
| Create a GET method for the search API. | Run the AWS CLI [put-method](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/apigateway/put-method.html) command to create a `GET `method for the search API:<pre>aws apigateway put-method \<br />  --rest-api-id <API-ID> \<br />  --resource-id <ID from the previous command output> \<br />  --http-method GET \<br />  --authorization-type "NONE" \<br />  --no-api-key-required</pre><br />For `resource-id`, specify the ID from the output of the `create-resource` command. | Cloud architect, Cloud administrator |
| Create a method response for the search API. | Run the AWS CLI [put-method-response](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/apigateway/put-method-response.html) command to add a method response for the search API:<pre>aws apigateway put-method-response \<br />  --rest-api-id <API-ID> \<br />  --resource-id  <ID from the create-resource command output> \<br />  --http-method GET \<br />  --status-code 200 \<br />  --response-models "{\"application/json\": \"Empty\"}"</pre><br />For `resource-id`, specify the ID from the output of the earlier `create-resource` command. | Cloud architect, Cloud administrator |
| Set up a proxy Lambda integration for the search API. | Run the AWS CLI [put-integration](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/apigateway/put-integration.html) command to set up an integration with the Lambda search function:<pre>aws apigateway put-integration \<br />  --rest-api-id <API-ID> \<br />  --resource-id  <ID from the create-resource command output> \<br />  --http-method GET \<br />  --type AWS_PROXY \<br />  --integration-http-method GET \<br />  --uri arn:aws:apigateway:region:lambda:path/2015-03-31/functions/arn:aws:lambda:<region>:<account-id>:function:<function-name>/invocations</pre><br />For `resource-id`, specify the ID from the earlier `create-resource` command. | Cloud architect, Cloud administrator |
| Grant API Gateway permission to call the Lambda search function. | Run the AWS CLI [add-permission](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lambda/add-permission.html) command to give API Gateway permission to use the search function:<pre>aws lambda add-permission \<br />  --function-name <function-name> \<br />  --statement-id apigateway-get \<br />  --action lambda:InvokeFunction \<br />  --principal apigateway.amazonaws.com \<br />  --source-arn "arn:aws:execute-api:<region>:<account-id>:api-id/*/GET/search</pre><br />Change the `source-arn` path if you used a different API resource name instead of `search`. | Cloud architect, Cloud administrator |
| Deploy the search API. | Run the AWS CLI [create-deployment](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/apigateway/create-deployment.html) command to create a stage resource named `dev`:<pre>aws apigateway create-deployment \<br />  --rest-api-id <API-ID> \<br />  --stage-name dev</pre><br />If you update the API, you can use the same AWS CLI command to redeploy it to the same stage. | Cloud architect, Cloud administrator |

### Create and configure Kibana roles
<a name="create-and-configure-kibana-roles"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Log in to the Kibana console. | [See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/build-a-multi-tenant-serverless-architecture-in-amazon-opensearch-service.html) | Cloud architect, Cloud administrator |
| Create and configure Kibana roles. | To provide data isolation and to make sure that one tenant cannot retrieve the data of another tenant, you need to use document security, which allows tenants to access only documents that contain their tenant ID.[See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/build-a-multi-tenant-serverless-architecture-in-amazon-opensearch-service.html) | Cloud architect, Cloud administrator |
| Map users to roles. | [See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/build-a-multi-tenant-serverless-architecture-in-amazon-opensearch-service.html)We recommend that you automate the creation of the tenant and Kibana roles at the time of tenant onboarding. | Cloud architect, Cloud administrator |
| Create the tenant-data index. | In the navigation pane, under **Management**, choose **Dev Tools**, and then run the following command. This command creates the `tenant-data` index to define the mapping for the `TenantId` property.<pre>PUT /tenant-data<br />{<br />  "mappings": {<br />    "properties": {<br />      "TenantId": { "type": "keyword"}<br />    }<br />  }<br />}</pre> | Cloud architect, Cloud administrator |

### Create VPC endpoints for Amazon S3 and AWS STS
<a name="create-vpc-endpoints-for-s3-and-sts"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Create a VPC endpoint for Amazon S3. | Run the AWS CLI [create-vpc-endpoint](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/create-vpc-endpoint.html) command to create a VPC endpoint for Amazon S3. The endpoint enables the Lambda index function in the VPC to access Amazon S3.<pre>aws ec2 create-vpc-endpoint \<br />  --vpc-id <VPC-ID> \<br />  --service-name com.amazonaws.us-east-1.s3 \<br />  --route-table-ids <route-table-ID></pre><br />For `vpc-id`, specify the VPC that you’re using for the Lambda index function. For `service-name`, use the correct URL for the Amazon S3 endpoint. For `route-table-ids`, specify the route table that’s associated with the VPC endpoint. | Cloud architect, Cloud administrator |
| Create a VPC endpoint for AWS STS. | Run the AWS CLI [create-vpc-endpoint](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/create-vpc-endpoint.html) command to create a VPC endpoint for AWS Security Token Service (AWS STS). The endpoint enables the Lambda index and search functions in the VPC to access AWS STS. The functions use AWS STS when they assume the IAM role.<pre>aws ec2 create-vpc-endpoint \<br />  --vpc-id <VPC-ID> \<br />  --vpc-endpoint-type Interface \<br />  --service-name com.amazonaws.us-east-1.sts \<br />  --subnet-id <subnet-ID> \<br />  --security-group-id <security-group-ID></pre><br />For `vpc-id`, specify the VPC that you’re using for the Lambda index and search functions. For `subnet-id`, provide the subnet in which this endpoint should be created. For `security-group-id`, specify the security group to associate this endpoint with. (It could be the same as the security group Lambda uses.) | Cloud architect, Cloud administrator |

### Test multi-tenancy and data isolation
<a name="test-multi-tenancy-and-data-isolation"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Update the Python files for the index and search functions. | [See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/build-a-multi-tenant-serverless-architecture-in-amazon-opensearch-service.html)You can get the Elasticsearch endpoint from the **Overview **tab of the OpenSearch Service console. It has the format `<AWS-Region>.es.amazonaws.com`. | Cloud architect, App developer |
| Update the Lambda code. | Use the AWS CLI [update-function-code](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lambda/update-function-code.html) command to update the Lambda code with the changes you made to the Python files:<pre>aws lambda update-function-code \<br />  --function-name index-lambda-function \<br />  --zip-file fileb://index_lambda_package.zip<br /><br />aws lambda update-function-code \<br />  --function-name search-lambda-function \<br />  --zip-file fileb://search_lambda_package.zip</pre> | Cloud architect, App developer |
| Upload raw data to the S3 bucket. | Use the AWS CLI [cp](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3/cp.html) command to upload data for the Tenant-1 and Tenant-2 objects to the `tenantrawdata` bucket (specify the name of the S3 bucket you created for this purpose):<pre>aws s3 cp tenant-1-data s3://tenantrawdata<br />aws s3 cp tenant-2-data s3://tenantrawdata</pre><br />The S3 bucket is set up to run the Lambda index function whenever data is uploaded so that the document is indexed in Elasticsearch. | Cloud architect, Cloud administrator |
| Search data from the Kibana console. | On the Kibana console, run the following query:<pre>GET tenant-data/_search</pre><br />This query displays all the documents indexed in Elasticsearch. In this case, you should see two separate documents for Tenant-1 and Tenant-2. | Cloud architect, Cloud administrator |
| Test the search API from API Gateway. | [See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/build-a-multi-tenant-serverless-architecture-in-amazon-opensearch-service.html)For screen illustrations, see the [Additional information](#build-a-multi-tenant-serverless-architecture-in-amazon-opensearch-service-additional) section. | Cloud architect, App developer |
| Clean up resources. | Clean up all the resources you created to prevent additional charges to your account. | AWS DevOps, Cloud architect, Cloud administrator |

## Related resources
<a name="build-a-multi-tenant-serverless-architecture-in-amazon-opensearch-service-resources"></a>
+ [AWS SDK for Python (Boto)](https://aws.amazon.com/sdk-for-python/)
+ [AWS Lambda documentation](https://docs.aws.amazon.com/lambda/)
+ [API Gateway documentation](https://docs.aws.amazon.com/apigateway/)
+ [Amazon S3 documentation](https://docs.aws.amazon.com/s3/)
+ [Amazon OpenSearch Service documentation](https://docs.aws.amazon.com/elasticsearch-service/)
  + [Fine-grained access control in Amazon OpenSearch Service](https://docs.amazonaws.cn/en_us/elasticsearch-service/latest/developerguide/fgac.html)
  + [Creating a search application with Amazon OpenSearch Service](https://docs.aws.amazon.com/elasticsearch-service/latest/developerguide/search-example.html)
  + [Launching your Amazon OpenSearch Service domains within a VPC](https://docs.aws.amazon.com/elasticsearch-service/latest/developerguide/es-vpc.html)

## Additional information
<a name="build-a-multi-tenant-serverless-architecture-in-amazon-opensearch-service-additional"></a>

**Data partitioning models**

There are three common data partitioning models used in multi-tenant systems: silo, pool, and hybrid. The model you choose depends on the compliance, noisy neighbor, operations, and isolation needs of your environment.

*Silo model*

In the silo model, each tenant’s data is stored in a distinct storage area where there is no commingling of tenant data. You can use two approaches to implement the silo model with OpenSearch Service: domain per tenant and index per tenant.
+ **Domain per tenant** – You can use a separate OpenSearch Service domain (synonymous with an Elasticsearch cluster) per tenant. Placing each tenant in its own domain provides all the benefits associated with having data in a standalone construct. However, this approach introduces management and agility challenges. Its distributed nature makes it harder to aggregate and assess the operational health and activity of tenants. This is a costly option that requires each OpenSearch Service domain to have three master nodes and two data nodes for production workloads at the minimum.

![Domain per tenant silo model for multi-tenant serverless architectures.](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/images/pattern-img/750196bb-03f6-4b6e-92cd-eb7141602547/images/c2195f82-e5ed-40bb-b76a-3b0210bf1254.png)

+ **Index per tenant** – You can place tenant data in separate indexes within an OpenSearch Service cluster. With this approach, you use a tenant identifier when you create and name the index, by prepending the tenant identifier to the index name. The index per tenant approach helps you achieve your silo goals without introducing a completely separate cluster for each tenant. However, you might encounter memory pressure if the number of indexes grows, because this approach requires more shards, and the master node has to handle more allocation and rebalancing.

![Index per tenant silo model for multi-tenant serverless architectures.](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/images/pattern-img/750196bb-03f6-4b6e-92cd-eb7141602547/images/354a9463-25bb-422b-84de-d4875a7c8ea2.png)

**Isolation in the silo model** – In the silo model, you use IAM policies to isolate the domains or indexes that hold each tenant’s data. These policies prevent one tenant from accessing another tenant’s data. To implement your silo isolation model, you can create a resource-based policy that controls access to your tenant resource. This is often a domain access policy that specifies which actions a principal can perform on the domain’s sub-resources, including Elasticsearch indexes and APIs. With IAM identity-based polices, you can specify *allowed* or *denied* actions on the domain, indexes, or APIs within OpenSearch Service. The `Action` element of an IAM policy describes the specific action or actions that are allowed or denied by the policy, and the `Principal `element specifies the affected accounts, users, or roles.

The following sample policy grants Tenant-1 full access (as specified by `es:*`) to the sub-resources on the `tenant-1` domain only. The trailing `/*` in the `Resource` element indicates that this policy applies to the domain’s sub-resources, not to the domain itself. When this policy is in effect, tenants are not allowed to create a new domain or modify settings on an existing domain.

```
{
   "Version": "2012-10-17",
   "Statement": [
      {
         "Effect": "Allow",
         "Principal": {
            "AWS": "arn:aws:iam::<aws-account-id>:user/Tenant-1"
         },
         "Action": "es:*",
         "Resource": "arn:aws:es:<Region>:<account-id>:domain/tenant-1/*"
      }
   ]
}
```

To implement the tenant per index silo model, you would need to modify this sample policy to further restrict Tenant-1 to the specified index or indexes, by specifying the index name. The following sample policy restricts Tenant-1 to the `tenant-index-1` index.

```
{
   "Version": "2012-10-17",
   "Statement": [
      {
         "Effect": "Allow",
         "Principal": {
            "AWS": "arn:aws:iam::123456789012:user/Tenant-1"
         },
         "Action": "es:*",
         "Resource": "arn:aws:es:<Region>:<account-id>:domain/test-domain/tenant-index-1/*"
      }
   ]
}
```

*Pool model*

In the pool model, all tenant data is stored in an index within the same domain. The tenant identifier is included in the data (document) and used as the partition key, so you can determine which data belongs to which tenant. This model reduces the management overhead. Operating and managing the pooled index is easier and more efficient than managing multiple indexes. However, because tenant data is commingled within the same index, you lose the natural tenant isolation that the silo model provides. This approach might also degrade performance because of the noisy neighbor effect.

![Pool model for multi-tenant serverless architectures.](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/images/pattern-img/750196bb-03f6-4b6e-92cd-eb7141602547/images/c2c3bb0f-6ccd-47a7-ab67-e7f3f8c7f289.png)

**Tenant isolation in the pool model** – In general, tenant isolation is challenging to implement in the pool model. The IAM mechanism used with the silo model doesn’t allow you to describe isolation based on the tenant ID stored in your document.

An alternative approach is to use the [fine-grained access control](https://docs.aws.amazon.com/elasticsearch-service/latest/developerguide/fgac.html) (FGAC) support provided by the Open Distro for Elasticsearch. FGAC allows you to control permissions at an index, document, or field level. With each request, FGAC evaluates the user credentials and either authenticates the user or denies access. If FGAC authenticates the user, it fetches all roles mapped to that user and uses the complete set of permissions to determine how to handle the request.

To achieve the required isolation in the pooled model, you can use [document-level security](https://opendistro.github.io/for-elasticsearch-docs/docs/security/access-control/document-level-security/), which lets you restrict a role to a subset of documents in an index. The following sample role restricts queries to Tenant-1. By applying this role to Tenant-1, you can achieve the necessary isolation.

```
{
   "bool": {
     "must": {
       "match": {
         "tenantId": "Tenant-1"
       }
     }
   }
 }
```

*Hybrid model*

The hybrid model uses a combination of the silo and pool models in the same environment to offer unique experiences to each tenant tier (such as free, standard, and premium tiers). Each tier follows the same security profile that was used in the pool model.

![Hybrid model for multi-tenant serverless architectures.](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/images/pattern-img/750196bb-03f6-4b6e-92cd-eb7141602547/images/e7def98a-38ef-435a-9881-7e95ae4d4940.png)

**Tenant isolation in the hybrid model** – In the hybrid model, you follow the same security profile as in the pool model, where using the FGAC security model at the document level provided tenant isolation. Although this strategy simplifies cluster management and offers agility, it complicates other aspects of the architecture. For example, your code requires additional complexity to determine which model is associated with each tenant. You also have to ensure that single-tenant queries don’t saturate the entire domain and degrade the experience for other tenants.

**Testing in API Gateway**

*Test window for Tenant-1 query*

![Test window for Tenant-1 query.](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/images/pattern-img/750196bb-03f6-4b6e-92cd-eb7141602547/images/a6757d3f-977a-4ecc-90cb-83ab7f1c3588.png)

*Test window for Tenant-2 query*

![Test window for Tenant-2 query.](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/images/pattern-img/750196bb-03f6-4b6e-92cd-eb7141602547/images/31bfd656-33ca-4750-b6e6-da4d703c2071.png)

## Attachments
<a name="attachments-750196bb-03f6-4b6e-92cd-eb7141602547"></a>

To access additional content that is associated with this document, download and unzip the following file: [attachment.zip](samples/p-attach/750196bb-03f6-4b6e-92cd-eb7141602547/attachments/attachment.zip)
