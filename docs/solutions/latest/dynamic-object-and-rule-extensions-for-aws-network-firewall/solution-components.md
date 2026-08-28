---
source_url: https://docs.aws.amazon.com/solutions/latest/dynamic-object-and-rule-extensions-for-aws-network-firewall/solution-components.html
---

# Solution components
<a name="solution-components"></a>

## Amazon DynamoDB
<a name="amazon-dynamodb"></a>

 The solution uses DynamoDB to save solution data as rule bundle, rule, object and audit. The data is used by the Lambda functions to update the underlying ANFW rules.

## Amazon EventBridge
<a name="amazon-eventbridge"></a>

 The solution uses the EventBridge rule to invoke Lambda functions periodically to keep the rules synchronized between the solution and the underlying ANFW rules.

## AWS Config
<a name="aws-config"></a>

 The solution queries an AWS Config aggregator for the metadata of a given cloud resource, for example, the IP address for an EC2 instance.

## AWS Network Firewall
<a name="aws-network-firewall"></a>

 The solution manages the rule group in Network Firewall and continuously updates the rules in rule groups according to the rules.

## Amazon Simple Storage Service\*
<a name="amazon-simple-storage-service"></a>

 The solution creates one Amazon S3 bucket in your account which is used to host the OPA policy bundle.

## Amazon Elastic Container Service\*
<a name="amazon-elastic-container-service"></a>

 The solution uses the Amazon Elastic Container Service (Amazon ECS) to host the OPA cluster to allow the Request Orchestrator Lambda to validate the requests’ validity.

**Note**
 \*Amazon S3 and Amazon ECS are required only when `enableOpa` is set to `true`. Refer to [Update solution configuration](deployment.md#step-1.-update-solution-configuration) for more information.

## AWS Lambda
<a name="aws-lambda"></a>

 The Dynamic Object and Rule Extensions for AWS Network Firewall solution uses Lambda functions to store data for rule bundle, rule, object, and audit information. Lambda functions also update ANFW periodically.

 The solution deploys the following three Lambda functions:

 **Request orchestrator**

 A Lambda function that orchestrates the incoming user-initiated request from Amazon API Gateway. It performs request validation, and manages the domain data such as rule bundle, rule, object according to the request in Amazon DynamoDB.

 **Auto Config Scheduler**

 A Lambda function that is periodically triggered by Amazon EventBridge to find the rule bundle entity targeted at the same underlying resources. The interval is based on the configuration, refer to [Update solution configuration](deployment.md#step-1.-update-solution-configuration) for more information.

 **Auto Config**

 A Lambda function to resolve the rules and objects defined in rule bundles and translate them into standard ANFW rules.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Dynamic Object and Rule Extensions for AWS Network Firewall. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query solutions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
