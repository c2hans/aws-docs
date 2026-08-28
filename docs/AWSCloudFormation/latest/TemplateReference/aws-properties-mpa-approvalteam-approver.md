---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-mpa-approvalteam-approver.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::MPA::ApprovalTeam Approver
<a name="aws-properties-mpa-approvalteam-approver"></a>

Contains details for an approver.

## Syntax
<a name="aws-properties-mpa-approvalteam-approver-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-mpa-approvalteam-approver-syntax.json"></a>

```
{
  "[ApproverId](#cfn-mpa-approvalteam-approver-approverid)" : {{String}},
  "[PrimaryIdentityId](#cfn-mpa-approvalteam-approver-primaryidentityid)" : {{String}},
  "[PrimaryIdentitySourceArn](#cfn-mpa-approvalteam-approver-primaryidentitysourcearn)" : {{String}},
  "[PrimaryIdentityStatus](#cfn-mpa-approvalteam-approver-primaryidentitystatus)" : {{String}},
  "[ResponseTime](#cfn-mpa-approvalteam-approver-responsetime)" : {{String}}
}
```

### YAML
<a name="aws-properties-mpa-approvalteam-approver-syntax.yaml"></a>

```
  [ApproverId](#cfn-mpa-approvalteam-approver-approverid): {{String}}
  [PrimaryIdentityId](#cfn-mpa-approvalteam-approver-primaryidentityid): {{String}}
  [PrimaryIdentitySourceArn](#cfn-mpa-approvalteam-approver-primaryidentitysourcearn): {{String}}
  [PrimaryIdentityStatus](#cfn-mpa-approvalteam-approver-primaryidentitystatus): {{String}}
  [ResponseTime](#cfn-mpa-approvalteam-approver-responsetime): {{String}}
```

## Properties
<a name="aws-properties-mpa-approvalteam-approver-properties"></a>

`ApproverId`  <a name="cfn-mpa-approvalteam-approver-approverid"></a>
ID for the approver.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`PrimaryIdentityId`  <a name="cfn-mpa-approvalteam-approver-primaryidentityid"></a>
ID for the user.
*Required*: Yes
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`PrimaryIdentitySourceArn`  <a name="cfn-mpa-approvalteam-approver-primaryidentitysourcearn"></a>
Amazon Resource Name (ARN) for the identity source. The identity source manages the user authentication for approvers.
*Required*: Yes
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`PrimaryIdentityStatus`  <a name="cfn-mpa-approvalteam-approver-primaryidentitystatus"></a>
Status for the identity source. For example, if an approver has accepted a team invitation with a user authentication method managed by the identity source.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ResponseTime`  <a name="cfn-mpa-approvalteam-approver-responsetime"></a>
Timestamp when the approver responded to an approval team invitation.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
