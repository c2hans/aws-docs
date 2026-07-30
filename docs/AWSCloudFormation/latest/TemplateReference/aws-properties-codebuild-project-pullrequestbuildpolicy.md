---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-codebuild-project-pullrequestbuildpolicy.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::CodeBuild::Project PullRequestBuildPolicy
<a name="aws-properties-codebuild-project-pullrequestbuildpolicy"></a>

A PullRequestBuildPolicy object that defines comment-based approval requirements for triggering builds on pull requests. This policy helps control when automated builds are executed based on contributor permissions and approval workflows.

## Syntax
<a name="aws-properties-codebuild-project-pullrequestbuildpolicy-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-codebuild-project-pullrequestbuildpolicy-syntax.json"></a>

```
{
  "[ApproverRoles](#cfn-codebuild-project-pullrequestbuildpolicy-approverroles)" : {{[ String, ... ]}},
  "[RequiresCommentApproval](#cfn-codebuild-project-pullrequestbuildpolicy-requirescommentapproval)" : {{String}}
}
```

### YAML
<a name="aws-properties-codebuild-project-pullrequestbuildpolicy-syntax.yaml"></a>

```
  [ApproverRoles](#cfn-codebuild-project-pullrequestbuildpolicy-approverroles): {{
    - String}}
  [RequiresCommentApproval](#cfn-codebuild-project-pullrequestbuildpolicy-requirescommentapproval): {{String}}
```

## Properties
<a name="aws-properties-codebuild-project-pullrequestbuildpolicy-properties"></a>

`ApproverRoles`  <a name="cfn-codebuild-project-pullrequestbuildpolicy-approverroles"></a>
List of repository roles that have approval privileges for pull request builds when comment approval is required. Only users with these roles can provide valid comment approvals. If a pull request contributor is one of these roles, their pull request builds will trigger automatically. This field is only applicable when `requiresCommentApproval` is not *DISABLED*.
*Required*: No
*Type*: Array of String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`RequiresCommentApproval`  <a name="cfn-codebuild-project-pullrequestbuildpolicy-requirescommentapproval"></a>
Specifies when comment-based approval is required before triggering a build on pull requests. This setting determines whether builds run automatically or require explicit approval through comments.
+ *DISABLED*: Builds trigger automatically without requiring comment approval
+ *ALL\_PULL\_REQUESTS*: All pull requests require comment approval before builds execute (unless contributor is one of the approver roles)
+ *FORK\_PULL\_REQUESTS*: Only pull requests from forked repositories require comment approval (unless contributor is one of the approver roles)
*Required*: Yes
*Type*: String
*Allowed values*: `DISABLED | ALL_PULL_REQUESTS | FORK_PULL_REQUESTS`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
