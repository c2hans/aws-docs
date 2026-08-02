---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/create-cross-account-amazon-eventbridge-connection-organization.html
---

# Create a cross-account Amazon EventBridge connection in an organization
<a name="create-cross-account-amazon-eventbridge-connection-organization"></a>

*Sam Wilson and Robert Stone, Amazon Web Services*

## Summary
<a name="create-cross-account-amazon-eventbridge-connection-organization-summary"></a>

Large distributed systems use Amazon EventBridge to communicate changes in state between various Amazon Web Services (AWS) accounts in an AWS Organizations organization. However, EventBridge is generally able to target only endpoints or consumers in the same AWS account. The exception is an event bus in a different account. That event bus is a valid target. To consume events from an event bus in another account, the events must be pushed from the source account's event bus to the destination account’s event bus. To avoid challenges when managing critical events across applications within different AWS accounts, use the recommended approach presented in this pattern.

This pattern illustrates how to implement an event-driven architecture with EventBridge that involves multiple AWS accounts in an AWS Organizations organization. The pattern uses AWS Cloud Development Kit (AWS CDK) Toolkit and AWS CloudFormation.

EventBridge offers a serverless event bus that helps you receive, filter, transform, route, and deliver events. A critical component of event-driven architectures, EventBridge supports separation between producers of messages and consumers of those messages. In a single account, this is straight forward. A multi-account structure requires additional considerations for events on the event bus in one account to be consumed in other accounts within the same organization.

