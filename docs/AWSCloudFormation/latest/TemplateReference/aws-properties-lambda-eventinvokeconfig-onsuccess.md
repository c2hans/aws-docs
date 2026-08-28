---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-lambda-eventinvokeconfig-onsuccess.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Lambda::EventInvokeConfig OnSuccess
<a name="aws-properties-lambda-eventinvokeconfig-onsuccess"></a>

A destination for events that were processed successfully.

To retain records of successful [asynchronous invocations](https://docs.aws.amazon.com/lambda/latest/dg/invocation-async.html#invocation-async-destinations), you can configure an Amazon SNS topic, Amazon SQS queue, Lambda function, or Amazon EventBridge event bus as the destination.

**Note**
`OnSuccess` is not supported in `CreateEventSourceMapping` or `UpdateEventSourceMapping` requests.

## Syntax
<a name="aws-properties-lambda-eventinvokeconfig-onsuccess-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-lambda-eventinvokeconfig-onsuccess-syntax.json"></a>

```
{
  "[Destination](#cfn-lambda-eventinvokeconfig-onsuccess-destination)" : {{String}}
}
```

### YAML
<a name="aws-properties-lambda-eventinvokeconfig-onsuccess-syntax.yaml"></a>

```
  [Destination](#cfn-lambda-eventinvokeconfig-onsuccess-destination): {{String}}
```

## Properties
<a name="aws-properties-lambda-eventinvokeconfig-onsuccess-properties"></a>

`Destination`  <a name="cfn-lambda-eventinvokeconfig-onsuccess-destination"></a>
The Amazon Resource Name (ARN) of the destination resource.
Amazon SNS destinations have a message size limit of 256 KB. If the combined size of the function request and response payload exceeds the limit, Lambda will drop the payload when sending `OnFailure` event to the destination. For details on this behavior, refer to [Retaining records of asynchronous invocations](https://docs.aws.amazon.com/lambda/latest/dg/invocation-async-retain-records.html).
*Required*: Yes
*Type*: String
*Pattern*: `^$|arn:(aws[a-zA-Z0-9-]*):([a-zA-Z0-9\-])+:([a-z]+(-[a-z]+)+-\d{1})?:(\d{12})?:(.*)`
*Minimum*: `0`
*Maximum*: `350`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Examples
<a name="aws-properties-lambda-eventinvokeconfig-onsuccess--examples"></a>

### On-Success Destination Configuration
<a name="aws-properties-lambda-eventinvokeconfig-onsuccess--examples--On-Success_Destination_Configuration"></a>

Configure a function to send a record of successful asynchronous invocations to an SQS queue.

#### YAML
<a name="aws-properties-lambda-eventinvokeconfig-onsuccess--examples--On-Success_Destination_Configuration--yaml"></a>

```
          OnSuccess:
            Destination: arn:aws:sqs:us-east-2:123456789012:destination
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
