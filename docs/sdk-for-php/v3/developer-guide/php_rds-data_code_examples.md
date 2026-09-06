---
source_url: https://docs.aws.amazon.com/sdk-for-php/v3/developer-guide/php_rds-data_code_examples.html
---

# Amazon RDS Data Service examples using SDK for PHP
<a name="php_rds-data_code_examples"></a>

The following code examples show you how to perform actions and implement common scenarios by using the AWS SDK for PHP with Amazon RDS Data Service.

*Scenarios* are code examples that show you how to accomplish specific tasks by calling multiple functions within a service or combined with other AWS services.

Each example includes a link to the complete source code, where you can find instructions on how to set up and run the code in context.

**Topics**
+ [Scenarios](#scenarios)

## Scenarios
<a name="scenarios"></a>

### Create an Aurora Serverless work item tracker
<a name="cross_RDSDataTracker_php_topic"></a>

The following code example shows how to create a web application that tracks work items in an Amazon Aurora Serverless database and uses Amazon Simple Email Service (Amazon SES) to send reports.

**SDK for PHP**
 Shows how to use the AWS SDK for PHP to create a web application that tracks work items in an Amazon RDS database and emails reports by using Amazon Simple Email Service (Amazon SES). This example uses a front end built with React.js to interact with a RESTful PHP backend.
+ Integrate a React.js web application with AWS services.
+ List, add, update, and delete items in an Amazon RDS table.
+ Send an email report of filtered work items using Amazon SES.
+ Deploy and manage example resources with the included AWS CloudFormation script.
 For complete source code and instructions on how to set up and run, see the full example on [GitHub](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/php/cross_service/aurora_item_tracker).

**Services used in this example**
+ Aurora
+ Amazon RDS
+ Amazon RDS Data Service
+ Amazon SES
