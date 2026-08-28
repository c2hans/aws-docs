---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-emr-step.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::EMR::Step
<a name="aws-resource-emr-step"></a>

Use `Step` to specify a cluster (job flow) step, which runs only on the master node. Steps are used to submit data processing jobs to a cluster.

## Syntax
<a name="aws-resource-emr-step-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-emr-step-syntax.json"></a>

```
{
  "Type" : "AWS::EMR::Step",
  "Properties" : {
      "[ActionOnFailure](#cfn-emr-step-actiononfailure)" : {{String}},
      "[EncryptionKeyArn](#cfn-emr-step-encryptionkeyarn)" : {{String}},
      "[HadoopJarStep](#cfn-emr-step-hadoopjarstep)" : {{HadoopJarStepConfig}},
      "[JobFlowId](#cfn-emr-step-jobflowid)" : {{String}},
      "[LogUri](#cfn-emr-step-loguri)" : {{String}},
      "[Name](#cfn-emr-step-name)" : {{String}}
    }
}
```

### YAML
<a name="aws-resource-emr-step-syntax.yaml"></a>

```
Type: AWS::EMR::Step
Properties:
  [ActionOnFailure](#cfn-emr-step-actiononfailure): {{String}}
  [EncryptionKeyArn](#cfn-emr-step-encryptionkeyarn): {{String}}
  [HadoopJarStep](#cfn-emr-step-hadoopjarstep): {{
    HadoopJarStepConfig}}
  [JobFlowId](#cfn-emr-step-jobflowid): {{String}}
  [LogUri](#cfn-emr-step-loguri): {{String}}
  [Name](#cfn-emr-step-name): {{String}}
```

## Properties
<a name="aws-resource-emr-step-properties"></a>

`ActionOnFailure`  <a name="cfn-emr-step-actiononfailure"></a>
This specifies what action to take when the cluster step fails. Possible values are `CANCEL_AND_WAIT` and `CONTINUE`.
*Required*: Yes
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`EncryptionKeyArn`  <a name="cfn-emr-step-encryptionkeyarn"></a>
The KMS key ARN to encrypt the logs published to the given Amazon S3 destination. When omitted, EMR falls back to cluster-level logging behavior.
*Required*: No
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`HadoopJarStep`  <a name="cfn-emr-step-hadoopjarstep"></a>
The `HadoopJarStepConfig` property type specifies a job flow step consisting of a JAR file whose main function will be executed. The main function submits a job for the cluster to execute as a step on the master node, and then waits for the job to finish or fail before executing subsequent steps.
*Required*: Yes
*Type*: [HadoopJarStepConfig](aws-properties-emr-step-hadoopjarstepconfig.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`JobFlowId`  <a name="cfn-emr-step-jobflowid"></a>
A string that uniquely identifies the cluster (job flow).
*Required*: Yes
*Type*: String
*Pattern*: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\r\n\t]*`
*Minimum*: `0`
*Maximum*: `256`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`LogUri`  <a name="cfn-emr-step-loguri"></a>
The Amazon S3 destination URI for log publishing. When omitted, EMR falls back to cluster-level logging behavior.
*Required*: No
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Name`  <a name="cfn-emr-step-name"></a>
The name of the cluster step.
*Required*: Yes
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## Return values
<a name="aws-resource-emr-step-return-values"></a>

### Ref
<a name="aws-resource-emr-step-return-values-ref"></a>

When you pass the logical ID of this resource to the intrinsic `Ref` function, `Ref` returns returns the ID of the step.

For more information about using the `Ref` function, see [`Ref`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-ref.html).

### Fn::GetAtt
<a name="aws-resource-emr-step-return-values-fn--getatt"></a>

####
<a name="aws-resource-emr-step-return-values-fn--getatt-fn--getatt"></a>

`Id`  <a name="Id-fn::getatt"></a>
The identifier of the cluster step.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
