---
source_url: https://docs.aws.amazon.com/code-library/latest/ug/dynamodb_example_cross_DynamoDBDataTracker_section.html
---

There are more AWS SDK examples available in the [AWS Doc SDK Examples](https://github.com/awsdocs/aws-doc-sdk-examples) GitHub repo.

# Create a web application to track DynamoDB data
<a name="dynamodb_example_cross_DynamoDBDataTracker_section"></a>

The following code examples show how to create a web application that tracks work items in an Amazon DynamoDB table and uses Amazon Simple Email Service (Amazon SES) to send reports.

------
#### [ .NET ]

**SDK for .NET**
 Shows how to use the Amazon DynamoDB .NET API to create a dynamic web application that tracks DynamoDB work data.
 For complete source code and instructions on how to set up and run, see the full example on [GitHub](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/dotnetv3/cross-service/DynamoDbItemTracker).

**Services used in this example**
+ DynamoDB
+ Amazon SES

------
#### [ Java ]

**SDK for Java 2.x**
 Shows how to use the Amazon DynamoDB API to create a dynamic web application that tracks DynamoDB work data.
 For complete source code and instructions on how to set up and run, see the full example on [GitHub](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/javav2/usecases/creating_dynamodb_web_app).

**Services used in this example**
+ DynamoDB
+ Amazon SES

------
#### [ Kotlin ]

**SDK for Kotlin**
 Shows how to use the Amazon DynamoDB API to create a dynamic web application that tracks DynamoDB work data.
 For complete source code and instructions on how to set up and run, see the full example on [GitHub](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/kotlin/usecases/itemtracker_dynamodb).

**Services used in this example**
+ DynamoDB
+ Amazon SES

------
#### [ Python ]

**SDK for Python (Boto3)**
 Shows how to use the AWS SDK for Python (Boto3) to create a REST service that tracks work items in Amazon DynamoDB and emails reports by using Amazon Simple Email Service (Amazon SES). This example uses the Flask web framework to handle HTTP routing and integrates with a React webpage to present a fully functional web application.
+ Build a Flask REST service that integrates with AWS services.
+ Read, write, and update work items that are stored in a DynamoDB table.
+ Use Amazon SES to send email reports of work items.
 For complete source code and instructions on how to set up and run, see the full example in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/python/cross_service/dynamodb_item_tracker) on GitHub.

**Services used in this example**
+ DynamoDB
+ Amazon SES

------

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS SDK Code Examples. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query code-library` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