For information about account-specific considerations for producers and consumers, see the [Additional information](#create-cross-account-amazon-eventbridge-connection-organization-additional) section.

## Prerequisites and limitations
<a name="create-cross-account-amazon-eventbridge-connection-organization-prereqs"></a>

**Prerequisites**
+ An AWS Organizations organization with at least two associated AWS accounts
+ An AWS Identity and Access Management (IAM) role in both AWS accounts that allows you to provision infrastructure in both AWS accounts by using AWS CloudFormation
+ Git [installed locally](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)
+ AWS Command Line Interface (AWS CLI) [installed locally](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html)
+ AWS CDK [installed locally](https://docs.aws.amazon.com/cdk/latest/guide/cli.html) and [bootstrapped](https://docs.aws.amazon.com/cdk/v2/guide/bootstrapping.html#bootstrapping-howto) in both AWS accounts

**Product versions**

This pattern has been built and tested by using the following tools and versions:
+ AWS CDK Toolkit 2.126.0
+ Node.js 18.19.0
+ npm 10.2.3
+ Python 3.12

This pattern should work with any version of AWS CDK v2 or npm. Node.js versions 13.0.0 through 13.6.0 are not compatible with AWS CDK.

## Architecture
<a name="create-cross-account-amazon-eventbridge-connection-organization-architecture"></a>

**Target architecture**

The following diagram shows the architecture workflow for pushing an event from one account and consuming it in another account.

![The three-step process for connecting the Source producer account and Destination consumer account.](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/images/pattern-img/34a5f3ae-511d-4636-999f-c73396770117/images/ccc4878a-6281-4a77-a483-4e6f299d7807.png)

The workflow contains the following steps:

1. The Producer AWS Lambda function in the Source account puts an event on the account’s EventBridge event bus.

1. The cross-account EventBridge rule routes the event to an EventBridge event bus in the Destination account.

1. The EventBridge event bus in the Destination account has a target Lambda rule that invokes the Consumer Lambda function.

A best practice is to use a [Dead Letter Queue (DLQ)](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-dead-letter-queues.html) for handling failed invocations of the Consumer Lambda function. However, the DLQ was omitted from this solution for clarity. To learn more about how to implement a DLQ in your workflows and improve your workflows’ ability to recover from failures, see the [Implementing AWS Lambda error handling patterns](https://aws.amazon.com/blogs/compute/implementing-aws-lambda-error-handling-patterns/) blog post.

**Automation and scale**

AWS CDK automatically provisions the required architecture. EventBridge can scale to thousands of records per second depending on the AWS Region. For more information, see the [Amazon EventBridge quotas documentation](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-quota.html).

## Tools
<a name="create-cross-account-amazon-eventbridge-connection-organization-tools"></a>

**AWS services**
+ [AWS Cloud Development Kit (AWS CDK)](https://docs.aws.amazon.com/cdk/v2/guide/home.html) is a software development framework that helps you define and provision AWS Cloud infrastructure in code. This pattern uses the [AWS CDK Toolkit](https://docs.aws.amazon.com/cdk/latest/guide/cli.html), a command line cloud development kit that helps you interact with your AWS CDK app.
+ [Amazon EventBridge](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-what-is.html) is a serverless event bus service that helps you connect your applications with real-time data from a variety of sources. For example, AWS Lambda functions, HTTP invocation endpoints using API destinations, or event buses in other AWS accounts.
+ [AWS Lambda](https://docs.aws.amazon.com/lambda/latest/dg/welcome.html) is a compute service that helps you run code without needing to provision or manage servers. It runs your code only when needed and scales automatically, so you pay only for the compute time that you use.
+ [AWS Organizations](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_introduction.html) is an account management service that helps you consolidate multiple AWS accounts into an organization that you create and centrally manage.

**Other tools**
+ [Node.js](https://nodejs.org/en/docs/) is an event-driven JavaScript runtime environment designed for building scalable network applications.
+ [npm](https://docs.npmjs.com/about-npm) is a software registry that runs in a Node.js environment and is used to share or borrow packages and manage deployment of private packages.
+ [Python](https://www.python.org/) is a general-purpose computer programming language.

**Code repository**

The code for this pattern is available in the GitHub [cross-account-eventbridge-in-organization](https://github.com/aws-samples/aws-cdk-examples/tree/main/python/cross-account-eventbridge-in-organization) repository.

## Best practices
<a name="create-cross-account-amazon-eventbridge-connection-organization-best-practices"></a>

For best practices when working with EventBridge, see the following resources:
+ [Best practices for Amazon EventBridge event patterns](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-patterns-best-practices.html)
+ [Best practices when defining rules in Amazon EventBridge](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-rules-best-practices.html)

## Epics
<a name="create-cross-account-amazon-eventbridge-connection-organization-epics"></a>

### Prepare your local AWS CDK deployment environment
<a name="prepare-your-local-cdk-deployment-environment"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Configure local credentials for the Source account and Destination account. | Review [Setting up new configuration and credentials](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-quickstart.html#getting-started-quickstart-new), and use the authentication and credential method that makes the most sense to your environment.Be sure to configure the AWS CLI for both Source account and Destination account authentication.<br />These instructions assume that you have configured two AWS profiles locally: `sourceAccount` and `destinationAccount`. | App developer |
| Bootstrap both AWS accounts. | To bootstrap the accounts, run the following commands:<pre>cdk bootstrap --profile sourceAccount<br />cdk bootstrap --profile destinationAccount</pre> | App developer |
| Clone the pattern code. | To clone the repository, run the following command:<pre>git clone git@github.com:aws-samples/aws-cdk-examples.git</pre><br />Then, change the directory to the newly cloned project folder:<pre>cd aws-cdk-examples/python/cross-account-eventbridge-in-organization</pre> | App developer |

### Deploy ProducerStack to the Source account
<a name="deploy-producerstack-to-the-source-account"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Modify `cdk.json` with your AWS Organizations and account details. | In the root folder of the project, make the following changes to `cdk.json`:[See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/create-cross-account-amazon-eventbridge-connection-organization.html) | App developer |
| Deploy the ProducerStack resources. | Run the following command from the project’s root directory:<pre>cdk deploy ProducerStack --profile sourceAccount</pre><br />When prompted, accept the new IAM roles and other security-related permissions created through AWS CloudFormation. | App developer |
| Verify that ProducerStack resources are deployed. | To verify the resources, do the following:[See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/create-cross-account-amazon-eventbridge-connection-organization.html) | App developer |

### Deploy ConsumerStack to the Destination account
<a name="deploy-consumerstack-to-the-destination-account"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Deploy the ConsumerStack resources. | Run the following command from the project’s root directory:<pre>cdk deploy ConsumerStack --profile destinationAccount</pre><br />When prompted, accept the new IAM roles and other security-related permissions created through CloudFormation. | App developer |
| Verify that ConsumerStack resources are deployed | [See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/create-cross-account-amazon-eventbridge-connection-organization.html) | App developer |

### Produce and consume events
<a name="produce-and-consume-events"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Invoke the Producer Lambda function. | [See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/create-cross-account-amazon-eventbridge-connection-organization.html) | App developer |
| Verify that the event was received. | [See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/create-cross-account-amazon-eventbridge-connection-organization.html) | App developer |

### Cleanup
<a name="cleanup"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Destroy the ConsumerStack resources. | If you are using this pattern as a test, clean up the deployed resources to avoid incurring additional costs.<br />Run the following command from the project’s root directory:<pre>cdk destroy ConsumerStack --profile destinationAccount</pre><br />You will be prompted to confirm deletion of the stack. | App developer |
| Destroy the ProducerStack resources. | Run the following command from the project’s root directory:<pre>cdk destroy ProducerStack --profile sourceAccount</pre><br />You will be prompted to confirm deletion of the stack. | App developer |

## Troubleshooting
<a name="create-cross-account-amazon-eventbridge-connection-organization-troubleshooting"></a>

| Issue | Solution |
| --- | --- |
| No event was received in the Destination account. | [See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/create-cross-account-amazon-eventbridge-connection-organization.html) |
| Invoking a Lambda function from the console returns the following error:: <br />`User: arn:aws:iam::123456789012:user/XXXXX is not authorized to perform: lambda:Invoke` | Contact your AWS account administrator to receive the appropriate `lambda:Invoke` action permissions on the `ProducerStack-ProducerLambdaXXXX` Lambda function. |

## Related resources
<a name="create-cross-account-amazon-eventbridge-connection-organization-resources"></a>

**References**
+ [AWS Organizations User Guide](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_introduction.html)
+ [Amazon EventBridge event patterns](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-event-patterns.html)
+ [Rules in Amazon EventBridge](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-rules.html)

**Tutorials and videos**
+ [Tutorial: Creating and configuration an organization](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_tutorials_basic.html)
+ [AWS re:Invent 2023 - Advanced event-driven patterns with Amazon EventBridge (COM301-R)](https://www.youtube.com/watch?v=6X4lSPkn4ps)

## Additional information
<a name="create-cross-account-amazon-eventbridge-connection-organization-additional"></a>

**Producer rule**

In the Source account, an EventBridge event bus is created to accept messages from producers (as shown in the *Architecture* section). A rule with accompanying IAM permissions is created on this event bus. The rules target the EventBridge event bus in the Destination account based on the following `cdk.json` structure:

```
"rules": [
  {
    "id": "CrossAccount",
    "sources": ["Producer"],
    "detail_types": ["TestType"],
    "targets": [
      {
        "id": "ConsumerEventBus",
        "arn": "arn:aws:events:us-east-2:012345678901:event-bus/CrossAccount"
      }
    ]
  }
]
```

For each consuming event bus, the event pattern and the target event bus must be included.

*Event Pattern*

[Event patterns](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-event-patterns.html) filter which events this rule will apply to. For purposes of this example, the event sources and the record `detail_types` identify which events to transmit from the Source account’s event bus to the Destination account’s event bus.

*Target event bus*

This rule targets an event bus that exists in another account. The full `arn` (Amazon Resource Name) is needed to uniquely identify the target event bus, and the `id` is the [logical ID](https://docs.aws.amazon.com/cdk/v2/guide/identifiers.html#identifiers_logical_ids) used by AWS CloudFormation. The target event bus need not actually exist at the time of target rule creation.

**Destination account-specific considerations**

In the Destination account, an EventBridge event bus is created to receive messages from the Source account’s event bus. To allow events to be published from the Source account, you must create a [resource-based policy](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-use-resource-based.html):

```
{
  "Version": "2012-10-17",
  "Statement": [{
    "Sid": "AllowOrgToPutEvents",
    "Effect": "Allow",
    "Principal": "*",
    "Action": "events:PutEvents",
    "Resource": "arn:aws:events:us-east-2:012345678901:event-bus/CrossAccount",
    "Condition": {
      "StringEquals": {
        "aws:PrincipalOrgID": "o-XXXXXXXXX"
      }
    }
  }]
}
```

It's especially important to grant the `events:PutEvents` permission, which allows any other account in the same organization to publish events to this event bus. Setting `aws:PrincipalOrgId` as the organization ID grants the needed permissions.

**Event pattern**

You can modify the included event pattern to meet your use case:

```
rule = events.Rule(
    self,
    self.id + 'Rule' + rule_definition['id'],
    event_bus=event_bus,
    event_pattern=events.EventPattern(
        source=rule_definition['sources'],
        detail_type=rule_definition['detail_types'],
    )
)
```

To reduce unnecessary processing, the event pattern should specify that only events to be processed by the Destination account are transmitted to the Destination account’s event bus.

*Resource-based policy*

This example uses the organization ID to control which accounts are allowed to put events on the Destination account’s event bus. Consider using a more restrictive policy, such as specifying the Source account.

*EventBridge quotas*

Keep in mind the following [quotas](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-quota.html):
+ 300 rules per event bus is the default quota. This can be expanded if necessary, but it should fit most use cases.
+ Five targets per rule is the maximum allowed. We recommend that application architects should use a distinct rule for each Destination account to support fine-grained control over the event pattern.
