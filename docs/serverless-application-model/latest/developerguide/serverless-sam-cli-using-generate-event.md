---
source_url: https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-sam-cli-using-generate-event.html
---

# Generate sample event payloads with AWS SAM
<a name="serverless-sam-cli-using-generate-event"></a>

To test your Lambda functions, you can generate and customize sample event payloads that imitate the data your Lambda functions will receive when triggered by other AWS services. This includes services like API Gateway, CloudFormation, Amazon S3, and more.

Generating sample event payloads helps you test the behavior of your Lambda function with a variety of different inputs without needing to work in a live environment. This approach also saves time when compared to manually creating AWS service event samples to test functions.

For the full list of services that you can generate sample event payloads for, use this command:

```
sam local generate-event --help
```

For the list of options you can use for a particular service, use this command:

```
sam local generate-event [SERVICE] --help
```

Examples:

```
#Generates the event from S3 when a new object is created
sam local generate-event s3 put

# Generates the event from S3 when an object is deleted
sam local generate-event s3 delete
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Serverless Application Model. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query serverless-application-model` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
