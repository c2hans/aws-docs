---
source_url: https://docs.aws.amazon.com/code-library/latest/ug/lambda_example_cross_AuroraRestLendingLibrary_section.html
---

There are more AWS SDK examples available in the [AWS Doc SDK Examples](https://github.com/awsdocs/aws-doc-sdk-examples) GitHub repo.

# Create a lending library REST API
<a name="lambda_example_cross_AuroraRestLendingLibrary_section"></a>

The following code example shows how to create a lending library where patrons can borrow and return books by using a REST API backed by an Amazon Aurora database.

------
#### [ Python ]

**SDK for Python (Boto3)**
 Shows how to use the AWS SDK for Python (Boto3) with the Amazon Relational Database Service (Amazon RDS) API and AWS Chalice to create a REST API backed by an Amazon Aurora database. The web service is fully serverless and represents a simple lending library where patrons can borrow and return books. Learn how to:
+ Create and manage a serverless Aurora database cluster.
+ Use AWS Secrets Manager to manage database credentials.
+ Implement a data storage layer that uses Amazon RDS to move data into and out of the database.
+ Use AWS Chalice to deploy a serverless REST API to Amazon API Gateway and AWS Lambda.
+ Use the Requests package to send requests to the web service.
 For complete source code and instructions on how to set up and run, see the full example on [GitHub](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/python/cross_service/aurora_rest_lending_library).

**Services used in this example**
+ API Gateway
+ Aurora
+ Lambda
+ Secrets Manager

------

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS SDK Code Examples. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query code-library` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
