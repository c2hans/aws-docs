---
source_url: https://docs.aws.amazon.com/eks/latest/APIReference/API_UpdateLabelsPayload.html
---

# UpdateLabelsPayload
<a name="API_UpdateLabelsPayload"></a>

An object representing a Kubernetes `label` change for a managed node group.

## Contents
<a name="API_UpdateLabelsPayload_Contents"></a>

 ** addOrUpdateLabels **   <a name="AmazonEKS-Type-UpdateLabelsPayload-addOrUpdateLabels"></a>
The Kubernetes `labels` to add or update.
Type: String to string map
Key Length Constraints: Minimum length of 1. Maximum length of 63.
Value Length Constraints: Minimum length of 1. Maximum length of 63.
Required: No

 ** removeLabels **   <a name="AmazonEKS-Type-UpdateLabelsPayload-removeLabels"></a>
The Kubernetes `labels` to remove.
Type: Array of strings
Required: No

## See Also
<a name="API_UpdateLabelsPayload_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/eks-2017-11-01/UpdateLabelsPayload)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/eks-2017-11-01/UpdateLabelsPayload)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/eks-2017-11-01/UpdateLabelsPayload)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon EKS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query eks` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
