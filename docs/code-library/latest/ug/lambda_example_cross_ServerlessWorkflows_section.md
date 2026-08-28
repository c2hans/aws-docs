---
source_url: https://docs.aws.amazon.com/code-library/latest/ug/lambda_example_cross_ServerlessWorkflows_section.html
---

There are more AWS SDK examples available in the [AWS Doc SDK Examples](https://github.com/awsdocs/aws-doc-sdk-examples) GitHub repo.

# Use Step Functions to invoke Lambda functions
<a name="lambda_example_cross_ServerlessWorkflows_section"></a>

The following code example shows how to create an AWS Step Functions state machine that invokes AWS Lambda functions in sequence.

------
#### [ Java ]

**SDK for Java 2.x**
 Shows how to create an AWS serverless workflow by using AWS Step Functions and the AWS SDK for Java 2.x. Each workflow step is implemented using an AWS Lambda function.
 For complete source code and instructions on how to set up and run, see the full example on [GitHub](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/javav2/usecases/creating_workflows_stepfunctions).

**Services used in this example**
+ DynamoDB
+ Lambda
+ Amazon SES
+ Step Functions

------

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS SDK Code Examples. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query code-library` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
