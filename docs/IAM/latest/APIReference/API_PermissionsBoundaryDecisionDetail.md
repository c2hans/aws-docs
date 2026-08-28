---
source_url: https://docs.aws.amazon.com/IAM/latest/APIReference/API_PermissionsBoundaryDecisionDetail.html
---

# PermissionsBoundaryDecisionDetail
<a name="API_PermissionsBoundaryDecisionDetail"></a>

Contains information about the effect that a permissions boundary has on a policy simulation when the boundary is applied to an IAM entity.

## Contents
<a name="API_PermissionsBoundaryDecisionDetail_Contents"></a>

 ** AllowedByPermissionsBoundary **
Specifies whether an action is allowed by a permissions boundary that is applied to an IAM entity (user or role). A value of `true` means that the permissions boundary does not deny the action. This means that the policy includes an `Allow` statement that matches the request. In this case, if an identity-based policy also allows the action, the request is allowed. A value of `false` means that either the requested action is not allowed (implicitly denied) or that the action is explicitly denied by the permissions boundary. In both of these cases, the action is not allowed, regardless of the identity-based policy.
Type: Boolean
Required: No

## See Also
<a name="API_PermissionsBoundaryDecisionDetail_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iam-2010-05-08/PermissionsBoundaryDecisionDetail)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iam-2010-05-08/PermissionsBoundaryDecisionDetail)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iam-2010-05-08/PermissionsBoundaryDecisionDetail)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Identity and Access Management. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query IAM` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
