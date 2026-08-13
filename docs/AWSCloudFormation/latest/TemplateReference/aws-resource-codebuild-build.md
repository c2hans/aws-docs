---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-codebuild-build.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::CodeBuild::Build
<a name="aws-resource-codebuild-build"></a>

Information about a build.

## Syntax
<a name="aws-resource-codebuild-build-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-codebuild-build-syntax.json"></a>

```
{
  "Type" : "AWS::CodeBuild::Build",
  "Properties" : {
      "[ProjectName](#cfn-codebuild-build-projectname)" : {{String}}
    }
}
```

### YAML
<a name="aws-resource-codebuild-build-syntax.yaml"></a>

```
Type: AWS::CodeBuild::Build
Properties:
  [ProjectName](#cfn-codebuild-build-projectname): {{String}}
```

## Properties
<a name="aws-resource-codebuild-build-properties"></a>

`ProjectName`  <a name="cfn-codebuild-build-projectname"></a>
The name of the AWS CodeBuild project.
*Required*: No
*Type*: String
*Minimum*: `1`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## Return values
<a name="aws-resource-codebuild-build-return-values"></a>

### Ref
<a name="aws-resource-codebuild-build-return-values-ref"></a>

### Fn::GetAtt
<a name="aws-resource-codebuild-build-return-values-fn--getatt"></a>

####
<a name="aws-resource-codebuild-build-return-values-fn--getatt-fn--getatt"></a>

`Arn`  <a name="Arn-fn::getatt"></a>
The Amazon Resource Name (ARN) of the build.

`BuildComplete`  <a name="BuildComplete-fn::getatt"></a>
Whether the build is complete. True if complete; otherwise, false.

`BuildNumber`  <a name="BuildNumber-fn::getatt"></a>
The number of the build. For each project, the `buildNumber` of its first build is `1`. The `buildNumber` of each subsequent build is incremented by `1`. If a build is deleted, the `buildNumber` of other builds does not change.

`BuildStatus`  <a name="BuildStatus-fn::getatt"></a>
The current status of the build. Valid values include:
+ `FAILED`: The build failed.
+ `FAULT`: The build faulted.
+ `IN_PROGRESS`: The build is still in progress.
+ `STOPPED`: The build stopped.
+ `SUCCEEDED`: The build succeeded.
+ `TIMED_OUT`: The build timed out.

`CurrentPhase`  <a name="CurrentPhase-fn::getatt"></a>
The current build phase.

`EncryptionKey`  <a name="EncryptionKey-fn::getatt"></a>
The AWS Key Management Service customer master key (CMK) to be used for encrypting the build output artifacts.
 You can use a cross-account KMS key to encrypt the build output artifacts if your service role has permission to that key.
You can specify either the Amazon Resource Name (ARN) of the CMK or, if available, the CMK's alias (using the format `alias/<alias-name>`).

`EndTime`  <a name="EndTime-fn::getatt"></a>
When the build process ended, expressed in Unix time format.

`Id`  <a name="Id-fn::getatt"></a>
The unique ID for the build.

`Initiator`  <a name="Initiator-fn::getatt"></a>
The entity that started the build. Valid values include:
+ If CodePipeline started the build, the pipeline's name (for example, `codepipeline/my-demo-pipeline`).
+ If a user started the build, the user's name (for example, `MyUserName`).
+ If the Jenkins plugin for AWS CodeBuild started the build, the string `CodeBuild-Jenkins-Plugin`.

`QueuedTimeoutInMinutes`  <a name="QueuedTimeoutInMinutes-fn::getatt"></a>
 The number of minutes a build is allowed to be queued before it times out.

`ServiceRole`  <a name="ServiceRole-fn::getatt"></a>
The name of a service role used for this build.

`StartTime`  <a name="StartTime-fn::getatt"></a>
When the build process started, expressed in Unix time format.

`TimeoutInMinutes`  <a name="TimeoutInMinutes-fn::getatt"></a>
How long, in minutes, from 5 to 2160 (36 hours), for AWS CodeBuild to wait before timing out this build if it does not get marked as completed.
