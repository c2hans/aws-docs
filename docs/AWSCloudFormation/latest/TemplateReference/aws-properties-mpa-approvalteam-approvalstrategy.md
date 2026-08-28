---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-mpa-approvalteam-approvalstrategy.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::MPA::ApprovalTeam ApprovalStrategy
<a name="aws-properties-mpa-approvalteam-approvalstrategy"></a>

Strategy for how an approval team grants approval.

## Syntax
<a name="aws-properties-mpa-approvalteam-approvalstrategy-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-mpa-approvalteam-approvalstrategy-syntax.json"></a>

```
{
  "[MofN](#cfn-mpa-approvalteam-approvalstrategy-mofn)" : {{MofNApprovalStrategy}}
}
```

### YAML
<a name="aws-properties-mpa-approvalteam-approvalstrategy-syntax.yaml"></a>

```
  [MofN](#cfn-mpa-approvalteam-approvalstrategy-mofn): {{
    MofNApprovalStrategy}}
```

## Properties
<a name="aws-properties-mpa-approvalteam-approvalstrategy-properties"></a>

`MofN`  <a name="cfn-mpa-approvalteam-approvalstrategy-mofn"></a>
Minimum number of approvals (M) required for a total number of approvers (N).
*Required*: Yes
*Type*: [MofNApprovalStrategy](aws-properties-mpa-approvalteam-mofnapprovalstrategy.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
