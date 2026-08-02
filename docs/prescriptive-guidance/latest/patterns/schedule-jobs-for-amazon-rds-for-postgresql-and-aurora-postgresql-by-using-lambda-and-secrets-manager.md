---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/schedule-jobs-for-amazon-rds-for-postgresql-and-aurora-postgresql-by-using-lambda-and-secrets-manager.html
---

# Schedule jobs for Amazon RDS for PostgreSQL and Aurora PostgreSQL by using Lambda and Secrets Manager
<a name="schedule-jobs-for-amazon-rds-for-postgresql-and-aurora-postgresql-by-using-lambda-and-secrets-manager"></a>

*Yaser Raja, Amazon Web Services*

## Summary
<a name="schedule-jobs-for-amazon-rds-for-postgresql-and-aurora-postgresql-by-using-lambda-and-secrets-manager-summary"></a>

For on-premises databases and databases that are hosted on Amazon Elastic Compute Cloud (Amazon EC2) instances, database administrators often use the **cron** utility to schedule jobs.

For example, a job for data extraction or a job for data purging can easily be scheduled using **cron**. For these jobs, database credentials are typically either hard-coded or stored in a properties file. However, when you migrate to Amazon Relational Database Service (Amazon RDS) or Amazon Aurora PostgreSQL-Compatible Edition, you lose the ability to log in to the host instance to schedule **cron** jobs.

This pattern describes how to use AWS Lambda and AWS Secrets Manager to schedule jobs for Amazon RDS for PostgreSQL and Aurora PostgreSQL-Compatible databases after migration.

## Prerequisites and limitations
<a name="schedule-jobs-for-amazon-rds-for-postgresql-and-aurora-postgresql-by-using-lambda-and-secrets-manager-prereqs"></a>

**Prerequisites**
+ An active AWS account
+ An Amazon RDS for PostgreSQL or Aurora PostgreSQL-Compatible database

