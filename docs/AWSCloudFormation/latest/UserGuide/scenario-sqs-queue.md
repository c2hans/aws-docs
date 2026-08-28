---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/scenario-sqs-queue.html
---

# Amazon SQS template snippets
<a name="scenario-sqs-queue"></a>

This example shows an Amazon SQS queue.

## JSON
<a name="scenario-sqs-queue-example-1.json"></a>

```
1. "MyQueue" : {
2.     "Type" : "AWS::SQS::Queue",
3.     "Properties" : {
4.         "VisibilityTimeout" : "{{value}}"
5.     }
6. }
```

## YAML
<a name="scenario-sqs-queue-example-1.yaml"></a>

```
1. MyQueue:
2.   Type: AWS::SQS::Queue
3.   Properties:
4.     VisibilityTimeout: {{value}}
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
