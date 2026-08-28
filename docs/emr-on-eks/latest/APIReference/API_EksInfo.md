---
source_url: https://docs.aws.amazon.com/emr-on-eks/latest/APIReference/API_EksInfo.html
---

# EksInfo
<a name="API_EksInfo"></a>

The information about the Amazon EKS cluster.

## Contents
<a name="API_EksInfo_Contents"></a>

 ** namespace **   <a name="emroneks-Type-EksInfo-namespace"></a>
The namespaces of the Amazon EKS cluster.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 63.
Pattern: `[a-z0-9]([-a-z0-9]*[a-z0-9])?`
Required: No

 ** nodeLabel **   <a name="emroneks-Type-EksInfo-nodeLabel"></a>
The nodeLabel of the nodes where the resources of this virtual cluster can get scheduled. It requires relevant scaling and policy engine addons.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `^[a-z0-9](?:[a-z0-9-]*[a-z0-9])?$`
Required: No

## See Also
<a name="API_EksInfo_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/emr-containers-2020-10-01/EksInfo)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/emr-containers-2020-10-01/EksInfo)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/emr-containers-2020-10-01/EksInfo)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon EMR on EKS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query emr-on-eks` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
