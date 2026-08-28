---
source_url: https://docs.aws.amazon.com/eks/latest/APIReference/API_SsoIdentity.html
---

# SsoIdentity
<a name="API_SsoIdentity"></a>

An IAM Identity CenterIAM; Identity Center identity (user or group) that can be assigned permissions in a capability.

## Contents
<a name="API_SsoIdentity_Contents"></a>

 ** id **   <a name="AmazonEKS-Type-SsoIdentity-id"></a>
The unique identifier of the IAM Identity CenterIAM; Identity Center user or group.
Type: String
Required: Yes

 ** type **   <a name="AmazonEKS-Type-SsoIdentity-type"></a>
The type of identity. Valid values are `SSO_USER` or `SSO_GROUP`.
Type: String
Valid Values: `SSO_USER | SSO_GROUP`
Required: Yes

## See Also
<a name="API_SsoIdentity_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/eks-2017-11-01/SsoIdentity)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/eks-2017-11-01/SsoIdentity)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/eks-2017-11-01/SsoIdentity)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon EKS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query eks` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