**Limitations**
+ A job must complete within 15 minutes, which is the Lambda function timeout limit. For other limits, see the [AWS Lambda documentation](https://docs.aws.amazon.com/lambda/latest/dg/limits.html).
+ Job code must be written in a [language supported by Lambda](https://docs.aws.amazon.com/lambda/latest/dg/lambda-runtimes.html).

## Architecture
<a name="schedule-jobs-for-amazon-rds-for-postgresql-and-aurora-postgresql-by-using-lambda-and-secrets-manager-architecture"></a>

**Source technology stack**

This stack features jobs written in languages such as Bash, Python, and Java. Database credentials are stored in the properties file, and the job is scheduled using Linux **cron**.

**Target technology stack**

This stack has a Lambda function that uses the credentials stored in Secrets Manager to connect to the database and to perform the activity. The Lambda function is initiated at the scheduled interval by using Amazon CloudWatch Events.

**Target architecture**

![CloudWatch event starting a Lambda function that schedules jobs for the RDS DB instance.](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/images/pattern-img/8e0d1c90-0599-4909-a800-26a89b87f686/images/61f9ca34-9157-4565-96ba-5234d389ac2a.png)

## Tools
<a name="schedule-jobs-for-amazon-rds-for-postgresql-and-aurora-postgresql-by-using-lambda-and-secrets-manager-tools"></a>
+ [Amazon CloudWatch Events](https://docs.aws.amazon.com/AmazonCloudWatch/latest/events/WhatIsCloudWatchEvents.html) delivers a near real-time stream of system events that describe changes in AWS resources. Using simple rules that you can quickly set up, you can match events and route them to one or more target functions or streams. CloudWatch Events becomes aware of operational changes as they occur. It responds to these operational changes and takes corrective action as necessary, by sending messages to respond to the environment, activating functions, making changes, and capturing state information. You can also use CloudWatch Events to schedule automated actions that self-initiate at certain times using **cron** or **rate** expressions.
+ [AWS Lambda](https://docs.aws.amazon.com/lambda/latest/dg/welcome.html) is a compute service that lets you run code without provisioning or managing servers. Lambda runs your code only when needed and scales automatically, from a few requests per day to thousands per second. You pay only for the compute time you consume; there is no charge when your code is not running. With Lambda, you can run code for virtually any type of application or backend service with zero administration. Lambda runs your code on a high-availability compute infrastructure and manages all the compute resources, including server and operating system maintenance, capacity provisioning and automatic scaling, code monitoring, and logging. All you need to do is provide your code in one of the [languages that Lambda supports](https://docs.aws.amazon.com/lambda/latest/dg/lambda-runtimes.html).
+ [AWS Secrets Manager](https://docs.aws.amazon.com/secretsmanager/latest/userguide/intro.html) helps you protect secrets for accessing your applications, services, and IT resources. You can easily rotate, manage, and retrieve database credentials, API keys, and other secrets throughout their lifecycle. Users and applications retrieve secrets by calling Secrets Manager APIs, which eliminates the need to hard-code sensitive information in plain text. Secrets Manager offers secret rotation with built-in integration for Amazon RDS, Amazon Redshift, and Amazon DocumentDB. The service is extensible to other types of secrets, including API keys and OAuth tokens. Secrets Manager enables you to control access to secrets using fine-grained permissions and to audit secret rotation centrally for resources in the AWS Cloud, third-party services, and on premises.

## Epics
<a name="schedule-jobs-for-amazon-rds-for-postgresql-and-aurora-postgresql-by-using-lambda-and-secrets-manager-epics"></a>

### Store database credentials in Secrets Manager
<a name="store-database-credentials-in-asm"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Create a database user for the Lambda function. | It is a good practice to use separate database users for different parts of your application. If a separate database user already exists for your cron jobs, use that. Otherwise, create a new database user. For more information, see [Managing PostgreSQL users and roles](https://aws.amazon.com/blogs/database/managing-postgresql-users-and-roles/) (AWS blog post). | DBA |
| Store database credentials as a secret in Secrets Manager. | Follow the instructions in [Create a database secret](https://docs.aws.amazon.com/secretsmanager/latest/userguide/create_database_secret.html) (Secrets Manager documentation). | DBA, DevOps |

### Author the code for the Lambda function
<a name="author-the-code-for-the-lam-function"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Choose a programming language supported by Lambda. | For a list of supported languages, see [Lambda runtimes](https://docs.aws.amazon.com/lambda/latest/dg/lambda-runtimes.html) (Lambda documentation). | Developer |
| Write the logic to fetch the database credentials from Secrets Manager. | For sample code, see [How to securely provide database credentials to Lambda functions by using AWS Secrets Manager](https://aws.amazon.com/blogs/security/how-to-securely-provide-database-credentials-to-lambda-functions-by-using-aws-secrets-manager/) (AWS blog post). | Developer |
| Write the logic to perform the scheduled database activity. | Migrate your existing code for the scheduling job that you're using on premises to the Lambda function. For more information, see [Deploying Lambda functions](https://docs.aws.amazon.com/lambda/latest/dg/lambda-deploy-functions.html) (Lambda documentation). | Developer |

### Deploy the code and create the Lambda function
<a name="deploy-the-code-and-create-the-lam-function"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Create the Lambda function deployment package. | This package contains the code and its dependencies. For more information, see [Deployment packages](https://docs.aws.amazon.com/lambda/latest/dg/gettingstarted-package.html) (Lambda documentation). | Developer |
| Create the Lambda function. | In the Lambda console, choose **Create function**, enter a function name, choose the runtime environment, and then choose **Create function**. | DevOps |
| Upload the deployment package. | Choose the Lambda function you created to open its configuration. You can write your code directly in the code section or upload your deployment package. To upload your package, go to the **Function code** section, choose the **Code entry type** to upload a .zip file, and then select the package. | DevOps |
| Configure the Lambda function per your requirements. | For example, you can set the **Timeout** parameter to the duration you expect your Lambda function to take. For more information, see [Configuring function options](https://docs.aws.amazon.com/lambda/latest/dg/configuration-function-common.html) (Lambda documentation). | DevOps |
| Set permissions for the Lambda function role to access Secrets Manager. | For instructions, see [Use secrets in AWS Lambda functions](https://docs.aws.amazon.com/secretsmanager/latest/userguide/retrieving-secrets_lambda.html) (Secrets Manager documentation). | DevOps |
| Test the Lambda function. | Initiate the Lambda function manually to make sure it works as expected. | DevOps |

### Schedule the Lambda function by using CloudWatch Events
<a name="schedule-the-lam-function-by-using-cwe"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Create a rule to run your Lambda function on a schedule. | Schedule the Lambda function by using CloudWatch Events. For instructions, see [Schedule Lambda functions using CloudWatch Events](https://docs.aws.amazon.com/AmazonCloudWatch/latest/events/RunLambdaSchedule.html) (CloudWatch Events tutorial). | DevOps |

## Related resources
<a name="schedule-jobs-for-amazon-rds-for-postgresql-and-aurora-postgresql-by-using-lambda-and-secrets-manager-resources"></a>
+ [AWS Secrets Manager](https://docs.aws.amazon.com/secretsmanager/latest/userguide/intro.html)
+ [Getting started with Lambda](https://docs.aws.amazon.com/lambda/latest/dg/getting-started.html)
+ [Creating a CloudWatch Events Rule That Triggers on an Event](https://docs.aws.amazon.com/AmazonCloudWatch/latest/events/Create-CloudWatch-Events-Rule.html)
+ [AWS Lambda Limits](https://docs.aws.amazon.com/lambda/latest/dg/limits.html)
+ [Query your AWS database from your serverless application](https://aws.amazon.com/blogs/database/query-your-aws-database-from-your-serverless-application/) (blog post)
