---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-amplify-jobs.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Amplify::Jobs
<a name="aws-resource-amplify-jobs"></a>

<a name="aws-resource-amplify-jobs-description"></a>The `AWS::Amplify::Jobs` resource Property description not available. for Amplify.

## Syntax
<a name="aws-resource-amplify-jobs-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-amplify-jobs-syntax.json"></a>

```
{
  "Type" : "AWS::Amplify::Jobs",
  "Properties" : {
      "[AppId](#cfn-amplify-jobs-appid)" : {{String}},
      "[BranchName](#cfn-amplify-jobs-branchname)" : {{String}}
    }
}
```

### YAML
<a name="aws-resource-amplify-jobs-syntax.yaml"></a>

```
Type: AWS::Amplify::Jobs
Properties:
  [AppId](#cfn-amplify-jobs-appid): {{String}}
  [BranchName](#cfn-amplify-jobs-branchname): {{String}}
```

## Properties
<a name="aws-resource-amplify-jobs-properties"></a>

`AppId`  <a name="cfn-amplify-jobs-appid"></a>
 The unique ID for an Amplify app.
*Required*: Yes
*Type*: String
*Pattern*: `^d[a-z0-9]+$`
*Minimum*: `1`
*Maximum*: `20`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`BranchName`  <a name="cfn-amplify-jobs-branchname"></a>
The name of the branch to use for the request.
*Required*: Yes
*Type*: String
*Pattern*: `^(?s).+$`
*Minimum*: `1`
*Maximum*: `255`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## Return values
<a name="aws-resource-amplify-jobs-return-values"></a>

### Ref
<a name="aws-resource-amplify-jobs-return-values-ref"></a>

### Fn::GetAtt
<a name="aws-resource-amplify-jobs-return-values-fn--getatt"></a>

####
<a name="aws-resource-amplify-jobs-return-values-fn--getatt-fn--getatt"></a>

`Arn`  <a name="Arn-fn::getatt"></a>
Property description not available.

`CommitId`  <a name="CommitId-fn::getatt"></a>
Property description not available.

`CommitTime`  <a name="CommitTime-fn::getatt"></a>
Property description not available.

`JobId`  <a name="JobId-fn::getatt"></a>
Property description not available.

`StartTime`  <a name="StartTime-fn::getatt"></a>
Property description not available.

`Status`  <a name="Status-fn::getatt"></a>
Property description not available.
