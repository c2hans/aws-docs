---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-mpa-approvalteam-mofnapprovalstrategy.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::MPA::ApprovalTeam MofNApprovalStrategy
<a name="aws-properties-mpa-approvalteam-mofnapprovalstrategy"></a>

Strategy for how an approval team grants approval.

## Syntax
<a name="aws-properties-mpa-approvalteam-mofnapprovalstrategy-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-mpa-approvalteam-mofnapprovalstrategy-syntax.json"></a>

```
{
  "[MinApprovalsRequired](#cfn-mpa-approvalteam-mofnapprovalstrategy-minapprovalsrequired)" : {{Integer}}
}
```

### YAML
<a name="aws-properties-mpa-approvalteam-mofnapprovalstrategy-syntax.yaml"></a>

```
  [MinApprovalsRequired](#cfn-mpa-approvalteam-mofnapprovalstrategy-minapprovalsrequired): {{Integer}}
```

## Properties
<a name="aws-properties-mpa-approvalteam-mofnapprovalstrategy-properties"></a>

`MinApprovalsRequired`  <a name="cfn-mpa-approvalteam-mofnapprovalstrategy-minapprovalsrequired"></a>
Minimum number of approvals (M) required for a total number of approvers (N).
*Required*: Yes
*Type*: Integer
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
