---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-codebuild-buildbatch.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::CodeBuild::BuildBatch
<a name="aws-resource-codebuild-buildbatch"></a>

Contains information about a batch build.

## Syntax
<a name="aws-resource-codebuild-buildbatch-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-codebuild-buildbatch-syntax.json"></a>

```
{
  "Type" : "AWS::CodeBuild::BuildBatch",
  "Properties" : {
      "[ProjectName](#cfn-codebuild-buildbatch-projectname)" : {{String}}
    }
}
```

### YAML
<a name="aws-resource-codebuild-buildbatch-syntax.yaml"></a>

```
Type: AWS::CodeBuild::BuildBatch
Properties:
  [ProjectName](#cfn-codebuild-buildbatch-projectname): {{String}}
```

## Properties
<a name="aws-resource-codebuild-buildbatch-properties"></a>

`ProjectName`  <a name="cfn-codebuild-buildbatch-projectname"></a>
The name of the batch build project.
*Required*: No
*Type*: String
*Minimum*: `1`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## Return values
<a name="aws-resource-codebuild-buildbatch-return-values"></a>

### Ref
<a name="aws-resource-codebuild-buildbatch-return-values-ref"></a>

### Fn::GetAtt
<a name="aws-resource-codebuild-buildbatch-return-values-fn--getatt"></a>

####
<a name="aws-resource-codebuild-buildbatch-return-values-fn--getatt-fn--getatt"></a>

`Arn`  <a name="Arn-fn::getatt"></a>
The ARN of the batch build.

`BuildBatchNumber`  <a name="BuildBatchNumber-fn::getatt"></a>
The number of the batch build. For each project, the `buildBatchNumber` of its first batch build is `1`. The `buildBatchNumber` of each subsequent batch build is incremented by `1`. If a batch build is deleted, the `buildBatchNumber` of other batch builds does not change.

`BuildBatchStatus`  <a name="BuildBatchStatus-fn::getatt"></a>
The status of the batch build.

`BuildTimeoutInMinutes`  <a name="BuildTimeoutInMinutes-fn::getatt"></a>
Specifies the maximum amount of time, in minutes, that the build in a batch must be completed in.

`Complete`  <a name="Complete-fn::getatt"></a>
Indicates if the batch build is complete.

`CurrentPhase`  <a name="CurrentPhase-fn::getatt"></a>
The current phase of the batch build.

`EncryptionKey`  <a name="EncryptionKey-fn::getatt"></a>
The AWS Key Management Service customer master key (CMK) to be used for encrypting the batch build output artifacts.
You can use a cross-account KMS key to encrypt the build output artifacts if your service role has permission to that key.
You can specify either the Amazon Resource Name (ARN) of the CMK or, if available, the CMK's alias (using the format `alias/<alias-name>`).

`Id`  <a name="Id-fn::getatt"></a>
The identifier of the batch build.

`Initiator`  <a name="Initiator-fn::getatt"></a>
The entity that started the batch build. Valid values include:
+ If CodePipeline started the build, the pipeline's name (for example, `codepipeline/my-demo-pipeline`).
+ If a user started the build, the user's name.
+ If the Jenkins plugin for AWS CodeBuild started the build, the string `CodeBuild-Jenkins-Plugin`.

`QueuedTimeoutInMinutes`  <a name="QueuedTimeoutInMinutes-fn::getatt"></a>
Specifies the amount of time, in minutes, that the batch build is allowed to be queued before it times out.

`StartTime`  <a name="StartTime-fn::getatt"></a>
The date and time that the batch build started.
