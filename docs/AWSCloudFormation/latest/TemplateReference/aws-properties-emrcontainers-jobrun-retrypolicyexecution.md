---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-emrcontainers-jobrun-retrypolicyexecution.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::EMRContainers::JobRun RetryPolicyExecution
<a name="aws-properties-emrcontainers-jobrun-retrypolicyexecution"></a>

The current status of the retry policy executed on the job.

## Syntax
<a name="aws-properties-emrcontainers-jobrun-retrypolicyexecution-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-emrcontainers-jobrun-retrypolicyexecution-syntax.json"></a>

```
{
  "[CurrentAttemptCount](#cfn-emrcontainers-jobrun-retrypolicyexecution-currentattemptcount)" : {{Integer}}
}
```

### YAML
<a name="aws-properties-emrcontainers-jobrun-retrypolicyexecution-syntax.yaml"></a>

```
  [CurrentAttemptCount](#cfn-emrcontainers-jobrun-retrypolicyexecution-currentattemptcount): {{Integer}}
```

## Properties
<a name="aws-properties-emrcontainers-jobrun-retrypolicyexecution-properties"></a>

`CurrentAttemptCount`  <a name="cfn-emrcontainers-jobrun-retrypolicyexecution-currentattemptcount"></a>
The current number of attempts made on the driver of the job.
*Required*: Yes
*Type*: Integer
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
