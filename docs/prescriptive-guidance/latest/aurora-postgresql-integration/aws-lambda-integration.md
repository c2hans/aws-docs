---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/aurora-postgresql-integration/aws-lambda-integration.html
---

# Aurora PostgreSQL-Compatible integration with Lambda
<a name="aws-lambda-integration"></a>

AWS Lambda is a serverless computing service for running code without provisioning or managing servers. By integrating Lambda with Amazon Aurora PostgreSQL-Compatible Edition, you can build event-driven architectures and extend the functionality of your Aurora PostgreSQL-Compatible database.

## Lambda integration use cases
<a name="lambda-use-cases"></a>

Common use cases for integrating Aurora PostgreSQL-Compatible with Lambda include the following:
+ **Data processing and transformation** ‒ Offload complex data processing tasks from Aurora PostgreSQL-Compatible to Lambda functions. Scenarios can be data cleansing, data enrichment, data validation, and complex calculations.
+ **Event-driven workflows** ‒ Use Lambda functions to trigger actions or workflows based on events or changes in Aurora PostgreSQL-Compatible. Scenarios include sending notifications, triggering ETL processes, or invoking other AWS services when data is inserted, updated, or deleted in Aurora PostgreSQL-Compatible.
+ **Real-time analytics and reporting** ‒ Use Lambda functions to perform real-time analytics or generate reports based on data stored in Aurora PostgreSQL-Compatible. Lambda functions can query Aurora PostgreSQL-Compatible, process the data, and generate reports or visualizations on-demand or based on a schedule.
+ **Serverless APIs and microservices** ‒ Use Lambda functions to build serverless APIs or microservices that interact with Aurora PostgreSQL-Compatible. Lambda functions can handle API requests, query or modify data in Aurora PostgreSQL-Compatible, and return the response.
+ **Asynchronous processing** ‒ Offload long-running or asynchronous tasks from Aurora PostgreSQL-Compatible to Lambda functions. Scenarios include sending email messages, generating reports, or processing large datasets without blocking the main application or database. Long-running tasks must be within the Lambda 15-minute time limit.

To set up integration between Aurora PostgreSQL-Compatible and Lambda, follow the instructions in the [AWS documentation](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/PostgreSQL-Lambda.html).
