---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-lambda-eventsourcemapping-destinationconfig.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Lambda::EventSourceMapping DestinationConfig
<a name="aws-properties-lambda-eventsourcemapping-destinationconfig"></a>

A configuration object that specifies the destination of an event after Lambda processes it. For more information, see [Adding a destination](https://docs.aws.amazon.com/lambda/latest/dg/invocation-async-retain-records.html#invocation-async-destinations).

## Syntax
<a name="aws-properties-lambda-eventsourcemapping-destinationconfig-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-lambda-eventsourcemapping-destinationconfig-syntax.json"></a>

```
{
  "[OnFailure](#cfn-lambda-eventsourcemapping-destinationconfig-onfailure)" : {{OnFailure}}
}
```

### YAML
<a name="aws-properties-lambda-eventsourcemapping-destinationconfig-syntax.yaml"></a>

```
  [OnFailure](#cfn-lambda-eventsourcemapping-destinationconfig-onfailure): {{
    OnFailure}}
```

## Properties
<a name="aws-properties-lambda-eventsourcemapping-destinationconfig-properties"></a>

`OnFailure`  <a name="cfn-lambda-eventsourcemapping-destinationconfig-onfailure"></a>
The destination configuration for failed invocations.
*Required*: No
*Type*: [OnFailure](aws-properties-lambda-eventsourcemapping-onfailure.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Examples
<a name="aws-properties-lambda-eventsourcemapping-destinationconfig--examples"></a>

### On-Failure Destination Configuration
<a name="aws-properties-lambda-eventsourcemapping-destinationconfig--examples--On-Failure_Destination_Configuration"></a>

Configure a function to send a record of failed batches to an SQS queue.

#### YAML
<a name="aws-properties-lambda-eventsourcemapping-destinationconfig--examples--On-Failure_Destination_Configuration--yaml"></a>

```
      DestinationConfig:
          OnFailure:
            Destination: arn:aws:sqs:us-east-2:123456789012:dlq
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
