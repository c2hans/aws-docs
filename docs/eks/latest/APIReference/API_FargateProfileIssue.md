---
source_url: https://docs.aws.amazon.com/eks/latest/APIReference/API_FargateProfileIssue.html
---

# FargateProfileIssue
<a name="API_FargateProfileIssue"></a>

An issue that is associated with the Fargate profile.

## Contents
<a name="API_FargateProfileIssue_Contents"></a>

 ** code **   <a name="AmazonEKS-Type-FargateProfileIssue-code"></a>
A brief description of the error.
Type: String
Valid Values: `PodExecutionRoleAlreadyInUse | AccessDenied | ClusterUnreachable | InternalFailure`
Required: No

 ** message **   <a name="AmazonEKS-Type-FargateProfileIssue-message"></a>
The error message associated with the issue.
Type: String
Required: No

 ** resourceIds **   <a name="AmazonEKS-Type-FargateProfileIssue-resourceIds"></a>
The AWS resources that are affected by this issue.
Type: Array of strings
Required: No

## See Also
<a name="API_FargateProfileIssue_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/eks-2017-11-01/FargateProfileIssue)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/eks-2017-11-01/FargateProfileIssue)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/eks-2017-11-01/FargateProfileIssue)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon EKS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query eks` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
