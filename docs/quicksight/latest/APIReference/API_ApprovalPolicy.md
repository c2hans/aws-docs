---
source_url: https://docs.aws.amazon.com/quicksight/latest/APIReference/API_ApprovalPolicy.html
---

# ApprovalPolicy
<a name="API_ApprovalPolicy"></a>

A governance approval policy that specifies which principals and governed actions require approval, and which assets the policy applies to.

## Contents
<a name="API_ApprovalPolicy_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** Actions **   <a name="QS-Type-ApprovalPolicy-Actions"></a>
The list of governed actions that trigger the approval workflow.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 10 items.
Valid Values: `SHARE`
Required: Yes

 ** ApplicableTo **   <a name="QS-Type-ApprovalPolicy-ApplicableTo"></a>
The scoping configuration that determines who the approval policy applies to.
Type: [ApplicableTo](API_ApplicableTo.md) object
Required: Yes

 ** ApprovalGroups **   <a name="QS-Type-ApprovalPolicy-ApprovalGroups"></a>
The list of group ARNs whose members can approve requests.
Type: Array of strings
Array Members: Minimum number of 1 item.
Required: Yes

 ** AssetTypes **   <a name="QS-Type-ApprovalPolicy-AssetTypes"></a>
The list of asset types that the approval policy applies to.
Type: Array of strings
Array Members: Minimum number of 1 item.
Valid Values: `AGENT | SPACE | KNOWLEDGE_BASE`
Required: Yes

 ** CreatedAt **   <a name="QS-Type-ApprovalPolicy-CreatedAt"></a>
The date and time that the approval policy was created.
Type: Timestamp
Required: Yes

 ** Name **   <a name="QS-Type-ApprovalPolicy-Name"></a>
The name of the approval policy.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Required: Yes

 ** PolicyArn **   <a name="QS-Type-ApprovalPolicy-PolicyArn"></a>
The Amazon Resource Name (ARN) of the approval policy.
Type: String
Required: Yes

 ** PolicyId **   <a name="QS-Type-ApprovalPolicy-PolicyId"></a>
The unique identifier of the approval policy.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[a-zA-Z0-9\-_]+`
Required: Yes

 ** UpdatedAt **   <a name="QS-Type-ApprovalPolicy-UpdatedAt"></a>
The date and time that the approval policy was last updated.
Type: Timestamp
Required: Yes

 ** Description **   <a name="QS-Type-ApprovalPolicy-Description"></a>
A description of the approval policy.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Required: No

## See Also
<a name="API_ApprovalPolicy_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/quicksight-2018-04-01/ApprovalPolicy)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/quicksight-2018-04-01/ApprovalPolicy)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/quicksight-2018-04-01/ApprovalPolicy)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Quick Sight. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query quicksight` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
