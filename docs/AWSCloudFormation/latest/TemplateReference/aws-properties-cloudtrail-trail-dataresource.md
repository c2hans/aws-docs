---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-cloudtrail-trail-dataresource.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::CloudTrail::Trail DataResource
<a name="aws-properties-cloudtrail-trail-dataresource"></a>

You can configure the `DataResource` in an `EventSelector` to log data events for the following three resource types:
+  `AWS::DynamoDB::Table`
+  `AWS::Lambda::Function`
+  `AWS::S3::Object`

To log data events for all other resource types including objects stored in [directory buckets](https://docs.aws.amazon.com/AmazonS3/latest/userguide/directory-buckets-overview.html), you must use [AdvancedEventSelectors](https://docs.aws.amazon.com/awscloudtrail/latest/APIReference/API_AdvancedEventSelector.html). You must also use `AdvancedEventSelectors` if you want to filter on the `eventName` field.

Configure the `DataResource` to specify the resource type and resource ARNs for which you want to log data events.

**Note**
The total number of allowed data resources is 250. This number can be distributed between 1 and 5 event selectors, but the total cannot exceed 250 across all selectors for the trail.

The following example demonstrates how logging works when you configure logging of all data events for a general purpose bucket named `amzn-s3-demo-bucket1`. In this example, the CloudTrail user specified an empty prefix, and the option to log both `Read` and `Write` data events.

1. A user uploads an image file to `amzn-s3-demo-bucket1`.

1. The `PutObject` API operation is an Amazon S3 object-level API. It is recorded as a data event in CloudTrail. Because the CloudTrail user specified an S3 bucket with an empty prefix, events that occur on any object in that bucket are logged. The trail processes and logs the event.

1. A user uploads an object to an Amazon S3 bucket named `arn:aws:s3:::amzn-s3-demo-bucket1`.

1. The `PutObject` API operation occurred for an object in an S3 bucket that the CloudTrail user didn't specify for the trail. The trail doesn’t log the event.

The following example demonstrates how logging works when you configure logging of AWS Lambda data events for a Lambda function named *MyLambdaFunction*, but not for all Lambda functions.

1. A user runs a script that includes a call to the *MyLambdaFunction* function and the *MyOtherLambdaFunction* function.

1. The `Invoke` API operation on *MyLambdaFunction* is an Lambda API. It is recorded as a data event in CloudTrail. Because the CloudTrail user specified logging data events for *MyLambdaFunction*, any invocations of that function are logged. The trail processes and logs the event.

1. The `Invoke` API operation on *MyOtherLambdaFunction* is an Lambda API. Because the CloudTrail user did not specify logging data events for all Lambda functions, the `Invoke` operation for *MyOtherLambdaFunction* does not match the function specified for the trail. The trail doesn’t log the event.

## Syntax
<a name="aws-properties-cloudtrail-trail-dataresource-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-cloudtrail-trail-dataresource-syntax.json"></a>

```
{
  "[Type](#cfn-cloudtrail-trail-dataresource-type)" : {{String}},
  "[Values](#cfn-cloudtrail-trail-dataresource-values)" : {{[ String, ... ]}}
}
```

### YAML
<a name="aws-properties-cloudtrail-trail-dataresource-syntax.yaml"></a>

```
  [Type](#cfn-cloudtrail-trail-dataresource-type): {{String}}
  [Values](#cfn-cloudtrail-trail-dataresource-values): {{
    - String}}
```

## Properties
<a name="aws-properties-cloudtrail-trail-dataresource-properties"></a>

`Type`  <a name="cfn-cloudtrail-trail-dataresource-type"></a>
The resource type in which you want to log data events. You can specify the following *basic* event selector resource types:
+  `AWS::DynamoDB::Table`
+  `AWS::Lambda::Function`
+  `AWS::S3::Object`
Additional resource types are available through *advanced* event selectors. For more information, see [AdvancedEventSelector](https://docs.aws.amazon.com/awscloudtrail/latest/APIReference/API_AdvancedEventSelector.html).
*Required*: Yes
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Values`  <a name="cfn-cloudtrail-trail-dataresource-values"></a>
An array of Amazon Resource Name (ARN) strings or partial ARN strings for the specified resource type.
+ To log data events for all objects in all S3 buckets in your AWS account, specify the prefix as `arn:aws:s3`.
**Note**
This also enables logging of data event activity performed by any user or role in your AWS account, even if that activity is performed on a bucket that belongs to another AWS account.
+ To log data events for all objects in an S3 bucket, specify the bucket and an empty object prefix such as `arn:aws:s3:::amzn-s3-demo-bucket1/`. The trail logs data events for all objects in this S3 bucket.
+ To log data events for specific objects, specify the S3 bucket and object prefix such as `arn:aws:s3:::amzn-s3-demo-bucket1/example-images`. The trail logs data events for objects in this S3 bucket that match the prefix.
+ To log data events for all Lambda functions in your AWS account, specify the prefix as `arn:aws:lambda`.
**Note**
This also enables logging of `Invoke` activity performed by any user or role in your AWS account, even if that activity is performed on a function that belongs to another AWS account.
+ To log data events for a specific Lambda function, specify the function ARN.
**Note**
Lambda function ARNs are exact. For example, if you specify a function ARN *arn:aws:lambda:us-west-2:111111111111:function:helloworld*, data events will only be logged for *arn:aws:lambda:us-west-2:111111111111:function:helloworld*. They will not be logged for *arn:aws:lambda:us-west-2:111111111111:function:helloworld2*.
+ To log data events for all DynamoDB tables in your AWS account, specify the prefix as `arn:aws:dynamodb`.
*Required*: No
*Type*: Array of String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
