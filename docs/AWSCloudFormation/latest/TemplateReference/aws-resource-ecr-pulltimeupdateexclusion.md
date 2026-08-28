---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-ecr-pulltimeupdateexclusion.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::ECR::PullTimeUpdateExclusion
<a name="aws-resource-ecr-pulltimeupdateexclusion"></a>

<a name="aws-resource-ecr-pulltimeupdateexclusion-description"></a>The `AWS::ECR::PullTimeUpdateExclusion` resource Property description not available. for ECR.

## Syntax
<a name="aws-resource-ecr-pulltimeupdateexclusion-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-ecr-pulltimeupdateexclusion-syntax.json"></a>

```
{
  "Type" : "AWS::ECR::PullTimeUpdateExclusion",
  "Properties" : {
      "[PrincipalArn](#cfn-ecr-pulltimeupdateexclusion-principalarn)" : {{String}}
    }
}
```

### YAML
<a name="aws-resource-ecr-pulltimeupdateexclusion-syntax.yaml"></a>

```
Type: AWS::ECR::PullTimeUpdateExclusion
Properties:
  [PrincipalArn](#cfn-ecr-pulltimeupdateexclusion-principalarn): {{String}}
```

## Properties
<a name="aws-resource-ecr-pulltimeupdateexclusion-properties"></a>

`PrincipalArn`  <a name="cfn-ecr-pulltimeupdateexclusion-principalarn"></a>
The ARN of the IAM principal to remove from the pull time update exclusion list.
*Required*: Yes
*Type*: String
*Pattern*: `^arn:aws(-[a-z]+)*:iam::[0-9]{12}:(role|user)/[\w+=,.@-]+(/[\w+=,.@-]+)*$`
*Maximum*: `200`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## Return values
<a name="aws-resource-ecr-pulltimeupdateexclusion-return-values"></a>

### Ref
<a name="aws-resource-ecr-pulltimeupdateexclusion-return-values-ref"></a>

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
