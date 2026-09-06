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
