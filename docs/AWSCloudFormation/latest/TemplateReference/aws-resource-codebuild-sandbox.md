---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-codebuild-sandbox.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::CodeBuild::Sandbox
<a name="aws-resource-codebuild-sandbox"></a>

Contains sandbox information.

## Syntax
<a name="aws-resource-codebuild-sandbox-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-codebuild-sandbox-syntax.json"></a>

```
{
  "Type" : "AWS::CodeBuild::Sandbox",
  "Properties" : {
      "[ProjectName](#cfn-codebuild-sandbox-projectname)" : {{String}}
    }
}
```

### YAML
<a name="aws-resource-codebuild-sandbox-syntax.yaml"></a>

```
Type: AWS::CodeBuild::Sandbox
Properties:
  [ProjectName](#cfn-codebuild-sandbox-projectname): {{String}}
```

## Properties
<a name="aws-resource-codebuild-sandbox-properties"></a>

`ProjectName`  <a name="cfn-codebuild-sandbox-projectname"></a>
The AWS CodeBuild project name.
*Required*: No
*Type*: String
*Minimum*: `1`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## Return values
<a name="aws-resource-codebuild-sandbox-return-values"></a>

### Ref
<a name="aws-resource-codebuild-sandbox-return-values-ref"></a>

### Fn::GetAtt
<a name="aws-resource-codebuild-sandbox-return-values-fn--getatt"></a>

####
<a name="aws-resource-codebuild-sandbox-return-values-fn--getatt-fn--getatt"></a>

`Arn`  <a name="Arn-fn::getatt"></a>
The ARN of the sandbox.

`EncryptionKey`  <a name="EncryptionKey-fn::getatt"></a>
The AWS Key Management Service customer master key (CMK) to be used for encrypting the sandbox output artifacts.

`Id`  <a name="Id-fn::getatt"></a>
The ID of the sandbox.

`QueuedTimeoutInMinutes`  <a name="QueuedTimeoutInMinutes-fn::getatt"></a>
The number of minutes a sandbox is allowed to be queued before it times out.

`RequestTime`  <a name="RequestTime-fn::getatt"></a>
When the sandbox process was initially requested, expressed in Unix time format.

`ServiceRole`  <a name="ServiceRole-fn::getatt"></a>
The name of a service role used for this sandbox.

`StartTime`  <a name="StartTime-fn::getatt"></a>
When the sandbox process started, expressed in Unix time format.

`Status`  <a name="Status-fn::getatt"></a>
The status of the sandbox.

`TimeoutInMinutes`  <a name="TimeoutInMinutes-fn::getatt"></a>
How long, in minutes, from 5 to 2160 (36 hours), for AWS CodeBuild to wait before timing out this sandbox if it does not get marked as completed.
