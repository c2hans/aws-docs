---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-bedrock-modelinvocationjob.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Bedrock::ModelInvocationJob
<a name="aws-resource-bedrock-modelinvocationjob"></a>

Creates a batch inference job to invoke a model on multiple prompts. Format your data according to [Format your inference data](https://docs.aws.amazon.com/bedrock/latest/userguide/batch-inference-data) and upload it to an Amazon S3 bucket. For more information, see [Process multiple prompts with batch inference](https://docs.aws.amazon.com/bedrock/latest/userguide/batch-inference.html).

The response returns a `jobArn` that you can use to stop or get details about the job.

## Syntax
<a name="aws-resource-bedrock-modelinvocationjob-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-bedrock-modelinvocationjob-syntax.json"></a>

```
{
  "Type" : "AWS::Bedrock::ModelInvocationJob"
}
```

### YAML
<a name="aws-resource-bedrock-modelinvocationjob-syntax.yaml"></a>

```
Type: AWS::Bedrock::ModelInvocationJob
```

## Return values
<a name="aws-resource-bedrock-modelinvocationjob-return-values"></a>

### Ref
<a name="aws-resource-bedrock-modelinvocationjob-return-values-ref"></a>

### Fn::GetAtt
<a name="aws-resource-bedrock-modelinvocationjob-return-values-fn--getatt"></a>

####
<a name="aws-resource-bedrock-modelinvocationjob-return-values-fn--getatt-fn--getatt"></a>

`JobArn`  <a name="JobArn-fn::getatt"></a>
The Amazon Resource Name (ARN) of the batch inference job.

`JobExpirationTime`  <a name="JobExpirationTime-fn::getatt"></a>
The time at which the batch inference job times or timed out.

`JobName`  <a name="JobName-fn::getatt"></a>
The name of the batch inference job.

`LastModifiedTime`  <a name="LastModifiedTime-fn::getatt"></a>
The time at which the batch inference job was last modified.

`ModelId`  <a name="ModelId-fn::getatt"></a>
The unique identifier of the foundation model used for model inference.

`RoleArn`  <a name="RoleArn-fn::getatt"></a>
The Amazon Resource Name (ARN) of the service role with permissions to carry out and manage batch inference. You can use the console to create a default service role or follow the steps at [Create a service role for batch inference](https://docs.aws.amazon.com/bedrock/latest/userguide/batch-iam-sr.html).

`Status`  <a name="Status-fn::getatt"></a>
The status of the batch inference job.
The following statuses are possible:
+ Submitted – This job has been submitted to a queue for validation.
+ Validating – This job is being validated for the requirements described in [Format and upload your batch inference data](https://docs.aws.amazon.com/bedrock/latest/userguide/batch-inference-data.html). The criteria include the following:
  + Your IAM service role has access to the Amazon S3 buckets containing your files.
  + Your files are .jsonl files and each individual record is a JSON object in the correct format. Note that validation doesn't check if the `modelInput` value matches the request body for the model.
  + Your files fulfill the requirements for file size and number of records. For more information, see [Quotas for Amazon Bedrock](https://docs.aws.amazon.com/bedrock/latest/userguide/quotas.html).
+ Scheduled – This job has been validated and is now in a queue. The job will automatically start when it reaches its turn.
+ Expired – This job timed out because it was scheduled but didn't begin before the set timeout duration. Submit a new job request.
+ InProgress – This job has begun. You can start viewing the results in the output S3 location.
+ Completed – This job has successfully completed. View the output files in the output S3 location.
+ PartiallyCompleted – This job has partially completed. Not all of your records could be processed in time. View the output files in the output S3 location.
+ Failed – This job has failed. Check the failure message for any further details. For further assistance, reach out to the [Support Center](https://console.aws.amazon.com/support/home/).
+ Stopped – This job was stopped by a user.
+ Stopping – This job is being stopped by a user.

`SubmitTime`  <a name="SubmitTime-fn::getatt"></a>
The time at which the batch inference job was submitted.

`Tags`  <a name="Tags-fn::getatt"></a>
Property description not available.

`TimeoutDurationInHours`  <a name="TimeoutDurationInHours-fn::getatt"></a>
The number of hours after which the batch inference job was set to time out.
