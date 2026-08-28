---
source_url: https://docs.aws.amazon.com/eks/latest/APIReference/API_UpgradePolicyResponse.html
---

# UpgradePolicyResponse
<a name="API_UpgradePolicyResponse"></a>

This value indicates if extended support is enabled or disabled for the cluster.

 [Learn more about EKS Extended Support in the *Amazon EKS User Guide*.](https://docs.aws.amazon.com/eks/latest/userguide/extended-support-control.html)

## Contents
<a name="API_UpgradePolicyResponse_Contents"></a>

 ** supportType **   <a name="AmazonEKS-Type-UpgradePolicyResponse-supportType"></a>
If the cluster is set to `EXTENDED`, it will enter extended support at the end of standard support. If the cluster is set to `STANDARD`, it will be automatically upgraded at the end of standard support.
 [Learn more about EKS Extended Support in the *Amazon EKS User Guide*.](https://docs.aws.amazon.com/eks/latest/userguide/extended-support-control.html)
Type: String
Valid Values: `STANDARD | EXTENDED`
Required: No

## See Also
<a name="API_UpgradePolicyResponse_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/eks-2017-11-01/UpgradePolicyResponse)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/eks-2017-11-01/UpgradePolicyResponse)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/eks-2017-11-01/UpgradePolicyResponse)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon EKS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query eks` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
