---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-deadline-queuelimitassociation.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Deadline::QueueLimitAssociation
<a name="aws-resource-deadline-queuelimitassociation"></a>

Associates a limit with a particular queue. After the limit is associated, all workers for jobs that specify the limit associated with the queue are subject to the limit. You can't associate two limits with the same `amountRequirementName` to the same queue.

## Syntax
<a name="aws-resource-deadline-queuelimitassociation-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-deadline-queuelimitassociation-syntax.json"></a>

```
{
  "Type" : "AWS::Deadline::QueueLimitAssociation",
  "Properties" : {
      "[FarmId](#cfn-deadline-queuelimitassociation-farmid)" : {{String}},
      "[LimitId](#cfn-deadline-queuelimitassociation-limitid)" : {{String}},
      "[QueueId](#cfn-deadline-queuelimitassociation-queueid)" : {{String}}
    }
}
```

### YAML
<a name="aws-resource-deadline-queuelimitassociation-syntax.yaml"></a>

```
Type: AWS::Deadline::QueueLimitAssociation
Properties:
  [FarmId](#cfn-deadline-queuelimitassociation-farmid): {{String}}
  [LimitId](#cfn-deadline-queuelimitassociation-limitid): {{String}}
  [QueueId](#cfn-deadline-queuelimitassociation-queueid): {{String}}
```

## Properties
<a name="aws-resource-deadline-queuelimitassociation-properties"></a>

`FarmId`  <a name="cfn-deadline-queuelimitassociation-farmid"></a>
The unique identifier of the farm that contains the queue-limit association.
*Required*: Yes
*Type*: String
*Pattern*: `^farm-[0-9a-f]{32}$`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`LimitId`  <a name="cfn-deadline-queuelimitassociation-limitid"></a>
The unique identifier of the limit in the association.
*Required*: Yes
*Type*: String
*Pattern*: `^limit-[0-9a-f]{32}$`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`QueueId`  <a name="cfn-deadline-queuelimitassociation-queueid"></a>
The unique identifier of the queue in the association.
*Required*: Yes
*Type*: String
*Pattern*: `^queue-[0-9a-f]{32}$`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## Return values
<a name="aws-resource-deadline-queuelimitassociation-return-values"></a>

### Ref
<a name="aws-resource-deadline-queuelimitassociation-return-values-ref"></a>

When you pass the logical ID of this resource to the intrinsic `Ref` function, `Ref` returns the unique identifier for the queue-limit association.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
