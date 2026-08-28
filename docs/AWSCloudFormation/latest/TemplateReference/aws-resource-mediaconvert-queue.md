---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-mediaconvert-queue.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::MediaConvert::Queue
<a name="aws-resource-mediaconvert-queue"></a>

The AWS::MediaConvert::Queue resource is an AWS Elemental MediaConvert resource type that you can use to manage the resources that are available to your account for parallel processing of jobs. For more information about queues, see [Working with AWS Elemental MediaConvert Queues](https://docs.aws.amazon.com/mediaconvert/latest/ug/working-with-queues.html) in the * AWS Elemental MediaConvert User Guide *.

## Syntax
<a name="aws-resource-mediaconvert-queue-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-mediaconvert-queue-syntax.json"></a>

```
{
  "Type" : "AWS::MediaConvert::Queue",
  "Properties" : {
      "[ConcurrentJobs](#cfn-mediaconvert-queue-concurrentjobs)" : {{Integer}},
      "[Description](#cfn-mediaconvert-queue-description)" : {{String}},
      "[MaximumConcurrentFeeds](#cfn-mediaconvert-queue-maximumconcurrentfeeds)" : {{Integer}},
      "[Name](#cfn-mediaconvert-queue-name)" : {{String}},
      "[PricingPlan](#cfn-mediaconvert-queue-pricingplan)" : {{String}},
      "[Status](#cfn-mediaconvert-queue-status)" : {{String}},
      "[Tags](#cfn-mediaconvert-queue-tags)" : {{[ [`Tag`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-resource-tags.html), ... ]}}
    }
}
```

### YAML
<a name="aws-resource-mediaconvert-queue-syntax.yaml"></a>

```
Type: AWS::MediaConvert::Queue
Properties:
  [ConcurrentJobs](#cfn-mediaconvert-queue-concurrentjobs): {{Integer}}
  [Description](#cfn-mediaconvert-queue-description): {{String}}
  [MaximumConcurrentFeeds](#cfn-mediaconvert-queue-maximumconcurrentfeeds): {{Integer}}
  [Name](#cfn-mediaconvert-queue-name): {{String}}
  [PricingPlan](#cfn-mediaconvert-queue-pricingplan): {{String}}
  [Status](#cfn-mediaconvert-queue-status): {{String}}
  [Tags](#cfn-mediaconvert-queue-tags): {{
    - [`Tag`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-resource-tags.html)}}
```

## Properties
<a name="aws-resource-mediaconvert-queue-properties"></a>

`ConcurrentJobs`  <a name="cfn-mediaconvert-queue-concurrentjobs"></a>
Specify the maximum number of jobs your queue can process concurrently. For on-demand queues, the value you enter is constrained by your service quotas for Maximum concurrent jobs, per on-demand queue and Maximum concurrent jobs, per account. For reserved queues, specify the number of jobs you can process concurrently in your reservation plan instead.
*Required*: No
*Type*: Integer
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Description`  <a name="cfn-mediaconvert-queue-description"></a>
Optional. A description of the queue that you are creating.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`MaximumConcurrentFeeds`  <a name="cfn-mediaconvert-queue-maximumconcurrentfeeds"></a>
Specify the maximum number of Elemental Inference feeds MediaConvert can process concurrently.
*Required*: No
*Type*: Integer
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Name`  <a name="cfn-mediaconvert-queue-name"></a>
The name of the queue that you are creating.
*Required*: No
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`PricingPlan`  <a name="cfn-mediaconvert-queue-pricingplan"></a>
When you use CloudFormation, you can create only on-demand queues. Therefore, always set `PricingPlan` to the value "ON\_DEMAND" when declaring an AWS::MediaConvert::Queue in your CloudFormation template.
To create a reserved queue, use the AWS Elemental MediaConvert console at https://console.aws.amazon.com/mediaconvert to set up a contract. For more information, see [Working with AWS Elemental MediaConvert Queues](https://docs.aws.amazon.com/mediaconvert/latest/ug/working-with-queues.html) in the * AWS Elemental MediaConvert User Guide *.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Status`  <a name="cfn-mediaconvert-queue-status"></a>
Initial state of the queue. Queues can be either ACTIVE or PAUSED. If you create a paused queue, then jobs that you send to that queue won't begin.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Tags`  <a name="cfn-mediaconvert-queue-tags"></a>
An array of key-value pairs to apply to this resource.
For more information, see [Tag](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-resource-tags.html).
*Required*: No
*Type*: Array of [`Tag`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-resource-tags.html)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-mediaconvert-queue-return-values"></a>

### Ref
<a name="aws-resource-mediaconvert-queue-return-values-ref"></a>

When you pass the logical ID of an `AWS::MediaConvert::Queue` resource to the intrinsic `Ref` function, the function returns the name of the queue, such as `Queue 2`.

For more information about using the `Ref` function, see [`Ref`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-ref.html).

### Fn::GetAtt
<a name="aws-resource-mediaconvert-queue-return-values-fn--getatt"></a>

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [`Fn::GetAtt`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-getatt.html).

####
<a name="aws-resource-mediaconvert-queue-return-values-fn--getatt-fn--getatt"></a>

`Arn`  <a name="Arn-fn::getatt"></a>
The Amazon Resource Name (ARN) of the queue, such as `arn:aws:mediaconvert:us-west-2:123456789012`.

`Name`  <a name="Name-fn::getatt"></a>
The name of the queue, such as `Queue 2`.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
