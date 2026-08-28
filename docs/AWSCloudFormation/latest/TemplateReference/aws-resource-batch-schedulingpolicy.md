---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-batch-schedulingpolicy.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Batch::SchedulingPolicy
<a name="aws-resource-batch-schedulingpolicy"></a>

The `AWS::Batch::SchedulingPolicy` resource specifies the parameters for an AWS Batch scheduling policy. For more information, see [Scheduling Policies](https://docs.aws.amazon.com/batch/latest/userguide/scheduling_policies.html) in the * AWS Batch User Guide *.

## Syntax
<a name="aws-resource-batch-schedulingpolicy-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-batch-schedulingpolicy-syntax.json"></a>

```
{
  "Type" : "AWS::Batch::SchedulingPolicy",
  "Properties" : {
      "[FairsharePolicy](#cfn-batch-schedulingpolicy-fairsharepolicy)" : {{FairsharePolicy}},
      "[Name](#cfn-batch-schedulingpolicy-name)" : {{String}},
      "[QuotaSharePolicy](#cfn-batch-schedulingpolicy-quotasharepolicy)" : {{QuotaSharePolicy}},
      "[Tags](#cfn-batch-schedulingpolicy-tags)" : {{{{{Key}}: {{Value}}, ...}}}
    }
}
```

### YAML
<a name="aws-resource-batch-schedulingpolicy-syntax.yaml"></a>

```
Type: AWS::Batch::SchedulingPolicy
Properties:
  [FairsharePolicy](#cfn-batch-schedulingpolicy-fairsharepolicy): {{
    FairsharePolicy}}
  [Name](#cfn-batch-schedulingpolicy-name): {{String}}
  [QuotaSharePolicy](#cfn-batch-schedulingpolicy-quotasharepolicy): {{
    QuotaSharePolicy}}
  [Tags](#cfn-batch-schedulingpolicy-tags): {{
    {{Key}}: {{Value}}}}
```

## Properties
<a name="aws-resource-batch-schedulingpolicy-properties"></a>

`FairsharePolicy`  <a name="cfn-batch-schedulingpolicy-fairsharepolicy"></a>
The fair-share scheduling policy details. Only one of fairsharePolicy or quotaSharePolicy can be set. Once set, this policy type cannot be removed or changed to a quotaSharePolicy.
*Required*: No
*Type*: [FairsharePolicy](aws-properties-batch-schedulingpolicy-fairsharepolicy.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Name`  <a name="cfn-batch-schedulingpolicy-name"></a>
The name of the fair-share scheduling policy. It can be up to 128 letters long. It can contain uppercase and lowercase letters, numbers, hyphens (-), and underscores (\_).
*Required*: No
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`QuotaSharePolicy`  <a name="cfn-batch-schedulingpolicy-quotasharepolicy"></a>
The quota share scheduling policy details.
*Required*: No
*Type*: [QuotaSharePolicy](aws-properties-batch-schedulingpolicy-quotasharepolicy.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Tags`  <a name="cfn-batch-schedulingpolicy-tags"></a>
The tags that you apply to the scheduling policy to help you categorize and organize your resources. Each tag consists of a key and an optional value. For more information, see [Tagging AWS Resources](https://docs.aws.amazon.com/general/latest/gr/aws_tagging.html) in *AWS General Reference*.
These tags can be updated or removed using the [TagResource](https://docs.aws.amazon.com/batch/latest/APIReference/API_TagResource.html) and [UntagResource](https://docs.aws.amazon.com/batch/latest/APIReference/API_UntagResource.html) API operations.
*Required*: No
*Type*: Object of String
*Pattern*: `.*`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-batch-schedulingpolicy-return-values"></a>

### Ref
<a name="aws-resource-batch-schedulingpolicy-return-values-ref"></a>

When you pass the logical ID of this resource to the intrinsic `Ref` function, `Ref` returns the scheduling policy ARN, such as `arn:aws:batch:us-east-1:111122223333:scheduling-policy/HighPriority`.

For more information about using the `Ref` function, see [`Ref`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-ref.html).

### Fn::GetAtt
<a name="aws-resource-batch-schedulingpolicy-return-values-fn--getatt"></a>

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [`Fn::GetAtt`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-getatt.html).

####
<a name="aws-resource-batch-schedulingpolicy-return-values-fn--getatt-fn--getatt"></a>

`Arn`  <a name="Arn-fn::getatt"></a>
Returns the scheduling policy ARN, such as `arn:aws:batch:us-east-1:111122223333:scheduling-policy/HighPriority`.

## See also
<a name="aws-resource-batch-schedulingpolicy--seealso"></a>
+ [Scheduling Policy Parameters](https://docs.aws.amazon.com/batch/latest/userguide/scheduling_policy_parameters.html) in the * AWS Batch User Guide *.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
