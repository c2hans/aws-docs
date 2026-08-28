---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-mpa-approvalteam.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::MPA::ApprovalTeam
<a name="aws-resource-mpa-approvalteam"></a>

Creates a new approval team. For more information, see [Approval team](https://docs.aws.amazon.com/mpa/latest/userguide/mpa-concepts.html) in the *Multi-party approval User Guide*.

## Syntax
<a name="aws-resource-mpa-approvalteam-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-mpa-approvalteam-syntax.json"></a>

```
{
  "Type" : "AWS::MPA::ApprovalTeam",
  "Properties" : {
      "[ApprovalStrategy](#cfn-mpa-approvalteam-approvalstrategy)" : {{ApprovalStrategy}},
      "[Approvers](#cfn-mpa-approvalteam-approvers)" : {{[ Approver, ... ]}},
      "[Description](#cfn-mpa-approvalteam-description)" : {{String}},
      "[Name](#cfn-mpa-approvalteam-name)" : {{String}},
      "[Policies](#cfn-mpa-approvalteam-policies)" : {{[ Policy, ... ]}},
      "[Tags](#cfn-mpa-approvalteam-tags)" : {{[ Tag, ... ]}}
    }
}
```

### YAML
<a name="aws-resource-mpa-approvalteam-syntax.yaml"></a>

```
Type: AWS::MPA::ApprovalTeam
Properties:
  [ApprovalStrategy](#cfn-mpa-approvalteam-approvalstrategy): {{
    ApprovalStrategy}}
  [Approvers](#cfn-mpa-approvalteam-approvers): {{
    - Approver}}
  [Description](#cfn-mpa-approvalteam-description): {{String}}
  [Name](#cfn-mpa-approvalteam-name): {{String}}
  [Policies](#cfn-mpa-approvalteam-policies): {{
    - Policy}}
  [Tags](#cfn-mpa-approvalteam-tags): {{
    - Tag}}
```

## Properties
<a name="aws-resource-mpa-approvalteam-properties"></a>

`ApprovalStrategy`  <a name="cfn-mpa-approvalteam-approvalstrategy"></a>
Contains details for how an approval team grants approval.
*Required*: Yes
*Type*: [ApprovalStrategy](aws-properties-mpa-approvalteam-approvalstrategy.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Approvers`  <a name="cfn-mpa-approvalteam-approvers"></a>
Contains details for an approver.
*Required*: Yes
*Type*: Array of [Approver](aws-properties-mpa-approvalteam-approver.md)
*Minimum*: `1`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Description`  <a name="cfn-mpa-approvalteam-description"></a>
Description for the team.
*Required*: Yes
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Name`  <a name="cfn-mpa-approvalteam-name"></a>
Name of the team.
*Required*: Yes
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Policies`  <a name="cfn-mpa-approvalteam-policies"></a>
Contains details for a policy. Policies define what operations a team that define the permissions for team resources.
*Required*: Yes
*Type*: Array of [Policy](aws-properties-mpa-approvalteam-policy.md)
*Minimum*: `1`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Tags`  <a name="cfn-mpa-approvalteam-tags"></a>
Tags that you have added to the specified resource.
*Required*: No
*Type*: Array of [Tag](aws-properties-mpa-approvalteam-tag.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-mpa-approvalteam-return-values"></a>

### Ref
<a name="aws-resource-mpa-approvalteam-return-values-ref"></a>

### Fn::GetAtt
<a name="aws-resource-mpa-approvalteam-return-values-fn--getatt"></a>

####
<a name="aws-resource-mpa-approvalteam-return-values-fn--getatt-fn--getatt"></a>

`Arn`  <a name="Arn-fn::getatt"></a>
Amazon Resource Name (ARN) for the team.

`CreationTime`  <a name="CreationTime-fn::getatt"></a>
Timestamp when the team was created.

`LastUpdateTime`  <a name="LastUpdateTime-fn::getatt"></a>
Timestamp when the team was last updated.

`NumberOfApprovers`  <a name="NumberOfApprovers-fn::getatt"></a>
Total number of approvers in the team.

`Status`  <a name="Status-fn::getatt"></a>
Status for the team. For more information, see [Team health](https://docs.aws.amazon.com/mpa/latest/userguide/mpa-health.html) in the *Multi-party approval User Guide*.

`StatusCode`  <a name="StatusCode-fn::getatt"></a>
Status code for the team. For more information, see [Team health](https://docs.aws.amazon.com/mpa/latest/userguide/mpa-health.html) in the *Multi-party approval User Guide*.

`StatusMessage`  <a name="StatusMessage-fn::getatt"></a>
Message describing the status for the team.

`UpdateSessionArn`  <a name="UpdateSessionArn-fn::getatt"></a>
Timestamp when the team was last updated.

`VersionId`  <a name="VersionId-fn::getatt"></a>
Version ID for the team.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
