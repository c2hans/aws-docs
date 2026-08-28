---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-sqs-queuepolicy.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::SQS::QueuePolicy
<a name="aws-resource-sqs-queuepolicy"></a>

The `AWS::SQS::QueuePolicy` type applies a policy to Amazon SQS queues. For an example snippet, see [Declaring an Amazon SQS policy](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/quickref-iam.html#scenario-sqs-policy) in the *CloudFormation User Guide*.

## Syntax
<a name="aws-resource-sqs-queuepolicy-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-sqs-queuepolicy-syntax.json"></a>

```
{
  "Type" : "AWS::SQS::QueuePolicy",
  "Properties" : {
      "[PolicyDocument](#cfn-sqs-queuepolicy-policydocument)" : {{Json}},
      "[Queues](#cfn-sqs-queuepolicy-queues)" : {{[ String, ... ]}}
    }
}
```

### YAML
<a name="aws-resource-sqs-queuepolicy-syntax.yaml"></a>

```
Type: AWS::SQS::QueuePolicy
Properties:
  [PolicyDocument](#cfn-sqs-queuepolicy-policydocument): {{Json}}
  [Queues](#cfn-sqs-queuepolicy-queues): {{
    - String}}
```

## Properties
<a name="aws-resource-sqs-queuepolicy-properties"></a>

`PolicyDocument`  <a name="cfn-sqs-queuepolicy-policydocument"></a>
A policy document that contains the permissions for the specified Amazon SQS queues. For more information about Amazon SQS policies, see [Using custom policies with the Amazon SQS access policy language](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-creating-custom-policies.html) in the *Amazon SQS Developer Guide*.
*Required*: Yes
*Type*: Json
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Queues`  <a name="cfn-sqs-queuepolicy-queues"></a>
The URLs of the queues to which you want to add the policy. You can use the ` [ Ref](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-ref.html) ` function to specify an ` [ AWS::SQS::Queue](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sqs-queue.html) ` resource.
*Required*: Yes
*Type*: Array of String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-sqs-queuepolicy-return-values"></a>

### Fn::GetAtt
<a name="aws-resource-sqs-queuepolicy-return-values-fn--getatt"></a>

####
<a name="aws-resource-sqs-queuepolicy-return-values-fn--getatt-fn--getatt"></a>

`Id`  <a name="Id-fn::getatt"></a>
The provider-assigned unique ID for this managed resource.

## Examples
<a name="aws-resource-sqs-queuepolicy--examples"></a>

### Amazon SQS Queue Policy
<a name="aws-resource-sqs-queuepolicy--examples--Amazon_SQS_Queue_Policy"></a>

The following sample is a queue policy that allows AWS account 111122223333 to send and receive messages on queue queue2. You add the policy to the resources section of your template.

#### JSON
<a name="aws-resource-sqs-queuepolicy--examples--Amazon_SQS_Queue_Policy--json"></a>

```

"SampleSQSPolicy" : {
  "Type" : "AWS::SQS::QueuePolicy",
  "Properties" : {
    "Queues" :  ["https://sqs:us-east-2.amazonaws.com/444455556666/queue2"],
    "PolicyDocument": {
      "Statement":[{
        "Action":["SQS:SendMessage", "SQS:ReceiveMessage"],
        "Effect":"Allow",
        "Resource": "arn:aws:sqs:us-east-2:444455556666:queue2",
        "Principal": {
          "AWS": [
            "111122223333"]
        }
      }]
    }
  }
}
```

#### YAML
<a name="aws-resource-sqs-queuepolicy--examples--Amazon_SQS_Queue_Policy--yaml"></a>

```

SampleSQSPolicy:
  Type: AWS::SQS::QueuePolicy
  Properties:
    Queues:
      - "https://sqs:us-east-2.amazonaws.com/444455556666/queue2"
    PolicyDocument:
      Statement:
        -
          Action:
            - "SQS:SendMessage"
            - "SQS:ReceiveMessage"
          Effect: "Allow"
          Resource: "arn:aws:sqs:us-east-2:444455556666:queue2"
          Principal:
            AWS:
              - "111122223333"
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
