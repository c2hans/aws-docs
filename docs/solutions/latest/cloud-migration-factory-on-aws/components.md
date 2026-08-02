---
source_url: https://docs.aws.amazon.com/solutions/latest/cloud-migration-factory-on-aws/components.html
---

# Architecture details
<a name="components"></a>

## Migration automation server
<a name="comp-mes"></a>

This solution uses a migration automation server to run migrations using Rest APIs. This server isn’t automatically deployed with the solution and must be built manually. For more information, refer to [Build a Migration Automation Server](configure-migration-automation-server.md). We recommend that you build the server in your AWS environment, but you can also build on-premises in your network environment. The server must meet the following requirements:
+ Windows Server 2019 or later versions
+ Minimum 4 CPUs with 8 GB RAM
+ Deployed as a new virtual machine with no additional applications installed
+ (If built in AWS) In the same AWS account and Region as Cloud Migration Factory

Once installed, the server requires internet access and non-restrictive internal network connectivity to the in-scope source servers (servers to be migrated to AWS).

If port restriction is required from the migration automation server to the source servers, the following ports must be open from the migration automation server to the source servers:
+ SMB port (TCP 445)
+ SSH port (TCP 22)
+ WinRM port (TCP 5985, 5986)

We recommend that the migration automation server be in the same Active Directory domain as the source servers. If the source servers reside in multiple domains, the security configuration for the domain trust in each domain determines whether you need more than one migration automation server.

While the traditional approach uses a Windows-based automation server, scripts can now alternatively be executed directly through AWS Systems Manager Automation Document.
+ If domain trust exists in all the domains with source servers, a single migration automation server will be able to connect to and run automation scripts for all domains.
+ If a domain trust does not exist in all the domains, you must create an additional migration automation server for each untrusted domain, or for each action to be performed on the automation server alternative credentials will need to be provided with appropriate permissions on the source servers.

## Migration services Rest APIs
<a name="comp-mes-api"></a>

The Cloud Migration Factory on AWS solution automates the migration process using Rest APIs that are processed through AWS Lambda functions, an Amazon API Gateway, AWS Managed Services, and AWS Application Migration Service (AWS MGN). When you make a request or initiate a transaction, such as adding a server or viewing a list of servers or applications, Rest API calls are made to Amazon API Gateway which initiates an AWS Lambda function to run the request. The following services detail the components for the automated migration process.

### Log in services
<a name="comp2-log-in"></a>

Log in services include the `login` Lambda functions and Amazon Cognito. Once you log in to the solution using the `login` API via the API Gateway, the function validates the credentials, retrieves an authentication token from Amazon Cognito, and returns the token details back to you. You can use this authentication token to connect to the other services in this solution.

### Admin services
<a name="comp2-admin"></a>

Admin services include the Amazon API Gateway, `admin` Lambda functions, and Amazon DynamoDB. Administrators for the solution can use the `admin` Lambda function to define the migration metadata schema, which are the application and server attributes. The admin services API provides the schema definition for the DynamoDB table. User data including application and server attributes must adhere to this schema definition. Typical attributes include the `app_name`, `wave_id`, `server_name`, and other fields as identified in [Import migration metadata into the factory](test-solution-automation-scripts.md#import-migration-metadata-into-the-factory). By default, the AWS CloudFormation template deploys a common schema automatically, but this can be customized after deployment.

Administrators can also use admin services to define migration roles for the members of their migration team. The administrator has granular control to map specific user roles to specific attributes and migration stages. A migration stage is a period of time to run certain migration tasks, for example, a build stage, a testing stage, and a cutover stage.

### User services
<a name="comp2-user"></a>

User services include the Amazon API Gateway, `user` Lambda functions, and Amazon DynamoDB. Users can manage the migration metadata, allowing them to read, create, update, and delete the wave, application, and server data in the migration metadata pipeline.

**Note**
A migration wave is a concept of application grouping with a start and an end or cutover date. Wave data includes the migration candidate applications and application groupings scheduled for a particular migration wave.

User services offer an API for the migration team to manipulate the data in the solution: create, update, and delete the data using the Python script and source CSV files. For detailed steps, refer to Automated migration activities using Migration Factory web console and Automated migration activities using command prompt.

### Tools services
<a name="comp2-tools"></a>

Tool services upon deployment include the Amazon API Gateway, extensible `tools` Lambda functions, Amazon DynamoDB, AWS Managed Services, and AWS Application Migration Service. You can use these services to connect to third-party APIs and automate the migration process. On-deployment integration with AWS Application Migration Service can help a migration team to orchestrate the server launch process with a single button press to launch all servers in the same wave consisting of a group of applications and servers that have the same cutover date.

With the pipeline capability built into this solution, a migration team can compose complex migration sequences that contain many tasks, providing a fully managed and automated experience. The migration team can use tasks from the provided automation capabilities in the tools and AWS provided scripts, or write their own custom automation scripts.

## Migration Factory web interface
<a name="comp-webui"></a>

The solution includes a Migration Factory web interface which can be hosted, by default in an Amazon S3 bucket, or on a provided web server (not part of the solution deployment) which allows you to complete the following tasks using a web browser:
+ Update wave, application, and server metadata from your web browser
+ Manage application and server schema definitions
+ Create end-to-end migration pipelines to automate and manage all aspects of application migrations
+ Run automation scripts to automate migration activities such as check prerequisites, install MGN agents
+ Create migration credentials to connect to the source servers
+ Connect to AWS services such as AWS Application Migration Service and AWS Systems Manager to automate the migration process
