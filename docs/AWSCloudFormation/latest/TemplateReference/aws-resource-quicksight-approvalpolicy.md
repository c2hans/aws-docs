---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-quicksight-approvalpolicy.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::ApprovalPolicy
<a name="aws-resource-quicksight-approvalpolicy"></a>

<a name="aws-resource-quicksight-approvalpolicy-description"></a>The `AWS::QuickSight::ApprovalPolicy` resource Property description not available. for QuickSight.

## Syntax
<a name="aws-resource-quicksight-approvalpolicy-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-quicksight-approvalpolicy-syntax.json"></a>

```
{
  "Type" : "AWS::QuickSight::ApprovalPolicy",
  "Properties" : {
      "[Actions](#cfn-quicksight-approvalpolicy-actions)" : {{[ , ... ]}},
      "[ApplicableTo](#cfn-quicksight-approvalpolicy-applicableto)" : {{ApplicableTo}},
      "[ApprovalGroups](#cfn-quicksight-approvalpolicy-approvalgroups)" : {{[ String, ... ]}},
      "[AssetTypes](#cfn-quicksight-approvalpolicy-assettypes)" : {{[ , ... ]}},
      "[Description](#cfn-quicksight-approvalpolicy-description)" : {{String}},
      "[Name](#cfn-quicksight-approvalpolicy-name)" : {{String}},
      "[PolicyId](#cfn-quicksight-approvalpolicy-policyid)" : {{String}}
    }
}
```

### YAML
<a name="aws-resource-quicksight-approvalpolicy-syntax.yaml"></a>

```
Type: AWS::QuickSight::ApprovalPolicy
Properties:
  [Actions](#cfn-quicksight-approvalpolicy-actions): {{
    - }}
  [ApplicableTo](#cfn-quicksight-approvalpolicy-applicableto): {{
    ApplicableTo}}
  [ApprovalGroups](#cfn-quicksight-approvalpolicy-approvalgroups): {{
    - String}}
  [AssetTypes](#cfn-quicksight-approvalpolicy-assettypes): {{
    - }}
  [Description](#cfn-quicksight-approvalpolicy-description): {{String}}
  [Name](#cfn-quicksight-approvalpolicy-name): {{String}}
  [PolicyId](#cfn-quicksight-approvalpolicy-policyid): {{String}}
```

## Properties
<a name="aws-resource-quicksight-approvalpolicy-properties"></a>

`Actions`  <a name="cfn-quicksight-approvalpolicy-actions"></a>
The list of governed actions that trigger the approval workflow.
*Required*: Yes
*Type*: Array
*Minimum*: `1`
*Maximum*: `10`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ApplicableTo`  <a name="cfn-quicksight-approvalpolicy-applicableto"></a>
The scoping configuration that determines who the approval policy applies to.
*Required*: Yes
*Type*: [ApplicableTo](aws-properties-quicksight-approvalpolicy-applicableto.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ApprovalGroups`  <a name="cfn-quicksight-approvalpolicy-approvalgroups"></a>
The list of group ARNs whose members can approve requests.
*Required*: Yes
*Type*: Array of String
*Minimum*: `1`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`AssetTypes`  <a name="cfn-quicksight-approvalpolicy-assettypes"></a>
The list of asset types that the approval policy applies to.
*Required*: Yes
*Type*: Array
*Minimum*: `1`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Description`  <a name="cfn-quicksight-approvalpolicy-description"></a>
A description of the approval policy.
*Required*: No
*Type*: String
*Minimum*: `0`
*Maximum*: `1024`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Name`  <a name="cfn-quicksight-approvalpolicy-name"></a>
The name of the approval policy.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `256`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`PolicyId`  <a name="cfn-quicksight-approvalpolicy-policyid"></a>
The unique identifier of the approval policy.
*Required*: Yes
*Type*: String
*Pattern*: `^[a-zA-Z0-9\-_]+$`
*Minimum*: `1`
*Maximum*: `64`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## Return values
<a name="aws-resource-quicksight-approvalpolicy-return-values"></a>

### Ref
<a name="aws-resource-quicksight-approvalpolicy-return-values-ref"></a>

### Fn::GetAtt
<a name="aws-resource-quicksight-approvalpolicy-return-values-fn--getatt"></a>

####
<a name="aws-resource-quicksight-approvalpolicy-return-values-fn--getatt-fn--getatt"></a>

`CreatedAt`  <a name="CreatedAt-fn::getatt"></a>
The date and time that the approval policy was created.

`PolicyArn`  <a name="PolicyArn-fn::getatt"></a>
The Amazon Resource Name (ARN) of the approval policy.

`UpdatedAt`  <a name="UpdatedAt-fn::getatt"></a>
The date and time that the approval policy was last updated.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
